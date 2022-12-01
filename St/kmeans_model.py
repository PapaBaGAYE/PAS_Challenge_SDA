import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import pickle

kmeans_S = pickle.load(open('C:/Users/PapaBaGAYE/Desktop/stlt/St/model_S.pkl', 'rb'))
kmeans_L = pickle.load(open('C:/Users/PapaBaGAYE/Desktop/stlt/St/model_L2.pkl', 'rb'))

clusters_S = {
  "0" : ["physique Chimie", "Genie civile", "Systèmes, Réseaux et Télécoms", "Informatique Developpement d’applications(web, mobile, gaming, etc.)", "Economie et gestion" ],
  "1" : ["Mathématiques physique Informatique", "Medecine", "Admission à l'école Polytechnique", "Admission à l'école supérieur UAM au pole Sciences et technologies", "Ecole Nationale de l'aviation Civile"],
  "2" : [],
  "3" : [],
  "4" : [],
  "5" : [],
  "6" : [],
  "7" : [],
  "8" : ["Mathématiques et Informatique", "Physique Chimie", "Biologie", "Science de l'environement", "Admission à l\'école Polytechnique", "Admission à l'école supérieur UAM au pole Sciences et technologies", "Ecole Nationale de l\'aviation Civile"],
  "9" : ["Mathématiques et Informatique", "Economie et gestion"],
  "10" : ["Mathématiques et Informatique", "Physique Chimie,Biologie", "Science de l'environement"],
  "11" : ["Physique Chimie", "Biologie", "Science de l'environement", "Economie et gestion"],
  "12" : ["Biologie,Science de l'environement", "Economie et gestion"],
  "13" : ["Biologie", "Science de l'environement", "Economie et gestion", "Physique Chimie"],
  "14" : ["Mathématiques et Informatique"],
  "15" : ["Mathématiques et Informatique", "Physique Chimie"],
  "16" : ["Mathématiques et Informatique", "Biologie"],
  "17" : ["Biologie", "Science de l'environement", "Economie et gestion", "Physique Chimie"],
  "18" : ["Physique Chimie"],
  "19" : ["Mathématiques et Informatique", "Physique Chimie", "Biologie", "Science de l'environement", "Médecine"],
  "20" : ["Biologie", "Science de l'environement"],
  "21" : ["Mathématiques et Informatique"],
  "22" : [],
  "23" : [],
  "24" : ["Mathématiques et Informatique", "Biologie", "Science de l'environement", "Economie et gestion"],
  "25" : ["Physique Chimie"],
  "26" : ["Mathématiques et Informatique", "Biologie", "Science de l'environement", "Médecine"],
  "27" : []
}

st.title("Clustering")
st.subheader("***SDA***")
# st.markdown("")

option = st.selectbox(
    "Choisir votre serie de Bac",
    ("", 'Baccalauréat S1 / S2', 'Baccalauréat L2'))

st.write(option)

if option == "Baccalauréat S1 / S2":
    Maths = st.slider(
        label="Maths",
        min_value=0,
        max_value=20,
        value=0)

    PC = st.slider(
        label="PC",
        min_value=0,
        max_value=20,
        value=0)

    SVT = st.slider(
        label="SVT",
        min_value=0,
        max_value=20,
        value=0)

    Philo = st.slider(
        label="Philo",
        min_value=0,
        max_value=20,
        value=0)

    Fr = st.slider(
        label="Fr",
        min_value=0,
        max_value=20,
        value=0)

    Anglais = st.slider(
        label="Anglais",
        min_value=0,
        max_value=20,
        value=0)

    HG = st.slider(
        label="HG",
        min_value=0,
        max_value=20,
        value=0)

    Moy = (Maths*5 + PC*6 + SVT*6 + Philo*2 + Fr*3 + Anglais*2 + HG*2) / 26

    but = st.button(label='Prédire')

    if but:
        if Maths == 0 or PC == 0 or SVT == 0 or Philo == 0 or Fr == 0 or Anglais == 0 or HG == 0:
            st.markdown('Veuillez renseingner de bonnes valeurs')
        else:
            pred = kmeans_S.predict([[Maths, PC, SVT, Philo, Fr, Anglais, HG, Moy]])
            st.markdown(f"Les filères les plus adaptées à cet élève sont : ")
            for mat in clusters_S[str(pred[0])]:
                st.markdown(f"- {mat}")

            etu = pd.DataFrame(
                            {
                                "Module" : ["Maths", "PC", "SVT", "Philo", "Français", "Anglais", "HG"],
                                "Notes" : [Maths, PC, SVT, Philo, Fr, Anglais, HG]
                            }   
                        )

            # fig = px.bar(data_frame=etu, x="Module", y="Notes", title="Notes")
            # st.plotly_chart(fig)

elif option == "Baccalauréat L2":
    Philo = st.slider(
        label="Philo",
        min_value=0,
        max_value=20,
        value=0)

    HG = st.slider(
        label="HG",
        min_value=0,
        max_value=20,
        value=0)

    Fr = st.slider(
        label="Fr",
        min_value=0,
        max_value=20,
        value=0)

    Anglais = st.slider(
        label="ANglais",
        min_value=0,
        max_value=20,
        value=0)

    LV2 = st.slider(
        label="LV2",
        min_value=0,
        max_value=20,
        value=0)

    PC_SVT = st.slider(
        label="PC_SVT",
        min_value=0,
        max_value=20,
        value=0)

    Oral_LV1 = st.slider(
        label="Oral_LV1",
        min_value=0,
        max_value=20,
        value=0)

    Maths = st.slider(
            label="Maths",
            min_value=0,
            max_value=20,
            value=0)

    Moy = (Philo*6 + HG*6 + Fr*5 + Anglais*4 + LV2*2 + PC_SVT*2 + Maths*2 + Oral_LV1) / 28

    but = st.button(label='Prédire')

    if but:
        if Philo == 0 or HG == 0 or Fr == 0 or Anglais == 0 or LV2 == 0 or PC_SVT == 0 or Maths == 0 or Oral_LV1 == 0:
            st.markdown('Veuillez renseingner de bonnes valeurs')
        else:
            pred = kmeans_L.predict([[Philo, HG, Fr, Anglais, LV2, PC_SVT, Maths, Oral_LV1, Moy]])
            st.markdown(f"L'élève fait parti du cluster {pred[0]}")

            etu = pd.DataFrame(
                            {
                                "Module" : ["Philo", "HG", "Fr", "Anglais", "LV2", "PC_SVT", "Maths", "Oral_LV1"],
                                "Notes" : [Philo, HG, Fr, Anglais, LV2, PC_SVT, Maths, Oral_LV1]
                            }   
                        )

            # fig = px.bar(data_frame=etu, x="Module", y="Notes", title="Notes")
            # st.plotly_chart(fig)