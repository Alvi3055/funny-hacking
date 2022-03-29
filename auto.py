import pyfiglet
import time
import os
import termcolor

banner="starting"
banner_so=pyfiglet.figlet_format(banner,font='bell')
print(banner_so)
time.sleep(3)
os.system('clear')

banner1="Albida"
banner_s=pyfiglet.figlet_format(banner1)
print(banner_s)
time.sleep(1)



print("what can you do sir?Plz inter your chosen number:\n 1.Facebook hack\n 2.Instagram hack\n 3.Gmail hack\n 4.Telegram hack")

def hacking(social):
    name="start hacking"
    print(pyfiglet.figlet_format(name,font='larry3d'))
    time.sleep(3)
    target=input("inter your target "+social+" id link:")
    name1=input("inter your target "+social+" id name")
    print("Your target id is ", target)
    print("Your target id name is",name1)
    last=(input("To continue hacking write 'start'"))
    if last=="start" or "start ":
        write="Hacking started"
        banner_m=(pyfiglet.figlet_format(write,font="colossal"))
        print(termcolor.cprint(banner_m,"red"))
        time.sleep(15)
    print("Your targeted "+social +" id password is:'My name is",name1,".Who are you?'")


def input_number():
    input1=int(input("Plz select your choice"))
    if input1==1:
        return "Facebook"
    elif input1==2:
        return "Instagram"
    elif input1==3:
        return "Gmail"
    elif input1==4:
        return "Telegram"
        
number=input_number()

hacking(number)
