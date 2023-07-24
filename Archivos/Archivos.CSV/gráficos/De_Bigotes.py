import pandas as pd
import matplotlib.pyplot as plt   #es una librería para visualizar datos de forma gráfica
import seaborn as sns   #es una librería que nos permite armar gráficos estadísticos

#abriendo el csv
df = pd.read_csv("Archivos\\Archivos.CSV\\archivo_creado.csv") 
    
#creando el gráfico de bigotes
sns.boxplot(x="Nombre",y="Edad",data=df)

#mostrando el gráfico
plt.show()
