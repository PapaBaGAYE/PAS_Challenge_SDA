import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import pickle


kmeans_S = pickle.load(open('C:/Users/PapaBaGAYE/Desktop/stlt/St/model_S.pkl', 'rb'))
kmeans_L = pickle.load(open('C:/Users/PapaBaGAYE/Desktop/stlt/St/model_L2.pkl', 'rb'))

st.title("CLustering")
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
            st.markdown(f"L'élève fait parti du cluster {pred[0]}")

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


    Moy = (Philo*6	+ HG*6 + Fr*5 + Anglais*4 + LV2*2 + PC_SVT*2 + Maths*2 + Oral_LV1) / 28

    but = st.button(label='Prédire')

    if but:
        if Philo == 0 or HG == 0 or Fr == 0 or Anglais == 0 or LV2 == 0 or PC_SVT == 0 or Maths == 0 or Oral_LV1 == 0:
            st.markdown('Veuillez renseingner de bonnes valeurs')
        else:
            pred = kmeans_L.predict([[Philo, HG, Fr, Anglais, LV2, PC_SVT, Maths, Oral_LV1, Moy]])
            st.markdown(f"L'élève fait parti du cluster {pred[0]}")