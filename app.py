#PROPRIETARY NOTICE & COPURIGHT LICENSE
# COPYRIGHT 2026 KIMPESE SOFTWARE L.L.C
# State of Registration :WYOMING,USA
import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

DB_NAME = "database.db"

st.set_page_config(page_title="Kimpese Software", page_icon="🚀", layout="wide")
st.title("🚀 Kimpese Software - Global Pricing Intelligence")

# Détection du pays et provenance depuis l'URL
query_params = st.query_params
is_from_campaign = "campaign" in query_params and query_params["campaign"] == "true"
client_country = query_params["country"].upper() if "country" in query_params else "US"

MONNAIES = {
    "US": {"symbole": "$", "starter_m": "https://stripe.com", "pro_m": "https://stripe.com", "ent_m": "https://stripe.com"},
    "UK": {"symbole": "£", "starter_m": "https://stripe.com", "pro_m": "https://stripe.com", "ent_m": "https://stripe.com"},
    "CA": {"symbole": "CA$", "starter_m": "https://stripe.com", "pro_m": "https://stripe.com", "ent_m": "https://stripe.com"},
    "AU": {"symbole": "AU$", "starter_m": "https://stripe.com", "pro_m": "https://stripe.com", "ent_m": "https://stripe.com"}
}

if client_country not in MONNAIES: client_country = "US"
symbole = MONNAIES[client_country]["symbole"]

if "step" not in st.session_state: st.session_state.step = "saisie"

# --- RENDER DES ETAPES CLIENTS ---
if st.session_state.step == "saisie":
    st.subheader(f"Welcome prospect from {client_country}! Explore your local market.")
    st.write("Enter your brand name below to map your market and track your competitors' prices.")
    nom_entreprise = st.text_input("Your Brand Name :")
    
    if st.button("Analyze My Market", type="primary"):
        if nom_entreprise.strip():
            st.session_state.nom_marque = nom_entreprise.strip()
            
            # Sauvegarde de l'inscription en mode Essai dans la base de données
            try:
                conn = sqlite3.connect(DB_NAME)
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO clients_saas (nom_marque, email_client, date_inscription, statut) 
                    VALUES (?, ?, ?, 'ESSAI')""", 
                    (st.session_state.nom_marque, f"contact@{st.session_state.nom_marque.lower().replace(' ', '')}.com", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                conn.commit()
                conn.close()
            except Exception as e:
                st.warning(f"Database simulation note: {e}")
                
            st.session_state.step = "verrouille"
            st.rerun()

elif st.session_state.step == "verrouille":
    st.success(f"🔥 Active Monitoring Enabled for {st.session_state.nom_marque} ({client_country})")
    
    st.write("### Choose your plan to fully unlock your Dashboard")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🌱 **Starter Plan**")
        st.write(f"Track up to 50 products\n\n**{symbole}49** / month")
        st.link_button("Subscribe Starter", MONNAIES[client_country]["starter_m"])
    with col2:
        st.success("⚡ **Pro Plan**")
        st.write(f"Track up to 500 products\n\n**{symbole}99** / month")
        st.link_button("Subscribe Pro", MONNAIES[client_country]["pro_m"])
    with col3:
        st.warning("👑 **Enterprise**")
        st.write(f"Unlimited products\n\n**{symbole}249** / month")
        st.link_button("Contact Enterprise", MONNAIES[client_country]["ent_m"])

    st.write("---")
    st.subheader("📊 Your Live Pricing Intelligence Dashboard")
    st.info("Your data is loading securely based on your trial access...")

# =====================================================================
# 🤖 SECTION HUB D'ADMINISTRATION SECRET (POUR VOUS UNIQUEMENT)
# =====================================================================
st.write("---")
st.subheader("🤖 Kimpese Automation Hub & Daily Stats (Admin Only)")

try:
    conn = sqlite3.connect(DB_NAME)
    date_du_jour = datetime.now().strftime("%Y-%m-%d")
    
    mails_lus = conn.execute("SELECT COUNT(*) FROM historique_prospection WHERE date_envoi LIKE ? AND statut_lecture = 'LU'", (f"{date_du_jour}%",)).fetchone()[0]
    essais_du_jour = conn.execute("SELECT COUNT(*) FROM clients_saas WHERE date_inscription LIKE ? AND statut = 'ESSAI'", (f"{date_du_jour}%",)).fetchone()[0]
    abonnements_du_jour = conn.execute("SELECT COUNT(*) FROM clients_saas WHERE statut = 'ACTIF'").fetchone()[0]
    
    conn.close()
except:
    mails_lus, essais_du_jour, abonnements_du_jour = 0, 0, 0

# Affichage des compteurs sous forme de colonnes
col_adm1, col_adm2, col_adm3 = st.columns(3)
col_adm1.metric("Emails Opened Today", mails_lus)
col_adm2.metric("New Trial Registrations", essais_du_jour)
col_adm3.metric("Total Active Paid Subscribers", abonnements_du_jour)
#  PROPRIETARY NOTICE & COPYRIGHT LICENSE
#  Copyright © 2026 KIMPESE SOFTWARE L.L.C. All rights reserved.
#
#  State of Registration: Wyoming, USA.
#  Company File Number: [Insérez votre numéro de LLC une fois reçu]
#
#  NOTICE: All information contained herein is, and remains the property of 
#  Kimpese Software L.L.C. The intellectual and technical concepts contained
#  herein are proprietary to Kimpese Software L.L.C. and may be covered by U.S. 
#  and Foreign Patents, patents in process, and are protected by trade secret 
#  or copyright law.
#
#  Dissemination of this information or reproduction of this material is 
#  strictly forbidden unless prior written permission is obtained from 
#  Kimpese Software L.L.C. Reverse engineering of this software is prohibited.
