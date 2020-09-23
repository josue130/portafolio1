#E:Recibe un parametro de entrada
#R:Solo pueden entrar numeros enteros positivos
#S: Retorna True si es impar o False si par
def impar(num):
     if isinstance(num,int) and num>0:
          return impar_aux(num)
def impar(num):
     if num==0:
          return True
     elif num%2!=0:
          return True
     else:
          return False
