"""Lead Magnet Generator – Freebies + Opt-in Texte"""
from fpdf import FPDF
from pathlib import Path
from core.config import COLORS, OUTPUT_DIR
from core.utils import safe_filename, write_text
from datetime import datetime

class LeadPDF(FPDF):
    def __init__(self, color_name="teal"):
        super().__init__()
        self.color = COLORS.get(color_name, COLORS["teal"])

    def add_cover(self, title, subtitle):
        self.add_page()
        self.set_fill_color(*self.color)
        self.rect(0, 0, 210, 80, "F")
        self.set_y(30)
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(255, 255, 255)
        self.multi_cell(0, 10, title, align="C")
        self.ln(4)
        self.set_font("Helvetica", "", 12)
        self.multi_cell(0, 7, subtitle, align="C")
        self.set_y(120)
        self.set_text_color(80, 80, 80)
        self.set_font("Helvetica", "I", 11)
        self.cell(0, 8, "Kostenloser Download · Sofort nutzbar", align="C")

    def add_content_page(self, title, points):
        self.add_page()
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*self.color)
        self.cell(0, 12, title, ln=True)
        self.ln(4)
        self.set_font("Helvetica", "", 11)
        self.set_text_color(40, 40, 40)
        for p in points:
            self.multi_cell(0, 7, f"• {p}")
            self.ln(2)

def create_lead_magnet(title: str, niche: str = "produktivität", color: str = "teal"):
    """Erstellt ein kostenloses Lead-Magnet PDF + Opt-in Texte."""

    pdf = LeadPDF(color)
    pdf.add_cover(title, f"Dein kostenloser Einstieg in {niche}")

    points = [
        f"Die 3 größten Fehler bei {niche} und wie du sie vermeidest",
        "Eine einfache tägliche Routine, die wirklich funktioniert",
        "Welche Tools du brauchst (und welche nicht)",
        "Der 7-Tage Quick-Start Plan",
        "Bonus: Checkliste zum Abhaken",
    ]
    pdf.add_content_page("Was du in diesem Freebie lernst", points)

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(*pdf.color)
    pdf.cell(0, 10, "7-Tage Quick-Start", ln=True)
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(40, 40, 40)
    for day in range(1, 8):
        pdf.cell(0, 8, f"Tag {day}: _______________________________", ln=True)

    folder = OUTPUT_DIR / f"leadmagnet_{safe_filename(title)}"
    folder.mkdir(parents=True, exist_ok=True)
    pdf.output(str(folder / "lead_magnet.pdf"))

    optin = f"""Headline: Sichere dir deinen kostenlosen {title}

Subheadline: In wenigen Minuten zu mehr Klarheit bei {niche}.

Button: Jetzt kostenlos herunterladen

Dankesseite: Dein Freebie ist unterwegs! Schau in dein Postfach (auch Spam).

Email-Betreff: Dein {title} ist da 🎁
Email-Body: Hier ist dein kostenloses PDF. Viel Erfolg damit!
""".strip()

    write_text(folder / "optin_texte.txt", optin)
    write_text(folder / "beschreibung.txt", f"Kostenloses Lead-Magnet zu {niche}: {title}")

    return str(folder)
