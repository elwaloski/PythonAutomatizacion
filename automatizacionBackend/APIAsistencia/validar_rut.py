import funciones
import logging
import datetime

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


rut_valido = "18050200-9"
rut_invalido = "78079790-8"

if funciones.validar_rut(rut_valido):
    print(f"{rut_valido} es un RUT válido.")
    logINFO(f'Es rut valido {rut_valido}', 'INFO')
else:
    print(f"{rut_valido} no es un RUT válido.")
    logINFO(f'no es un RUT válido. {rut_valido}', 'INFO')

if funciones.validar_rut(rut_invalido):
    print(f"{rut_invalido} es un RUT válido.")
    logINFO(f"{rut_invalido} es un RUT válido.", 'CRITICAL')
else:
    print(f"{rut_invalido} no es un RUT válido.")
    logINFO(f"{rut_invalido} no es un RUT válido.", 'CRITICAL')