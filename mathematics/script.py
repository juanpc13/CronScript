import scipy.stats

def regresionLineal(x, y):
  # obteniendo resultados para graficar
  pendiente, intercepto, r, p, stderr = scipy.stats.linregress(x, y)
  #retornar el valor de la CoeficienteRelacion
  return pendiente, intercepto, r, p, stderr

def getCoeficienteRelacion(x, y):
  # obteniendo resultados para graficar
  pendiente, intercepto, r, p, stderr = scipy.stats.linregress(x, y)
  #retornar el valor de la CoeficienteRelacion
  return r

import matplotlib.pyplot as plt

def genGraf(filename, titulo, xLabel, yLabel, xArray, yArray):
  fig, ax = plt.subplots(figsize=(16, 10))

  # obteniendo resultados para graficar
  pendiente, intercepto, r, p, stderr = scipy.stats.linregress(xArray, yArray)

  line = f'Regresion Lineal: Y = {intercepto:.3f} + {pendiente:.3f}X, R={r:.3f}'

  ax.plot(xArray, yArray, linewidth=0, color = 'b', marker='o', label='Puntos')
  ax.plot(xArray, intercepto + pendiente * xArray, color = 'r', label=line)

  # Plot Labels
  plt.title(titulo, fontsize=26)
  plt.ylabel(yLabel, fontsize=20)
  plt.xlabel(xLabel, fontsize=20)
  
  # Plot fontsize
  plt.xticks(fontsize=16, rotation=0)
  plt.yticks(fontsize=16, rotation=0)

  # Plot legend
  #plt.legend(loc='best', fontsize=24)
  ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), fancybox=True, shadow=True, ncol=5, fontsize=24)
  
  # Show or Save
  #plt.show()
  plt.savefig(filename)
#genGraf('', '', '', x, y, 1, 2)