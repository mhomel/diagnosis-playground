
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych
df = pd.read_csv("pacjenci.csv")

# Funkcje pomocnicze

def classify_risk(row):
    if row["Ciśnienie skurczowe"] > 140 or row["Tętno"] > 85 or row["Cholesterol"] >= 240:
        return "Wysokie"
    elif row["Ciśnienie skurczowe"] > 130 or row["Tętno"] > 80 or row["Cholesterol"] >= 200:
        return "Średnie"
    else:
        return "Niskie"

def cholesterol_level(value):
    if value >= 240:
        return "Wysoki"
    elif value < 200:
        return "Niski"
    else:
        return "Średni"

# Wstępna analiza danych

print("Podgląd danych:")
print(df.head())
print("\nDostępne kolumny:")
print(df.columns)

# Nowe kolumny

# Wzrost w metrach
df["Wzrost (m)"] = df["Wzrost (cm)"] / 100

# Obliczanie BMI
df["BMI"] = df["Waga (kg)"] / (df["Wzrost (m)"] ** 2)
df["BMI"] = df["BMI"].round(1)

# Klasyfikacja ryzyka
df["Ryzyko"] = df.apply(classify_risk, axis=1)

# Klasyfikacja poziomu cholesterolu
df["Poziom cholesterolu"] = df["Cholesterol"].apply(cholesterol_level)

#  Grupowanie i statystyki

grupy = df.groupby(["Płeć", "Status"])
srednie = grupy[["BMI", "Cholesterol", "Tętno", "Ciśnienie skurczowe"]].mean()
print("\nŚrednie wartości według płci i statusu:")
print(srednie)

# Opisowe statystyki dla wybranych kolumn
print("\nStatystyki opisowe:")
print(df[["BMI", "Cholesterol", "Tętno"]].describe())

# Lista pacjentów wysokiego ryzyka
df_wysokie = df[df["Ryzyko"] == "Wysokie"]
print("\nPacjenci z wysokim ryzykiem:")
print(df_wysokie)

#  Wizualizacje 

# Średnie BMI wg statusu zdrowia
bmi_srednia = df.groupby("Status")["BMI"].mean()

# Wykres z Pandas
bmi_srednia.plot(kind="bar", title="Średnie BMI wg statusu zdrowia", ylabel="BMI", xlabel="Status zdrowia")

# Wykres z Matplotlib
plt.figure()
plt.bar(bmi_srednia.index, bmi_srednia.values, color="skyblue")
plt.title("Średnie BMI wg statusu zdrowia")
plt.xlabel("Status zdrowia")
plt.ylabel("Średnie BMI")
plt.grid(axis="y")
plt.tight_layout()
plt.show()
