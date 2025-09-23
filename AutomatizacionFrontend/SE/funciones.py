import datetime
import os
import logging
from selenium.webdriver.chrome.options import Options


def screenshot(NombreArchivo,driver):
    dir_name="Evidencia"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    now = datetime.datetime.now()
    filename = dir_name+"\\"+NombreArchivo+"_{}.png".format(now.strftime("%d%m%Y_%H%M%S"))
    driver.save_screenshot(filename)
    return filename

def logINFO(message,tipodelog):
    # Configura el nivel de registro y el formato del mensaje
    if tipodelog=="INFO":
        logging.basicConfig(filename='appINFO.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
        logging.info(message)
    elif tipodelog=="DEBUG":
        logging.basicConfig(filename='appINFO.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
        logging.debug(message)
    elif tipodelog=="WARNING":
        logging.basicConfig(filename='appINFO.log', level=logging.WARNING, format='%(asctime)s %(levelname)s %(message)s')
        logging.warning(message)
    elif tipodelog=="ERROR":
        logging.basicConfig(filename='appINFO.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')
        logging.error(message)
    elif tipodelog=="CRITICAL":
        logging.basicConfig(filename='appINFO.log', level=logging.CRITICAL, format='%(asctime)s %(levelname)s %(message)s')
        logging.critical(message)
