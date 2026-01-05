import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# Configuration de la page avec un style plus pro
st.set_page_config(page_title="SafeRoute | Sécurité Urbaine", page_icon="🛡️", layout="wide")

# CSS pour personnaliser l'interface (plus Gen Z, plus clean)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #6c5ce7; color: white; }
    .stAlert { border-radius: 15px; }
    h1 { color: #2d3436; font-family: 'Helvetica'; }
    </style>
    """, unsafe_allow_html=True)

# Barre latérale avec Logo et Infos Projet
with st.sidebar:
    st.title("🛡️ SafeRoute")
    st.info(f"**Projet :** M1 Tourisme\n**Équipe :** Groupe de 6\n**Zone :** Métropole Waze")
    st.markdown("---")
    menu = st.radio("Navigation", ["🗺️ Carte Safe", "🤝 Co-Walking", "🚨 Signalement", "📚 Guide & Conseils"])

# --- ONGLET 1 : LA CARTE ---
if menu == "🗺️ Carte Safe":
    st.header("Itinéraires & Zones Sécurisées")
    st.write("Visualisez les rues éclairées et les commerces partenaires 'Safe Haven'.")
    
    # Création de la carte centrée sur la zone (Ex: Lille)
    m = folium.Map(location=[50.6292, 3.0573], zoom_start=13, tiles="cartodbpositron")
    
    # Ajout de zones sécurisées
    folium.Circle([50.633, 3.06], radius=300, color="green", fill=True, popup="Zone Lumière Renforcée").add_to(m)
    folium.Marker([50.623, 3.066], popup="**Le Safe Bar** - Ouvert jusqu'à 2h", icon=folium.Icon(color='blue', icon='shop', prefix='fa')).add_to(m)
    
    st_folium(m, width="100%", height=500)
    
    st.success("✅ **Conseil :** Privilégiez les tracés en vert pour votre retour.")

# --- ONGLET 2 : CO-WALKING ---
elif menu == "🤝 Co-Walking":
    st.header("Trouver des partenaires de route")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Annonces en cours")
        st.info("👤 **Léa** (Univ Lille) : Gare Lille Flandres ➔ Solférino (Départ : 23h30)")
        st.info("👤 **Adam** (IAE) : Vieux-Lille ➔ Vauban (Départ : 00h15)")
    
    with col2:
        st.subheader("Publier une annonce")
        with st.form("new_walk"):
            dep = st.text_input("Départ")
            dest = st.text_input("Destination")
            time = st.time_input("Heure de départ")
            if st.form_submit_button("Lancer l'appel"):
                st.balloons()
                st.success("Annonce publiée ! Reste sur cette page pour les notifications.")

# --- ONGLET 3 : SIGNALEMENT ---
elif menu == "🚨 Signalement":
    st.header("Signaler un incident en direct")
    st.warning("Tes signalements aident la communauté à rester en sécurité.")
    
    type_sig = st.selectbox("Type d'alerte", ["Lampadaire éteint", "Travaux dangereux", "Zone sombre/isolée", "Autre"])
    desc = st.text_area("Précisions sur le lieu")
    if st.button("Envoyer l'alerte"):
        st.error(f"Signalement enregistré à {datetime.now().strftime('%H:%M')}. Merci !")

# --- ONGLET 4 : GUIDE ---
elif menu == "📚 Guide & Conseils":
    st.header("Bonnes pratiques de sécurité")
    st.markdown("""
    - 📱 **Batterie :** Vérifie toujours d'avoir plus de 20% avant de partir.
    - 🎧 **Écouteurs :** Garde une oreille libre pour rester attentif à ton environnement.
    - 🤝 **Collectif :** Ne reste pas seul(e) si tu as un doute, entre dans un 'Safe Haven'.
    """)
