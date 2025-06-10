import os
"""
___  ____ _         _       _       _   _  __  
|  \/  (_) |       | |     | |     | | | |/  | 
| .  . |_| | _____ | | __ _| |__   | | | |`| | 
| |\/| | | |/ / _ \| |/ _` | '_ \  | | | | | | 
| |  | | |   < (_) | | (_| | | | | \ \_/ /_| |_
\_|  |_/_|_|\_\___/|_|\__,_|_| |_|  \___/ \___/                                            
                                               
created by: Criações Inesperadas
powered by: devdeczin
(obrigado por usar :) )                                                        
"""

carlos = input("APERTE QUALQUER TECLA PARA CONTINUAR: ")

opcao = input('''
DIGITE 1 PARA FERRAMENTAS Zero-Attacker (by Asjad) \n
DIGITE 2 PARA FERRAMENTAS AUTO TOR \n
DIGITE 3 PARA FERRAMENTAS WIFI ANALYSER \n
DIGITE 4 PARA FERRAMENTAS ZPHISHING \n
Sua opção:''')

if carlos == "Y":
    print(opcao)

if opcao == "1":
        os.system("git clone https://github.com/AsjadOooO/Zero-attacker.git")
        os.system("cls")
        os.system("cd Zero-attacker")

elif opcao == "2":
        os.system("git clone https://github.com/FDX100/Auto_Tor_IP_changer.git")
        os.system("cls")
        os.system("cd Auto_Tor_IP_changer")

elif opcao == "3":
        os.system("git clone https://github.com/NitheshD05/Wifi-analyser.git")
        os.system("cls")
        os.system("cd Wifi-analyser")

elif opcao == "4":
        os.system("git clone https://github.com/htr-tech/zphisher.git")
        os.system("cls")
        os.system("cd zphisher")
else:
        print("RESPOSTA INVÁLIDA")