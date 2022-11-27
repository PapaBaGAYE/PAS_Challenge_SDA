import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import pickle


kmeans = pickle.load(open('C:/Users/PapaBaGAYE/Desktop/stlt/kmeans.pkl', 'rb'))

st.title("CLustering")
st.subheader("***SDA***")
# st.markdown("")

Maths = st.number_input(
    label="Maths",
    min_value=0,
    max_value=20,
    value=0)

PC = st.number_input(
    label="PC",
    min_value=0,
    max_value=20,
    value=0)

SVT = st.number_input(
    label="SVT",
    min_value=0,
    max_value=20,
    value=0)

Philo = st.number_input(
    label="Philo",
    min_value=0,
    max_value=20,
    value=0)

Fr = st.number_input(
    label="Fr",
    min_value=0,
    max_value=20,
    value=0)

Anglais = st.number_input(
    label="Anglais",
    min_value=0,
    max_value=20,
    value=0)

HG = st.number_input(
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
        pred = kmeans.predict([[Maths, PC, SVT, Philo, Fr, Anglais, HG, Moy]])
        st.markdown(f"L'élève fait parti du cluster {pred[0]}")