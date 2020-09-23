def multiplicacion(num,m):
     if isinstance(num,int) and (m,int):
          return mul_aux(num,m)
     else:
          print("Error en parametros de entrada")
def mul_aux(num,m):
     if m==0:
          return 0
     elif m==1:
          return num
     else:
          return num + mul_aux(num,m-1)
