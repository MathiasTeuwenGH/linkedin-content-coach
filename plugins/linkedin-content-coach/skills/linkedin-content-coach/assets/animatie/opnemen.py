"""
Neemt een animatiepagina (met window.renderAt(t) en window.T_END) beeld per beeld op
en maakt er een GIF (om te posten), een MP4 (reserve), een PNG van het slotbeeld
en een filmstrip om zelf na te kijken.

Gebruik:
    python opnemen.py animatie.html naam            # eindversie (scherp)
    python opnemen.py animatie.html naam --proef    # snelle proef, halve resolutie

Nodig: Python met Playwright en een Chromium-browser. ffmpeg is beter voor de GIF,
maar zonder ffmpeg maakt het script de GIF met Pillow.
"""
import argparse, os, shutil, subprocess, sys, tempfile
from pathlib import Path

MAX_GIF_MB = 5.0   # bovengrens voor een GIF op LinkedIn


def opnemen(html, map_beelden, fps, schaal):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        pagina = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=schaal)
        pagina.goto(Path(html).resolve().as_uri())
        pagina.evaluate("document.fonts.ready")
        duur = pagina.evaluate("window.T_END")
        n = int(round(duur * fps)) + 1
        for i in range(n):
            pagina.evaluate(f"window.renderAt({i / fps})")
            pagina.screenshot(path=str(Path(map_beelden) / f"f{i:04d}.png"))
        browser.close()
    return n


def gif_met_ffmpeg(map_beelden, fps, uit, kleuren):
    filt = (f"fps=15,scale=1080:1350:flags=lanczos,split[a][b];"
            f"[a]palettegen=max_colors={kleuren}:stats_mode=diff[p];[b][p]paletteuse=dither=sierra2_4a")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps),
                    "-i", str(Path(map_beelden) / "f%04d.png"), "-vf", filt, "-loop", "0", uit], check=True)


def gif_met_pillow(beelden, fps, uit, kleuren):
    from PIL import Image
    stap = max(1, round(fps / 15))
    frames = [Image.open(b).convert("RGB").resize((1080, 1350)).quantize(colors=kleuren)
              for b in beelden[::stap]]
    frames[0].save(uit, save_all=True, append_images=frames[1:], loop=0,
                   duration=int(1000 * stap / fps), optimize=True)


def filmstrip(beelden, uit, aantal=8):
    from PIL import Image
    kies = [beelden[round(i * (len(beelden) - 1) / (aantal - 1))] for i in range(aantal)]
    w, h = 270, 338
    strip = Image.new("RGB", (w * aantal, h), "white")
    for i, b in enumerate(kies):
        strip.paste(Image.open(b).convert("RGB").resize((w, h)), (i * w, 0))
    strip.save(uit)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("html")
    a.add_argument("naam")
    a.add_argument("--proef", action="store_true")
    a.add_argument("--fps", type=int, default=25)
    args = a.parse_args()

    schaal = 1 if args.proef else 2
    tmp = tempfile.mkdtemp()
    n = opnemen(args.html, tmp, args.fps, schaal)
    beelden = sorted(str(p) for p in Path(tmp).glob("f*.png"))
    heeft_ffmpeg = shutil.which("ffmpeg") is not None

    gif = f"{args.naam}.gif"
    for kleuren in (128, 96, 64, 48):
        if heeft_ffmpeg:
            gif_met_ffmpeg(tmp, args.fps, gif, kleuren)
        else:
            gif_met_pillow(beelden, args.fps, gif, kleuren)
        mb = os.path.getsize(gif) / 1e6
        if mb <= MAX_GIF_MB:
            break
    print(f"GIF: {gif} ({mb:.1f} MB, {kleuren} kleuren)")
    if mb > MAX_GIF_MB:
        print("Let op: GIF nog te groot. Maak de animatie korter of rustiger.")

    if heeft_ffmpeg and not args.proef:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(args.fps),
                        "-i", str(Path(tmp) / "f%04d.png"), "-vf", "scale=1080:1350:flags=lanczos",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow",
                        "-movflags", "+faststart", f"{args.naam}.mp4"], check=True)
        print(f"MP4: {args.naam}.mp4")

    shutil.copy(beelden[-1], f"{args.naam}-slotbeeld.png")
    filmstrip(beelden, f"{args.naam}-filmstrip.png")
    print(f"Slotbeeld en filmstrip gemaakt ({n} beelden).")
    shutil.rmtree(tmp)


if __name__ == "__main__":
    sys.exit(main())
