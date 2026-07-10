import streamlit as st
import re
import os
import pandas as pd
from datetime import datetime

# 1. CONFIGURATION GLOBALE D'ORIGINE
st.set_page_config(page_title="Kimpese Software", page_icon="💻", layout="wide")

# Nom du fichier de stockage permanent
FICHIER_CSV = "prospects.csv"

def initialiser_csv():
    if not os.path.exists(FICHIER_CSV):
        df_initial = pd.DataFrame(columns=["Date d'inscription", "Emails Collectés"])
        df_initial.to_csv(FICHIER_CSV, index=False, encoding="utf-8")

def enregistrer_email_csv(email):
    initialiser_csv()
    date_actuelle = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nouvelle_ligne = pd.DataFrame([[date_actuelle, email]], columns=["Date d'inscription", "Emails Collectés"])
    nouvelle_ligne.to_csv(FICHIER_CSV, mode='a', header=False, index=False, encoding="utf-8")

def lire_emails_csv():
    initialiser_csv()
    try:
        return pd.read_csv(FICHIER_CSV, encoding="utf-8")
    except Exception:
        return pd.DataFrame(columns=["Date d'inscription", "Emails Collectés"])


# =====================================================================
# INJECTION CSS POUR LE DESIGN VERT ET NOIR ET EFFACER LE MOT "VISIBILITÉ"
# =====================================================================
st.markdown("""
<style>
/* Forçage absolu du fond noir */
.stApp, div[data-testid="stAppViewContainer"], div[data-testid="stHeader"] {
    background-color: #000000 !important;
    color: #00FF00 !important;
}
/* Style vert rétro pour les entrées de texte */
input, div[data-baseweb="input"] {
    background-color: #000000 !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
}
input[type="text"], input[type="password"] {
    color: #00FF00 !important;
    -webkit-text-fill-color: #00FF00 !important;
}
/* Supprime définitivement les textes d'icônes natifs comme 'visible' ou 'hidden' */
div[data-testid="InputWithDynamicNotification"] span, button div {
    display: none !important;
}
/* Style des boutons en vert terminal */
button, .stButton>button {
    background-color: #051a05 !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
}
/* Forçage de la police monospace verte */
h3, h4, h5, p, span, label, div {
    color: #00FF00 !important;
    font-family: 'Courier New', Courier, monospace !important;
}
</style>
""", unsafe_allow_html=True)


# =====================================================================
# SECTION 1 : TITRE PRINCIPAL
# =====================================================================
st.markdown("<h3 style='text-align: center; color: #00FF00; margin-bottom: 25px;'>KIMPESE SOFTWARE</h3>", unsafe_allow_html=True)


# =====================================================================
# SECTION 2 : LOGO & MÉTÉO (ALIGNÉS ET PARFAITEMENT CENTRÉS)
# =====================================================================
# Augmentation millimétrée de la colonne de gauche (de 2.25 à 2.32) pour centrer totalement
col_vide_gauche, col_logo, col_meteo, col_vide_droite = st.columns([2.32, 1.2, 0.9, 0.58])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=170)
    else:
        st.markdown("<div style='border: 1px dashed #00FF00; padding: 20px; text-align: center;'>[ Logo Manquant ]</div>", unsafe_allow_html=True)

with col_meteo:
    st.markdown("""
    <div style='text-align: center; border: 1px solid #00FF00; padding: 8px; background-color: #051a05; border-radius: 5px; width: 130px; margin-top: 15px;'>
        <span style='font-size: 18px; color: #FFFFFF; font-weight: bold;'>☀️ 85°F</span><br>
        <span style='color: #00FF00; font-size: 10px;'>● Live Weather</span>
    </div>
    """, unsafe_allow_html=True)


# =====================================================================
# SECTION 3 : BANDEAU DÉFILANT FLUIDE (SANS CADRE LOURD)
# =====================================================================
st.write("")
st.markdown(
    """
    <marquee style='color: #00FF00; font-family: monospace; font-size: 20px; background: transparent; padding: 5px;'>
        [SYSTEM]: MAPPING COMPETITOR PRICING OVERSIGHT
    </marquee>
    """, 
    unsafe_allow_html=True
)
st.write("")


# =====================================================================
# SECTION 4 : TEXTES D'INTRODUCTION
# =====================================================================
st.markdown("#### 🟢 Market Analysis Engine • Country: US")
st.write("Select your industry vertical:")


# =====================================================================
# SECTION 5 : LES 3 CARTES DE TARIFICATION (CÔTE À CÔTE)
# =====================================================================
col_card_1, col_card_2, col_card_3 = st.columns(3)

with col_card_1:
    st.markdown("""
    <div style='border: 1px solid #00FF00; padding: 15px; border-radius: 5px; background-color: #000000; min-height: 150px;'>
        <div style='color: #00FF00; font-weight: bold; font-size: 18px;'>⚡ Starter Tracker</div>
        <p style='font-size: 13px; color: #00FF00; margin-top: 5px; opacity: 0.8;'>Basic monitoring tools<br>Up to 50 items tracked<br>Standard daily updates</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Launch Starter", key="btn_starter"):
        st.info("Starter Plan selected.")

with col_card_2:
    st.markdown("""
    <div style='border: 1px solid #00FF00; padding: 15px; border-radius: 5px; background-color: #000000; min-height: 150px;'>
        <div style='color: #00FF00; font-weight: bold; font-size: 18px;'>⚡ Pro Tracker</div>
        <p style='font-size: 13px; color: #00FF00; margin-top: 5px; opacity: 0.8;'>Track 500 active products<br>Instant stock & price alerts<br>Multi-country tracking</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Launch Pro Trial", key="btn_pro"):
        st.info("Pro Trial Plan selected.")

with col_card_3:
    st.markdown("""
    <div style='border: 1px solid #00FF00; padding: 15px; border-radius: 5px; background-color: #000000; min-height: 150px;'>
        <div style='color: #00FF00; font-weight: bold; font-size: 18px;'>🤝 Enterprise</div>
        <p style='font-size: 13px; color: #00FF00; margin-top: 5px; opacity: 0.8;'>Unlimited products & stores<br>Custom API access<br>Dedicated Account Manager</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Contact Sales", key="btn_ent"):
        st.info("Enterprise Contact Request logged.")


# =====================================================================
# SECTION 6 : CAPTURE DES EMAILS
# =====================================================================
st.write("---")
st.write("Enter your business email to request priority access credentials:")

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


# =====================================================================
# SECTION 7 : PANNEAU ADMINISTRATEUR SÉCURISÉ (TOUT EN BAS)
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
        st.info("Aucun e-mail enregistré.")
elif mot_de_passe != "":
    st.error("❌ Mot de passe administrateur incorrect.")


# =====================================================================
# SECTION 8 : COPYRIGHT
# =====================================================================
st.write("") 
st.write("---")
st.markdown(
    """
    <div style='text-align: center; color: #00FF00; font-size: 14px; opacity: 0.6;'>
        © 2026 Kimpese Software. All rights reserved.
    </div>
    """, 
    unsafe_allow_html=True
)
