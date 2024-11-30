import streamlit as st
st.write ("Hello world")

user_input = st.text_input ("Zadejte něco: ")                          
st.write("Zadali jste: ", user_input)


if st.button("Stiskni mne"):
	st.write("Tlačítko bylo stisknuto")

number = st.slider("Vyber číslo: ", 0, 100, 50)
st.write("Vybranéčíslo:", number)

option = st.selectbox(
	"Jakou máte rádi zmrzlinu",
	("Čokoládová", "Vanilková", "Jahodová")
)
st.write("Vaše oblíbená zmrzlina je: ", option)


st.markdown("""

# NADPIS PRVNÍ ÚROVNĚ
*kurzíva*
**tučně**

- Bod1
- Bod 2
- Bod 3

""")



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#vytvoření DataFrame
df = pd.DataFrame ({
	"První sloupec": [1, 2, 3, 4],
	"Druhý sloupec": [10, 20, 30, 40]
})

# Zobrazení dataframe v aplikaci
st.write("Zobrazení datového rámce:")
st.dataframe(df)

#vytvoření grafu
plt.figure(figsize=(10,4))
plt.bar(df["První sloupec"], df["Druhý sloupec"])

#nastavení popísků
plt.xlabel("První sloupec")
plt.ylabel("Druhý sloupec")
plt.title("Graf sloupcové hodnoty")

# zobarzení garfu ve streamlit
st.write("Visualizace dat v grafu")
st.pyplot(plt)


# nasleduji moje experimenty

number = st.number_input("Zadej číslo")
if number < 100:
	st.write("Toto je malé číslo")
else:
	st.write("Toto je velké číslo")

name = st.text_input("Jak se jmenuješ?")
st.write("Hello", name)


st.write("ahoj"[3])
list = ["a", "b", "c", "d"]
st.write(list[1:3])
st.write(list[3])


st.write("Násobky dvou")
n1 = st.number_input("Zadejte číslo jedna")
n2 = st.number_input("Zadejte číslo dva")
r = range(n1,n2)
for n in r:
   x = n * 2
   print(x)


