import random
player_1 = input("Apostador 1 ingresa tu nombre -> ")
player_2= input("Apostador 2 ingresa tu nombre -> ")
coinp1= 0
coinp2=0
print(player_1,"vs", player_2)
while coinp1<5 and coinp2<5 :
    coin = random.randint(0,1)
    if coin==0:
        print("ha salido cara", player_1, "ha ganado")
        coinp1+=1
    if coin==1:
        print("ha salido sello", player_2,"ha ganado")
        coinp2+=1
if coinp1>coinp2:
    print("Ha ganado",player_1,"con un puntaje total de",coinp1,"-",coinp2)
else:
    print("Ha ganado",player_2,"con un puntaje total de",coinp2,"-",coinp1)