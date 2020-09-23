def tiene_ceros(num):
     if num==0:
          return True
     if isinstance(num,int) and num>0:
          return aux(num)
     else:
          print("El numero ingresado no es un numero entero o no es mayor a cero")
          
def aux(num):
     if num==0:
          return False
     else:
          if (num%10)==0:
               return True
          
          else:
               return aux(num//10)
