import time
import final
import random
import colorama
def main():
    food = 100
    energy = 100
    sila = 30
    print(colorama.Fore.LIGHTGREEN_EX+colorama.Style.BRIGHT+"2 ГЛАВА. ПОБЕГ")
    t = int(input(f"""{colorama.Fore.CYAN}1. Поспать.
{colorama.Fore.YELLOW}2. Покушать( не шаурмы =[ ).
{colorama.Fore.LIGHTRED_EX}3. Потягаться на турниках. 
4. Просто БЕЖИМ!"""))
    if t == 2:
        print("Еееее ты покушал #*#*#-*# *#*#")
        print("-99999999999999999 ХП")
        print("Лучше в школьной столовке поесть...")
        food += 5
    elif t == 3:
        for i in range(0, random.randint(10, 20)):
            print(f"+ {i} силы")
            sila += random.randint(1, 5)
            food -= 2
            energy -= 2
            time.sleep(3)
        print("Потренирован!")
    elif t == 1:
        time.sleep(15)
        energy += 10
        print("Ты поспал!")
    elif t == 4 and energy >= 60 and sila >= 80 and food >= 70:
        print("Охранник: СРОЧНО! Сектор Б, камера номер 5, заключенный сбежал!")
        time.sleep(3)
        print("Ты: Быстрее! Мне надо бежать, или мне будет ещё хуже...")
        time.sleep(2)
        print("Полиция: за ним!")
        time.sleep(6)
        print("Ты: фууууух сбежал... надо бы и домой теперь...")
        time.sleep(3)
        final.main()