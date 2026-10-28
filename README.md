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

Als henhverduurzaming.nl gekocht is: hernoem `bron/CNAME.later` naar `CNAME` in de hoofdmap en stel de DNS in volgens de GitHub Pages-handleiding.
