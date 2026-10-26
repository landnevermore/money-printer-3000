# 💰 MoneyOS – Ultimate Money Printer

**All-in-One System für digitale Produkte, Marketing, Faceless Shorts, Lead Magnets und Bundles.**

Alles lokal. Alles kostenlos. Kein Abo.

---

## ✨ Was drin ist

| Modul | Funktion |
|-------|----------|
| **Digital Products** | Professionelle PDFs (Habit Tracker, Budget, Journal, Fitness, Business...) + fertige Sales Packages |
| **Marketing** | Hooks, Captions, Hashtags, Email-Sequenzen, Pinterest-Texte |
| **Shorts** | Faceless Shorts-Skripte (Hook + Body + CTA) für TikTok / Reels / YouTube |
| **Lead Magnets** | Kostenlose Freebies + Opt-in Texte |
| **Bundles** | Mehrere Produkte zu einem Pack zusammenfassen |
| **Dashboard** | Schöne Streamlit-Oberfläche + Tutorial beim ersten Start |

---

## 🚀 Installation

```bash
git clone https://github.com/landnevermore/money-printer-3000.git
cd money-printer-3000
pip install -r requirements.txt
```

---

## 💻 Starten

### Dashboard (empfohlen)
```bash
streamlit run app.py
```

Beim ersten Start erscheint ein Tutorial.

### Optional: CLI (Digital Products)
```bash
python -c "from modules.digital_products import create_product; print(create_product('habit', color='teal'))"
```

---

## 📁 Output

Alles landet im Ordner `output/`:

```
output/
├── 30-Tage_Habit_Tracker_teal/
│   ├── product.pdf
│   ├── title.txt
│   ├── description.txt
│   ├── tags.txt
│   └── pricing.txt
├── marketing_30-Tage_Habit_Tracker/
│   ├── hooks.txt
│   ├── captions.txt
│   ├── hashtags.txt
│   ├── email_sequence.txt
│   └── pinterest.txt
├── shorts_digitale_Produkte/
│   ├── script_1_educational.txt
│   ├── caption_1.txt
│   └── ...
└── BUNDLE_Ultimate_Productivity_Pack/
    └── ...
```

---

## 💸 So machst du Geld damit

1. Digital Product erstellen
2. Marketing-Paket dazu generieren
3. 2–3 Shorts-Skripte schreiben, die das Produkt bewerben
4. Bei Gumroad / Etsy hochladen (9–15 € Single, 24–39 € Bundle)
5. Shorts posten → Traffic → Verkäufe

Viele Creator verdienen mit genau diesem Modell 1.000–5.000 €+ pro Monat.

---

## 🔧 Erweitern

Neue Produkttypen → `modules/digital_products/generator.py`  
Neue Marketing-Vorlagen → `modules/marketing/generator.py`  
Neue Shorts-Stile → `modules/shorts/generator.py`

---

## Lizenz

MIT – mach damit was du willst (auch kommerziell).

---

**Viel Erfolg beim Geld drucken.** 💰
