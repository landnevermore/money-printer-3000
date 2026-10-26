"""Digital Products Generator – PDFs mit Sales Packages"""
from fpdf import FPDF
from datetime import datetime
from pathlib import Path
import random
from core.config import COLORS, OUTPUT_DIR
from core.utils import safe_filename, write_text

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
    "business": {
        "default_title": "Business Launch Planner",
        "subtitle": "Von der Idee bis zum ersten Kunden – strukturiert und klar",
        "pages": ["cover", "business", "notes", "notes"],
        "tags": ["business planner", "startup", "launch", "unternehmer", "business plan", "printable"],
        "price": "14.90",
    },
    "fitness": {
        "default_title": "Fitness & Workout Tracker",
        "subtitle": "Tracke Workouts, Fortschritte und bleib motiviert",
        "pages": ["cover", "fitness", "fitness", "notes"],
        "tags": ["fitness tracker", "workout", "gym", "training", "health", "printable"],
        "price": "9.90",
    },
}

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
        for m in ["Monat 1", "Monat 2", "Monat 3"]:
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
        for day in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]:
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
        for cat in ["Wohnen", "Lebensmittel", "Transport", "Freizeit", "Abos", "Sparen", "Sonstiges"]:
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
        for p in ["Instagram / Reels", "TikTok", "YouTube", "X / Threads", "Blog / Newsletter"]:
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
        for day in ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]:
            self.set_font("Helvetica", "B", 10)
            self.set_text_color(*self.color)
            self.cell(0, 7, day, ln=True)
            self.set_font("Helvetica", "", 9)
            self.set_text_color(60, 60, 60)
            for m in ["Frühstück", "Mittag", "Abend"]:
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
            self.cell(0, 8, "", border="B", ln=True)

    def add_business(self):
        self.add_page()
        self._section_title("Business Launch Plan")
        sections = [
            "1. Problem & Lösung",
            "2. Zielgruppe",
            "3. Angebot & Preis",
            "4. Erste Kunden gewinnen",
            "5. Nächste 30 Tage",
        ]
        for s in sections:
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(*self.color)
            self.cell(0, 9, s, ln=True)
            self.set_draw_color(210, 210, 210)
            for _ in range(4):
                self.cell(0, 7, "", border="B", ln=True)
            self.ln(4)

    def add_fitness(self):
        self.add_page()
        self._section_title("Workout Tracker")
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(*self.color)
        self.set_text_color(255, 255, 255)
        for h, w in [("Übung", 70), ("Sätze", 25), ("Wdh", 25), ("Gewicht", 30), ("Notiz", 40)]:
            self.cell(w, 8, h, border=1, fill=True, align="C")
        self.ln()
        self.set_text_color(40, 40, 40)
        self.set_font("Helvetica", "", 9)
        for _ in range(10):
            self.cell(70, 8, "", border=1)
            self.cell(25, 8, "", border=1)
            self.cell(25, 8, "", border=1)
            self.cell(30, 8, "", border=1)
            self.cell(40, 8, "", border=1)
            self.ln()

    def add_notes(self):
        self.add_page()
        self._section_title("Notizen & Ideen")
        self.set_draw_color(220, 220, 220)
        for _ in range(20):
            self.cell(0, 8, "", border="B", ln=True)


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
    return {"title": title, "description": description, "tags": tags, "pricing": pricing}


def create_product(product_type: str, title: str = None, color: str = "navy", batch_index: int = 0):
    if product_type not in PRODUCT_TEMPLATES:
        raise ValueError(f"Unbekannter Typ: {product_type}")

    template = PRODUCT_TEMPLATES[product_type]
    title = title or template["default_title"]
    if batch_index > 0 and not title:
        variants = [template["default_title"], f"{template['default_title']} – Premium",
                    f"Minimal {template['default_title']}", f"{template['default_title']} 2026"]
        title = variants[batch_index % len(variants)]

    pdf = UltimatePDF(color)
    page_map = {
        "cover": lambda: pdf.add_cover(title, template["subtitle"]),
        "habit_30": pdf.add_habit_30,
        "habit_90": pdf.add_habit_90,
        "weekly": pdf.add_weekly,
        "budget": pdf.add_budget,
        "content": pdf.add_content,
        "journal": pdf.add_journal,
        "meal": pdf.add_meal,
        "checklist": pdf.add_checklist,
        "business": pdf.add_business,
        "fitness": pdf.add_fitness,
        "notes": pdf.add_notes,
    }
    for page in template["pages"]:
        if page in page_map:
            page_map[page]()

    folder_name = f"{safe_filename(title)}_{color}"
    folder = OUTPUT_DIR / folder_name
    folder.mkdir(parents=True, exist_ok=True)

    pdf_path = folder / "product.pdf"
    pdf.output(str(pdf_path))

    sales = generate_sales_texts(product_type, title, color)
    write_text(folder / "title.txt", sales["title"])
    write_text(folder / "description.txt", sales["description"])
    write_text(folder / "tags.txt", sales["tags"])
    write_text(folder / "pricing.txt", sales["pricing"])

    return str(folder)


def list_product_types():
    return list(PRODUCT_TEMPLATES.keys())
