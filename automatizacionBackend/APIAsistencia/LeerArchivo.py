import os

def LeerArchivo():
    global RUT
    global URLEntrada
    global URLSalida
    global EnvioMail
    global MailDestino
    
    ruta_archivo = "config.CFG"
    if os.path.exists(ruta_archivo):

        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                if linea.startswith("-RUT"):
                    rut = linea.split()[1]
                    RUT=rut  
                elif linea.startswith("-URLEntrada"):
                    entrada = linea.split()[1]
                    URLEntrada=entrada   
                elif linea.startswith("-URLSalida"):
                    salida = linea.split()[1]
                    URLSalida=salida
                elif linea.startswith("-EnvioMail"):
                    mail = linea.split()[1]
                    EnvioMail=mail
                elif linea.startswith("-MailDestino"):
                    correo = linea.split()[1]
                    MailDestino=correo
        return "ArchivoLeido"
    else:
        print("El archivo no existe.")
        return "El archivo no existe"