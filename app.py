import streamlit as st
import re
import os
import pandas as pd
from datetime import datetime

# 1. CONFIGURATION DU THÈME SOMBRE D'ORIGINE
st.set_page_config(page_title="Kimpese Software", page_icon="💻", layout="centered")

# Injection de style pour forcer le fond noir et l'ambiance terminal rétro
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #00FF00;
        font-family: 'Courier New', Courier, monospace;
    }
    input, div[data-baseweb="input"] {
        background-color: #111111 !important;
        color: #00FF00 !important;
        border: 1px solid #00FF00 !important;
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
    """,
    unsafe_allow_html=True
)

# Configuration du fichier CSV
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

def supprimer_email_csv(email_a_supprimer):
    df = lire_emails_csv()
    df_filtre = df[df["Emails Collectés"] != email_a_supprimer]
    df_filtre.to_csv(FICHIER_CSV, index=False, encoding="utf-8")


# =====================================================================
# SECTION 1 : LOGO INITIAL (STYLE TERMINAL)
# =====================================================================
st.markdown("<h3 style='text-align: center; color: #00FF00;'>KIMPESE SOFTWARE</h3>", unsafe_allow_html=True)


# =====================================================================
# SECTION 2 : ZONE PUBLIQUE (Saisie e-mail & Flash défilant initial)
# =====================================================================
st.write("")
st.write("Enter your business email to request priority access credentials:")

with st.form(key="email_form", clear_on_submit=True):
    email_saisi = st.text_input("Business Email :", placeholder="name@company.com")
    submit_button = st.form_submit_button(label="Submit Request")

if submit_button:
    if email_saisi.strip() == "":
        st.error("❌ Le champ ne peut pas être vide.")
    elif re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email_saisi):
        enregistrer_email_csv(email_saisi)
        st.success("✅ Request saved! Our deployment team will email your secure credentials within 24 hours.")
        st.rerun()
    else:
        st.error("❌ Please enter a valid business email address (e.g., name@company.com).")

st.write("")

# Le fameux bandeau défilant vert de la première version
st.markdown(
    """
    <marquee style='color: #00FF00; font-family: monospace; font-size: 20px; background-color: #051a05; padding: 10px; border: 1px solid #00FF00;'>
        [SYSTEM]: MAPPING COMPETITOR PRICING OVERSIGHT
    </marquee>
    """, 
    unsafe_allow_html=True
)


# =====================================================================
# SECTION 3 : PANNEAU ADMIN MASQUÉ (DANS LE MÊME STYLE)
# =====================================================================
st.write("")
st.write("---")
st.markdown("<h4 style='color: #00FF00;'>🔒 Administration Panel</h4>", unsafe_allow_html=True)

with st.form(key="admin_form"):
    mot_de_passe = st.text_input("Enter Admin Password to view prospects:", type="password")
    valider_admin = st.form_submit_button(label="🔑 Connexion Admin")

if valider_admin or mot_de_passe == "KimpeseAdmin2026":
    if mot_de_passe == "KimpeseAdmin2026":
        st.markdown("<h5 style='color: #00FF00;'>👥 Captured Prospect Emails</h5>", unsafe_allow_html=True)
        
        df_prospects = lire_emails_csv()
        
        if not df_prospects.empty:
            st.dataframe(df_prospects, use_container_width=True)
            
            st.markdown("<h5 style='color: #00FF00;'>⚙️ Gestion des données</h5>", unsafe_allow_html=True)
            liste_emails = df_prospects["Emails Collectés"].tolist()
            email_selectionne = st.selectbox("Sélectionnez un e-mail à supprimer :", options=liste_emails)
            
            if st.form_submit_button(label="🗑️ Supprimer définitivement"):
                supprimer_email_csv(email_selectionne)
                st.success(f"L'e-mail '{email_selectionne}' a été retiré.")
                st.rerun()
            
            csv_data = df_prospects.to_csv(index=False, encoding="utf-8")
            st.download_button(
                label="📥 Télécharger le fichier CSV complet",
                data=csv_data,
                file_name="liste_prospects_export.csv",
                mime="text/csv"
            )
        else:
            st.info("Aucun e-mail enregistré.")
    elif mot_de_passe != "":
        st.error("❌ Mot de passe incorrect.")
else:
    st.info("Le tableau des prospects est masqué. Saisissez le mot de passe pour y accéder.")


# =====================================================================
# SECTION 4 : COPYRIGHT
# =====================================================================
st.write("---")
st.markdown(
    """
    <div style='text-align: center; color: #555555; font-size: 14px;'>
        © 2026 Kimpese Software. All rights reserved.
    </div>
    """, 
    unsafe_allow_html=True
)
