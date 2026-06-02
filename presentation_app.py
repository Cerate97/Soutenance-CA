from pathlib import Path
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
SERVICE = "Pôle IA & Data"
PROJET = "Application Tracings US"

TRACINGS_APP_URL = "https://app.snowflake.com/streamlit/mrtemyi/xe52060/#/apps/h46dxjb4hig26lge2sn5"

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
ECOLE_DARK = "#514B50"

THUASNE_BLUE = "#005AA7"
THUASNE_RED = "#D71920"

DARK_TEXT = "#1F2937"
LIGHT_BG = "#F8FAFC"
GREY_TEXT = "#4B5563"

# =====================================================
# CSS
# =====================================================
st.markdown(
    f"""
    <style>
        :root {{
            --ecole-primary: {ECOLE_PRIMARY};
            --ecole-secondary: {ECOLE_SECONDARY};
            --ecole-dark: {ECOLE_DARK};
            --thuasne-blue: {THUASNE_BLUE};
            --thuasne-red: {THUASNE_RED};
            --dark-text: {DARK_TEXT};
            --light-bg: {LIGHT_BG};
            --grey-text: {GREY_TEXT};
        }}

        .stApp {{
            background:
                radial-gradient(circle at top left, rgba(49,149,168,0.12), transparent 30%),
                radial-gradient(circle at top right, rgba(110,198,214,0.18), transparent 34%),
                linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%);
        }}

        .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 2rem;
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background: linear-gradient(180deg, var(--thuasne-blue) 0%, #003E73 100%);
        }}

        section[data-testid="stSidebar"] * {{
            color: white !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label {{
            padding: 8px 10px;
            border-radius: 10px;
            transition: 0.2s ease-in-out;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
            background: rgba(255,255,255,0.16);
        }}

        .top-label {{
            text-align: center;
            color: var(--grey-text);
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 5px;
        }}

        .hero-title {{
            font-size: 43px;
            line-height: 1.12;
            font-weight: 900;
            text-align: center;
            color: var(--dark-text);
            margin-top: 8px;
            margin-bottom: 8px;
        }}

        .hero-subtitle {{
            font-size: 22px;
            text-align: center;
            color: var(--grey-text);
            margin-bottom: 24px;
        }}

        .gradient-text {{
            background: linear-gradient(90deg, var(--ecole-primary), var(--ecole-secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .section-title {{
            font-size: 34px;
            font-weight: 850;
            color: var(--dark-text);
            margin-bottom: 8px;
        }}

        .section-subtitle {{
            font-size: 18px;
            color: var(--grey-text);
            margin-bottom: 24px;
        }}

        .hero-banner {{
            background: linear-gradient(135deg, var(--ecole-primary), var(--ecole-secondary));
            border-radius: 26px;
            padding: 30px;
            color: white;
            box-shadow: 0 18px 45px rgba(15,23,42,0.16);
            margin-bottom: 26px;
            position: relative;
            overflow: hidden;
        }}

        .hero-banner:after {{
            content: "";
            position: absolute;
            right: -45px;
            top: -45px;
            width: 175px;
            height: 175px;
            border-radius: 50%;
            background: rgba(255,255,255,0.16);
        }}

        .hero-banner h2 {{
            color: white;
            font-size: 30px;
            margin-bottom: 8px;
        }}

        .hero-banner p {{
            color: rgba(255,255,255,0.94);
            font-size: 17px;
            max-width: 950px;
        }}

        .glass-card {{
            background: rgba(255,255,255,0.94);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(229,231,235,0.95);
            border-radius: 20px;
            padding: 24px;
            box-shadow: 0 12px 30px rgba(15,23,42,0.08);
            margin-bottom: 20px;
            transition: all 0.25s ease-in-out;
            min-height: 160px;
        }}

        .glass-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 16px 38px rgba(15,23,42,0.13);
        }}

        .accent-card {{
            background: linear-gradient(135deg, rgba(49,149,168,0.12), rgba(110,198,214,0.16));
            border: 1px solid rgba(49,149,168,0.22);
            border-left: 7px solid var(--ecole-primary);
            border-radius: 20px;
            padding: 26px;
            box-shadow: 0 12px 30px rgba(15,23,42,0.07);
            margin-bottom: 20px;
        }}

        .problem-card {{
            background: rgba(255,255,255,0.94);
            border-left: 7px solid var(--thuasne-red);
            border-radius: 18px;
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: 0 10px 24px rgba(15,23,42,0.06);
        }}

        .success-card {{
            background: rgba(16,185,129,0.09);
            border-left: 7px solid #10B981;
            border-radius: 18px;
            padding: 22px;
            margin-bottom: 18px;
        }}

        .info-line {{
            margin: 6px 0;
            color: var(--grey-text);
            font-size: 15px;
        }}

        .info-line strong {{
            color: var(--dark-text);
        }}

        .timeline {{
            position: relative;
            padding-left: 25px;
            margin-top: 10px;
        }}

        .timeline-item {{
            border-left: 3px solid var(--ecole-primary);
            padding-left: 18px;
            padding-bottom: 18px;
            position: relative;
        }}

        .timeline-item:before {{
            content: "";
            width: 14px;
            height: 14px;
            background: var(--ecole-secondary);
            border-radius: 50%;
            position: absolute;
            left: -8.5px;
            top: 4px;
            box-shadow: 0 0 0 5px rgba(110,198,214,0.22);
        }}

        .timeline-title {{
            font-weight: 800;
            color: var(--dark-text);
            font-size: 17px;
        }}

        .timeline-text {{
            color: var(--grey-text);
            font-size: 15px;
        }}

        div[data-testid="stLinkButton"] a {{
            background: linear-gradient(90deg, var(--ecole-primary), var(--ecole-secondary)) !important;
            color: white !important;
            border-radius: 14px !important;
            border: none !important;
            font-weight: 800 !important;
            font-size: 18px !important;
            padding: 0.85rem 1rem !important;
            box-shadow: 0 12px 25px rgba(49,149,168,0.28);
            transition: all 0.25s ease-in-out;
        }}

        div[data-testid="stLinkButton"] a:hover {{
            transform: translateY(-2px);
            box-shadow: 0 16px 35px rgba(49,149,168,0.38);
        }}

        .footer {{
            text-align: center;
            color: #6B7280;
            font-size: 14px;
            margin-top: 40px;
            padding-top: 15px;
            border-top: 1px solid #E5E7EB;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# Fonctions UI
# =====================================================
def display_sidebar_logo():
    if LOGO_ECOLE.exists():
        st.sidebar.image(str(LOGO_ECOLE), width=135)
    else:
        st.sidebar.caption("Logo école non trouvé")
def display_home_logos():
    st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    col_logo_ecole, col_center, col_logo_thuasne = st.columns(
        [1.4, 4, 1.4],
        vertical_alignment="center"
    )

    with col_logo_ecole:
        if LOGO_ECOLE.exists():
            st.image(str(LOGO_ECOLE), width=300)
        else:
            st.caption("Logo école non trouvé")

    with col_center:
        st.markdown(
            f"""
            <div class="top-label">
                🎓Soutenance de stage · {FORMATION}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_logo_thuasne:
        if LOGO_THUASNE.exists():
            st.image(str(LOGO_THUASNE), width=200)
        else:
            st.caption("Logo Thuasne non trouvé")


def page_title(title, subtitle=None):
    st.markdown(
        f"""
        <div class="section-title">{title}</div>
        """,
        unsafe_allow_html=True
    )

    if subtitle:
        st.markdown(
            f"""
            <div class="section-subtitle">{subtitle}</div>
            """,
            unsafe_allow_html=True
        )


def footer():
    st.markdown(
        f"""
        <div class="footer">
            🎓Soutenance de stage — {NOM_ETUDIANTE} — {ENTREPRISE}
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# Sidebar
# =====================================================
display_sidebar_logo()


pages = [
    "Accueil",
    "Contexte & objectifs",
    "Solution développée",
    "Démonstration Tracings US",
    "Bilan & conclusion"
]

page = st.sidebar.radio(
    "Navigation",
    pages,
    label_visibility="collapsed"
)

progression = {
    "Accueil": 0.15,
    "Contexte & objectifs": 0.35,
    "Solution développée": 0.55,
    "Démonstration Tracings US": 0.75,
    "Bilan & conclusion": 1.0
}

st.sidebar.markdown("---")
st.sidebar.progress(progression[page])
st.sidebar.caption("Progression de la présentation")

# =====================================================
# Page 1 - Accueil
# =====================================================
if page == "Accueil":
    display_home_logos()

    st.markdown(
        """
        <div class="hero-title">
            Optimisation du pilotage de la performance
            <br>
            <span class="gradient-text">par la Data & la Business Intelligence</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-subtitle">
            Automatisation du matching client des Tracings US chez Thuasne
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-banner">
            <h2>Présentation de soutenance</h2>
            <p>
                Cette présentation synthétise le contexte du stage, la problématique rencontrée,
                la solution développée et introduit la démonstration de l’application Tracings US
                hébergée sur Snowflake.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="glass-card">
                <h3>👩‍💻 Présenté par</h3>
                <p class="info-line"><strong>{NOM_ETUDIANTE}</strong></p>
                <p class="info-line">Rapport de stage</p>
                <p class="info-line">Année universitaire : <strong>{ANNEE_UNIVERSITAIRE}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="glass-card">
                <h3>🎓 Formation</h3>
                <p class="info-line"><strong>{FORMATION}</strong></p>
                <p class="info-line">Saint-Étienne School of Economics</p>
                <p class="info-line">Parcours orienté data, statistiques et modélisation.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            f"""
            <div class="glass-card">
                <h3>🏢 Entreprise d’accueil</h3>
                <p class="info-line"><strong>{ENTREPRISE}</strong></p>
                <p class="info-line">{SERVICE}</p>
                <p class="info-line">Projet : <strong>{PROJET}</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="glass-card">
                <h3>🤝 Encadrement</h3>
                <p class="info-line">Tuteur professionnel : <strong>{TUTEUR_ENTREPRISE}</strong></p>
                <p class="info-line">Tuteur pédagogique : <strong>{TUTEUR_PEDAGOGIQUE}</strong></p>
                <p class="info-line">Suivi du projet et accompagnement méthodologique.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    footer()

# =====================================================
# Page 2 - Contexte & objectifs
# =====================================================
elif page == "Contexte & objectifs":
    
    page_title(
            "Contexte et objectifs du projet",
        )
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(
            """
            <div class="accent-card">
                <h3>📌 Contexte métier</h3>
                <p>
                    Les fichiers <strong>Tracings US</strong> sont transmis par des partenaires
                    ou distributeurs. Ils contiennent des données commerciales qui doivent être
                    nettoyées, rapprochées avec les référentiels internes, puis intégrées dans
                    Snowflake pour être exploitées par les équipes métier.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="problem-card">
                <h3>❓ Problématique</h3>
                <p>
                    Comment automatiser et fiabiliser le traitement des fichiers Tracings US
                    afin de réduire les corrections manuelles et améliorer l’exploitation des
                    données commerciales ?
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <h3>⚠️ Limites initiales</h3>
                <ul>
                    <li>Traitements manuels longs</li>
                    <li>Risque d’erreurs</li>
                    <li>Clients difficiles à identifier</li>
                    <li>Référentiels à maintenir</li>
                    <li>Besoin d’exports fiables</li>
                    <li>Centralisation dans Snowflake</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("Objectifs du projet")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <h3>⚙️ Automatiser</h3>
                <p>Réduire les manipulations manuelles lors du traitement des fichiers.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <h3>🔎 Fiabiliser</h3>
                <p>Améliorer le matching client et identifier les lignes non reconnues.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="glass-card">
                <h3>📊 Exploiter</h3>
                <p>Sauvegarder les données dans Snowflake et produire des exports exploitables.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    footer()

# =====================================================
# Page 3 - Solution développée
# =====================================================
elif page == "Solution développée":
    page_title(
        "Solution développée",
        "Une application Streamlit connectée à l’environnement data de Thuasne."
    )

    st.markdown(
        """
        <div class="success-card">
            <h3>✅ Principe général</h3>
            <p>
                L’application Tracings US centralise les étapes clés du traitement :
                import du fichier, nettoyage, matching client, gestion des unmatched,
                mise à jour des référentiels, export Excel et sauvegarde dans Snowflake.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Technologies utilisées")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <h3>🐍 Python / Pandas</h3>
                <p>Traitement, nettoyage et transformation des données.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <h3>🌐 Streamlit</h3>
                <p>Interface web interactive pour les utilisateurs métier.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="glass-card">
                <h3>❄️ Snowflake</h3>
                <p>Stockage, consultation et mise à jour des données.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown(
            """
            <div class="glass-card">
                <h3>☁️ Azure Function</h3>
                <p>Suggestions de matching lorsque le référentiel ne suffit pas.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.markdown(
            """
            <div class="glass-card">
                <h3>📄 OpenPyXL</h3>
                <p>Lecture et génération des fichiers Excel.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col6:
        st.markdown(
            """
            <div class="glass-card">
                <h3>🤖 ThuasneGPT</h3>
                <p>Support interne pour optimiser certains scripts et structurer le rapport.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("Workflow simplifié")

    st.markdown(
        """
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-title">1. Import du fichier partenaire</div>
                <div class="timeline-text">Chargement du fichier Excel contenant les Tracings US.</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-title">2. Nettoyage et préparation</div>
                <div class="timeline-text">Contrôle des colonnes, transformation des données et calculs nécessaires.</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-title">3. Matching client</div>
                <div class="timeline-text">Recherche dans les référentiels Snowflake et appel Azure si besoin.</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-title">4. Correction et validation</div>
                <div class="timeline-text">Gestion des clients non reconnus et mise à jour des référentiels.</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-title">5. Export et sauvegarde</div>
                <div class="timeline-text">Génération d’un fichier Excel et insertion des données dans Snowflake.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    footer()

# =====================================================
# Page 4 - Lancer l'application
# =====================================================
elif page == "Démonstration Tracings US":
    page_title(
        "Démonstration de l’application Tracings US"

    )

    st.markdown(
        """
        <div class="hero-banner">
            <h2>🚀 Démonstration en conditions réelles</h2>
            <p>
                Cette partie permet d’ouvrir l’application Tracings US hébergée sur Snowflake.
                Les explications détaillées seront réalisées directement dans l’application.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <h3>Ce qui sera présenté</h3>
                <ul>
                    <li>Chargement d’un fichier de tracing</li>
                    <li>Lancement du matching</li>
                    <li>Analyse des résultats</li>
                    <li>Gestion des clients non reconnus</li>
                    <li>Mise à jour des référentiels</li>
                    <li>Export et sauvegarde dans Snowflake</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="accent-card">
                <h3>Accès à l’application</h3>
                <p>
                    Le bouton ci-dessous ouvre directement l’application Tracings US.
                    L’accès  nécessite une authentification Snowflake.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.link_button(
            "🚀 Lancer l’application Tracings US",
            TRACINGS_APP_URL,
            use_container_width=True
        )

    footer()

# =====================================================
# Page 5 - Bilan & conclusion
# =====================================================
elif page == "Bilan & conclusion":
    page_title(
        "Bilan et conclusion",
        "Synthèse des apports du projet et des compétences développées."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="glass-card">
                <h3>📈 Apports métier</h3>
                <ul>
                    <li>Réduction des traitements manuels</li>
                    <li>Fiabilisation du matching client</li>
                    <li>Meilleure traçabilité</li>
                    <li>Exports exploitables</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="glass-card">
                <h3>💻 Compétences techniques</h3>
                <ul>
                    <li>Python</li>
                    <li>Pandas</li>
                    <li>Streamlit</li>
                    <li>SQL / Snowflake</li>
                    <li>Excel / OpenPyXL</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="glass-card">
                <h3>🤝 Compétences transversales</h3>
                <ul>
                    <li>Autonomie</li>
                    <li>Rigueur</li>
                    <li>Documentation</li>
                    <li>Communication</li>
                    <li>Analyse des besoins</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.markdown(
        """
        <div class="success-card">
            <h3>Conclusion</h3>
            <p>
                Ce stage m’a permis de participer à un projet concret autour de la donnée,
                de l’automatisation et de la Business Intelligence.
                L’application Tracings US répond à un besoin métier réel en améliorant
                la fiabilité, la rapidité et la traçabilité du traitement des fichiers partenaires.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-title">
            Merci pour votre attention
        </div>
        <div class="hero-subtitle">
            Avez-vous des questions ?
        </div>
        """,
        unsafe_allow_html=True
    )

    footer()
