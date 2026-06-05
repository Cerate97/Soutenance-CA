from pathlib import Path
import textwrap
import streamlit as st

# =====================================================
# Configuration page
# =====================================================
st.set_page_config(
    page_title="Soutenance - Rapport de stage",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# Informations à personnaliser
# =====================================================
NOM_ETUDIANTE = "Cérate Lauréance AGNIKPE"
FORMATION = "Master 1 APE – parcours DSMI"
ANNEE_UNIVERSITAIRE = "2025-2026"

TUTEUR_ENTREPRISE = "Laurent Billoudet"
TUTEUR_PEDAGOGIQUE = "Federica Ceron"

ENTREPRISE = "Thuasne"
SERVICE = "Pôle Data"
PROJET = "Application Tracings US"

TRACINGS_APP_URL = "https://app.snowflake.com/streamlit/mrtemyi/xe52060/#/apps/h46dxjb4hig26lge2sn5"

# =====================================================
# Indicateurs projet
# =====================================================
TEMPS_AVANT = "24h ou plus"
TEMPS_DEBUT = "≈ 30 min"
TEMPS_ACTUEL = "5 à 10 min"

TAUX_MATCHING_TEST = "91 %"
NB_CLIENTS_TEST = "771"
NB_MATCHES_TEST = "704"
NB_UNMATCHED_TEST = "67"

# =====================================================
# Chemins
# =====================================================
BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"

LOGO_ECOLE = ASSETS_DIR / "logo_ecole.png"
LOGO_THUASNE = ASSETS_DIR / "logo_thuasne.png"

# =====================================================
# Couleurs
# =====================================================
ECOLE_PRIMARY = "#3195A8"
ECOLE_SECONDARY = "#6EC6D6"

THUASNE_BLUE = "#005AA7"
THUASNE_NAVY = "#003D70"
THUASNE_RED = "#D71920"

DARK_TEXT = "#111827"
GREY_TEXT = "#4B5563"
LIGHT_BG = "#F8FAFC"

GREEN = "#10B981"
ORANGE = "#F59E0B"
BLUE_SOFT = "#EAF7FA"

# =====================================================
# CSS
# =====================================================
st.markdown(
    f"""
<style>
    :root {{
        --ecole-primary: {ECOLE_PRIMARY};
        --ecole-secondary: {ECOLE_SECONDARY};
        --thuasne-blue: {THUASNE_BLUE};
        --thuasne-navy: {THUASNE_NAVY};
        --thuasne-red: {THUASNE_RED};
        --dark-text: {DARK_TEXT};
        --grey-text: {GREY_TEXT};
        --light-bg: {LIGHT_BG};
        --green: {GREEN};
        --orange: {ORANGE};
        --blue-soft: {BLUE_SOFT};
    }}

    /* =====================================================
       Fond général
    ===================================================== */
    .stApp {{
        background:
            radial-gradient(circle at 0% 0%, rgba(49,149,168,0.14), transparent 28%),
            radial-gradient(circle at 100% 0%, rgba(110,198,214,0.16), transparent 32%),
            linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
    }}

    .block-container {{
        padding-top: 3.2rem !important;
        padding-bottom: 2rem !important;
        max-width: 1180px;
    }}

    /* =====================================================
       SIDEBAR - nouvelle harmonie visuelle
    ===================================================== */
    section[data-testid="stSidebar"] {{
        background:
            radial-gradient(circle at 10% 0%, rgba(110,198,214,0.35), transparent 25%),
            radial-gradient(circle at 90% 100%, rgba(49,149,168,0.30), transparent 25%),
            linear-gradient(180deg, #003D70 0%, #005AA7 48%, #064E69 100%);
        border-right: 1px solid rgba(255,255,255,0.18);
        box-shadow: 8px 0 28px rgba(15,23,42,0.10);
    }}

    section[data-testid="stSidebar"] > div {{
        padding-top: 1.3rem;
    }}

    /* Logo dans une petite carte blanche */
    section[data-testid="stSidebar"] img {{
        background: rgba(255,255,255,0.96);
        border-radius: 16px;
        padding: 8px;
        box-shadow: 0 10px 24px rgba(0,0,0,0.16);
        margin-bottom: 16px;
    }}

    /* Texte sidebar */
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {{
        color: rgba(255,255,255,0.94) !important;
        font-weight: 650;
    }}

    /* Radio group : menu sous forme de pills */
    section[data-testid="stSidebar"] div[role="radiogroup"] {{
        margin-top: 6px;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        background: rgba(255,255,255,0.075);
        border: 1px solid rgba(255,255,255,0.10);
        padding: 10px 12px;
        border-radius: 14px;
        margin-bottom: 7px;
        transition: all 0.22s ease-in-out;
        box-shadow: none;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.25);
        transform: translateX(3px);
    }}

    /* Élément sélectionné */
    section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {{
        background: linear-gradient(90deg, rgba(255,255,255,0.96), rgba(235,250,253,0.96));
        border: 1px solid rgba(255,255,255,0.95);
        border-left: 5px solid var(--ecole-secondary);
        box-shadow: 0 10px 24px rgba(0,0,0,0.18);
        transform: translateX(3px);
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p,
    section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) span {{
        color: var(--thuasne-navy) !important;
        font-weight: 850 !important;
    }}

    /* Couleur du bouton radio */
    section[data-testid="stSidebar"] input[type="radio"] {{
        accent-color: var(--ecole-secondary);
    }}

    /* Séparateur sidebar */
    section[data-testid="stSidebar"] hr {{
        border-color: rgba(255,255,255,0.20);
        margin-top: 18px;
        margin-bottom: 18px;
    }}

    /* Progression sidebar */
    section[data-testid="stSidebar"] .stProgress > div > div {{
        background-color: rgba(255,255,255,0.23) !important;
        border-radius: 999px;
        height: 8px;
    }}

    section[data-testid="stSidebar"] .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, var(--ecole-secondary), #FFFFFF) !important;
        border-radius: 999px;
    }}

    section[data-testid="stSidebar"] .stCaptionContainer,
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] {{
        color: rgba(255,255,255,0.75) !important;
    }}

    /* =====================================================
       Accueil
    ===================================================== */
    .top-pill {{
        display: inline-block;
        width: 100%;
        box-sizing: border-box;
        text-align: center;
        color: var(--grey-text);
        background: transparent;
        border: none;
        border-radius: 0;
        padding: 8px 0;
        font-size: 15px;
        font-weight: 750;
        margin-top: 8px;
    }}


    .hero-title {{
        font-size: 36px;
        line-height: 1.25;
        font-weight: 900;
        text-align: center;
        color: var(--dark-text);
        margin-top: 20px;
        margin-bottom: 14px;
        letter-spacing: -0.5px;
    }}

    .hero-subtitle {{
        font-size: 19px;
        line-height: 1.5;
        text-align: center;
        color: var(--grey-text);
        margin-bottom: 24px;
    }}

    .gradient-text {{
        background: linear-gradient(90deg, var(--ecole-primary), var(--ecole-secondary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    /* =====================================================
       Titres de pages
    ===================================================== */
    .section-wrap {{
        margin-bottom: 22px;
    }}

    .section-title {{
        font-size: 31px;
        line-height: 1.32;
        font-weight: 900;
        color: var(--dark-text);
        margin-top: 0;
        margin-bottom: 6px;
        padding-left: 15px;
        border-left: 6px solid var(--ecole-primary);
        letter-spacing: -0.3px;
    }}

    .section-subtitle {{
        font-size: 17px;
        line-height: 1.45;
        color: var(--grey-text);
        margin-left: 21px;
        margin-bottom: 0;
    }}

    /* =====================================================
       Bandeau principal
    ===================================================== */
    .hero-banner {{
        background:
            radial-gradient(circle at top right, rgba(255,255,255,0.22), transparent 30%),
            linear-gradient(135deg, var(--ecole-primary), var(--ecole-secondary));
        border-radius: 26px;
        padding: 28px;
        color: white;
        box-shadow: 0 18px 44px rgba(15,23,42,0.14);
        margin-bottom: 24px;
        position: relative;
        overflow: hidden;
    }}

    .hero-banner h2 {{
        color: white;
        font-size: 28px;
        line-height: 1.25;
        margin-top: 0;
        margin-bottom: 8px;
        font-weight: 900;
    }}

    .hero-banner p {{
        color: rgba(255,255,255,0.96);
        font-size: 16px;
        line-height: 1.55;
        max-width: 980px;
        margin-bottom: 0;
    }}

    /* =====================================================
       Cartes
    ===================================================== */
    .card,
    .accent-card,
    .problem-card,
    .success-card,
    .warning-card {{
        border-radius: 20px;
        padding: 21px;
        margin-bottom: 17px;
        min-height: 128px;
        overflow-wrap: break-word;
        transition: all 0.22s ease-in-out;
    }}

    .card {{
        background: rgba(255,255,255,0.97);
        border: 1px solid rgba(226,232,240,0.95);
        box-shadow: 0 9px 24px rgba(15,23,42,0.065);
    }}

    .card:hover,
    .accent-card:hover,
    .problem-card:hover,
    .success-card:hover,
    .warning-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(15,23,42,0.10);
    }}

    .accent-card {{
        background: linear-gradient(135deg, rgba(49,149,168,0.11), rgba(110,198,214,0.15));
        border: 1px solid rgba(49,149,168,0.23);
        border-left: 7px solid var(--ecole-primary);
        box-shadow: 0 9px 24px rgba(15,23,42,0.06);
    }}

    .problem-card {{
        background: rgba(255,255,255,0.97);
        border: 1px solid rgba(226,232,240,0.95);
        border-left: 7px solid var(--thuasne-red);
        box-shadow: 0 9px 24px rgba(15,23,42,0.06);
    }}

    .success-card {{
        background: rgba(16,185,129,0.10);
        border: 1px solid rgba(16,185,129,0.18);
        border-left: 7px solid var(--green);
    }}

    .warning-card {{
        background: rgba(245,158,11,0.12);
        border: 1px solid rgba(245,158,11,0.22);
        border-left: 7px solid var(--orange);
    }}

    .card h3,
    .accent-card h3,
    .problem-card h3,
    .success-card h3,
    .warning-card h3 {{
        color: var(--dark-text);
        font-size: 20px;
        line-height: 1.3;
        font-weight: 850;
        margin-top: 0;
        margin-bottom: 11px;
    }}

    .card p,
    .accent-card p,
    .problem-card p,
    .success-card p,
    .warning-card p {{
        color: var(--grey-text);
        font-size: 15.5px;
        line-height: 1.55;
        margin-bottom: 7px;
    }}

    .card ul,
    .accent-card ul,
    .problem-card ul,
    .success-card ul,
    .warning-card ul {{
        color: var(--grey-text);
        font-size: 15.5px;
        line-height: 1.45;
        padding-left: 21px;
        margin-bottom: 0;
    }}

    .card li,
    .accent-card li,
    .problem-card li,
    .success-card li,
    .warning-card li {{
        margin-bottom: 6px;
    }}

    .info-line {{
        margin: 6px 0;
        color: var(--grey-text);
        font-size: 15px;
    }}

    .info-line strong {{
        color: var(--dark-text);
    }}

    /* =====================================================
       KPI
    ===================================================== */
    .kpi-card {{
        background: rgba(255,255,255,0.98);
        border: 1px solid rgba(226,232,240,0.95);
        border-radius: 21px;
        padding: 20px 16px;
        margin-bottom: 18px;
        box-shadow: 0 9px 24px rgba(15,23,42,0.065);
        text-align: center;
        min-height: 136px;
        transition: all 0.22s ease-in-out;
    }}

    .kpi-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 14px 30px rgba(15,23,42,0.10);
    }}

    .kpi-icon {{
        font-size: 31px;
        margin-bottom: 2px;
    }}

    .kpi-value {{
        font-size: 30px;
        font-weight: 900;
        color: var(--ecole-primary);
        line-height: 1.2;
    }}

    .kpi-label {{
        color: var(--grey-text);
        font-size: 14.3px;
        line-height: 1.35;
        margin-top: 7px;
    }}

    /* =====================================================
       Architecture
    ===================================================== */
    .flow-card {{
        background: rgba(255,255,255,0.98);
        border: 1px solid rgba(226,232,240,0.95);
        border-radius: 18px;
        padding: 18px;
        min-height: 118px;
        margin-bottom: 16px;
        text-align: center;
        box-shadow: 0 8px 22px rgba(15,23,42,0.055);
    }}

    .flow-number {{
        width: 34px;
        height: 34px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--ecole-primary), var(--ecole-secondary));
        color: white;
        font-weight: 900;
        display: inline-flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 10px;
    }}

    .flow-title {{
        color: var(--dark-text);
        font-weight: 850;
        font-size: 16px;
        margin-bottom: 6px;
    }}

    .flow-text {{
        color: var(--grey-text);
        font-size: 14.3px;
        line-height: 1.4;
    }}

    /* =====================================================
       Bouton
    ===================================================== */
    div[data-testid="stLinkButton"] a {{
        background: linear-gradient(90deg, var(--ecole-primary), var(--ecole-secondary)) !important;
        color: white !important;
        border-radius: 15px !important;
        border: none !important;
        font-weight: 850 !important;
        font-size: 18px !important;
        padding: 0.9rem 1rem !important;
        box-shadow: 0 12px 25px rgba(49,149,168,0.26);
    }}

    div[data-testid="stLinkButton"] a:hover {{
        transform: translateY(-2px);
        box-shadow: 0 16px 32px rgba(49,149,168,0.35);
    }}

    .footer {{
        text-align: center;
        color: #6B7280;
        font-size: 13.5px;
        margin-top: 30px;
        padding-top: 14px;
        border-top: 1px solid #E5E7EB;
    }}

    @media screen and (max-width: 900px) {{
        .hero-title {{
            font-size: 30px;
        }}

        .section-title {{
            font-size: 27px;
        }}

        .hero-subtitle {{
            font-size: 17px;
        }}
    }}
</style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# Fonctions UI
# =====================================================
def clean_html(content):
    return textwrap.dedent(str(content)).strip()


def html(content):
    st.markdown(clean_html(content), unsafe_allow_html=True)


def divider():
    st.divider()


def page_title(title, subtitle=None):
    if subtitle:
        html(
            f"""
<div class="section-wrap">
    <div class="section-title">{title}</div>
    <div class="section-subtitle">{subtitle}</div>
</div>
            """
        )
    else:
        html(
            f"""
<div class="section-wrap">
    <div class="section-title">{title}</div>
</div>
            """
        )


def card(title, body, css_class="card"):
    body = clean_html(body)
    html(
        f"""
<div class="{css_class}">
    <h3>{title}</h3>
    {body}
</div>
        """
    )


def kpi_card(value, label, icon):
    html(
        f"""
<div class="kpi-card">
    <div class="kpi-icon">{icon}</div>
    <div class="kpi-value">{value}</div>
    <div class="kpi-label">{label}</div>
</div>
        """
    )


def flow_card(number, title, text):
    html(
        f"""
<div class="flow-card">
    <div class="flow-number">{number}</div>
    <div class="flow-title">{title}</div>
    <div class="flow-text">{text}</div>
</div>
        """
    )


def footer():
    html(
        f"""
<div class="footer">
    🎓 Soutenance de stage — {NOM_ETUDIANTE} — {ENTREPRISE}
</div>
        """
    )


def display_sidebar_logo():
    if LOGO_ECOLE.exists():
        st.sidebar.image(str(LOGO_ECOLE), width=120)
    else:
        st.sidebar.caption("Logo école non trouvé")


def display_home_logos():
    col_logo_ecole, col_center, col_logo_thuasne = st.columns([1.25, 3.7, 1.25])

    with col_logo_ecole:
        if LOGO_ECOLE.exists():
            st.image(str(LOGO_ECOLE), width=240)
        else:
            st.caption("Logo école non trouvé")

    with col_center:
        html(
            f"""
<div class="top-pill">
    🎓 Soutenance de stage · {FORMATION}
</div>
            """
        )

    with col_logo_thuasne:
        if LOGO_THUASNE.exists():
            st.image(str(LOGO_THUASNE), width=170)
        else:
            st.caption("Logo Thuasne non trouvé")


# =====================================================
# Pages
# =====================================================
def page_accueil():
    display_home_logos()

    html(
        """
<div class="hero-title">
Optimisation du pilotage de la performance par la Data & la Business Intelligence:
<br>
<span class="gradient-text">Automatisation du matching client des Tracings US chez Thuasne</span>
</div>
        """
    )


    html(
        """
<div class="hero-subtitle">
    Une application Streamlit intégrée à Snowflake pour accélérer,
    fiabiliser et tracer le traitement des données commerciales partenaires.
</div>
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        card(
            "👩‍💻 Présenté par",
            f"""
<p class="info-line"><strong>{NOM_ETUDIANTE}</strong></p>
<p class="info-line">Année universitaire : <strong>{ANNEE_UNIVERSITAIRE}</strong></p>
<p class="info-line">Formation : <strong>{FORMATION}</strong></p>
            """
        )

    with col2:
        card(
            "🏢 Cadre du stage",
            f"""
<p class="info-line">Entreprise : <strong>{ENTREPRISE}</strong></p>
<p class="info-line">Service : <strong>{SERVICE}</strong></p>
<p class="info-line">Projet : <strong>{PROJET}</strong></p>
            """
        )

    col3, col4 = st.columns(2)

    with col3:
        card(
            "🤝 Encadrement",
            f"""
<p class="info-line">Tuteur entreprise : <strong>{TUTEUR_ENTREPRISE}</strong></p>
<p class="info-line">Tuteur pédagogique : <strong>{TUTEUR_PEDAGOGIQUE}</strong></p>
            """
        )

    with col4:
        card(
            "🎯 Objectif général",
            """
<p>
Transformer un traitement long et manuel en un processus plus rapide,
plus fiable et exploitable pour le pilotage commercial.
</p>
            """,
            "accent-card"
        )

    footer()


def page_contexte():
    page_title(
        "Thuasne & contexte du projet",
        "Un projet data au service de la fiabilisation des données commerciales."
    )

    col1, col2 = st.columns(2)

    with col1:
        card(
            "🏢 Présentation de Thuasne",
            """
<p>
Thuasne est une entreprise spécialisée dans les dispositifs médicaux :
compression médicale, orthopédie, maintien, mobilité et rééducation.
</p>
<p>
Dans un contexte international, la fiabilité des données commerciales est essentielle
pour suivre l’activité, analyser la performance et accompagner la prise de décision.
</p>
            """,
            "accent-card"
        )

    with col2:
        card(
            "📊 Pôle d’intervention : Data",
            """
<p>
Le stage s’inscrit au sein du pôle Data, qui accompagne les équipes métier
dans la collecte, la structuration, la fiabilisation et l’exploitation des données.
</p>
<p>
Le pôle intervient sur la Business Intelligence, l’automatisation des traitements,
la qualité des données et l’intégration d’outils comme Snowflake, Python et Streamlit.
</p>
            """,
            "accent-card"
        )

    divider()

    col1, col2 = st.columns(2)

    with col1:
        card(
            "📌 Contexte métier : les Tracings US",
            """
<p>
Les fichiers Tracings US sont transmis par plusieurs partenaires.
Ils contiennent des données commerciales qui doivent être rapprochées
avec les référentiels internes avant d’être exploitées.
</p>
<p>
Ces données permettent de suivre les ventes indirectes, d’alimenter les analyses
commerciales et de fiabiliser certains indicateurs utilisés pour le pilotage.
</p>
            """
        )

    with col2:
        card(
            "❌ Situation initiale",
            """
<ul>
<li>Attente des fichiers des 4 partenaires avant traitement global</li>
<li>Traitement d’un fichier pouvant prendre 24h ou plus</li>
<li>Nombreuses corrections manuelles</li>
<li>Clients parfois difficiles à identifier</li>
<li>Risque d’erreur dans le rattachement client</li>
<li>Traçabilité limitée des corrections</li>
</ul>
            """,
            "problem-card"
        )

    card(
        "❓ Problématique",
        """
<p style="font-size:18px;">
Comment automatiser et fiabiliser le traitement des Tracings US afin de réduire les délais,
limiter les corrections manuelles et fournir une donnée client fiable pour le pilotage commercial ?
</p>
        """,
        "problem-card"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "⚙️ Automatiser",
            """
<p>Permettre le traitement indépendant des fichiers partenaires, sans attendre la réception des quatre fichiers.</p>
            """
        )

    with col2:
        card(
            "🔎 Fiabiliser",
            """
<p>Améliorer le matching client et identifier clairement les cas non reconnus ou ambigus.</p>
            """
        )

    with col3:
        card(
            "📊 Exploiter",
            """
<p>Centraliser les données dans Snowflake et les rendre disponibles pour les analyses BI.</p>
            """
        )

    footer()


def page_solution():
    page_title(
        "Solution développée",
        "Une application Streamlit intégrée à Snowflake pour structurer le traitement de bout en bout."
    )

    card(
        "✅ Principe de la solution",
        """
<p>
L’application permet de charger un fichier partenaire, contrôler les données,
réaliser le matching client, gérer les cas unmatched ou ambiguous,
enrichir le référentiel et sauvegarder les résultats dans Snowflake.
</p>
        """,
        "success-card"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "📥 Chargement & contrôle",
            """
<p>
L’utilisatrice charge le fichier dès qu’il est disponible.
Le format et les données sont préparés avant traitement.
</p>
            """
        )

    with col2:
        card(
            "🔎 Matching client",
            """
<p>
L’application recherche automatiquement le client correspondant
à partir des référentiels disponibles.
</p>
            """
        )

    with col3:
        card(
            "🧩 Référentiel enrichi",
            """
<p>
Les corrections validées alimentent le référentiel,
ce qui réduit progressivement les cas non matchés.
</p>
            """
        )

    divider()

    st.subheader("Architecture simplifiée")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        flow_card("1", "Fichier partenaire", "PEL, Cascade, SPS ou Frontline")

    with col2:
        flow_card("2", "Application", "Chargement, contrôle et matching via Streamlit")

    with col3:
        flow_card("3", "Snowflake", "Stockage, référentiels et historisation")

    with col4:
        flow_card("4", "Vue agrégée", "Format unique pour l’exploitation BI")

    divider()

    st.subheader("Technologies utilisées")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        card("🐍 Python / Pandas", "<p>Traitement et transformation des données.</p>")

    with col2:
        card("🌐 Streamlit", "<p>Interface web interactive pour les utilisateurs.</p>")

    with col3:
        card("❄️ Snowflake", "<p>Stockage, vues et référentiels.</p>")

    with col4:
        card("☁️ Azure Function", "<p>Suggestions de matching lorsque nécessaire.</p>")

    footer()


def page_resultats():
    page_title(
        "Résultats & impacts",
        "Des gains observés sur le temps de traitement, la qualité du matching et la traçabilité."
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        kpi_card(TEMPS_AVANT, "Temps de traitement initial d’un fichier", "⏱️")

    with col2:
        kpi_card(TEMPS_DEBUT, "Temps au début du dispositif", "🚀")

    with col3:
        kpi_card(TEMPS_ACTUEL, "Temps observé après enrichissement du référentiel", "✅")

    with col4:
        kpi_card(TAUX_MATCHING_TEST, "Taux de matching observé sur un fichier test", "🔎")

    divider()

    col1, col2 = st.columns(2)

    with col1:
        card(
            "📈 Avant / Après",
            """
<ul>
<li>Avant : attente des 4 partenaires avant traitement global</li>
<li>Après : traitement indépendant des fichiers</li>
<li>Avant : traitement pouvant dépasser 24h</li>
<li>Après : traitement observé entre 5 et 10 minutes</li>
<li>Amélioration progressive grâce aux corrections précédentes</li>
</ul>
            """,
            "success-card"
        )

    with col2:
        card(
            "📊 Exemple observé",
            f"""
<ul>
<li>{NB_CLIENTS_TEST} identifiants clients analysés</li>
<li>{NB_MATCHES_TEST} clients automatiquement matchés</li>
<li>{NB_UNMATCHED_TEST} clients non reconnus automatiquement</li>
<li>Taux de matching d’environ {TAUX_MATCHING_TEST}</li>
</ul>
            """,
            "accent-card"
        )

    card(
        "🎯 Impact métier",
        """
<p>
Le dispositif améliore la fiabilité du rattachement client, réduit les corrections manuelles
et facilite l’exploitation des données pour les analyses commerciales,
les commissions et le pilotage de la performance.
</p>
        """,
        "accent-card"
    )

    footer()


def page_demonstration():
    page_title(
        "Démonstration",
        "Présentation de l’application Tracings US dans son environnement Snowflake."
    )

    html(
        """
<div class="hero-banner">
<h2>🚀 Démonstration en conditions réelles</h2>
<p>
Cette partie sera réalisée directement dans l’application.
L’objectif est de montrer concrètement le traitement d’un fichier,
le matching client et la gestion des cas non reconnus.
</p>
</div>
        """
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        card(
            "Scénario de démonstration",
            """
<ul>
<li>Chargement d’un fichier partenaire</li>
<li>Lancement du traitement</li>
<li>Visualisation des résultats</li>
<li>Gestion des cas unmatched ou ambiguous</li>
<li>Sauvegarde dans Snowflake</li>
</ul>
            """
        )

    with col2:
        card(
            "Accès à l’application",
            """
<p>
Le bouton ci-dessous ouvre l’application Tracings US.
L’accès nécessite une authentification Snowflake.
</p>
            """,
            "accent-card"
        )

        st.link_button(
            "🚀 Lancer l’application Tracings US",
            TRACINGS_APP_URL,
            use_container_width=True
        )

    footer()


def page_bilan():
    page_title(
        "Bilan & perspectives",
        "Synthèse des apports du projet et pistes d’amélioration."
    )

    col1, col2 = st.columns(2)

    with col1:
        card(
            "✅ Apports du projet",
            """
<ul>
<li>Réduction du temps de traitement</li>
<li>Traitement indépendant des fichiers partenaires</li>
<li>Fiabilisation du matching client</li>
<li>Meilleure traçabilité des données</li>
<li>Données exploitables dans Snowflake et la BI</li>
</ul>
            """,
            "success-card"
        )

    with col2:
        card(
            "🔭 Perspectives",
            """
<ul>
<li>Suivre le taux de matching par partenaire</li>
<li>Renforcer la journalisation des corrections</li>
<li>Industrialiser davantage le traitement</li>
<li>Étendre la logique à d’autres flux similaires</li>
</ul>
            """,
            "accent-card"
        )

    divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "💻 Compétences techniques",
            """
<ul>
<li>Python / Pandas</li>
<li>Streamlit</li>
<li>Snowflake</li>
<li>SQL</li>
<li>Traitement Excel</li>
</ul>
            """
        )

    with col2:
        card(
            "📊 Compétences data",
            """
<ul>
<li>Qualité des données</li>
<li>Matching client</li>
<li>Historisation</li>
<li>Exploitation BI</li>
</ul>
            """
        )

    with col3:
        card(
            "🤝 Compétences transversales",
            """
<ul>
<li>Analyse du besoin</li>
<li>Autonomie</li>
<li>Rigueur</li>
<li>Communication</li>
<li>Documentation</li>
</ul>
            """
        )

    footer()


def page_conclusion():
    page_title(
        "Conclusion",
        "Une mission concrète au service de l’automatisation, de la qualité des données et du pilotage commercial."
    )

    card(
        "✅ Synthèse",
        """
<p>
Ce projet a permis de transformer un processus initialement long,
manuel et dépendant de plusieurs fichiers partenaires en un dispositif
plus rapide, plus fiable et mieux intégré à l’environnement Data de Thuasne.
</p>
<p>
L’application Tracings US permet désormais de traiter les fichiers indépendamment,
de fiabiliser le matching client et d’alimenter une donnée structurée
dans Snowflake pour les usages BI.
</p>
        """,
        "success-card"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        card(
            "🎯 Apport métier",
            """
<p>
Réduction des délais et meilleure fiabilité des données commerciales.
</p>
            """
        )

    with col2:
        card(
            "💻 Apport technique",
            """
<p>
Développement d’une application data avec Python, Streamlit et Snowflake.
</p>
            """
        )

    with col3:
        card(
            "📊 Apport décisionnel",
            """
<p>
Données plus fiables pour le reporting, les commissions et le pilotage commercial.
</p>
            """
        )

    html(
        """
<div class="hero-title" style="margin-top:34px;">
Merci pour votre attention
</div>
<div class="hero-subtitle">
Avez-vous des questions ?
</div>
        """
    )

    footer()


# =====================================================
# Navigation
# =====================================================

PAGES = {
    "Accueil": page_accueil,
    "Thuasne & contexte": page_contexte,
    "Solution développée": page_solution,
    "Résultats & impacts": page_resultats,
    "Démonstration": page_demonstration,
    "Bilan & perspectives": page_bilan,
    "Conclusion": page_conclusion,
}

page = st.sidebar.radio(
    "Navigation",
    list(PAGES.keys()),
    label_visibility="collapsed"
)

st.sidebar.markdown("---")
progression = (list(PAGES.keys()).index(page) + 1) / len(PAGES)
st.sidebar.progress(progression)
st.sidebar.caption("Progression de la présentation")

PAGES[page]()
