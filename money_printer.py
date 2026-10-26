#!/usr/bin/env python3
"""
Ultimate Money Printer 3000
Vollautomatischer Digital-Product Generator + Sales Package Creator
"""

from fpdf import FPDF
from datetime import datetime
import os
import argparse
import random
import textwrap

# ============================================================
# FARBTHEMES
# ============================================================
COLORS = {
    "navy":   (30, 58, 95),
    "teal":   (15, 118, 110),
    "purple": (88, 28, 135),
    "rose":   (159, 18, 57),
    "forest": (20, 83, 45),
    "slate":  (51, 65, 85),
    "coral":  (194, 65, 12),
    "indigo": (67, 56, 202),
}

# ============================================================
# PRODUKT-TEMPLATES
# ============================================================
PRODUCT_TEMPLATES = {
    "habit": {
        "default_title": "30-Tage Habit Tracker",
        "subtitle": "Baue starke Gewohnheiten auf und werde die beste Version von dir",
        "pages": ["cover", "habit_30", "habit_90", "weekly", "notes"],
        "tags": ["habit tracker", "gewohnheiten", "produktivität", "self improvement", "planner", "printable", "digital download"],
        "price": "9.90",
    },
    "weekly": {
        "default_title": "Wochenplaner Undatiert",
        "subtitle": "Plane deine Woche klar, fokussiert und stressfrei",
        "pages": ["cover", "weekly", "weekly", "notes", "notes"],
        "tags": ["wochenplaner", "weekly planner", "undatiert", "produktivität", "organisation", "printable"],
        "price": "8.90",
    },
    "budget": {
        "default_title": "Budget & Finanz Tracker",
        "subtitle": "Behalte den Überblick über Einnahmen, Ausgaben und Sparziele",
        "pages": ["cover", "budget", "budget", "notes"],
        "tags": ["budget planner", "finanzplaner", "geld sparen", "ausgaben tracker", "finance", "printable"],
        "price": "11.90",
    },
    "content": {
        "default_title": "Content Kalender für Creator",
        "subtitle": "Plane deine Inhalte strategisch und werde konsistent",
        "pages": ["cover", "content", "content", "notes"],
        "tags": ["content calendar", "content planner", "creator", "social media", "instagram", "tiktok", "youtube"],
        "price": "12.90",
    },
    "journal": {
        "default_title": "Gratitude & Reflexions Journal",
        "subtitle": "Tägliche Dankbarkeit und bewusste Reflexion für mehr Lebensqualität",
        "pages": ["cover", "journal", "journal", "journal", "notes"],
        "tags": ["gratitude journal", "dankbarkeitstagebuch", "mental health", "self care", "journal", "printable"],
        "price": "9.90",
    },
    "meal": {
        "default_title": "Meal Planner + Einkaufsliste",
        "subtitle": "Plane deine Mahlzeiten und spare Zeit & Geld",
        "pages": ["cover", "meal", "meal", "notes"],
        "tags": ["meal planner", "essensplaner", "einkaufsliste", "meal prep", "gesund essen", "printable"],
        "price": "8.90",
    },
    "checklist": {
        "default_title": "Ultimate Checklisten Pack",
        "subtitle": "Für Umzug, Reisen, Business-Launch und den Alltag",
        "pages": ["cover", "checklist", "checklist", "notes"],
        "tags": ["checkliste", "checklist", "organisation", "umzug", "reisen", "printable", "digital download"],
        "price": "7.90",
    },
}

# ============================================================
# PDF GENERATOR
# ============================================================
class UltimatePDF(FPDF):
    def __init__(self, color_name="navy"):
        super().__init__()
        self.color = COLORS.get(color_name, COLORS["navy"])
        self.set_auto_page_break(auto=True, margin=18)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 10, f"Seite {self.page_no()}", align="C")

    def _section_title(self, text):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*self.color)
        self.cell(0, 12, text, ln=True)
        self.ln(2)

    def add_cover(self, title, subtitle):
        self.add_page()
        # Top color block
        self.set_fill_color(*self.color)
        self.rect(0, 0, 210, 95, "F")

        self.set_y(38)
        self.set_font("Helvetica", "B", 26)
        self.set_text_color(255, 255, 255)
        self.multi_cell(0, 11, title, align="C")

        self.ln(6)
        self.set_font("Helvetica", "", 13)
        self.multi_cell(0, 7, subtitle, align="C")

        self.set_y(155)
        self.set_text_color(90, 90, 90)
        self.set_font("Helvetica", "", 11)
        self.cell(0, 8, "Digitales Produkt · Sofort nutzbar", align="C")
        self.ln(6)
        self.set_font("Helvetica", "I", 10)
        self.cell(0, 8, datetime.now().strftime("%B %Y"), align="C")

    def add_habit_30(self):
        self.add_page()
        self._section_title("30-Tage Habit Tracker")

        habits = ["Sport / Bewegung", "Lesen (20 Min)", "Meditieren", "Wasser trinken",
                  "Früh schlafen", "Deep Work", "Dankbarkeit", "Gesund essen"]

        self.set_font("Helvetica", "B", 8)
        self.set_fill_color(*self.color)
        self.set_text_color(255, 255, 255)
        self.cell(48, 7, "Habit", border=1, fill=True)
        for d in range(1, 8):
            self.cell(18, 7, str(d), border=1, align="C", fill=True)
        self.ln()

        self.set_text_color(40, 40, 40)
        self.set_font("Helvetica", "", 8)
        for h in habits:
            self.cell(48, 8, h, border=1)
            for _ in range(7):
                self.cell(18, 8, "", border=1)
            self.ln()

        self.ln(8)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.multi_cell(0, 5, "Tipp: Drucke die Seite aus oder nutze sie digital. Kreuze jeden Tag ab.")

    def add_habit_90(self):
        self.add_page()
        self._section_title("90-Tage Übersicht")

        self.set_font("Helvetica", "", 9)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 6, "Nutze diese Seite, um deinen Fortschritt über 3 Monate zu tracken.\n")

        months = ["Monat 1", "Monat 2", "Monat 3"]
        for m in months:
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(*self.color)
            self.cell(0, 9, m, ln=True)
            self.set_draw_color(200, 200, 200)
            for _ in range(4):
                self.cell(0, 8, "", border="B", ln=True)
            self.ln(4)

    def add_weekly(self):
        self.add_page()
        self._section_title("Wochenplaner")

        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        for day in days:
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(*self.color)
            self.cell(0, 8, day, ln=True)
            self.set_draw_color(210, 210, 210)
            for _ in range(3):
                self.cell(0, 7, "", border="B", ln=True)
            self.ln(2)

    def add_budget(self):
        self.add_page()
        self._section_title("Budget Tracker")

        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*self.color)
        self.cell(0, 8, "Monatliche Übersicht", ln=True)
        self.ln(2)

        headers = ["Kategorie", "Geplant", "Ausgegeben", "Differenz"]
        widths = [55, 35, 40, 40]

        self.set_fill_color(*self.color)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 9)
        for h, w in zip(headers, widths):
            self.cell(w, 8, h, border=1, fill=True, align="C")
        self.ln()

        self.set_text_color(40, 40, 40)
        self.set_font("Helvetica", "", 9)
        categories = ["Wohnen", "Lebensmittel", "Transport", "Freizeit", "Abos", "Sparen", "Sonstiges"]
        for cat in categories:
            self.cell(widths[0], 8, cat, border=1)
            for w in widths[1:]:
                self.cell(w, 8, "", border=1)
            self.ln()

        self.ln(10)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*self.color)
        self.cell(0, 8, "Sparziele", ln=True)
        self.set_draw_color(200, 200, 200)
        for _ in range(5):
            self.cell(0, 8, "", border="B", ln=True)

    def add_content(self):
        self.add_page()
        self._section_title("Content Kalender")

        self.set_font("Helvetica", "", 9)
        self.set_text_color(60, 60, 60)
        self.multi_cell(0, 5, "Plane deine Inhalte für die nächste Woche / den nächsten Monat.\n")

        platforms = ["Instagram / Reels", "TikTok", "YouTube", "X / Threads", "Blog / Newsletter"]
        for p in platforms:
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(*self.color)
            self.cell(0, 8, p, ln=True)
            self.set_draw_color(210, 210, 210)
            for _ in range(3):
                self.cell(0, 7, "", border="B", ln=True)
            self.ln(3)

    def add_journal(self):
        self.add_page()
        self._section_title("Tägliches Journal")

        prompts = [
            "Wofür bin ich heute dankbar?",
            "Was ist heute gut gelaufen?",
            "Was kann ich morgen besser machen?",
            "Wie fühle ich mich gerade?",
            "Eine Sache, die ich heute gelernt habe:",
        ]

        for prompt in prompts:
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(*self.color)
            self.cell(0, 8, prompt, ln=True)
            self.set_draw_color(220, 220, 220)
            for _ in range(3):
                self.cell(0, 7, "", border="B", ln=True)
            self.ln(4)

    def add_meal(self):
        self.add_page()
        self._section_title("Meal Planner")

        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
        meals = ["Frühstück", "Mittag", "Abend"]

        for day in days:
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(*self.color)
            self.cell(0, 7, day, ln=True)
            self.set_font("Helvetica", "", 9)
            self.set_text_color(60, 60, 60)
            for m in meals:
                self.cell(30, 6, m + ":", border=0)
                self.cell(0, 6, "", border="B", ln=True)
            self.ln(2)

    def add_checklist(self):
        self.add_page()
        self._section_title("Checkliste")

        self.set_font("Helvetica", "", 10)
        self.set_text_color(50, 50, 50)

        for i in range(1, 16):
            self.cell(8, 8, "□", border=0)
            self.cell(0, 8, "" , border="B", ln=True)

    def add_notes(self):
        self.add_page()
        self._section_title("Notizen & Ideen")

        self.set_draw_color(220, 220, 220)
        for _ in range(20):
            self.cell(0, 8, "", border="B", ln=True)


# ============================================================
# SALES TEXT GENERATOR
# ============================================================
def generate_sales_texts(product_type: str, title: str, color: str):
    template = PRODUCT_TEMPLATES[product_type]

    description = f"""✨ {title}

{template['subtitle']}

Was du bekommst:
• Professionell gestaltete PDF (sofort nutzbar)
• Modernes, cleanes Design in der Farbe {color.capitalize()}
• Undatiert → jedes Jahr wiederverwendbar
• Ideal zum Ausdrucken oder digital Ausfüllen (GoodNotes, Notability, etc.)

Perfekt für alle, die produktiver, organisierter und bewusster leben wollen.

Sofortiger Download nach dem Kauf.
""".strip()

    tags = ", ".join(template["tags"] + [color, "digital product", "instant download", "pdf"])

    pricing = f"""Empfohlener Preis: {template['price']} €

Tipps:
- Single Produkt: {template['price']} €
- Bundle (3–5 Produkte): 24–29 €
- "Complete Pack": 39 €

Gumroad und Etsy funktionieren beide sehr gut für diese Art von Produkten.
""".strip()

    return {
        "title": title,
        "description": description,
        "tags": tags,
        "pricing": pricing,
    }


# ============================================================
# HAUPT-FUNKTION
# ============================================================
def create_product(product_type: str, title: str = None, color: str = "navy", output_base="output"):
    if product_type not in PRODUCT_TEMPLATES:
        raise ValueError(f"Unbekannter Typ: {product_type}")

    template = PRODUCT_TEMPLATES[product_type]
    title = title or template["default_title"]
    subtitle = template["subtitle"]

    pdf = UltimatePDF(color)

    page_map = {
        "cover": lambda: pdf.add_cover(title, subtitle),
        "habit_30": pdf.add_habit_30,
        "habit_90": pdf.add_habit_90,
        "weekly": pdf.add_weekly,
        "budget": pdf.add_budget,
        "content": pdf.add_content,
        "journal": pdf.add_journal,
        "meal": pdf.add_meal,
        "checklist": pdf.add_checklist,
        "notes": pdf.add_notes,
    }

    for page in template["pages"]:
        if page in page_map:
            page_map[page]()

    # Ordner anlegen
    safe_title = "".join(c if c.isalnum() or c in "- _" else "" for c in title).strip().replace(" ", "_")
    folder_name = f"{safe_title}_{color}"
    folder_path = os.path.join(output_base, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    pdf_path = os.path.join(folder_path, "product.pdf")
    pdf.output(pdf_path)

    # Sales Texte generieren
    sales = generate_sales_texts(product_type, title, color)

    with open(os.path.join(folder_path, "title.txt"), "w", encoding="utf-8") as f:
        f.write(sales["title"])

    with open(os.path.join(folder_path, "description.txt"), "w", encoding="utf-8") as f:
        f.write(sales["description"])

    with open(os.path.join(folder_path, "tags.txt"), "w", encoding="utf-8") as f:
        f.write(sales["tags"])

    with open(os.path.join(folder_path, "pricing.txt"), "w", encoding="utf-8") as f:
        f.write(sales["pricing"])

    return folder_path


def main():
    parser = argparse.ArgumentParser(description="Ultimate Money Printer 3000")
    parser.add_argument("--type", choices=list(PRODUCT_TEMPLATES.keys()), help="Produkttyp")
    parser.add_argument("--title", type=str, help="Eigener Titel")
    parser.add_argument("--color", choices=list(COLORS.keys()), default="navy", help="Farbtheme")
    parser.add_argument("--batch", type=int, help="Anzahl Varianten (Batch-Modus)")
    args = parser.parse_args()

    print("\n" + "="*55)
    print("   💰  ULTIMATE MONEY PRINTER 3000")
    print("   Full Automation Edition")
    print("="*55 + "\n")

    # Interaktiver Modus
    if not args.type and not args.batch:
        print("Verfügbare Produkttypen:")
        for i, t in enumerate(PRODUCT_TEMPLATES.keys(), 1):
            print(f"  {i}. {t}")
        choice = input("\nTyp wählen (Name oder Nummer): ").strip().lower()
        if choice.isdigit():
            keys = list(PRODUCT_TEMPLATES.keys())
            args.type = keys[int(choice)-1] if 1 <= int(choice) <= len(keys) else "habit"
        else:
            args.type = choice if choice in PRODUCT_TEMPLATES else "habit"

        args.title = input(f"Titel (Enter = Standard '{PRODUCT_TEMPLATES[args.type]['default_title']}'): ").strip() or None

        print("\nFarben:", ", ".join(COLORS.keys()))
        color_in = input("Farbe (Enter = navy): ").strip().lower()
        args.color = color_in if color_in in COLORS else "navy"

        batch_in = input("Batch-Modus? Wie viele Varianten? (Enter = 1): ").strip()
        args.batch = int(batch_in) if batch_in.isdigit() and int(batch_in) > 0 else 1

    product_type = args.type or "habit"
    batch_count = args.batch or 1

    print(f"\nGeneriere {batch_count}x '{product_type}' ...\n")

    created = []
    color_list = list(COLORS.keys())

    for i in range(batch_count):
        color = args.color if batch_count == 1 else random.choice(color_list)
        title = args.title

        if batch_count > 1 and not title:
            # leichte Variation der Titel im Batch
            base = PRODUCT_TEMPLATES[product_type]["default_title"]
            variants = [
                base,
                f"{base} – Premium",
                f"Minimal {base}",
                f"{base} 2026",
                f"Ultimate {base}",
            ]
            title = variants[i % len(variants)]

        folder = create_product(product_type, title, color)
        created.append(folder)
        print(f"  ✅ {folder}")

    print("\n" + "="*55)
    print(f"Fertig! {len(created)} Sales Package(s) erstellt.")
    print("Schau in den Ordner 'output/'")
    print("="*55 + "\n")
    print("Nächster Schritt:")
    print("1. Öffne einen der Ordner")
    print("2. Lade product.pdf + die Textdateien bei Gumroad/Etsy hoch")
    print("3. Preis aus pricing.txt nehmen")
    print("4. Geld verdienen 💸\n")


if __name__ == "__main__":
    main()
