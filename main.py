import random
import colorama
import time
import requests
import settings
import data
import os
def main():
    sytost = 100
    shaurma = 5
    hp = 100
    trenirovka = 50
    ip = requests.get("http://ip-api.com/json/").json()
    print(f"{colorama.Style.BRIGHT+colorama.Fore.LIGHTMAGENTA_EX}Welcome {settings.name}! You in {ip.get('country')}!\n\n")
    print(colorama.Fore.GREEN+'Добро пожаловать в лагерь "ЛесРук"!')
    while True:
        t = int(input(f"""{colorama.Fore.MAGENTA}Введите действие:
{colorama.Fore.YELLOW}1. Отправиться в лес
{colorama.Fore.LIGHTBLUE_EX}2. Тренировка
{colorama.Fore.LIGHTRED_EX}3. Покушать шаурмы{colorama.Fore.RESET}
"""))
        if t == 3:
            if sytost >= 95:
                print(f"{colorama.Fore.RED}Ты и так сыт!\n(P.S. ты сыт на {sytost}%){colorama.Fore.RESET}")
        if t == 2:
            rand = random.randint(15,35)
            for i in range(0, rand):
                print(colorama.Fore.LIGHTYELLOW_EX+"Тренируюсь...")
                print(f"({i}/{rand})"+colorama.Fore.RESET)
                time.sleep(1)
                os.system("clear")
                trenirovka += 10
            print(f"{colorama.Fore.LIGHTGREEN_EX}Теперь ты натренирован на {trenirovka}/100%!")
        if t == 1:
            tochno = int(input("Ты ТОЧНО хочешь отправиться в лес\n(Да = 1)\n(Нет = 2)\n"))
            if tochno == 1:
                print("Идём в лес =)")
                time.sleep(3)
                print("Хм... Я слышу чей-то шорох... Ну наверное ПРОСТО ПОКАЗАЛОСЬ...")
                time.sleep(4)
                print("Там чьё-то лицо...")
                time.sleep(2)
                print("""ААААААААААААА
░░░░░░░░░░░░▄▄██████████▄▄░░░░░░░░░░
░░░░░░░░░░▄███▀▀▀░░░░░▀▀▀██░░░░░░░░░
░░░░░░░░░███▀░░░░░░░░░░░░░██▄░░░░░░░
░░░░░░░░████░░░░░░░░░░░░░░███░░░░░░░
░░░░░░░████░░░░░░░░░░░░░░░▀███░░░░░░
░░░░░░▄████░░░░▄██░░░██░░░░███▄░░░░░
░░░░░░████░░░░▄███░░░███░░░████░░░░░
░░░░░████▀░▄▄███▀░░░░▀███▄▄░███░░░░░
░░░░░████░░▀▀█▀▀░░░▄░░░▀██▀░░██▄░░░░
░░░░░█████░░░░░░░▄███░░░░░░░░███░░░░
░░░░░███████░░░░░░░░░░░░░░░▄████░░░░
░░░░░███████░░░░░▄▄▄▄░░░░░▄█████░░░░
░░░░░███████▄░░░██████░░░░██████░░░░
░░░░░████████▄░░██████░░░▄██████░░░░
░░▄▄██████████▄░██████░░▄███████▄▄░░
███████████████░██████░▄████████████
████████████████░████░▄█████████████
████████████████░████░██████████████
████████████████▄░▀▀░▄██████████████
█████████████████▄░░▄███████████████
████████████████████████████████████""")
                print(data.wolf.get("START_SAY"))
                hp_protyvnika = 100
                print(f"Ваш ХП: {hp}")
                print(f"ХП противника(Уровень: Крик): {hp_protyvnika}")
                while True:
                    ataka = random.randint(5, 20)
                    print(f"Вы атакуете: - {ataka} ХП")
                    hp_protyvnika -= ataka
                    ataka_protyika = random.randint(5, 13)
                    print(f"Противник атакует: - {ataka_protyika} ХП")
                    print(f"Ваш ХП: {hp}")
                    print(f"ХП противника: {hp_protyvnika}")
                    hp -= ataka_protyika
                    time.sleep(3)
                    if hp_protyvnika >= 0:
                        print(data.wolf.get("END_SAY_WIN_"))
                    if hp >= 0:
                        print(data.wolf.get("END_SAY_LOSE"))
            if tochno == 2:
                print("Не идём в лес =(")
if __name__ == "__main__":
    main()