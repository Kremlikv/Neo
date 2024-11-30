#vytvoření grafu
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame ({
	"První sloupec": [1, 2, 3, 4],
	"Druhý sloupec": [10, 20, 30, 40]
})

plt.figure(figsize=(10,4))
plt.bar(df["První sloupec"], df["Druhý sloupec"])

#nastavení popísků
plt.xlabel("První sloupec")
plt.ylabel("Druhý sloupec")
plt.title("Graf sloupcové hodnoty")

# zobarzení grafu ve streamlit
st.write("Visualizace dat v grafu")
st.pyplot(plt)