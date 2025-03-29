'''frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)
   

x = 1
while x < 10:
    print(x)
    x += 1
x = (1,2,3,4,5,6,7,8,9)
for yx in x:
    print(yx)

for x in range(1,100,2):
 print(x)


tr = 1
while tr < 10:
   print(tr)
   tr += 1

for index in range(10, -11, -1 ):
    print(index)   
'''
#entrada de dados    
index = float(input(f"digite o numero da tabuada que deseje saber: ").replace(",","."))

for tabuada in range(1,10):
   result = (index*tabuada)
#saida de dados
   print(index,"X",tabuada,"=",result)


#entrada de dados
init = int(input("Qual o numero da tabuada que deseja saber: "))
proc = 1
#processsamento de dados
while proc <= 9:
   proc += 1
   result = init*proc
#saida de dados
   print(init, "X", proc, "=", result)