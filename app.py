import streamlit as st
import re
import os
import pandas as pd
from datetime import datetime

# 1. CONFIGURATION GLOBALE D'ORIGINE
st.set_page_config(page_title="Kimpese Software", page_icon="💻", layout="wide")

# Nom du fichier de stockage permanent
FICHIER_CSV = "prospects.csv"

# Fonction pour initialiser le fichier CSV avec des en-têtes s'il n'existe pas
def initialiser_csv():
    if not os.path.exists(FICHIER_CSV):
        df_initial = pd.DataFrame(columns=["Date d'inscription", "Emails Collectés"])
        df_initial.to_csv(FICHIER_CSV, index=False, encoding="utf-8")

# Fonction pour ajouter un e-mail dans le fichier CSV
def enregistrer_email_csv(email):
    initialiser_csv()
    date_actuelle = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nouvelle_ligne = pd.DataFrame([[date_actuelle, email]], columns=["Date d'inscription", "Emails Collectés"])
    nouvelle_ligne.to_csv(FICHIER_CSV, mode='a', header=False, index=False, encoding="utf-8")

# Fonction pour lire les e-mails enregistrés
def lire_emails_csv():
    initialiser_csv()
    try:
        return pd.read_csv(FICHIER_CSV, encoding="utf-8")
    except Exception:
        return pd.DataFrame(columns=["Date d'inscription", "Emails Collectés"])


# =====================================================================
# AJOUT : INJECTION DU STYLE POUR LE FOND NOIR RETRO HACKER
# =====================================================================
st.markdown("""
<style>
/* Applique le fond noir complet sur l'application */
.stApp {
    background-color: #0A0F17 !important;
    color: #F3F4F6 !important;
}
/* Force les zones de saisie à rester sombres avec bordure verte */
input, div[data-baseweb="input"], select, div[data-baseweb="select"] {
    background-color: #000000 !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
}
input[type="text"], input[type="password"] {
    color: #00FF00 !important;
    -webkit-text-fill-color: #00FF00 !important;
}
/* Aligne le style rétro des boutons */
button, .stButton>button {
    background-color: #051a05 !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
}
</style>
""", unsafe_allow_html=True)


# =====================================================================
# SECTION 1 : LOGO & DESIGN D'ORIGINE (TITRE CENTRÉ ET LOGO REPOUSSÉ)
# =====================================================================
st.markdown("<h3 style='text-align: center; color: #00FF00;'>KIMPESE SOFTWARE</h3>", unsafe_allow_html=True)

# Utilisation de proportions personnalisées (ex:) pour pousser vers la droite
col_pousse_gauche, col_img, col_wt, col_pousse_droite = st.columns([2, 1.2, 1.2, 1])

with col_img:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)

with col_wt:
    st.markdown("""
    <div style='text-align: center; border: 1px solid #00FF00; padding: 10px; background-color: #051a05; border-radius: 5px; width: 150px; margin-top: 10px;'>
        <span style='font-size: 22px; color: #FFFFFF; font-weight: bold;'>☀️ 85°F</span><br>
        <span style='color: #00FF00; font-size: 11px;'>● Live Weather</span>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("#### 🟢 Market Analysis Engine • Country: US")
st.write("Select your industry vertical:")


# =====================================================================
# SECTION 2 : LES 3 CARTES DE TARIFICATION ALIGNÉES CÔTE À CÔTE
# =====================================================================
col_card_1, col_card_2, col_card_3 = st.columns(3)

with col_card_1:
    st.markdown("""
    <div style='border: 1px solid #00FF00; padding: 15px; border-radius: 5px; background-color: #0A0F17; min-height: 150px;'>
        <div style='color: #00FF00; font-weight: bold;'>⚡ Starter Tracker</div>
        <p style='font-size: 13px; color: #9CA3AF; margin-top: 5px;'>Basic monitoring tools<br>Up to 50 items tracked<br>Standard daily updates</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Launch Starter", key="btn_starter"):
        st.info("Starter Plan selected.")

with col_card_2:
    st.markdown("""
    <div style='border: 1px solid #2ECC71; padding: 15px; border-radius: 5px; background-color: #0A0F17; min-height: 150px;'>
        <div style='color: #2ECC71; font-weight: bold;'>⚡ Pro Tracker</div>
        <p style='font-size: 13px; color: #9CA3AF; margin-top: 5px;'>Track 500 active products<br>Instant stock & price alerts<br>Multi-country tracking</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Launch Pro Trial", key="btn_pro"):
        st.info("Pro Trial Plan selected.")

with col_card_3:
    st.markdown("""
    <div style='border: 1px solid #9CA3AF; padding: 15px; border-radius: 5px; background-color: #0A0F17; min-height: 150px;'>
        <div style='color: #FFFFFF; font-weight: bold;'>🤝 Enterprise</div>
        <p style='font-size: 13px; color: #9CA3AF; margin-top: 5px;'>Unlimited products & stores<br>Custom API access<br>Dedicated Account Manager</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Contact Sales", key="btn_ent"):
        st.info("Enterprise Contact Request logged.")


# =====================================================================
# SECTION 3 : ZONE PUBLIQUE (Capture, validation et stockage des e-mails)
# =====================================================================
st.write("---")
st.write("**Enter your business email to request priority access credentials:**")

with st.form(key="email_form", clear_on_submit=True):
    email_saisi = st.text_input("Business Email :", placeholder="name@company.com")
    submit_button = st.form_submit_button(label="Submit Request")

if submit_button:
    if email_saisi.strip() == "":
        st.error("❌ Le champ ne peut pas être vide.")
    elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_saisi):
        enregistrer_email_csv(email_saisi.strip())
        st.success("✅ Request saved! Our deployment team will email your secure credentials within 24 hours.")
        st.rerun()
    else:
        st.error("❌ Please enter a valid business email address (e.g., name@company.com).")

st.write("")

# Le bandeau vert défilant officiel
st.markdown(
    """
    <marquee style='color: #00FF00; font-family: monospace; font-size: 20px; background-color: #051a05; padding: 10px; border: 1px solid #00FF00;'>
        [SYSTEM]: MAPPING COMPETITOR PRICING OVERSIGHT
    </marquee>
    """, 
    unsafe_allow_html=True
)


# =====================================================================
# SECTION 4 : ESPACE ADMINISTRATEUR SÉCURISÉ (Tout en bas)
# =====================================================================
st.write("---")
st.markdown("### 🔒 Administration Panel")

mot_de_passe = st.text_input("Enter Admin Password to view prospects:", type="password")

if mot_de_passe == "KimpeseAdmin2026":
    st.markdown("#### 👥 Captured Prospect Emails")
    
    df_prospects = lire_emails_csv()
    
    if not df_prospects.empty:
        st.dataframe(df_prospects, use_container_width=True)
        
        csv_data = df_prospects.to_csv(index=False, encoding="utf-8")
        st.download_button(
            label="📥 Télécharger le fichier CSV",
            data=csv_data,
            file_name="liste_prospects_export.csv",
            mime="text/csv"
        )
    else:
        st.info("Aucun e-mail n'a encore été enregistré dans le fichier.")
    
elif mot_de_passe != "":
    st.error("❌ Mot de passe administrateur incorrect.")
else:
    st.info("Le tableau des prospects est masqué. Saisissez le mot de passe pour y accéder.")


# =====================================================================
# SECTION 5 : MENTION DE COPYRIGHT (Pied de page)
# =====================================================================
st.write("") 
st.write("---")
st.markdown(
    """
    <div style='text-align: center; color: #888888; font-size: 14px;'>
        © 2026 Kimpese Software. All rights reserved.
    </div>
    """, 
    unsafe_allow_html=True
)
