import requests
import LeerArchivo
import funciones

ExisteArchivo=LeerArchivo.LeerArchivo()

if (ExisteArchivo=="El archivo no existe"):
    funciones.logINFO("El archivo Config.CFG no Existe en la ruta base!!!","INFO")
    funciones.logINFO("Crear Archivo con el nombre Config.CFG y con esta estructura","INFO")
    funciones.logINFO("-RUT xxxxxxxx-x","INFO")
    funciones.logINFO("-URLEntrada xxxxxxxx","INFO")
    funciones.logINFO("-URLSalida xxxxxxxx","INFO")
    funciones.logINFO("-EnvioMail SI (en caso de querer que envie un mail a otra casilla de correos!! No obligatorio)","INFO")
    funciones.logINFO("-MailDestino Mail No obligatorio","INFO")
else:
    ruttt=LeerArchivo.RUT

    if funciones.validar_rut(ruttt):
        print(f"{ruttt} es un RUT válido.")
        URLWSS=LeerArchivo.URLEntrada
        RUT=LeerArchivo.RUT
        URLWSS += RUT
        print(URLWSS)
        response = requests.get(URLWSS)

        if response.status_code == 200:           
            if(response.text=="RUT Inválido"):
                funciones.logINFO(f"Error Respuesta WSS {response.text} Asistencia no registrada","ERROR")
                print(response.text)
                if LeerArchivo.EnvioMail=="SI":
                    funciones.EnviaMail("Errro en Marcar de Asistencia",f" Asistencia No Marcada Error {response.text}")
            elif (response.text=="Marcas en mismo <br> sentido"):
                funciones.logINFO(f"Ya se registro la asistencia previamente {response.text}","ERROR")
                print(response.text)
                if LeerArchivo.EnvioMail=="SI":
                    funciones.EnviaMail("Ya se registro la asistencia previamente",f" Asistencia No Marcada {response.text}")
            else:
                print(response.text)
                funciones.logINFO(f"El codigo de respuesta del WSS es {response.text}","INFO")
                funciones.logINFO(f"Asistencia Entrada ingresa exitosamente","INFO")
                if LeerArchivo.EnvioMail=="SI":
                    funciones.EnviaMail("Ingreso Correcto",f" Asistencia Marcada de forma correcta {response.text}")
        else:
            print(f"Respuesta WSS incorrecta {response.status_code}")
            funciones.logINFO(f"Respuesta WSS incorrecta {response.status_code}","ERROR")
            funciones.logINFO(response.text,"ERROR")
            if LeerArchivo.EnvioMail=="SI":
                funciones.EnviaMail("Error En Marcar Asistencia",f"Error al enviar Marcan asistencia {response.text}")
    else:
        print(f"El Rut {ruttt} configurado en el archivo Config.CFG no es un RUT válido.")
        funciones.logINFO(f"El Rut {ruttt} configurado en el archivo Config.CFG no es un RUT válido.","ERROR")
