import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# --- CONFIGURATION UX/UI (Minimaliste Beige & Indigo) ---
st.set_page_config(page_title="SafeRoute | Sécurité & Solidarité", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #f5f5dc; }
    .main-title { font-size: 40px; font-weight: bold; color: #ffd700; text-align: center; margin-bottom: 0px; }
    .stButton>button { border-radius: 20px; background: #ffd700; color: #1a1a2e; font-weight: bold; border: none; }
    .safe-card { background: rgba(255, 255, 255, 0.07); padding: 15px; border-radius: 15px; border-left: 5px solid #ffd700; margin-bottom: 15px; }
    .badge-verified { background-color: #4cd137; color: white; padding: 2px 8px; border-radius: 10px; font-size: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Organisation OBS & RGPD) ---
with st.sidebar:
    st.markdown("<h1 style='color: #ffd700;'>🛡️ SafeRoute</h1>", unsafe_allow_html=True)
    st.caption("Projet Management de Projet Touristique")
    st.write("---")
    menu = st.radio("MENU PRINCIPAL", ["📍 Carte & Refuges", "🤝 Co-Walking & Matching", "🚨 SOS & Sécurité", "📈 Dashboard Équipe"])
    st.write("---")
    st.markdown("🔐 **Conformité RGPD** : Données chiffrées (Hébergement UE).")

# --- 1. CARTE INTERACTIVE (FSP1 & FSP2) ---
if menu == "📍 Carte & Refuges":
    st.markdown("<p class='main-title'>Itinéraires Sécurisés</p>", unsafe_allow_html=True)
    
    col_map, col_info = st.columns([3, 1])
    
    with col_map:
        m = folium.Map(location=[50.6292, 3.0573], zoom_start=13, tiles="CartoDB dark_matter")
        # Safe Haven (Commerce partenaire)
        folium.Marker([50.633, 3.060], popup="<b>Point de RDV : Grand Place</b>", icon=folium.Icon(color='green', icon='shield', prefix='fa')).add_to(m)
        # Zone sombre signalée
        folium.Circle([50.6348, 2.9646], radius=400, color="red", fill=True, popup="Zone signalée : Éclairage HS").add_to(m)
        st_folium(m, width="100%", height=500)
    
    with col_info:
        st.subheader("Légende")
        st.write("🟢 **Safe Haven** : Commerce refuge")
        st.write("🔴 **Vigilance** : Zone mal éclairée")
        st.write("---")
        st.markdown("### Noter une rue")
        rue = st.text_input("Nom de la rue")
        light = st.select_slider("Niveau d'éclairage", options=["Sombre", "Moyen", "Parfait"])
        if st.button("Valider le signalement"):
            st.toast("Merci ! La carte a été mise à jour pour la communauté.")

# --- 2. CO-WALKING & MATCHING (Système Intelligent FSP3) ---
elif menu == "🤝 Co-Walking & Matching":
    st.markdown("<p class='main-title'>Trouver un Partenaire</p>", unsafe_allow_html=True)
    
    type_user = st.segmented_control("Vous êtes :", ["Étudiant", "Touriste", "Habitant"])
    
    tab_list, tab_create = st.tabs(["Trajets disponibles", "Proposer un trajet"])
    
    with tab_list:
        st.markdown("""
        <div class='safe-card'>
            <b>👤 Alice <span class='badge-verified'>VÉRIFIÉ</span></b> (Étudiante)<br>
            📍 <b>Trajet :</b> Vieux-Lille ➔ Vauban<br>
            ⏰ <b>Départ :</b> 23:30 | <b>Safe Score :</b> ⭐ 4.9/5
        </div>
        <div class='safe-card'>
            <b>👤 Mark <span class='badge-verified'>VÉRIFIÉ</span></b> (Touriste)<br>
            📍 <b>Trajet :</b> Citadelle ➔ Gare Lille Flandres<br>
            ⏰ <b>Départ :</b> 00:05 | <b>Besoin :</b> Guide local
        </div>
        """, unsafe_allow_html=True)
        if st.button("Rejoindre un groupe"):
            st.success("Demande envoyée ! Attendez la confirmation sur votre mobile.")

    with tab_create:
        with st.form("create_walk"):
            st.text_input("Point de départ")
            st.text_input("Destination")
            st.time_input("Heure de départ")
            if st.form_submit_button("Publier l'annonce"):
                st.balloons()

# --- 3. SOS & SÉCURITÉ (Bouton Alerte FSP1) ---
elif menu == "🚨 SOS & Sécurité":
    st.markdown("<p class='main-title'>Assistance Immédiate</p>", unsafe_allow_html=True)
    
    st.error("Utilisez ces fonctions uniquement en cas de besoin réel.")
    
    col_sos, col_arrived = st.columns(2)
    with col_sos:
        if st.button("🔴 DÉCLENCHER SOS"):
            st.markdown("<h2 style='color:red; text-align:center;'>ALERTE NIVEAU 1 ENVOYÉE</h2>", unsafe_allow_html=True)
    
    with col_arrived:
        if st.button("🏠 JE SUIS BIEN ARRIVÉ"):
            st.success("Super ! Votre groupe de trajet a été informé.")

# --- 4. DASHBOARD ÉQUIPE (OBS & WBS) ---
elif menu == "📈 Dashboard Équipe":
    st.header("Gestion du Projet SafeRoute")
    st.markdown(f"**Chef de Projet :** Lisa Marie | **Planification :** Kamélia")
    
    # Simulation des indicateurs clés (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("Utilisateurs Actifs", "124", "+12%")
    col2.metric("Zones Sécurisées", "45", "MEL")
    col3.metric("Safe Score Moyen", "4.8/5", "⭐⭐⭐⭐")
    
    st.write("---")
    st.subheader("Objectifs Opérationnels")
    st.checkbox("Concevoir une application simple et rassurante", value=True)
    st.checkbox("Informer sur les zones sécurisées", value=True)
    st.checkbox("Mettre en place le système de groupes", value=True)
