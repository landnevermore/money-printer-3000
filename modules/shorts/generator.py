"""Faceless Shorts Script + Package Generator (Text-first, erweiterbar)"""
from pathlib import Path
from core.utils import safe_filename, write_text
from core.config import OUTPUT_DIR

def generate_shorts_script(topic: str, style: str = "educational") -> dict:
    """Erzeugt ein fertiges Shorts-Skript (Hook + Body + CTA)."""

    scripts = {
        "educational": {
            "hook": f"Die meisten wissen das nicht über {topic}...",
            "body": f"Hier sind 3 Dinge, die du über {topic} wissen solltest:\n1. Es ist einfacher als du denkst.\n2. Du brauchst keine teuren Tools.\n3. Konsistenz schlägt Perfektion.\n\nGenau deshalb funktioniert es.",
            "cta": "Speichere das Video und setze es heute noch um. Folge für mehr.",
        },
        "story": {
            "hook": f"Ich habe {topic} komplett unterschätzt.",
            "body": f"Am Anfang dachte ich, das bringt nichts. Nach 30 Tagen war alles anders. Hier ist, was ich gelernt habe und was du sofort anwenden kannst.",
            "cta": "Willst du den genauen Plan? Schreib 'Plan' in die Kommentare.",
        },
        "product": {
            "hook": f"Ich habe in unter 60 Sekunden ein digitales Produkt zu {topic} erstellt.",
            "body": f"Kein Design-Studium. Kein teures Tool. Einfach Idee → Generator → fertiges PDF + Verkaufstexte. Und das verkauft sich.",
            "cta": "Link zum Tool in der Bio. Probier's selbst.",
        },
    }

    base = scripts.get(style, scripts["educational"])
    full_script = f"HOOK:\n{base['hook']}\n\nBODY:\n{base['body']}\n\nCTA:\n{base['cta']}"

    return {
        "topic": topic,
        "style": style,
        "hook": base["hook"],
        "body": base["body"],
        "cta": base["cta"],
        "full_script": full_script,
        "caption": f"{base['hook']}\n\n{base['body']}\n\n{base['cta']}\n\n#{topic.replace(' ', '')} #shorts #faceless",
    }

def create_shorts_package(topic: str, style: str = "educational", count: int = 3):
    """Erzeugt mehrere Shorts-Skripte als fertiges Paket."""
    folder = OUTPUT_DIR / f"shorts_{safe_filename(topic)}"
    folder.mkdir(parents=True, exist_ok=True)

    styles = ["educational", "story", "product"]
    results = []
    for i in range(count):
        s = styles[i % len(styles)]
        script = generate_shorts_script(topic, s)
        write_text(folder / f"script_{i+1}_{s}.txt", script["full_script"])
        write_text(folder / f"caption_{i+1}.txt", script["caption"])
        results.append(script)

    overview = "\n\n".join([f"=== Short {i+1} ({r['style']}) ===\n{r['full_script']}" for i, r in enumerate(results)])
    write_text(folder / "all_scripts.txt", overview)

    return str(folder)
