#q7
cont = 0
total = 0
for num in range(1, 201, 1):
    div_primo = 0
    for i in range(1, num+1, 1):
       if num % i == 0:
            div_primo = div_primo + 1
    if div_primo == 2:
        print(num)
        total = total + 1

print(f"Nesse intervalo temos {total} números primos")

