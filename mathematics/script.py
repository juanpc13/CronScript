import scipy.stats

def regresionLineal(x, y):
  # obteniendo resultados para graficar
  pendiente, intercepto, r, p, stderr = scipy.stats.linregress(x, y)
  #retornar el valor de la CoeficienteRelacion
  return pendiente, intercepto, r, p, stderr