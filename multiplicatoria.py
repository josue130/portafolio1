#E: Recibe un parametro de entrada
#R: El parametro tiene que ser entero positivo
#S: Retorna la multiplicatoria del numero 
def multiplicatoria(num):
     if isinstance(num,int)and (num>0):
          return multi_aux(num)
     else:
          print("El numero no es entero positivo O es un str.")
def multi_aux(num):
     if num==0:
          return 1
     elif (num)%2==0:
          return num* multi_aux(num-1)
     else:
          return multi_aux(num-1)
