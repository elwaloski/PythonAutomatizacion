import os

def LeerArchivo():
    global IPCLOUD
    global BasedatoCLOUD
    global UsuarioCLOUD
    global PassCLOUD
    global URLWEBAUT
    ruta_archivo = "Config\\config.CFG"
    if os.path.exists(ruta_archivo):

        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                if linea.startswith("-IPCLOUD"):
                    ip = linea.split()[1]
                    IPCLOUD=ip
                elif linea.startswith("-BasedatoCLOUD"):
                    basedatos = linea.split()[1]
                    BasedatoCLOUD=basedatos
                elif linea.startswith("-UsuarioCLOUD"):
                    usuario = linea.split()[1]
                    UsuarioCLOUD=usuario
                elif linea.startswith("-PassCLOUD"):
                    password = linea.split()[1]
                    PassCLOUD=password
                elif linea.startswith("-URLWEB"):
                    URLWEB = linea.split()[1]
                    URLWEBAUT=URLWEB    
                    
        return "ArchivoLeido"
    else:
        print("El archivo no existe.")
        return "Error"