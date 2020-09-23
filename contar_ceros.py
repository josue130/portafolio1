#E: Recibe un numero entero ya sea negativo o positivo
#R: No puede recibir flotantes
#S: Retorna la cantidad de ceros en el numero en caso de haber.

def contar_ceros(num):
     if isinstance(num,int):
          return contar_aux(num)
     else:
          print("El numero no es entero")
def contar_aux(num):
     if num<0:
          return contar_aux(num*-1)
     elif num==0:
          return 0
     else:
          if num%10==0:
               return 1 + contar_aux(num//10)
          else:
               return contar_aux(num//10)
