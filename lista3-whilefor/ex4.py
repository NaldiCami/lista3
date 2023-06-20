import random

vezes = int(input("Quantas vezes você quer jogar a moeda? "))
cara = 0
coroa = 0
while vezes > 0:
    moeda = random.randint(0,1)
    if moeda == 0:
        print("Cara")
        cara +=1
    else:
        print("Coroa")
        coroa +=1
    vezes -= 1
print("Cara =",cara,"\nCoroa =",coroa)


Footer
© 2023 GitHub, Inc.
Footer navigation
Terms