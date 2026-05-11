#q4
num = int(input("Digite um número: "))

mult = 1
result = 0

while num !=0:
  mult = 1
  result = 0
  while result <100:
    result = num * mult
    mult +=1
    if result <100:
      print(result)
  num = int(input("Digite um número: "))
