
n = int(input('Digite o numero de elementos no Fibonacci: '))

fibo = []
t1 = 0
t2 = 1
cont = 3

fibo.append(t1)
fibo.append(t2)

print(f'{t1} -> {t2}',end='')

while True:
    t3 = t1 + t2
    fibo.append(t3)
    print(f' -> {t3}',end='')

    t1 = t2
    t2 = t3
    cont +=1

    if cont <= n:
        break
    
print(' -> FIM')

if n in fibo:
    print('O numero digitado pertence a sequencia!')
else:
    print('O numero digitado não pertence a sequencia!')
