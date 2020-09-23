#E:Recibe un parametro de entrada
#S:Retorna la cantidaad de digitos que tiene el numero
#R:


def largo(num):
     if num==0:
          return 0
     else:
          return 1 + largo(num//10)
