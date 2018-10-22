from turtle import *
def piirra_spiraali(arvot, paksuus = 1):
    co = arvot[0]
    lkm = int(arvot[1])
    r = int(arvot[2]) 
    a = float(arvot[3])
    paksuus = int(arvot[4])
    pensize(paksuus)
    color(co)
    down()
    for i in range (lkm):
        circle(r, 90)
        r = r + a
    up()

def piirra_tiedostosta(tiedosto):
    with open (tiedosto) as kohde:
        sisalto = kohde.read()
        sisalto = sisalto.split()
        for i in sisalto:
            arvot = i.split(",")
            print(arvot)
            piirra_spiraali(arvot)
       

    
piirra_tiedostosta("spiraali.txt")

       
