import pandas as pd
import matplotlib.pyplot as plt

def crear_dataframe(particles):
    data = {
        "Nombre": [p.nombre for p in particles.values()],
        "Tipo": [p.tipo for p in particles.values()],
        "Carga (e)": [p.carga for p in particles.values()],
        "Masa (MeV/c^2)": [p.masa for p in particles.values()],
        "Carga de Color": [p.carga_color for p in particles.values()],
        "Sabor": [p.sabor for p in particles.values()]
    }
    return pd.DataFrame(data)

def graficar_masa(df):
    df.plot(kind='bar', x='Nombre', y='Masa (MeV/c^2)', legend=False, color='skyblue')
    plt.title("Masa de las Partículas del Modelo Estándar")
    plt.ylabel("Masa (MeV/c^2)")
    plt.xlabel("Partícula")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

def graficar_distribucion_tipos(df):
    df['Tipo'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title("Distribución de Tipos de Partículas")
    plt.ylabel("")
    plt.show()
