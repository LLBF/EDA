import pandas as pd

lluvias = pd.read_json('Valores_mensuales_lluvia_Arteixo.json', orient='values')
lluvia = lluvias['resultados']
row = []

for x in range(len(lluvia)):
    Valor_a = lluvia[x]['Data'][0:4]
    Valor_m = lluvia[x]['Data'][5:7]
    Parametro = lluvia[x]['Parámetro']
    if Parametro == 'Chuvia':
        Parametro = 'Lluvia'
    elif Parametro == 'Chuvia diaria máxima':
        Parametro = 'Lluvia diaria máxima'
    elif Parametro == 'Humidade media das máximas a 1.5m':
        Parametro = 'Humedad media de máximas a 1.5m'
    Valor = lluvia[x]['Valor']
    Unidades = lluvia[x]['Unidades']
    row.append((Valor_a, Valor_m, Parametro, Valor, Unidades))

lluvia_columns = ['Año', 'Mes', 'Parámetro', 'Valor', 'Unidades']
Total = pd.DataFrame(row, columns= lluvia_columns)
Total = Total.loc[(Total.Valor)>0] #quito los 0 y -9999 y sobreescribo
Rain = Total.set_index(['Año','Mes']) #los indices son la fecha
print(Rain)

Rain.to_csv('Precipitaciones anual.xls')
