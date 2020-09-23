def sumatoriarangos(inicio,fin,rango):
     if isinstance(inicio,int) and isinstance(fin,int) and isinstance(rango,int):
          return SR_aux(inicio,fin,rango)

def SR_aux(inicio,fin,rango):
     if inicio>fin:
          return 0
     else:
          return inicio +  SR_aux(inicio + rango,fin,rango)
