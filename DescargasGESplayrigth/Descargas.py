import configparser
from playwright.sync_api import sync_playwright
import re

# Leer configuración
config = configparser.ConfigParser()
config.read('config.ini')
url = config['settings']['url']
user = config['Login']['user']
passw = config['Login']['pass']

# Abrir navegador Edge y cargar la página
with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=False)
    page = browser.new_page()
    page.goto(url)
    print(f"Página abierta: {url}")
    page.wait_for_timeout(2000)  # Esperar 5 segundos antes de cerrar
    page.get_by_role("textbox", name="Rut").click()
    page.get_by_role("textbox", name="Rut").fill(user)
    page.get_by_role("textbox", name="Clave").click()
    page.get_by_role("textbox", name="Clave").fill(passw)
    page.get_by_role("button", name="Ingresar").click()
    page.wait_for_timeout(4000)  # Esperar 5 segundos antes de cerrar
    page.get_by_text("Seleccione una unidad").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Hospital Clínico").click()
    page.get_by_text("SUPERVISOR DE ESTABLECIMIENTO").click()
    page.get_by_role("button", name="Conectese con unidad y perfil").click()
    page.wait_for_timeout(4000)
    page.get_by_text("Monitoreo y Consultas").click()
    page.wait_for_timeout(10000)  # Esperar 5 segundos antes de cerrar
    browser.close()
