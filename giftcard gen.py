import os
from colorama import Fore
import time
import string
import random

prp = Fore.MAGENTA
blu = Fore.BLUE
wh = Fore.WHITE
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
os.system("title  GiftCard Generator made By Nestor :)   ")
def logo():
        print(f"""

{prp} ▄▄ • ▪  ·▄▄▄▄▄▄▄▄ ▄▄·  ▄▄▄· ▄▄▄  ·▄▄▄▄    {wh}▄▄ • ▄▄▄ . ▐ ▄ 
{prp}▐█ ▀ ▪██ ▐▄▄·•██  ▐█ ▌▪▐█ ▀█ ▀▄ █·██▪ ██ {wh}▐█ ▀ ▪▀▄.▀·•█▌▐█
{prp}▄█ ▀█▄▐█·██▪  ▐█.▪██ ▄▄▄█▀▀█ ▐▀▀▄ ▐█· ▐█▌{wh}▄█ ▀█▄▐▀▀▪▄▐█▐▐▌
{prp}▐█▄▪▐█▐█▌██▌. ▐█▌·▐███▌▐█ ▪▐▌▐█•█▌██. ██ {wh}▐█▄▪▐█▐█▄▄▌██▐█▌
{prp}·▀▀▀▀ ▀▀▀▀▀▀  ▀▀▀ ·▀▀▀  ▀  ▀ .▀  ▀▀▀▀▀▀• {wh}·▀▀▀▀  ▀▀▀ ▀▀ █▪
            |Everything Randomly Generated Based on Algorythm|
         """)
logo()
print("")
print(f"Type '?' for help :D")
while 1:
    command = input(f"{wh}({prp}user{wh}/{prp} client{wh})")
    if command == "?":
        print(f"""
1{prp}.{wh} Ebay 
2{prp}.{wh} Amazon
3{prp}.{wh} Playstation
4{prp}.{wh} Paypal
5{prp}.{wh} Visa
6{prp}.{wh} Some Things About Us

  """)
    elif command == "1":
        total = input("How Many Would You Like To Generate? ")
        number = int(total)
        file = (total + " Generated By Nestor Gift Card Generator.txt")
        file2 = 'GiftCardsCodes.txt'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            newline = "\n"
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+newline)
    elif command == "2":
        total = input("How Many Would You Like To Generate? ")
        number = int(total)
        file = (total + " Generated By Nestor Gift Card Generator.txt")
        file2 = 'GiftCardsCodes.txt'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            space1 = "-"
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            space2 = "-"
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            newline = "\n"
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)
    elif command == "3":
        total = input("How Many Would You Like To Generate? ")
        number = int(total)
        file = (total + " Generated By Nestor Gift Card Generator.txt")
        file2 = 'GiftCardsCodes.txt'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            space1 = "-"
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            space2 = "-"
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            newline = "\n"
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
    elif command == "4":
        total = input("How Many Would You Like To Generate? ")
        number = int(total)
        file = (total + " Generated By Nestor Gift Card Generator.txt")
        file2 = 'GiftCardsCodes.txt'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            space1 = "-"
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            space2 = "-"
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            newline = "\n"
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+newline)
    elif command == "5":
        total = input("How Many Would You Like To Generate? ")
        number = int(total)
        file = (total + " Generated By Nestor Gift Card Generator.txt")
        file2 = 'GiftCardsCodes.txt'
        for x in range(number):
            generate1 = random.choice(gentype)
            generate2 = random.choice(gentype)
            generate3 = random.choice(gentype)
            generate4 = random.choice(gentype)
            generate5 = random.choice(gentype)
            generate6 = random.choice(gentype)
            generate7 = random.choice(gentype)
            generate8 = random.choice(gentype)
            generate9 = random.choice(gentype)
            generate10 = random.choice(gentype)
            generate11 = random.choice(gentype)
            generate12 = random.choice(gentype)
            generate13 = random.choice(gentype)
            generate14 = random.choice(gentype)
            generate15 = random.choice(gentype)
            generate16 = random.choice(gentype)
            newline = "\n"
            space = " "
            gen1 = random.choice(gentype)
            gen2 = random.choice(gentype)
            gen3 = random.choice(gentype)
            gen4 = random.choice(gentype)
            gen5 = random.choice(gentype)
            gen6 = random.choice(gentype)
        
        
            with open(file, 'a') as out:
                out.write(generate1+generate2+generate3+generate4+generate5+generate6+generate7+generate8+generate9+generate10+generate11+generate12+generate13+generate14+generate15+generate16+newline)
            with open(file2, 'a') as out2:
                out2.write(gen1+gen2+gen3+gen4+gen5+gen6+newline)

        

            