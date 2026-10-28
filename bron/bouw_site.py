"""Zet de pagina's van henhverduurzaming.nl in elkaar (kop + inhoud + voet)."""
import pathlib, sys

DOEL = pathlib.Path(sys.argv[1])

MENU = [
    ("index.html", "Home"),
    ("plan.html", "Het plan"),
    ("standpunt.html", "Ons standpunt"),
    ("tijdlijn.html", "Tijdlijn"),
    ("vragen.html", "Vragen"),
]

KOP = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel}</title>
<meta name="description" content="{omschrijving}">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="concept">Concept: deze teksten zijn nog niet vastgesteld door het bestuur.</div>
<header class="kop">
  <div class="wrap">
    <a class="logo" href="index.html"><strong>Verduurzaming Hakfort &amp; Huigenbos</strong><span>Bewonersvereniging Hakfort en Huigenbos</span></a>
    <button class="menu-knop" aria-expanded="false" aria-controls="menu">Menu</button>
    <nav id="menu" aria-label="Hoofdmenu">
      <ul>
{menu}
      </ul>
    </nav>
  </div>
</header>
"""

VOET = """<footer class="voet">
  <div class="wrap">
    <div class="kolommen">
      <div>
        <h2>Spreekuur</h2>
        <p>Maandag 17.30–19.30 uur<br>Donderdag 16.00–18.00 uur</p>
        <p>'t Glazen Huis, Huigenbos 10, Amsterdam</p>
      </div>
      <div>
        <h2>Contact</h2>
        <p><a href="mailto:hakfortenhuigenbos@gmail.com">hakfortenhuigenbos@gmail.com</a></p>
        <p><a href="https://www.hakfortenhuigenbos.nl">hakfortenhuigenbos.nl</a></p>
      </div>
      <div>
        <h2>Andere taal?</h2>
        <p>Gebruik de vertaalknop van uw browser, of de app Lees Simpel.</p>
      </div>
    </div>
    <p class="klein">Dit is een website van de Bewonersvereniging Hakfort en Huigenbos. Bijgewerkt: {bijgewerkt}.</p>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
"""

BIJGEWERKT = "28 oktober 2026"


def pagina(bestand, titel, omschrijving, inhoud):
    regels = []
    for href, naam in MENU:
        huidig = ' aria-current="page"' if href == bestand else ""
        regels.append(f'        <li><a href="{href}"{huidig}>{naam}</a></li>')
    html = KOP.format(titel=titel, omschrijving=omschrijving, menu="\n".join(regels))
    html += inhoud.strip() + "\n"
    html += VOET.format(bijgewerkt=BIJGEWERKT)
    (DOEL / bestand).write_text(html, encoding="utf-8")
    print("geschreven:", bestand)


for f in sorted(pathlib.Path(sys.argv[2]).glob("*.inhoud.html")):
    eerste, rest = f.read_text(encoding="utf-8").split("\n", 1)
    titel, omschrijving = [s.strip() for s in eerste.removeprefix("<!--").removesuffix("-->").split("|")]
    pagina(f.name.replace(".inhoud", ""), titel, omschrijving, rest)
