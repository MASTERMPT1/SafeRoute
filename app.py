import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from datetime import datetime

# --- CONFIGURATION UX/UI ---
st.set_page_config(page_title="SafeRoute | Sécurité & Solidarité MEL", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #1a1a2e; color: #f5f5dc; }
    .main-title { font-size: 45px; font-weight: bold; color: #ffd700; text-align: center; margin-bottom: 10px; }
    .stButton>button { border-radius: 25px; background: linear-gradient(90deg, #ffd700 0%, #ffae00 100%); color: #1a1a2e; font-weight: bold; border: none; height: 50px; }
    .safe-card { background: rgba(255, 255, 255, 0.08); padding: 20px; border-radius: 15px; border-left: 5px solid #ffd700; margin-bottom: 15px; }
    .review-card { background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 10px; border: 1px solid #ffd700; margin-bottom: 10px; font-style: italic; }
    .badge-verified { background-color: #4cd137; color: white; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: bold; }
    .badge-angel { background-color: #6c5ce7; color: white; padding: 3px 10px; border-radius: 12px; font-size: 11px; font-weight: bold; }
    .insta-link { color: #E1306C; font-weight: bold; font-size: 18px; text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='color: #ffd700; text-align: center;'>🛡️ SafeRoute</h1>", unsafe_allow_html=True)
    st.write("---")
    menu = st.radio("MENU", ["📍 Carte & Zones", "🤝 Co-Walking & Matching", "🚨 SOS & Sécurité", "⭐ Avis & Communauté", "👥 L'Équipe Projet"])
    st.write("---")
    st.markdown("📸 **Suis-nous sur Insta :**")
    st.markdown("<a href='https://instagram.com' class='insta-link'>@SafeRoute_MEL</a>", unsafe_allow_html=True)
    st.write("---")
    st.caption("M1 Management de Projet Touristique")

# --- 1. CARTE (AVEC SAFE HAVENS & OPEN DATA) ---
if menu == "📍 Carte & Zones":
    st.markdown("<p class='main-title'>Lieux Safe & Vigilance</p>", unsafe_allow_html=True)
    
    col_map, col_legend = st.columns([3, 1])
    
    with col_map:
        # Centré sur Lille (MEL)
        m = folium.Map(location=[50.6292, 3.0573], zoom_start=12, tiles="CartoDB dark_matter")
        
        # SAFE HAVENS (Commerces partenaires)
        for p in [[50.636, 3.062, "Safe Haven: Bar Le Windsor"], [50.628, 3.052, "Safe Haven: Kebab Solférino"]]:
            folium.Marker([p[0], p[1]], popup=p[2], icon=folium.Icon(color='blue', icon='shop', prefix='fa')).add_to(m)
            
        # OPEN DATA TRANSPO (Simulation temps réel)
        for p in [[50.637, 3.064, "Gare Lille Flandres - Métro: 2 min"]]:
            folium.Marker([p[0], p[1]], popup=p[2], icon=folium.Icon(color='orange', icon='subway', prefix='fa')).add_to(m)
            
        # SAFE ZONES (Éclairées)
        for p in [[50.633, 3.060, "Grand Place"]]:
            folium.Marker([p[0], p[1]], popup=f"SAFE: {p[2]}", icon=folium.Icon(color='green', icon='shield', prefix='fa')).add_to(m)
            
        # VIGILANCE
        for p in [[50.634, 2.964, "Ennetières-en-Weppes (Éclairage HS)"]]:
            folium.Circle([p[0], p[1]], radius=600, color="red", fill=True, popup=p[2]).add_to(m)
            
        st_folium(m, width="100%", height=500)
    
    with col_legend:
        st.subheader("Légende Pro")
        st.write("🔵 **Safe Haven** : Commerce refuge partenaire.")
        st.write("🟠 **Open Data** : Transports en temps réel.")
        st.write("🟢 **Safe** : Zone très éclairée.")
        st.write("🔴 **Vigilance** : Risque d'isolement.")

# --- 2. CO-WALKING (AVEC PARRAINAGE) ---
elif menu == "🤝 Co-Walking & Matching":
    st.markdown("<p class='main-title'>Matching Intelligent</p>", unsafe_allow_html=True)
    role = st.segmented_control("Tu es :", ["🎓 Étudiant", "🌍 Touriste", "🏠 Habitant"])
    
    col_search, col_results = st.columns([1, 1.5])
    with col_search:
        st.markdown("### 🔍 Ton trajet")
        with st.container(border=True):
            st.text_input("Départ")
            st.text_input("Arrivée")
            st.time_input("Heure prévue")
            st.button("Lancer le Matching")
        
        st.write("---")
        st.markdown("### 🏆 Ton Parrainage")
        st.info("Rang : **Ange Gardien** ✨")
        st.write("Accompagnements réalisés : **12**")
        st.progress(0.7)
        st.caption("Plus que 3 trajets pour devenir 'Protecteur de la MEL' !")

    with col_results:
        st.markdown("### 👥 Personnes à proximité")
        users = [
            {"name": "Alice", "role": "Étudiante", "txt": "Vieux-Lille ➔ Vauban | 23:45", "v": True, "r": "Ange Gardien"},
            {"name": "Léo", "role": "Étudiant", "txt": "Gare ➔ Hellemmes | 23:55", "v": True, "r": "Protecteur"},
            {"name": "Mark", "role": "Touriste", "txt": "Citadelle ➔ Centre | 00:10", "v": False, "r": "Nouvel Arrivant"}
        ]
        for u in users:
            verif = f"<span class='badge-verified'>VÉRIFIÉ</span>" if u['v'] else ""
            rang = f"<span class='badge-angel'>{u['r']}</span>"
            st.markdown(f"<div class='safe-card'><b>👤 {u['name']} {verif} {rang}</b> ({u['role']})<br>📍 {u['txt']}</div>", unsafe_allow_html=True)

# --- 3. SOS (AVEC ANGEL SHOT) ---
elif menu == "🚨 SOS & Sécurité":
    st.markdown("<p class='main-title'>Sécurité Totale</p>", unsafe_allow_html=True)
    
    st.subheader("🚨 Urgence Immédiate")
    c1, c2 = st.columns(2)
    with c1:
        if st.button("📞 APPEL POLICE (17)"):
            st.toast("Appel d'urgence...")
    with c2:
        if st.button("🔴 SOS GÉNÉRAL"):
            st.error("Signal envoyé à la communauté !")

    st.write("---")
    
    st.subheader("🛡️ Prévention Discrète")
    col_angel, col_discret = st.columns(2)
    with col_angel:
        st.markdown("**Angel Shot 📱**")
        if st.button("Simuler un Appel"):
            st.success("Appel entrant simulé : 'Allô maman, j'arrive...'")
    with col_discret:
        st.markdown("**Mode Discret 🔕**")
        st.toggle("Masquer l'écran")

    st.write("---")
    if st.button("🏠 JE SUIS BIEN ARRIVÉ.E"):
        st.balloons()

 # --- 4. AVIS & NOTES (NOUVEAU) ---

elif menu == "⭐ Avis & Communauté":
    st.markdown("<p class='main-title'>Avis des SafeRouters</p>", unsafe_allow_html=True)
    st.subheader("Note moyenne : ⭐ 4.8/5")
    reviews = [
        {"user": "Alice", "note": "⭐⭐⭐⭐⭐", "comm": "Grâce à SafeRoute, je ne stresse plus pour rentrer après la BU le soir !"},
        {"user": "Adam", "note": "⭐⭐⭐⭐", "comm": "Very helpful for a tourist who doesn't know the safe areas of Lille."},
        {"user": "Yasmine", "note": "⭐⭐⭐⭐⭐", "comm": "Le système de matching est top, j'ai rencontré des gens super sympas."},
        {"user": "Thomas", "note": "⭐⭐⭐⭐⭐", "comm": "Rassurant de voir les zones éclairées sur la carte."}
    ]
    for r in reviews:
        st.markdown(f"<div class='review-card'><b>{r['user']}</b> {r['note']}<br>'{r['comm']}'</div>", unsafe_allow_html=True)
    st.write("---")
    st.subheader("Laisser une note sur ton dernier trajet")
    st.select_slider("Ta note", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    st.text_area("Ton avis")
    elif st.button("Publier l'avis"):
    st.success("Merci ! Ton avis renforce la confiance de la communauté.") 
        
# --- 5. ÉQUIPE ---
elif menu == "👥 L'Équipe Projet":
    st.markdown("<p class='main-title'>L'Équipe SafeRoute</p>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='safe-card'> <b>Lisa Marie</b><br>Chef de projet</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'> <b>Kamélia</b><br>Responsable planification</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'> <b>Hala</b><br>Responsable financier</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='safe-card'> <b>Zélie</b><br>Chef de projet adjoint</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'> <b>Tingyu</b><br>Responsable RH</div>", unsafe_allow_html=True)
        st.markdown("<div class='safe-card'> <b>Nematullah Hussaini</b><br>Responsable Qualité</div>", unsafe_allow_html=True)
