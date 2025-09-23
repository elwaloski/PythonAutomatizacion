import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configura la información del remitente y destinatario
remitente_email = "PruebaPythonAsistencia@hotmail.com"
remitente_password = "Asado2023*"
destinatario_email = "waldo.gonzalez@dbnetcorp.com"
# Configura el servidor SMTP de Outlook
smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
# Construye el mensaje
mensaje = MIMEMultipart()
mensaje["From"] = remitente_email
mensaje["To"] = destinatario_email
mensaje["Subject"] = "Prueba python"
# Añade el cuerpo del mensaje
cuerpo_mensaje = "Hola, este es un ejemplo de envío de correo desde Python a través de Outlook."
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
