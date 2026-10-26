#!/usr/bin/env python3
"""
Money Printer 3000 - Super simpler Digital Product Generator
Erstellt schöne verkaufsfertige PDF-Planer in Sekunden.
"""

from fpdf import FPDF
from datetime import datetime
import os

# Farben (RGB)
COLORS = {
    "navy": (30, 58, 95),
    "teal": (15, 118, 110),
    "purple": (88, 28, 135),
    "rose": (159, 18, 57),
    "forest": (20, 83, 45),
    "slate": (51, 65, 85),
}

class PlannerPDF(FPDF):
    def __init__(self, color_name="navy"):
        super().__init__()
        self.color = COLORS.get(color_name, COLORS["navy"])
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Seite {self.page_no()}", align="C")

    def add_cover(self, title, subtitle):
        self.add_page()
        # Hintergrund-Farbe oben
        self.set_fill_color(*self.color)
        self.rect(0, 0, 210, 100, "F")

        self.set_y(40)
        self.set_font("Helvetica", "B", 28)
        self.set_text_color(255, 255, 255)
        self.multi_cell(0, 12, title, align="C")

        self.ln(8)
        self.set_font("Helvetica", "", 14)
        self.multi_cell(0, 8, subtitle, align="C")

        self.set_y(160)
        self.set_text_color(80, 80, 80)
        self.set_font("Helvetica", "", 11)
        self.cell(0, 8, "Erstellt mit Money Printer 3000", align="C")
        self.ln(6)
        self.cell(0, 8, datetime.now().strftime("%B %Y"), align="C")

    def add_habit_tracker(self, days=30):
        self.add_page()
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(*self.color)
        self.cell(0, 12, f"{days}-Tage Habit Tracker", ln=True)

        self.set_font("Helvetica", "", 10)
        self.set_text_color(60, 60, 60)
        self.ln(4)

        # Header
        self.set_fill_color(*self.color)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 9)
        self.cell(50, 8, "Habit", border=1, fill=True)
        for i in range(1, 8):
            self.cell(18, 8, str(i), border=1, align="C", fill=True)
        self.ln()

        self.set_text_color(40, 40, 40)
        self.set_font("Helvetica", "", 9)

        habits = ["Sport", "Lesen", "Meditieren", "Wasser trinken", "Früh schlafen", "Deep Work", "Dankbarkeit"]

        for habit in habits:
            self.cell(50, 9, habit, border=1)
            for _ in range(7):
                self.cell(18, 9, "", border=1)
            self.ln()

        self.ln(10)
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(100, 100, 100)
        self.multi_cell(0, 5, "Tipp: Drucke diese Seite aus oder nutze sie digital. Kreuze jeden Tag ab, an dem du die Gewohnheit geschafft hast.")

    def add_weekly_planner(self):
        self.add_page()
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(*self.color)
        self.cell(0, 12, "Wochenplaner", ln=True)
        self.ln(4)

        days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]

        for day in days:
            self.set_font("Helvetica", "B", 11)
            self.set_text_color(*self.color)
            self.cell(0, 8, day, ln=True)

            self.set_draw_color(200, 200, 200)
            for _ in range(3):
                self.cell(0, 8, "", border="B", ln=True)
            self.ln(3)

    def add_notes_page(self):
        self.add_page()
        self.set_font("Helvetica", "B", 18)
        self.set_text_color(*self.color)
        self.cell(0, 12, "Notizen & Reflexion", ln=True)
        self.ln(6)

        self.set_draw_color(220, 220, 220)
        for _ in range(18):
            self.cell(0, 9, "", border="B", ln=True)


def main():
    print("\n" + "="*50)
    print("   💰  MONEY PRINTER 3000")
    print("   Digital Product Generator")
    print("="*50 + "\n")

    title = input("Titel des Produkts (z.B. '30-Tage Habit Tracker'): ").strip() or "Mein Digitaler Planer"
    subtitle = input("Untertitel (z.B. 'Werde produktiver in 30 Tagen'): ").strip() or "Dein Weg zu besseren Gewohnheiten"

    print("\nVerfügbare Farben:")
    for i, name in enumerate(COLORS.keys(), 1):
        print(f"  {i}. {name}")
    color_choice = input("\nFarbe wählen (Name oder Nummer, Enter = navy): ").strip().lower()

    color_list = list(COLORS.keys())
    if color_choice.isdigit() and 1 <= int(color_choice) <= len(color_list):
        color_name = color_list[int(color_choice) - 1]
    elif color_choice in COLORS:
        color_name = color_choice
    else:
        color_name = "navy"

    print(f"\nErstelle PDF mit Farbe '{color_name}' ...")

    pdf = PlannerPDF(color_name)
    pdf.add_cover(title, subtitle)
    pdf.add_habit_tracker(30)
    pdf.add_weekly_planner()
    pdf.add_notes_page()

    # Output-Ordner
    os.makedirs("output", exist_ok=True)
    safe_name = "".join(c if c.isalnum() or c in "-_ " else "" for c in title).strip().replace(" ", "_")
    filename = f"output/{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"

    pdf.output(filename)

    print("\n" + "="*50)
    print(f"✅ Fertig! Deine PDF liegt hier:")
    print(f"   {filename}")
    print("="*50)
    print("\nNächster Schritt:")
    print("1. Öffne die PDF und prüfe sie")
    print("2. Gehe zu https://gumroad.com und lade sie hoch")
    print("3. Preis: 9–14 € empfehlen")
    print("4. Link teilen und Geld verdienen 💸\n")

if __name__ == "__main__":
    main()
