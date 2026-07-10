# PROPRIETARY NOTICE & COPYRIGHT LICENSE
# Copyright © 2026 KIMPESE SOFTWARE L.L.C. All rights reserved.
# State of Registration: Wyoming, USA. Secured under Wyoming, USA LLC Proprietary
# ---------------------------------------------------------------------
import streamlit as st
import re
import os
import pandas as pd
from datetime import datetime

# 1. CONFIGURATION GLOBALE D'ORIGINE
st.set_page_config(page_title="Kimpese Software | Global Pricing Intelligence", page_icon="🟢", layout="wide")

# Initialisation des variables d'état en mémoire vive
if "liste_emails" not in st.session_state:
    st.session_state.liste_emails = []

if "choix_plan" not in st.session_state:
    st.session_state.choix_plan = None

# Nom du fichier de stockage permanent CSV
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


# --- LE STYLE DESIGN SILICON VALLEY NOIR ET VERT INITIAL ---
st.markdown("""
<style>
/* Fond noir profond universel */
.stApp {
    background-color: #0A0F17 !important;
    color: #F3F4F6 !important;
    font-family: 'Courier New', Courier, monospace;
}
/* Style pour les inputs et formulaires */
input, div[data-baseweb="input"], select, div[data-baseweb="select"] {
    background-color: #000000 !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
}
input[type="text"], input[type="password"] {
    color: #00FF00 !important;
    -webkit-text-fill-color: #00FF00 !important;
}
button, .stButton>button {
    background-color: #051a05 !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
}
.stAlert {
    background-color: #111111 !important;
    color: #00FF00 !important;
    border: 1px solid #00FF00 !important;
}
h3, h4, h5, p, span, label {
    color: #00FF00 !important;
    font-family: 'Courier New', Courier, monospace !important;
}
</style>
""", unsafe_allow_html=True)


# =====================================================================
# SECTION 1 : LOGO & METEO INITIALE EN DIRECT
# =====================================================================
st.markdown("<h3 style='text-align: center; color: #00FF00;'>KIMPESE SOFTWARE</h3>", unsafe_allow_html=True)

# Alignement d'origine du logo et du bloc météo
col_logo, col_meteo = st.columns(2)
with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=150)
    else:
        st.markdown("<div style='padding: 10px; color: #00FF00;'>[ Logo Ready ]</div>", unsafe_allow_html=True)

with col_meteo:
    st.markdown("""
    <div style='text-align: center; border: 1px solid #00FF00; padding: 10px; background-color: #051a05; border-radius: 5px; width: 200px; margin: 0 auto;'>
        <span style='font-size: 25px; color: #FFFFFF;'>☀️ 85°F</span><br>
        <span style='color: #00FF00; font-size: 12px;'>● Live Weather</span>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("#### 🟢 Market Analysis Engine • Country: US")
st.write("Select your industry vertical:")


# =====================================================================
# SECTION 2 : CARTES DE TARIFS (Pro Tracker / Enterprise)
# =====================================================================
col2, col3 = st.columns(2)
with col2:
    st.markdown("""
    <div style='border: 1px solid #2ECC71; padding: 20px; border-radius: 5px; background-color: #0A0F17;'>
        <div style='color: #2ECC71; font-weight: bold; font-size: 20px;'>⚡ Pro Tracker</div>
        <p style='font-size: 14px; color: #9CA3AF;'>Track 500 active products<br>Instant stock & price alerts<br>Multi-country tracking</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Launch Pro Trial", key="btn_pro_trial"):
        st.session_state.choix_plan = "Pro"

with col3:
    st.markdown("""
    <div style='border: 1px solid #9CA3AF; padding: 20px; border-radius: 5px; background-color: #0A0F17;'>
        <div style='color: #FFFFFF; font-weight: bold; font-size: 20px;'>🤝 Enterprise</div>
        <p style='font-size: 14px; color: #9CA3AF;'>Unlimited products & stores<br>Custom API access<br>Dedicated Account Manager</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Contact Sales", key="btn_contact_sales"):
        st.session_state.choix_plan = "Enterprise"


# =====================================================================
# SECTION 3 : FORMULAIRE D'INSCRIPTION & RECTANGLE VERT DÉFILANT
# =====================================================================
st.write("---")
st.write("Enter your business email to request priority access credentials:")

with st.form(key="email_form", clear_on_submit=True):
    email_saisi = st.text_input("Business Email :", placeholder="ceo@yourbrand.com")
    submit_button = st.form_submit_button(label="Submit Request")

if submit_button:
    if email_saisi.strip() == "":
        st.error("❌ Le champ ne peut pas être vide.")
    elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_saisi):
        # Sauvegarde permanente dans le fichier CSV
        enregistrer_email_csv(email_saisi.strip())
        st.success("✅ Request saved! Our deployment team will email your secure credentials within 24 hours.")
        st.rerun()
    else:
        st.error("❌ Please enter a valid business email address (e.g., name@company.com).")

st.write("")

# Le fameux rectangle vert défilant
st.markdown(
    """
    <marquee style='color: #00FF00; font-family: monospace; font-size: 20px; background-color: #051a05; padding: 10px; border: 1px solid #00FF00;'>
        [SYSTEM]: MAPPING COMPETITOR PRICING OVERSIGHT
    </marquee>
    """, 
    unsafe_allow_html=True
)


# =====================================================================
# SECTION 4 : PANEL ADMINISTRATEUR DEPLIABLE TOUT EN BAS
# =====================================================================
st.write("---")
st.markdown("<h4 style='color: #00FF00;'>🔒 Administration Panel (Admin Only)</h4>", unsafe_allow_html=True)

mot_de_passe = st.text_input("Enter Admin Password to view prospects:", type="password")

if mot_de_passe == "KimpeseAdmin2026":
    with st.expander("🔑 Internal Database Viewer (Admin Only)", expanded=True):
        df_prospects = lire_emails_csv()
        
        if not df_prospects.empty:
            st.dataframe(df_prospects, use_container_width=True)
            
            # Bouton de téléchargement CSV
            csv_data = df_prospects.to_csv(index=False, encoding="utf-8")
            st.download_button(
                label="📥 Download Leads List (CSV)",
                data=csv_data,
                file_name="kimpese_leads.csv",
                mime="text/csv"
            )
        else:
            st.info("Aucun prospect enregistré pour le moment.")
elif mot_de_passe != "":
    st.error("❌ Mot de passe administrateur incorrect.")


# =====================================================================
# SECTION 5 : MENTION DE COPYRIGHT ET LICENCE D'ORIGINE
# =====================================================================
st.write("---")
st.markdown(
    """
    <div style='text-align: center; color: #4B5563; font-size: 12px; font-family: monospace;'>
        © 2026 KIMPESE SOFTWARE L.L.C. All rights reserved. Secured under Wyoming, USA LLC Proprietary.
    </div>
    """, 
    unsafe_allow_html=True
)
