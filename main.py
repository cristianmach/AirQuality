import os
import sqlite3
import warnings

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyodbc
import seaborn as sns

from public.routes import df_calidad_del_aire

# Imprimir la ruta absoluta
ruta_absoluta = os.path.abspath(df_calidad_del_aire)
#print(f"Ruta absoluta del archivo: {ruta_absoluta}")

# Leer el archivo en partes más pequeñas
chunksize = 1000000  # Número de filas a leer por vez
chunk_iter = pd.read_csv(df_calidad_del_aire, chunksize=chunksize)
df_general = pd.read_csv(df_calidad_del_aire, chunksize=chunksize)

# Leer y mostrar las primeras 5 filas del primer chunk
first_chunk = next(chunk_iter)
print(first_chunk.head())


