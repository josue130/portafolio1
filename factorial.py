#E: Recibe un parametro de entrada
#R: El paramtro tiene que ser entero positivo
#S: Retorna el factorial de un numero
def factorial(num):
     if isinstance(num,int) and (num>=0):
          return factorial_aux(num)

     else:
          print("El numero no es entero mayor o igual a cero")
def factorial_aux(num):
     if num==0:
          return 1
     else:
          return num * factorial_aux(num-1)
