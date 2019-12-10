# !/usr/bin/python3

import os
import socket
import sys, errno
import ipaddress
import subprocess
import platform
import getpass
from datetime import datetime #Modules

hote= socket.gethostname() #retourne l'adresse locale
port= 12800 #numéro de port


subprocess.call('clear', shell=True)#Sous-processus, , shell vaut True, la commande spécifiée sera exécutée à travers un shell

print("Interface CLIENT/SERVER: ")#affichage
print("1 : "Connection avec un seul PC")
print("2 : "Connection avec tous les PC (BROADCAST)")


choix= input()
choix= int(choix)

#BROADCAST
if choix==2:
	for j in range(1, 255):#
		ip ="127.0.1.%d" % (j)#
		remoteServer2 = ip#
		print (Fore.YELLOW +  Style.BRIGHT + ip + Style.RESET_ALL)##### couleurs
		t1 = datetime.now()#
		remoteServerIP2  = socket.gethostbyname(remoteServer2)#pour obtenir l'adresse IP de l'hôte local.
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##met en place la connection
			result = sock.connect_ex(((ip), int(port)))#connect, retourne un code erreur au lieu d'une exception
			if result == 0:
				print ("IP {}: 	 OUVERT".format((ip)))#affiche adresse + ouvert
				t2 = datetime.now()#		
				total =  t2 - t1#
				print ('Scan :', total)#affiche le temps RTT
				try:
					sock.connect_ex((remoteServerIP2, int(port)))#connect, retourne un code erreur au lieu d'une exception
					
					remoteServer = ip#
					remoteServerIP  = socket.gethostbyname(remoteServer)#pour obtenir l'adresse IP de l'hôte local.
					print ("Patientez 3 secondes", remoteServerIP)#affiche 
					msg_a_envoyer = b""#initialisation du message

					while msg_a_envoyer != b"fin":##si fin de message envoie

						msg_a_envoyer = input("> ")#affiche un prompt

						
						msg_a_envoyer = msg_a_envoyer.encode()#on encode le message

						## On envoie le message

						sock.send(msg_a_envoyer)#

						msg_recu = sock.recv(1024)#recoit des données
						

						print(msg_recu.decode())#affiche le message et le décode
				
						
				except KeyboardInterrupt:#si Ctrl+C on arrête le sous-processus
					print ("You pressed Ctrl+C")
					print("---------------------------------")
									
			
		except KeyboardInterrupt: #si Ctrl+C on arrête le processus
			print ("You pressed Ctrl+C")
			sys.exit() #Fin du processus
			
		
			
		
#Pour un seul ordinateur
if choix==1:
	remoteServer    = input("Entrer un adresse IPv4: ")#entrez une adresse
	remoteServerIP  = socket.gethostbyname(remoteServer)#pour obtenir l'adresse IP de l'hôte local.

	print ("Patientez 3 secondes", remoteServerIP)#affiche Patientez 3 secondes , et l'adresse rentrée
	

	t1 = datetime.now()#durée envoyer
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##met en place la connection

	try:
		for ip in range(1,255): 
			result = sock.connect_ex(("134.59.139."+str(ip), int(port)))#connection addr et port
			if result == 0:
				print ("IP {}: 	 Open".format("134.59.139."+str(ip)))
			sock.close()#fermeture du socket
			
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

	print ('Le scan est fini: ', total)#affiche la durée RTT du scan 				
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##met en place la connection
	sock.connect_ex((remoteServerIP, int(port)))#connection (addr, port)
	print("Connexion établie avec le serveur sur le port {}".format(port))#affiche le port
	#hostname = socket.gethostname()    
	#IPAddr = socket.gethostbyname(hostname)    
	#print("Votre Nom est:" + hostname)    
	#print("Votre ordinateur IP Address est:" + IPAddr)
	#print(platform.system())   
	#username =getpass.getuser()
	#print(username)
	print("Taper sur n'importe quelle touche")#affiche
		
	myHostName = socket.gethostname()
	msg_a_envoyer = b""#initialisation du message

	while msg_a_envoyer != b"fin":#si fin de message envoie

		msg_a_envoyer = input("> ")#affiche un prompt

		
		msg_a_envoyer = msg_a_envoyer.encode()#on encode le message

		# On envoie le message

		sock.send(msg_a_envoyer)

		msg_recu = sock.recv(1024)#recoit des données

		print(msg_recu.decode())#recoit et décode le message du serveur
	   
	 
		
	print("Fermeture de la connection") #Affiche "Fermeture de la connection"

	sock.close()#ferme le socket
    
	#netstat -an | grep 12800

