# PROPRIETARY NOTICE & COPYRIGHT LICENSE
# Copyright © 2026 KIMPESE SOFTWARE L.L.C. All rights reserved.
# State of Registration: Wyoming, USA. Secured under Wyoming, USA LLC Proprietary
# ---------------------------------------------------------------------
import streamlit as st
import os
import pandas as pd

# Configuration globale de la page
st.set_page_config(page_title="Kimpese Software | Global Pricing Intelligence", page_icon="🟢", layout="wide")

# Initialisation de la liste des e-mails en mémoire vive
if "liste_emails" not in st.session_state:
    st.session_state.liste_emails = []

# --- DESIGN SILICON VALLEY NOIR ET VERT ---
st.markdown("""
<style>
/* Fond noir profond universel */
.stApp {
    background-color: #0A0F17 !important;
    color: #F3F4F6 !important;
    font-family: 'Courier New', Courier, monospace;
}
/* Style pour les inputs et formulaires */
input, div[data-baseweb="input"] {
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
</style>
""", unsafe_allow_html=True)

# =====================================================================
# SECTION 1 : EN-TÊTE D'ORIGINE (LOGO ET MÉTÉO)
# =====================================================================
st.markdown("<h3 style='text-align: center; color: #00FF00;'>KIMPESE SOFTWARE</h3>", unsafe_allow_html=True)

# Note: Remettez ici votre code d'affichage d'image logo.png et météo si nécessaire
# ex: st.image("logo.png") ou votre composant météo d'origine

st.markdown("#### 🟢 Market Analysis Engine • Country: US")
st.write("Select your industry vertical:")

# =====================================================================
# SECTION 2 : ZONE D'INSCRIPTION & RECTANGLE VERT DÉFILANT
# =====================================================================
st.write("---")
st.write("**Enter your business email to request priority access credentials:**")

# Formulaire d'inscription avec bouton d'envoi
with st.form(key="email_form", clear_on_submit=True):
    email_saisi = st.text_input("Business Email :", placeholder="ceo@yourbrand.com")
    submit_button = st.form_submit_button(label="Submit Request")

if submit_button:
    if email_saisi.strip() != "":
        st.session_state.liste_emails.append(email_saisi.strip())
        st.success("✅ Request saved! Our deployment team will email your secure credentials within 24 hours.")
        st.rerun()

st.write("")
st.write("")

# Insertion du rectangle vert défilant officiel
st.markdown(
    """
    <marquee style='color: #00FF00; font-family: monospace; font-size: 20px; background-color: #051a05; padding: 10px; border: 1px solid #00FF00;'>
        [SYSTEM]: MAPPING COMPETITOR PRICING OVERSIGHT
    </marquee>
    """, 
    unsafe_allow_html=True
)

# =====================================================================
# SECTION 3 : PANEL ADMINISTRATEUR DÉPLIABLE SÉCURISÉ TOUT EN BAS
# =====================================================================
st.write("---")
st.markdown("<h4 style='color: #00FF00;'>🔒 Administration Panel (Admin Only)</h4>", unsafe_allow_html=True)

# Demande du mot de passe admin
mot_de_passe = st.text_input("Enter Admin Password to view prospects:", type="password")

if mot_de_passe == "KimpeseAdmin2026":
    with st.expander("📂 Internal Database Viewer", expanded=True):
        if st.session_state.liste_emails:
            df_leads = pd.DataFrame(st.session_state.liste_emails, columns=["Emails Collectés"])
            st.dataframe(df_leads, use_container_width=True)
            
            # Option d'export CSV d'origine
            csv = df_leads.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Leads List (CSV)", 
                data=csv, 
                file_name="kimpese_leads.csv", 
                mime="text/csv"
            )
        else:
            st.info("No leads captured in this active session yet.")
elif mot_de_passe != "":
    st.error("❌ Mot de passe administrateur incorrect.")

# =====================================================================
# SECTION 4 : MENTION DE COPYRIGHT D'ORIGINE
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
