import streamlit as st


st.image("logo_petit_noir.png", width=150)

# CSS personnalisé
st.markdown(
    """
    <style>


    /* Masquer complètement le bandeau si nécessaire */
    header {
        visibility: hidden;
    }
    header > div {
        display: none;
    }



    /* Personnaliser les autres éléments si nécessaire */
    /* Applique le style pour centrer le texte globalement */
        .center-text {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
            text-align: center;
            font-size: 20px;
        }

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');
   

    </style>
    """,
    unsafe_allow_html=True
)

st.header("Les zones d'entrainement.")

st.text("Les zones d'entrainement sont calculées sur la base de la vitesse critique.")

st.text("La vitesse critique est estimée sur la base de deux tests à intensité maximale sur 1200 mètres et 3600 mètres.")

st.text("La vitesse critique délimite les domaines d'effort élevés et sévères. Au délà de cette vitesse, l'athlète tend vers sa cosommation d'oxygène maximale (VO2Max).")

st.divider()

st.text("Renseignez des temps sur des efforts maximales de 3 à 5 minutes et de 10 à 15 minutes.")

st.divider()



st.subheader("Test 3 à 5 minutes")

distance_1 = st.number_input("Distance (mètres) ", min_value=0, max_value=10000, step=1)

col1, col2 = st.columns(2)

# Saisie des minutes dans la première colonne
with col1:
    minutes_1 = st.number_input("Minutes ", min_value=0, max_value=59, step=1)

# Saisie des secondes dans la deuxième colonne
with col2:
    secondes_1 = st.number_input("Secondes ", min_value=0, max_value=59, step=1)


st.subheader("Test 10 à 15 minutes")

distance_2 = st.number_input("Distance (mètres)", min_value=0, max_value=10000, step=1)

col1, col2 = st.columns(2)

# Saisie des minutes dans la première colonne
with col1:
    minutes_2 = st.number_input("Minutes", min_value=0, max_value=59, step=1)

# Saisie des secondes dans la deuxième colonne
with col2:
    secondes_2 = st.number_input("Secondes", min_value=0, max_value=59, step=1)

time_1 = minutes_1 * 60 + secondes_1
time_2 = minutes_2 * 60 + secondes_2





st.divider()

st.subheader("Vitesse critique")

if distance_1 == 0 or distance_2 == 0 or time_1 == 0 or time_2 == 0:
     st.warnings("Les distances et le temps ne peuvent être nuls")
else:

    cs = distance_1 / (time_1 + (time_2 - (distance_2/distance_1)*time_1)/(distance_2/distance_1 - 1))

    # convert speed m/s en allure mm:ss par km
    def calculate_pace(total_seconds, distance_meters):
            pace_seconds_per_km = total_seconds / (distance_meters / 1000)
            minutes, seconds = divmod(pace_seconds_per_km, 60)
            return f"{int(minutes)} min {int(seconds):02d} s / km"

    st.write(f"Vitesse critique: {calculate_pace(1, cs)}")



    zone1_max = round(0.75 * cs)
    zone2_max = round(0.85 * cs)
    zone3_max = round(0.93 * cs)
    zone4_max = round(1* cs)

    st.subheader("Zones 1")
    st.write(f"{0} - {zone1_max}")

    st.subheader("Zones 2")
    st.write(f"{zone1_max} - {zone2_max}")

    st.subheader("Zones 3")
    st.write(f"{zone2_max} - {zone3_max}")

    st.subheader("Zones 4")
    st.write(f"{zone3_max} - {zone4_max}")

    st.subheader("Zones 5")
    st.write(f"{zone4_max} - et plus")