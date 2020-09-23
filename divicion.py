def division(divisor,dividendo):
     if isinstance(divisor,int) and isinstance(dividendo,int):
          return divi_aux(divisor,dividendo)
     else:
          print("Error en parametros de entrada")

def divi_aux(d1,d2):
     if d2==0:
          print("Error divicion por cero")
     elif d1<d2:
          return 0
     elif d1==d2:
          return 1
     else:
          return 1 + divi_aux(d1-d2,d2)
