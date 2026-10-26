"""Marketing Asset Generator – Captions, Hooks, Hashtags, Emails"""
from pathlib import Path
from core.utils import safe_filename, write_text
from core.config import OUTPUT_DIR

def generate_marketing_pack(product_title: str, product_type: str = "digital", niche: str = "produktivität"):
    """Erzeugt ein komplettes Marketing-Paket für ein Produkt."""

    hooks = [
        f"Ich habe in 60 Sekunden ein digitales Produkt erstellt – und verkaufe es jetzt.",
        f"Hör auf zu suchen. Hier ist der {product_title}, den du brauchst.",
        f"Die meisten verschwenden Zeit. Dieser {product_title} spart dir Stunden.",
        f"Von 0 auf verkaufsfertig in unter einer Minute. So geht's:",
        f"Warum kompliziert, wenn es so einfach geht? {product_title}",
    ]

    captions = [
        f"✨ {product_title}\n\nEndlich ein Tool, das wirklich hilft.\nUndatiert. Sofort nutzbar. Schön designed.\n\nLink in Bio 🔗\n\n#digitalproducts #passiveseinkommen #{niche}",
        f"Frisch erstellt und ready to sell 💸\n\n{product_title}\n\nPerfekt für alle, die produktiver werden wollen.\n\n#etsy #gumroad #digitaldownload",
        f"Kleine Investition. Großer Effekt.\n\n{product_title} – jetzt verfügbar.\n\n#productivity #planner #selfimprovement",
    ]

    hashtags = {
        "allgemein": "#digitalproducts #passiveseinkommen #onlinebusiness #sidehustle #etsy #gumroad",
        "produktiv": "#productivity #planner #habittracker #organization #selfimprovement",
        "finance": "#budget #moneytips #finance #sparen #geld",
        "health": "#selfcare #mentalhealth #fitness #wellness",
    }

    email_sequence = f"""Betreff 1: Dein neuer {product_title} ist da
Body: Hey, ich habe gerade etwas Neues veröffentlicht, das dir helfen kann: {product_title}. Schau es dir an – Link im Post.

Betreff 2: Noch unsicher?
Body: Viele nutzen den {product_title} bereits, um klarer und produktiver zu werden. Falls du noch Fragen hast, antworte einfach auf diese Mail.

Betreff 3: Letzte Chance + Bonus
Body: Nur noch kurze Zeit zum Launch-Preis. Danach geht der Preis hoch. Hol ihn dir jetzt.
""".strip()

    pinterest = f"""Titel: {product_title} – Sofort Download
Beschreibung: Schöner, undatierter {product_title}. Ideal zum Ausdrucken oder digital nutzen. Perfekt für mehr Struktur und Fokus. Sofortiger Download.
Board-Ideen: Digital Products, Productivity, Planners, Self Improvement
""".strip()

    folder = OUTPUT_DIR / f"marketing_{safe_filename(product_title)}"
    folder.mkdir(parents=True, exist_ok=True)

    write_text(folder / "hooks.txt", "\n\n".join(f"{i+1}. {h}" for i, h in enumerate(hooks)))
    write_text(folder / "captions.txt", "\n\n---\n\n".join(captions))
    write_text(folder / "hashtags.txt", "\n".join(f"{k}: {v}" for k, v in hashtags.items()))
    write_text(folder / "email_sequence.txt", email_sequence)
    write_text(folder / "pinterest.txt", pinterest)

    return str(folder)
