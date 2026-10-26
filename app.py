"""
MoneyOS – Ultimate Money Printer Dashboard
All-in-One Tool für digitale Produkte, Marketing, Shorts, Lead Magnets & Bundles
"""
import streamlit as st
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from modules.digital_products import create_product, list_product_types, PRODUCT_TEMPLATES
from modules.marketing import generate_marketing_pack
from modules.shorts import create_shorts_package
from modules.lead_magnets import create_lead_magnet
from modules.bundles import create_bundle
from core.config import COLORS, OUTPUT_DIR

st.set_page_config(
    page_title="MoneyOS – Ultimate Money Printer",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# SESSION STATE & TUTORIAL
# ============================================================
if "tutorial_done" not in st.session_state:
    st.session_state.tutorial_done = False
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

def show_tutorial():
    st.title("👋 Willkommen bei MoneyOS")
    st.markdown("### Dein All-in-One Geld-Automations-System")

    st.info("Das Tutorial erscheint nur beim ersten Start. Du kannst es später jederzeit in der Sidebar erneut öffnen.")

    with st.expander("🚀 Was ist MoneyOS?", expanded=True):
        st.markdown("""
        MoneyOS hilft dir, **digitale Produkte zu erstellen**, **Marketing-Texte zu generieren**,  
        **Faceless Shorts-Skripte** zu schreiben, **Lead Magnets** zu bauen und alles zu **Bundles** zu schnüren –  
        alles lokal, kostenlos und ohne Abo.

        Du brauchst keine Design-Kenntnisse und keine teuren Tools.
        """)

    with st.expander("📦 Die Module im Überblick", expanded=True):
        st.markdown("""
        | Modul | Was es macht |
        |-------|--------------|
        | **Digital Products** | Professionelle PDFs (Planner, Tracker, Journals...) + fertige Verkaufstexte |
        | **Marketing** | Hooks, Captions, Hashtags, Email-Sequenzen, Pinterest-Texte |
        | **Shorts** | Faceless Shorts-Skripte (Hook + Body + CTA) für TikTok / Reels / YouTube |
        | **Lead Magnets** | Kostenlose Freebies + Opt-in Texte für Email-Listen |
        | **Bundles** | Mehrere Produkte zu einem teureren Paket zusammenpacken |
        """)

    with st.expander("💡 Empfohlener Workflow (so verdienst du Geld)", expanded=True):
        st.markdown("""
        1. **Digital Product** erstellen (z.B. Habit Tracker)
        2. Dazu **Marketing-Paket** generieren (Captions + Hooks)
        3. 2–3 **Shorts-Skripte** schreiben, die das Produkt bewerben
        4. Optional: **Lead Magnet** als Freebie anbieten
        5. Alles zu einem **Bundle** schnüren und bei Gumroad / Etsy hochladen
        6. Shorts posten → Traffic → Verkäufe

        Viele machen genau das und kommen auf 1.000–5.000 €+ pro Monat, sobald 20–40 Produkte live sind.
        """)

    with st.expander("⚙️ Erste Schritte", expanded=True):
        st.markdown("""
        1. Gehe links in der Sidebar auf **Digital Products**
        2. Wähle einen Typ (z.B. `habit`) und eine Farbe
        3. Klicke auf **Produkt generieren**
        4. Schau in den Ordner `output/` – dort liegt dein fertiges Sales Package
        5. Lade `product.pdf` + die Textdateien bei Gumroad oder Etsy hoch
        """)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✅ Tutorial verstanden – Los geht's!", use_container_width=True, type="primary"):
            st.session_state.tutorial_done = True
            st.rerun()

# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    st.title("💰 MoneyOS")
    st.caption("Ultimate Money Printer")

    page = st.radio(
        "Navigation",
        ["Dashboard", "Digital Products", "Marketing", "Shorts", "Lead Magnets", "Bundles", "Tutorial"],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("### Output")
    st.code(str(OUTPUT_DIR), language=None)
    if OUTPUT_DIR.exists():
        folders = [f.name for f in OUTPUT_DIR.iterdir() if f.is_dir()]
        st.caption(f"{len(folders)} Ordner im Output")

# ============================================================
# PAGES
# ============================================================
if page == "Tutorial" or not st.session_state.tutorial_done:
    show_tutorial()
    st.stop()

if page == "Dashboard":
    st.title("💰 MoneyOS Dashboard")
    st.markdown("Willkommen zurück. Wähle links ein Modul oder starte direkt:")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Produkt-Typen", len(list_product_types()))
    with c2:
        folders = list(OUTPUT_DIR.iterdir()) if OUTPUT_DIR.exists() else []
        st.metric("Generierte Pakete", len([f for f in folders if f.is_dir()]))
    with c3:
        st.metric("Module", 5)

    st.divider()
    st.subheader("Schnellstart")
    st.markdown("""
    - **Neues Produkt** → Digital Products
    - **Marketing dazu** → Marketing
    - **Shorts für Traffic** → Shorts
    - **Freebie für Email-Liste** → Lead Magnets
    - **Alles zusammenpacken** → Bundles
    """)

elif page == "Digital Products":
    st.title("📦 Digital Products")
    st.markdown("Erstelle professionelle PDF-Produkte inkl. fertiger Verkaufstexte.")

    col1, col2 = st.columns(2)
    with col1:
        ptype = st.selectbox("Produkt-Typ", list_product_types(),
                             format_func=lambda x: f"{x} – {PRODUCT_TEMPLATES[x]['default_title']}")
        title = st.text_input("Eigener Titel (optional)", placeholder=PRODUCT_TEMPLATES[ptype]["default_title"])
    with col2:
        color = st.selectbox("Farbe", list(COLORS.keys()))
        batch = st.number_input("Batch (Anzahl Varianten)", min_value=1, max_value=20, value=1)

    if st.button("🚀 Produkt generieren", type="primary", use_container_width=True):
        with st.spinner("Generiere..."):
            created = []
            color_list = list(COLORS.keys())
            for i in range(batch):
                c = color if batch == 1 else color_list[i % len(color_list)]
                t = title if title.strip() else None
                folder = create_product(ptype, t, c, batch_index=i)
                created.append(folder)
            st.success(f"{len(created)} Produkt(e) erstellt!")
            for f in created:
                st.code(f, language=None)

elif page == "Marketing":
    st.title("📣 Marketing Engine")
    st.markdown("Hooks, Captions, Hashtags, Email-Sequenzen und Pinterest-Texte.")

    product_title = st.text_input("Produkt-Titel", placeholder="30-Tage Habit Tracker")
    niche = st.text_input("Nische", value="produktivität")

    if st.button("✨ Marketing-Paket generieren", type="primary", use_container_width=True):
        if not product_title.strip():
            st.warning("Bitte einen Titel eingeben.")
        else:
            with st.spinner("Generiere Marketing-Assets..."):
                folder = generate_marketing_pack(product_title, niche=niche)
                st.success("Marketing-Paket erstellt!")
                st.code(folder, language=None)
                st.info("Enthält: hooks.txt, captions.txt, hashtags.txt, email_sequence.txt, pinterest.txt")

elif page == "Shorts":
    st.title("🎬 Faceless Shorts")
    st.markdown("Erzeuge fertige Shorts-Skripte (Hook + Body + CTA) für TikTok, Reels und YouTube Shorts.")

    topic = st.text_input("Thema", placeholder="digitale Produkte verkaufen")
    count = st.slider("Anzahl Skripte", 1, 10, 3)

    if st.button("🎥 Shorts-Paket generieren", type="primary", use_container_width=True):
        if not topic.strip():
            st.warning("Bitte ein Thema eingeben.")
        else:
            with st.spinner("Schreibe Skripte..."):
                folder = create_shorts_package(topic, count=count)
                st.success(f"{count} Shorts-Skripte erstellt!")
                st.code(folder, language=None)

elif page == "Lead Magnets":
    st.title("🎁 Lead Magnets")
    st.markdown("Kostenlose Freebies + Opt-in Texte für deine Email-Liste.")

    title = st.text_input("Titel des Freebies", placeholder="7-Tage Produktivitäts-Challenge")
    niche = st.text_input("Nische", value="produktivität")
    color = st.selectbox("Farbe", list(COLORS.keys()), index=1)

    if st.button("📥 Lead Magnet erstellen", type="primary", use_container_width=True):
        if not title.strip():
            st.warning("Bitte einen Titel eingeben.")
        else:
            with st.spinner("Erstelle Freebie..."):
                folder = create_lead_magnet(title, niche, color)
                st.success("Lead Magnet erstellt!")
                st.code(folder, language=None)
                st.info("Enthält: lead_magnet.pdf + optin_texte.txt")

elif page == "Bundles":
    st.title("📚 Bundles")
    st.markdown("Packe mehrere bereits generierte Ordner zu einem teureren Bundle zusammen.")

    name = st.text_input("Bundle-Name", placeholder="Ultimate Productivity Pack")
    price = st.text_input("Preis (€)", value="29.00")

    existing = []
    if OUTPUT_DIR.exists():
        existing = sorted([f.name for f in OUTPUT_DIR.iterdir() if f.is_dir() and not f.name.startswith("BUNDLE_")])

    selected = st.multiselect("Ordner auswählen (aus output/)", existing)

    if st.button("📦 Bundle erstellen", type="primary", use_container_width=True):
        if not name.strip() or not selected:
            st.warning("Name und mindestens einen Ordner angeben.")
        else:
            paths = [str(OUTPUT_DIR / s) for s in selected]
            with st.spinner("Erstelle Bundle..."):
                folder = create_bundle(name, paths, price)
                st.success("Bundle erstellt!")
                st.code(folder, language=None)
