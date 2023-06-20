n = int(input("Digite um número: "))
while n<1 or n>10:
    print("O número deve estar entre 1 e 10")
    n = int(input("Digite um número: "))
t = 1
while t<=10:
    print(n,"x",t,"=",n*t)
    t+=1
print("Pronto")