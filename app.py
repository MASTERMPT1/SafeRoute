import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Config de la page
st.set_page_config(page_title="SafeRoute - Rentrez sereins", page_icon="🛡️")

st.title("🛡️ SafeRoute")
st.markdown("### La solidarité pour un retour en toute sécurité")

# Menu de navigation
menu = ["Carte de Sécurité", "Proposer un Co-Walking", "Signaler une zone", "Conseils de sécurité"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Carte de Sécurité":
    st.subheader("📍 Zones éclairées et itinéraires recommandés")
    
    # Coordonnées de base (ex: Centre de Lille / Métropole)
    m = folium.Map(location=[50.6292, 3.0573], zoom_start=13)
    
    # Simulation de zones sécurisées (Points verts)
    folium.Marker([50.633, 3.06], popup="Zone très éclairée - Grand Place", icon=folium.Icon(color='green')).add_to(m)
    folium.Marker([50.620, 3.05], popup="Point de RDV sécurisé - Gare", icon=folium.Icon(color='blue')).add_to(m)
    
    st_folium(m, width=700, height=500)
    st.info("Les points verts indiquent les zones avec éclairage renforcé et caméras de ville.")

elif choice == "Proposer un Co-Walking":
    st.subheader("🤝 Créer un groupe de trajet")
    with st.form("form_walk"):
        depart = st.text_input("Lieu de départ")
        destination = st.text_input("Destination")
        heure = st.time_input("Heure de départ prévue")
        nb_pers = st.number_input("Nombre de personnes max", min_value=2, max_value=6)
        submit = st.form_submit_button("Publier l'annonce")
        
        if submit:
            st.success(f"Annonce publiée ! Les autres étudiants peuvent désormais te rejoindre pour le trajet vers {destination}.")

elif choice == "Signaler une zone":
    st.subheader("⚠️ Signaler un problème (Lampadaire HS, zone sombre)")
    type_pb = st.selectbox("Type de problème", ["Éclairage défaillant", "Zone isolée", "Travaux gênants"])
    desc = st.text_area("Description")
    if st.button("Envoyer le signalement"):
        st.warning("Signalement enregistré. Merci pour la communauté !")
