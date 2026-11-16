# Bewegende infographics (GIF)

Een korte animatie die zichzelf opbouwt naast een post: eerst een leeg vlak, dan verschijnen titel, cijfers en slotzin in leesvolgorde. Ze speelt eindeloos af als afbeelding in de feed, zonder playknop. Ze valt op tussen stilstaande beelden en houdt de lezer langer bij je post.

Gebruik ze als een beeld iets toont wat de post vertelt: een cijfer om te tellen, een vergelijking, een proces, een verschuiving. Een animatie die alleen versiert, werkt niet.

## Openingsvraag

> Bij welke post wil je een bewegende infographic? Plak de post, of kies een post die we samen schreven.

## Kan het hier? Eerst testen

Een bewegende infographic bouw je als een webpagina die zichzelf opbouwt, en die je daarna beeld per beeld opneemt. Daarvoor heb je nodig: code kunnen uitvoeren, Python met Playwright en een Chromium-browser, en liefst ffmpeg (zonder ffmpeg maakt `opnemen.py` de GIF met Pillow).

1. **Test eerst of je kunt opnemen**, voor je iets belooft: kan je code uitvoeren, en starten Playwright en de browser?
2. **Lukt dat niet, probeer het te installeren** (bv. `pip install playwright` en `playwright install chromium`). In sommige werkruimtes blokkeren de netwerkinstellingen die download.
3. **Lukt het ook dan niet**, zeg het eerlijk en in gewone woorden, en geef drie keuzes:
   > Een bewegende infographic kan ik hier niet opnemen. Wat wil je?
   > 1. Een gewone infographic die niet beweegt (dat kan ik wel).
   > 2. Een bouwpakket om de animatie zelf op te nemen in Claude Code op je eigen computer.
   > 3. Een draaiboek om ze met de hand na te bouwen in Canva of Figma.

   Voor starters die Claude Code niet kennen, zijn 1 en 3 het eenvoudigst.
   - **Keuze 1:** volg `visuals.md`.
   - **Keuze 2, het bouwpakket:** het animatiebestand (html, met tekst, kleuren en logo), `opnemen.py`, de lettertypes en het logo, plus een zin om te plakken in Claude Code: "Neem deze animatie op als GIF met het script opnemen.py. Installeer wat ontbreekt." Claude Code werkt op de computer van de gebruiker en kan daar de nodige programma's installeren, met zijn toestemming.
   - **Keuze 3:** het draaiboek (zie "Zonder code" onderaan).

**Werkt de gebruiker in ChatGPT of Copilot?** Geef hem altijd iets waar hij zelf verder mee kan:
- **ChatGPT (met code-uitvoering):** maak het draaiboek en geef deze prompt om te plakken:
  > Maak met Python (Pillow) een bewegende GIF van 1080 x 1350 pixels op basis van dit draaiboek: [draaiboek]. Kleuren: [kleurcodes]. Lettertype: het .ttf-bestand dat ik upload. Logo: de .png die ik upload, klein rechtsonder. Regels: het eerste beeld is leeg. Elk element verschijnt in leesvolgorde en schuift rustig in beeld in ongeveer 0,4 seconde. Geen geknipper. Het slotbeeld blijft 2 seconden staan. Totale duur 6 tot 8 seconden, 15 beelden per seconde. De GIF herhaalt eindeloos en blijft onder 5 MB. Toon me daarna het slotbeeld en geef me de GIF om te downloaden.
- **Copilot, of als code niet lukt: een stappenplan voor Canva:**
  1. Maak in Canva een ontwerp van 1080 x 1350 pixels.
  2. Zet de tekst en de elementen op hun plaats volgens het draaiboek, in je huisstijl en met je echte logo.
  3. Geef elk element een rustige animatie waarmee het verschijnt, in de volgorde waarin je het leest.
  4. Zet de duur op 6 à 8 seconden.
  5. Download het ontwerp als GIF. Controleer dat het bestand onder 5 MB blijft.
  6. Post het op LinkedIn via het foto-icoon, niet via het video-icoon.

Beloof nooit een GIF die je niet kunt maken.

Startbestanden in `assets/animatie/`:
- `start.html`: een werkend voorbeeld (tellende tegels) met de juiste opbouw. Pas huisstijl, tekst en tijdlijn aan.
- `opnemen.py`: neemt de pagina beeld per beeld op en maakt de GIF, een MP4, een PNG van het slotbeeld en een filmstrip om na te kijken.

## Stap 1: de brief en de feiten

1. Lees de post. Zeg in één zin wat "af" is: voor wie, welke ene boodschap, en één check (bv. "het slotbeeld is leesbaar op gsm-breedte").
2. Elk cijfer komt uit de bewijsbank van het brein (zie `brein.md`), een gekoppelde bron of de gebruiker zelf. Staat het niet in de bewijsbank, vraag het en stel voor om het toe te voegen. Verzin nooit een cijfer. Wat ontbreekt, komt tussen [haakjes] en vraag je.
3. Zet bij een gemiddelde of percentage waarop het rust ("7 klanten", "1 project"). Meld het als een cijfer op heel weinig gevallen steunt.
4. Klantnamen alleen als de gebruiker zegt dat het mag. Anders anoniem ("een dienstverlener met 40 klanten").
5. Gebruik de eigen zinnen van de post op het beeld, niet een gladde herschrijving. Weinig tekst. Toon cijfers als iets wat je kunt tellen (stippen, tegels, staven), niet als een zin.

## Stap 2: kies het type

Bij een eerste animatie of een nieuw idee: maak 2 à 4 korte proefjes (5 tot 8 seconden) in verschillende types en laat de gebruiker kiezen.

| Type | Wat je ziet | Goed voor |
|---|---|---|
| Tellende stippen of tegels | 1 stip = 1 klant, 1 offerte, 1 uur | Cijfers die je kunt tellen ("7 van de 15") |
| Verhaal in beeld | Een herkenbare scène die het waarom toont (bv. een mail die verdwijnt in een volle inbox) | Perspective, een misvatting, een pijn |
| Groeiende staven met tellers | Staven die tot hun waarde groeien, met het getal erbij | Een vergelijking, voor en na |
| Bewegend citaat | Woorden verschijnen op het ritme van de zin, één woord wordt doorstreept of onderlijnd | Een uitspraak van de gebruiker of een klant |
| Stappenschema dat zich opbouwt | Vakjes en pijlen verschijnen in leesvolgorde | Een werkwijze, een proces, een framework |
| Tijdlijn | Een lijn met momenten die één voor één oplichten | Groei, bouwen in het openbaar, een klantreis |

Een type werkt alleen als het beeld de boodschap van de post vertelt. Twijfel je, kies dan het eenvoudigste.

## Stap 3: de huisstijl

- Gebruik de huisstijl uit het brein (`huisstijl.md` en de map `huisstijl/`): kleurcodes, lettertypes en het echte logobestand (nooit nagetypt of nagetekend). Staat er "voorstel" bij, zeg dat dan.
- Lettertypes: laad de bestanden van de gebruiker met @font-face. Lukt het downloaden niet (sommige werkruimtes blokkeren lettertypesites), probeer een pakket dat de lettertypebestanden bevat (bv. via npm `@fontsource/<naam>`) of vraag de gebruiker de bestanden (.woff2 of .ttf) te uploaden. Lukt dat ook niet: kies een gelijkaardig lettertype dat er wel is en zeg het.
- Geen huisstijl? Twee kleuren plus zwart en wit, één lettertype, veel witruimte.
- Tweeregelige titel: regel 1 in de tekstkleur, regel 2 in hetzelfde lettertype in een zacht grijs. Logo klein rechtsonder, bron klein linksonder.
- Geen gedachtestreepjes en geen jargon in de tekst op het beeld.

## Stap 4: bouwen

Formaat: 1080 x 1350 pixels (staand). De animatie is een webpagina waarin één functie, `renderAt(t)` met t in seconden, bepaalt hoe alles eruitziet op dat moment. Geen CSS-animaties: zo is elk beeld voorspelbaar en kan je het precies opnemen. Zet de totale duur in `window.T_END`. Vertrek van `assets/animatie/start.html`.

Regels voor de beweging:
- Bouw op in leesvolgorde. Elk blok verschijnt in ongeveer 0,4 seconde en remt rustig af. Geen vering, geen stuiter, nooit knipperen.
- Een schema of systeem staat volledig in beeld na ongeveer 2,5 seconden. Een verhaal mag langer duren.
- Het slotbeeld blijft minstens 2 seconden staan, zodat iedereen het kan lezen.
- Beeld 1 is leeg. Zo toont de GIF bij elke herstart opnieuw de opbouw. Wat doorloopt (een pulserend punt), sluit naadloos aan.
- Labels nooit over een ander element. Liever minder en grotere elementen.
- Totale duur: 5 tot 10 seconden.

Opnemen: `python opnemen.py animatie.html naam` (eindversie) of met `--proef` (snel, halve scherpte). Het script laat de GIF onder 5 MB, de bovengrens voor een GIF op LinkedIn. Blijft hij te groot: maak de animatie korter of rustiger.

## Stap 5: zelf nakijken

Kijk naar de filmstrip en het slotbeeld, echt, met je eigen ogen. Controleer:
- Is beeld 1 leeg?
- Verschijnt alles in leesvolgorde en op tijd?
- Overlapt er niets?
- Kloppen de cijfers met de bron?
- Is het slotbeeld leesbaar op gsm-breedte (verklein naar ongeveer 390 pixels breed)?

Los de grootste zwakte op, neem opnieuw op en kijk opnieuw. Zeg nooit dat je iets nakeek als je het beeld niet bekeek.

Doe daarna de visuele controle (zie `visuele-controle.md`) en zet het blok **Visuele controle** onder de oplevering.

## Stap 6: opleveren

Lever:
- de GIF (1080 x 1350): het bestand om te posten
- de MP4 als reserve (scherper, maar LinkedIn toont hem als video met playknop)
- de PNG van het slotbeeld (als stilstaand beeld)
- de bronbestanden (html, lettertypes, logo, opnamescript), zodat een volgende versie snel gaat

Geef de gebruiker deze stappen om te posten:
1. Klik op "Start a post" en plak de tekst.
2. Klik op het foto-icoon, niet op het video-icoon. Een GIF die als video wordt opgeladen, blijft stilstaan.
3. Kies de GIF.
4. Kijk in het voorbeeld of hij beweegt, en post dan zelf.

Vraag feedback in drie lijstjes: behouden, vervangen, weghalen. Maak pas daarna de volgende versie. Reken op 2 à 3 rondes.

## Zonder code: het draaiboek

Kun je niet zelf opnemen? Lever dan per moment wat er verschijnt:

| Tijd | Wat verschijnt | Tekst | Kleur |
|---|---|---|---|
| 0,0 s | Leeg vlak | | achtergrond |
| 0,2 s | Titel regel 1 schuift zacht omhoog | "..." | tekstkleur |
| ... | ... | ... | ... |
| einde | Slotbeeld blijft 2 s staan | | |

Zeg erbij: formaat 1080 x 1350, bewegingen kort en rustig, exporteren als GIF onder 5 MB. De gebruiker kan dit nabouwen in een ontwerptool met animaties.

## Wat we leerden

- Een sjabloon dat de boodschap niet toont, werkt niet, hoe mooi het ook is. "Verwachting tegenover realiteit" in twee kolommen voelt al snel als een template.
- Minder tekst en cijfers om te tellen werken beter dan zinnen met cijfers.
- Bij een verhaal in beeld: zet een klein label bij het element van de lezer zelf (bv. "jouw aanvraag"), zodat meteen duidelijk is waar hij moet kijken.
- Een GIF post je als afbeelding, niet als video.
