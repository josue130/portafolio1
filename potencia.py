#Recibe dos parametros de entrada
#R: tienen que ser numero enteros
#s: Retorna la elevacion de numero deseado 
def potencia(num,pot):
     if isinstance(num,int) and isinstance(pot,int):
          return aux_pot(num,pot)
def aux_pot(num,pot):
     if pot==0:
          return 1
     else:
          return num * aux_pot(num,pot-1)
