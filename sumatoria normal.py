#Recibe dos parametros de entrada
#R: Los parametro tiene que ser enteros positivos
#s: Retorna la sumatoria de un numero 
def sumatoria(inicio,fin):
     if isinstance(inicio,int) and isinstance(fin,int):
          return sumatoria_aux(inicio,fin)
def sumatoria_aux(inicio,fin):
     if inicio>fin:
          return 0
     else:
          return inicio + sumatoria_aux(inicio+1,fin)
