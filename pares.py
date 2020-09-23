#E: Recibe numeros enteros positivos.
#R: El parametro de entrada tiene que ser entero positivo..
#S: Retorna un numero formado solo por los numeros parees.
def pares(num):
     if isinstance(num,int) and (num>0):
          return pares_aux(num)
     else:
          print("No es entero positivo o es un str")
def pares_aux(num):
     if num==0:
          return False
     else:
          if num%2==0:
               return True
          else:
               return False 
               
