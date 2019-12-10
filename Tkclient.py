# !/usr/bin/python3
import tkinter
from tkinter import *
import os
import socket
import sys, errno
import ipaddress
import subprocess
import platform
import getpass
from datetime import datetime #Modules

hote= socket.gethostname() #retourne l'adresse locale
port= 12805 #numéro de port

fonte =font=('Arial', '11')
c="gray15"
co="green2"#couleur de font
scanner= Tk()#crée un tkinter
lb= Label(scanner, text="Port Scanner", font=("Gang of Three","20"), bg=c, fg=co)#titre
lb.place(x=80,y=1)#emplacement de l'objet

lb1= Label(scanner, text="IPv4", font=fonte, bg=c, fg=co)#label
lb1.place(x=5,y=50)#emplacement de l'objet

inf= Entry(scanner, font=fonte, bg='white', fg='black')#entrée des adresses
inf.place(x=70,y=50)#emplacement de l'objet

ed12= Text(scanner, font=('Arial', '11',"bold"), bg='gray0', fg="white", width=70, height=35, selectbackground="green2", selectforeground="gray10")#tableau d'affichage des requêtes
ed12.place(x=5,y=110)#emplacement de l'objet

lb2= Label(scanner, text="Pour un Unicast Tapez une adresse IPv4 / Pour un Broadcast Tapez comme en exemple 127.0.0", font=fonte, bg=c, fg=co)#message d'utilisation
lb2.place(x=5,y=80)#emplacement de l'objet

def unicast():
        ed12.delete(0.0)#réinitialisation des messages
        remoteServer    = inf.get()#on récupère ce qu'on à tapez en entrée
        remoteServerIP  = socket.gethostbyname(remoteServer)#pour obtenir l'adresse IP de l'hôte local.
        t1 = datetime.now()#durée envoyer
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##met en place la connection
        try:
            for ip in range(1,255):
                        result = sock.connect_ex(("134.59.139."+str(ip), int(port)))
                        if result == 0:
                            print ("IP {}: 	 Open".format("134.59.139."+str(ip)))
                        sock.close()
        except KeyboardInterrupt:#le processus se ferme si on fait un Ctrl+C
                print ("You pressed Ctrl+C")
                sys.exit()#arrêt du système
        except socket.gaierror:#
                print ('Hostname could not be resolved. Exiting')
                sys.exit()#arrêt du système
        except socket.error:#erreurs détectées durant l’exécution son appelées des exceptions
                print ("Couldn't connect to server")
                sys.exit()#arrêt du système
        t2 = datetime.now()	#durée recue
        total =  t2 - t1#on fait la différence entre la durée d'envoie et la durée recue
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##met en place la connection
        sock.connect_ex((remoteServerIP, int(port)))#connection (addr, port)#
        msg_a_envoyer = b""#initialisation du message
        i=0#i initialisé à 0

        while i<4:#de 1 à 5 => on envoie 5 messages
                msg_a_envoyer = "a"#en envoie à comme message
                msg_a_envoyer = msg_a_envoyer.encode()#on encode le message
                # On envoie le message
                sock.send(msg_a_envoyer)
                msg_recu = sock.recv(1024)#recoit des données
                p=msg_recu.decode()#on décode le message recue
                ed12.insert(0.0,p)#recoit et décode le message du serveur
                i+=1#i=i+1 on incrémente de 1

        #ed12.insert(5.0,"Fermeture de la connection") #Affiche "Fermeture de la connection"
        #sock.close()

def broadcast():
        for j in range(1, 7):#de 1 à 254
                g=inf.get()#on récupère ce qu'on à tapez en entrée
                ip =g+".%d" % (j)#adresse
                remoteServer2 = ip#
                k=ip + "\n"
                #print(ip)
                remoteServerIP2  = socket.gethostbyname(remoteServer2)#pour obtenir l'adresse IP de l'hôte local.
                
                try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##met en place la connection
                        result = sock.connect_ex(((ip), int(port)))#connect, retourne un code erreur au lieu d'une exception
                        if result == 0:#si result ==0 alors il existe une connection
                                ed12.insert(END,"IP {}:    OUVERT \n".format(ip))#on affiche que le port est ouvert à cette adresse
                except OSError:#si serveur deconnecte alors fermeture de la connection
                        break
			
Bouton1 = Button(scanner, text ='Unicast', command = unicast)#bouton Unicast
Bouton1.place(x = 250, y = 48)#emplacement de l'objet

Bouton2 = Button(scanner, text ='Broadcast', command = broadcast)#bouton Broadcast
Bouton2.place(x = 300, y = 48)#emplacement de l'objet

scanner["bg"]="gray13"
scanner=resizable(height=False,width=False)
scanner.title('Port Scanner')#titre
scanner.geometry('400x540+450+20')#taille de la fenêtre
scanner.mainloop()#fermeture du tkinter
