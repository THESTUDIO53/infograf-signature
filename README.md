# INFOGRAF GOTI – Email Signature Generator

Statički web-sajt za generisanje email potpisa po INFOGRAF brending standardu. Zaposleni unose svoje podatke, kopiraju potpis i lepe u Outlook.

## Funkcionalnosti

- Live preview tokom kucanja
- Editabilna polja: **Ime, Pozicija, Mobilni, Email**
- Fiksni podaci: logo + partner-kolaž, kancelarijski tel, website, adresa
- Copy as Rich-Text (HTML) + Plain-Text – direktan paste u Outlook
- Logo partnerski kolaž ugrađen kao base64 JPEG (radi i offline)
- Table-based signature layout sa inline-stilovima – kompatibilan sa Outlook 2016/2019/2021/365 Desktop, Outlook on the Web i Outlook for Mac
- Vrednosti se pamte lokalno (localStorage)
- Font: **Source Sans 3** sa fallback-om na Calibri/Arial za Outlook
- Ikonice: inline SVG (mail, phone, globe, location)

## Deploy na GitHub Pages

```bash
git init
git add .
git commit -m "Initial commit – INFOGRAF Email Signature Generator"
git branch -M main
git remote add origin git@github.com:THESTUDIO53/infograf-signature.git
git push -u origin main
```

Settings → Pages → Source: Deploy from a branch / main / root → Save.

Sajt: `https://thestudio53.github.io/infograf-signature/`

## Kako se ubacuje u Outlook (uputstvo za zaposlene)

1. Otvorite sajt, popunite svoje podatke, kliknite **„Kopiraj potpis"**.
2. Outlook: `File → Options → Mail → Signatures…`
3. **„New"**, dajte ime potpisu (npr. „INFOGRAF").
4. Kliknite u editor i pritisnite `Ctrl + V` (Mac: `Cmd + V`).
5. Save. Po želji postavite kao default za nove mejlove i odgovore.

## Izmena firmenih podataka

U `index.html`, JavaScript blok na vrhu:

```javascript
var COMPANY = {
  officeTel:  '+381/ 21 551-311',
  website:    'www.info-graf.rs',
  websiteUrl: 'https://www.info-graf.rs',
  address:    'Joakima Vujića 16, 21000 Novi Sad, Serbia'
};

var DEFAULTS = {
  name:     'TEODORA SREDOJEVIĆ',
  position: 'Head of creative department',
  mobile:   '+381/ 63 47 80 26',
  email:    'teodora.sredojevic@info-graf.rs'
};
```

## Tehničke napomene

- Bez build-tool-ova — čist HTML/CSS/JS, jedan fajl deploybar.
- Google Fonts samo za web pregled. Outlook koristi Calibri/Arial fallback.
- Kompatibilnost: Chrome / Edge / Firefox / Safari (sa Clipboard API + execCommand fallback).
- Podaci se ne šalju na server. Sve ostaje u browser-u zaposlenog.

## Lokacija fajlova

- `index.html` – glavni sajt
- `assets/infograf-logo-header.png` – logo za web header
- `assets/infograf-collage-embed.jpg` – partner kolaž koji se ugrađuje u email potpis (500px wide, ~56KB)
- `assets/infograf-collage-hires.jpg` – visoko-rezolucijska verzija kolaža (1200px, za rezervu)
- `assets/infograf-logo.png` – originalna INFOGRAF logo PNG

© INFOGRAF GOTI – interna upotreba.
