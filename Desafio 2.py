p = str(input('Digite uma palavra: '))
t = len(p)
cont = mai = min = 0

for i in range(0, t):
    if p[i] in 'aA':
        cont += 1
        if p[i].isupper():
            mai += 1
        if p[i].islower():
            min += 1

if cont > 0:   
    print(f"A palavra {p} possui a letra 'a' e ela se repetiu {cont} vez(es).")
    print(f'Sendo {mai} A(s) maiuscula(s) e {min} a(s) minuscula(s)!')
else:
    print("A palavra não possui a letra 'a'!")         