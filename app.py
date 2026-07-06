#  PROPRIETARY NOTICE & COPYRIGHT LICENSE
#  Copyright © 2026 KIMPESE SOFTWARE L.L.C. All rights reserved.
#  State of Registration: Wyoming, USA.
# ==============================================================================
import streamlit as st
import sqlite3
from datetime import datetime

DB_NAME = "database.db"

# Configuration de la page
st.set_page_config(page_title="Kimpese Software | Global Pricing Intelligence", page_icon="🟢", layout="wide")

# --- DESIGN SILICON VALLEY (DARK THEME & LOGO COULEUR VERT EMERAUDE) ---
st.markdown("""
<style>
    /* Force le fond noir profond sur tout le site */
    .stApp {
        background-color: #0A0E17 !important;
        color: #F3F4F6 !important;
    }
    
    /* En-tête avec votre vrai logo stylisé */
    .logo-container {
        text-align: center;
        padding: 30px 0;
    }
    
    /* Reproduction numérique des lignes de votre logo vert émeraude */
    .brand-icon {
        font-size: 55px;
        font-weight: 300;
        color: #2ECC71; /* Le vert émeraude officiel de votre logo */
        font-family: sans-serif;
        letter-spacing: -5px;
        margin-bottom: -10px;
    }
    
    .brand-title {
        font-size: 42px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #FFFFFF !important;
        margin-top: 15px;
        margin-bottom: 0px;
    }
    
    .brand-subtitle {
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 4px;
        color: #9CA3AF !important;
        margin-top: 5px;
    }
    
    .tagline {
        color: #6B7280;
        font-size: 16px;
        margin-top: 15px;
    }
    
    /* Cartes de Tarifs style Silicon Valley */
    .sv-card {
        background: rgba(17, 24, 39, 0.8);
        border: 1px solid rgba(46, 204, 113, 0.2); /* Bordure vert émeraude discrète */
        border-radius: 16px;
        padding: 35px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(12px);
        transition: all 0.3s ease;
    }
    .sv-card:hover {
        border-color: #2ECC71; /* Illumination verte au survol */
        box-shadow: 0 0 25px rgba(46, 204, 113, 0.3);
        transform: translateY(-5px);
    }
    
    /* Badge Popular Vert */
    .sv-badge {
        background: linear-gradient(90deg, #2ECC71, #27AE60);
        color: white;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Ajustement des inputs de texte obligatoires pour le fond noir */
    label, p, h3 {
        color: #E5E7EB !important;
    }
    div[data-baseweb="input"] {
        background-color: #1F2937 !important;
        border: 1px solid #374151 !important;
    }
    div[data-baseweb="input"] input {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- BLOC LOGO REPRODUISANT VOTRE IDENTITÉ VISUELLE ---
st.markdown("""
<div class="logo-container">
    <div class="brand-icon">𝙆♾️</div>
    <div class="brand-title">KIMPESE</div>
    <div class="brand-subtitle">SOFTWARE</div>
    <p class="tagline">Next-Gen Pricing Intelligence for Global Brands</p>
</div>
""", unsafe_allow_html=True)

# Détection pays via paramètres d'URL
query_params = st.query_params
client_country = query_params["country"].upper() if "country" in query_params else "US"

MONNAIES = {
    "US": {"symbole": "$"}, "UK": {"symbole": "£"}, "CA": {"symbole": "CA$"}, "AU": {"symbole": "AU$"}
}
symbole = MONNAIES.get(client_country, MONNAIES["US"])["symbole"]

if "step" not in st.session_state: 
    st.session_state.step = "saisie"

st.write("---")

# --- COEUR DE L'INTERFACE UTILISATEUR ---
if st.session_state.step == "saisie":
    st.markdown(f"### 🌐 Market Analysis Engine • Country: {client_country}")
    nom_entreprise = st.text_input("Enter your brand name to map competitor pricing gaps overnight :", placeholder="e.g. Acme Corporation")
    
    if st.button("Analyze My Market Now", type="primary"):
        if nom_entreprise.strip():
            st.session_state.nom_marque = nom_entreprise.strip()
            try:
                conn = sqlite3.connect(DB_NAME)
                cur = conn.cursor()
                cur.execute("INSERT INTO clients_saas (nom_marque, email_client, date_inscription, statut) VALUES (?, ?, ?, 'ESSAI')", 
                            (st.session_state.nom_marque, f"contact@{st.session_state.nom_marque.lower().replace(' ', '')}.com", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                conn.commit()
                conn.close()
            except: pass
            st.session_state.step = "verrouille"
            st.rerun()

elif st.session_state.step == "verrouille":
    st.markdown(f"### 🧬 Scanner Status: <span style='color:#2ECC71;'>Active Tracking Enabled for {st.session_state.nom_marque}</span>", unsafe_allow_html=True)
    st.write("Our tracking bot is currently mapping your retail competitors. Choose a plan to unlock your intelligence dashboard.")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="sv-card">
            <div style="font-size: 20px; font-weight:700; color:#FFFFFF;">🌱 Starter</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{symbole}49<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Track 50 active products<br>Daily price updates<br>Single country analytics</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Starter Trial", key="btn_str", use_container_width=True)
        
    with col2:
        st.markdown(f"""
        <div class="sv-card" style="border-color: #2ECC71;">
            <div class="sv-badge">MOST POPULAR</div>
            <div style="font-size: 20px; font-weight:700; color:#2ECC71;">⚡ Pro Tracker</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{symbole}99<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Track 500 active products<br>Instant stock & price alerts<br>Multi-country (US/UK/CA/AU)</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Launch Pro Trial", key="btn_pro", use_container_width=True)
        
    with col3:
        st.markdown(f"""
        <div class="sv-card">
            <div style="font-size: 20px; font-weight:700; color:#FFFFFF;">👑 Enterprise</div>
            <div style="font-size: 38px; font-weight:800; margin:15px 0; color:#FFFFFF;">{symbole}249<span style="font-size:14px; font-weight:400; color:#9CA3AF;">/mo</span></div>
            <p style="color:#9CA3AF; font-size:14px; line-height:1.6;">Unlimited products & stores<br>Custom API access<br>Dedicated Account Manager</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Contact Sales", key="btn_ent", use_container_width=True)

# --- PIED DE PAGE JURIDIQUE DE LA LLC ---
st.write("---")
st.markdown("<p style='color:#4B5563; font-size:12px; text-align:center;'>© 2026 KIMPESE SOFTWARE L.L.C. All rights reserved. Secured under Wyoming LLC Proprietary Laws.</p>", unsafe_allow_html=True)
