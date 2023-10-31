import pandas as pd
import matplotlib.pyplot as plt

# Substitua 'seuarquivo.csv' pelo caminho do seu arquivo CSV
df = pd.read_csv('/home/barbara/Documentos/npp_controle_yr03_04.csv')

media_npp = df['npp_controle'].mean()

plt.bar('Média', media_npp, color='blue')
plt.xlabel('Variável')
plt.ylabel('Valor Médio')
plt.title('Média da Variável NPP')
plt.show()

