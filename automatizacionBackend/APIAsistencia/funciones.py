import datetime
import LeerArchivo
import os
import logging
from selenium.webdriver.chrome.options import Options
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def CrearRutaEvidencia():
    dir_nameGene="Evidencia"
    if not os.path.exists(dir_nameGene):
        os.mkdir(dir_nameGene)
    now = datetime.datetime.now()
    dir_name = "Evidencia_Pruebas_"+now.strftime("%d%m%Y_%H%M%S")
    if not os.path.exists(dir_nameGene+"\\"+dir_name):
        os.makedirs(dir_nameGene+"\\"+dir_name)  
    ruta_completa = os.path.abspath(dir_nameGene+"\\"+dir_name)
    return ruta_completa

def screenshot(RutaDirectorio,NombreArchivo, driver): 
    filename = os.path.join(RutaDirectorio, NombreArchivo+".png")
    driver.save_screenshot(filename)
    return filename

log_filename = 'Asistencia_{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))


# Define un mapeo de tipos de log a niveles de registro
nivel_de_registro = {
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# Configura el nivel de registro y el formato del mensaje
logging.basicConfig(filename=log_filename, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def logINFO(message, tipodelog="INFO"):
    nivel = nivel_de_registro.get(tipodelog, logging.INFO)
    logging.log(nivel, message)

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")  # Elimina puntos y guiones
    
    if not rut[:-1].isdigit() or (rut[-1] not in '0123456789Kk'):
        return False
    
    cuerpo_rut, digito_verificador = rut[:-1], rut[-1]
    
    suma = 0
    multiplicador = 2
    
    for digito in reversed(cuerpo_rut):
        suma += int(digito) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2
    
    resto = suma % 11
    digito_esperado = str(11 - resto) if resto != 0 else '0'
    
    return digito_esperado == digito_verificador.upper()

def EnviaMail(Asunto,Mensaje):
    LeerArchivo.LeerArchivo()
    # Configura la información del remitente y destinatario
    remitente_email = "PruebaPythonAsistencia@hotmail.com"
    remitente_password = "Asado2023*"
    destinatario_email = LeerArchivo.MailDestino
# Configura el servidor SMTP de Outlook
    smtp_server = "smtp-mail.outlook.com"
    smtp_port = 587
# Construye el mensaje
    mensaje = MIMEMultipart()
    mensaje["From"] = remitente_email
    mensaje["To"] = destinatario_email
    mensaje["Subject"] = Asunto
# Añade el cuerpo del mensaje
    cuerpo_mensaje = f"Estimade \n\n{Mensaje}\n\nSaludos cordiales,\nEquipo By Asistencia" 
    mensaje.attach(MIMEText(cuerpo_mensaje, "plain"))

# Inicia la conexión al servidor SMTP
    with smtplib.SMTP(smtp_server, smtp_port) as server:
    # Establece una conexión segura
        server.starttls()    
    # Inicia sesión en la cuenta de correo
        server.login(remitente_email, remitente_password)    
    # Envía el correo electrónico
        server.sendmail(remitente_email, destinatario_email, mensaje.as_string())

    print("Correo enviado con éxito.")