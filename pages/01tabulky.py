
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#vytvoření DataFrame
df = pd.DataFrame ({
	"Jméno": ["Novák", "Voříšek", "Koník", "Rybka"],
	"Věk": [16, 20, 30, 70]
})

# Zobrazení dataframe v aplikaci
st.write("Zobrazení datového rámce:")
st.dataframe(df)



