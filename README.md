# henhverduurzaming.nl

Informatiesite van de Bewonersvereniging Hakfort en Huigenbos over de verduurzaming van de flats door Rochdale.

## Teksten aanpassen

1. Pas de tekst aan in `bron/inhoud/<pagina>.inhoud.html`. De eerste regel is `<!-- titel | omschrijving -->`.
2. Kop, menu, voet en de datum "Bijgewerkt" staan in `bron/bouw_site.py`.
3. Bouw de pagina's opnieuw (vanuit deze map):

   ```
   python bron/bouw_site.py . bron/inhoud
   ```

4. Commit en push. GitHub Pages zet de nieuwe versie binnen een paar minuten online.

Opmaak staat in `css/style.css`. Kleine fouten kun je ook direct op github.com verbeteren, maar pas dan zowel de `.inhoud.html` als de gebouwde `.html` aan.

## Eigen domein

Het domein henhverduurzaming.nl (Mijndomein, op naam van Spinam) is gekoppeld via het bestand `CNAME` in de hoofdmap. DNS: vier A- en AAAA-records op het hoofddomein naar GitHub Pages, en `www` met dezelfde vier A-records. Let op: Mijndomein publiceert geen CNAME-records, dus voor www geen CNAME gebruiken. Geen wildcard-records (`*`).
