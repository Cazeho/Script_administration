# !/usr/bin/python3

from tkinter import *
import os
import platform
import socket
import getpass
import subprocess
import sys, errno
from threading import Thread
from time import sleep

#hote = socket.gethostname() #
hote= "127.0.1.1" #adresse ip du serveur
port= 12805 #numéro de port

subprocess.call('clear', shell=True) #Sous-processus, shell vaut True, la commande spécifiée sera exécutée à travers un shell

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #met en place la connection
connexion_principale.bind((hote, port)) #se connecte à l'adresse et au numéro de port du client,associe le socket à une adresse locale et au numéro de port
connexion_principale.listen(5) #commence à écouter les connexions entrantes
print("Le serveur écoute à présent sur le port {}".format(port)) #affiche le port
connexion_avec_client, infos_connexion = connexion_principale.accept() #accepte une connexion, retourne un nouveau socket et une adresse client
#connexion_principale.setsockopt( socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)


myHostName = socket.gethostname() #fonction du nom d'hôte

myIP = socket.gethostbyname(myHostName) #fonction de l'adrresse ip

username =getpass.getuser() #fonction du nom d'utilisateur

version=platform.system() #fonction de la version

processeur= platform.processor() #fonction du processeur

#dist = platform.dist()
#dist = " ".join(x for x in dist)#fonction de la distribution
msg_recu = b"" #
while msg_recu != b"fin": ##
    msg_recu = connexion_avec_client.recv(1024)#connectiion au client
    print(msg_recu.decode())#
    a="Hostname:" + " " + myHostName + "\n"#
    b="Username:" + " " + username + "\n"#
    c="IP:" + " " + myIP + "\n"#
    d="Processeur:" + " " + processeur + "\n"#
    e="Version:" + " " + version + "\n"#
    #f="Distribution:" + " " + dist#
    connexion_avec_client.send(a.encode())#on envoie le nom d'hôte au client/envoye des données mais il se peut que pas toutes le soit
    connexion_avec_client.send(b.encode())#on envoie l'adrresse ip au client
    connexion_avec_client.send(c.encode())#on envoie le nom d'utilisateur au client
    connexion_avec_client.send(d.encode())#on envoie la distribution au client
    connexion_avec_client.send(e.encode())#on envoie la distribution au client
    #connexion_avec_client.send(f.encode())#on envoie la distribution au client
try:
    print("a")
except socket.error:
    print("a")
