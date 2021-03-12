#Christina Andrea Putri - Universitas Kristen Duta Wacana 

# Iniciti Drink menjual 3 jenis minuman, yaitu kopi, teh, dan milkshake. Untuk kopi dan teh ada pilihan panas/dingin
# Untuk harga Kopi: Iced coffee = Rp20.000,00 ; Hot Coffee = Rp 18.000,00
# Untuk harga Teh : Iced Tea = Rp15.000,00 ; Hot Tea = Rp12.000,00
# Harga milkshake : Rp25.000
# Tentukan total pembelian 2 Iced Coffee, 1 Iced Tea, dan 1 Milkshake

#Input = jenis minuman, jumlah, iced/coffee (kopi/teh)
#Proses = menghitung total pesanan sesuai dengan harganya dan jumlahnya
#Output = total pesanan, total pembayaran

inp = input("Command : ")

#coffee
icedco = 20000
hotco = 18000
xi = 0 
xh = 0 


#tea
icedtea = 15000
hotea = 12000
ti = 0 
th = 0 

#milkshake 
mk = 25000
tm = 0 

def icc(x):
    coficed = x*icedco
    return coficed

def hotcof(y):
    hc = y*hotco
    return hc

def iced_tea(z):
    icedt = z*icedtea
    return icedt

def hot_tea(a):
    htea = a*hotea
    return htea

def ms(b):
    mshake = b*mk
    return mshake

while inp != "End" or inp!="end":
    inp = input("What do you want? \n =>")

    if inp == "Coffee" or inp=="coffee":
        inp_sum = int(input("How many coffee(s) do you want to buy? : "))

        for i in range(inp_sum):
            inp_cho = input("Iced/Hot (%d) : "%(i+1))

            if inp_cho =="Iced" or inp_cho=="iced":
                xi += 1
                print("Total order(s) of Iced Coffee : ",xi)
            else : 
                xh += 1 
                print("Total order(s) of Hot Coffee : ",xh)
        total1=icc(xi)+hotcof(xh)
        print("Total of Coffee : ",total1)
    elif inp == "Tea" or inp=="tea":
        inp_sum = int(input("How many tea(s) do you want to buy? : "))

        for y in range(inp_sum):
            inp_cho = input("Iced/Hot (%d) : "%(y+1))

            if inp_cho =="Iced" or inp_cho=="iced":
                ti += 1
                print("Total order(s) of Iced Tea : ",ti)
            else : 
                th += 1 
                print("Total order(s) of Hot Tea : ",th)
        total2=iced_tea(ti)+hot_tea(th)
        print("Total of Tea : ",total2)
    elif inp == "Milkshake" or inp=="milkshake":
        inp_sum = int(input("How many milkshake(s) do you want to buy? : "))

        for y in range(inp_sum):
            tm +=1
            print("Total order(s) of Milkshake : ",tm)
        total3=ms(tm)
        print("Total of Milkshake : ", total3)
    else : 
        print("Total Order : ", xi+xh+ti+th+tm)
        print("Payment :", total1+total2+total3)
        break