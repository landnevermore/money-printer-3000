"""Bundle Generator – mehrere Assets zu einem Verkaufspaket"""
from pathlib import Path
from core.config import OUTPUT_DIR
from core.utils import safe_filename, write_text
import shutil

def create_bundle(name: str, source_folders: list[str], price: str = "29.00"):
    """Erstellt ein Bundle aus vorhandenen Output-Ordnern."""
    bundle_dir = OUTPUT_DIR / f"BUNDLE_{safe_filename(name)}"
    bundle_dir.mkdir(parents=True, exist_ok=True)

    included = []
    for src in source_folders:
        src_path = Path(src)
        if src_path.exists() and src_path.is_dir():
            dest = bundle_dir / src_path.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(src_path, dest)
            included.append(src_path.name)

    readme = f"""# {name}

Dieses Bundle enthält:

""" + "\n".join(f"- {i}" for i in included) + f"""

Empfohlener Preis: {price} €

Verkaufstipp:
- Als "Complete Pack" oder "Ultimate Bundle" positionieren
- Gut geeignet für Gumroad Collections oder Etsy Listings
"""
    write_text(bundle_dir / "BUNDLE_INFO.txt", readme)
    write_text(bundle_dir / "pricing.txt", f"Empfohlener Bundle-Preis: {price} €")

    return str(bundle_dir)
