import pandas as pd
import datetime

calidad = pd.read_excel('./Calidad_aire_San_Pedro.xlsx')
fecha = pd.to_datetime(calidad['Fecha Lectura'], errors='ignore')
calidad['Fecha Lectura'] = fecha
Calidad = calidad.set_index(['Fecha Lectura'])
print(Calidad)
Calidad.to_csv('Calidad1.xls')
