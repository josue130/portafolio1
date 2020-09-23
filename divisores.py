def Divisores(num):
    if isinstance(num,int):
         return divisores_aux(num,num)
def divisores_aux(num,div):
     if div==0:
          return 0
     else:
          if num%div==0:
               print(div)
               return divisores_aux(num,div-1)
          else:
               return divisores_aux(num,div-1)
