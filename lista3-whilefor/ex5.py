import time
print("As opções são: ")
print("1 - Candidato Jair Rodrigues\n2 - Candidato Carlos Luz\n3 - Candidato Neves Rocha")
print("4 - Voto nulo\n5Voto branco")
v = 0
JR = 0
CL = 0
NR = 0
NL = 0
BR = 0
while v < 6:
    v = int(input("Digite seu voto: "))
    if v == 1:
        JR +=1
    elif v ==2:
        CL +=1
    elif v ==3:
        NR +=1
    elif v ==4:
        NL+=1
    elif v ==5:
        BR+=1
print("Resultado:")
time.sleep(1)
print("Jair Rodrigues =",JR)
print("Carlos Luz =",CL)
print("Never Rocha =",NR)
time.sleep(1)
print((NL/100)*(JR+CL+NR+NL+BR),"%","de votos nulos")
print((BR/100)*(JR+CL+NR+NL+BR),"%","de votos brancos")
time.sleep(2)
if JR>CL and JR>NR:
    print("O vencedor foi: Jair Rodrigues")
elif CL>JR and CL>NR:
    print("O vencedor foi: Carlos Luz")
elif NR>JR and NR>CL:
    print("O vencedor foi: Neves Rocha")
else:
    print("Ouve um empate técnico")