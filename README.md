# 💰 Ultimate Money Printer 3000

**Das ultimative System, um digitale Produkte vollautomatisch zu erzeugen und zu verkaufen.**

Erstelle in Sekunden professionelle PDF-Produkte (Habit Tracker, Budget-Planer, Content-Kalender, Journal, Checklisten usw.), generiere fertige Verkaufstexte + Tags und packe alles in ready-to-upload Sales Packages für Gumroad, Etsy und Payhip.

> Von der Idee bis zum verkaufsfertigen Produkt in unter 60 Sekunden.

---

## ⚡ Features (Ultimate Edition)

- **Mehrere Produkttypen** out of the box
  - 30/90-Tage Habit Tracker
  - Wochen- & Monatsplaner
  - Budget / Finance Tracker
  - Content-Kalender (Creator)
  - Gratitude / Mental Health Journal
  - Meal Planner + Einkaufsliste
  - Allgemeine Checklisten
- **Batch-Modus** → erzeuge 5–20 Varianten auf einmal (verschiedene Farben & Titel)
- **Automatische Sales Packages**
  - Fertige PDF
  - Produkt-Titel
  - Lange Beschreibung (Gumroad/Etsy-ready)
  - Tags / Keywords
  - Preis-Empfehlung
- **Schöne, moderne Designs** mit mehreren Farbthemes
- **CLI + Interaktiver Modus**
- Extrem leicht erweiterbar

---

## 🚀 Installation

```bash
git clone https://github.com/landnevermore/money-printer-3000.git
cd money-printer-3000
pip install -r requirements.txt
```

---

## 💻 Nutzung

### Interaktiver Modus (einfachste Variante)
```bash
python money_printer.py
```

### Direkte Generierung
```bash
# Ein einzelnes Produkt
python money_printer.py --type habit --title "30-Tage Fokus Challenge" --color teal

# Batch-Modus (5 Varianten)
python money_printer.py --type habit --batch 5

# Budget-Planer in Rose
python money_printer.py --type budget --color rose --title "Mein Finanz-Planer 2026"
```

### Verfügbare Produkttypen
| Typ          | Beschreibung                     |
|--------------|----------------------------------|
| `habit`      | Habit Tracker (30/90 Tage)       |
| `weekly`     | Wochenplaner                     |
| `budget`     | Budget- & Ausgaben-Tracker       |
| `content`    | Content-Kalender für Creator     |
| `journal`    | Gratitude / Reflexions-Journal   |
| `meal`       | Meal Planner + Einkaufsliste     |
| `checklist`  | Allgemeine Checklisten           |

### Verfügbare Farben
`navy` · `teal` · `purple` · `rose` · `forest` · `slate` · `coral` · `indigo`

---

## 📦 Was du nach dem Generieren bekommst

Jedes Produkt landet in einem eigenen Ordner unter `output/`:

```
output/
├── 30-Tage_Fokus_Challenge_teal/
│   ├── product.pdf              ← das fertige Produkt
│   ├── title.txt                ← fertiger Produkttitel
│   ├── description.txt          ← lange Verkaufsbeschreibung
│   ├── tags.txt                 ← Keywords für Etsy/Gumroad
│   └── pricing.txt              ← Preisempfehlung + Tipps
```

Du kannst den kompletten Ordner-Inhalt quasi 1:1 bei Gumroad/Etsy hochladen.

---

## 💸 So machst du richtig Geld damit (Ultimate Playbook)

1. **Batch generieren**  
   `python money_printer.py --type habit --batch 10`

2. **Beste Varianten aussuchen** und bei Gumroad / Etsy einstellen  
   Empfohlener Preis: **9–14 €** (Single) oder **24–29 €** (Bundle)

3. **Traffic-Quellen die funktionieren**
   - TikTok / Reels: "Ich habe in 60 Sekunden ein digitales Produkt erstellt"
   - Pinterest (sehr stark für Planner)
   - Reddit (r/passive_income, r/Entrepreneur, r/Etsy)
   - X / Threads
   - Kleine bezahlte Ads (Meta / Pinterest) sobald du 3–5 Produkte hast

4. **Skalieren**
   - Mache 15–30 Varianten pro Kategorie
   - Erstelle Bundles ("Complete Productivity Pack")
   - Biete "Lifetime Updates" an
   - Später: eigene kleine Storefront (Stan Store, Gumroad Collections, etc.)

Viele Creator verdienen mit genau diesem Modell 1.000–5.000€+ pro Monat, sobald sie 20–40 Produkte live haben.

---

## 🔧 Erweitern

Neue Produkttypen kannst du sehr einfach in `money_printer.py` unter `PRODUCT_TEMPLATES` hinzufügen.

---

## Lizenz

MIT – mach damit was du willst (auch kommerziell).

---

**Viel Erfolg beim Geld drucken.**  
Wenn du die ersten 500€ damit verdient hast, lass es mich wissen.
