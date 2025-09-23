import datetime
import os
import logging
from selenium.webdriver.chrome.options import Options
import smtplib
from selenium.webdriver.support import expected_conditions as EC
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import psycopg2
from psycopg2 import sql
from pywinauto import application
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException 


def CrearRutaEvidencia(x):
    dir_nameGene="Evidencia"
    if not os.path.exists(dir_nameGene):
        os.mkdir(dir_nameGene)
    now = datetime.datetime.now()
    dir_name = f"{x}_AutoGXPruebas_"+now.strftime("%d%m%Y_%H%M%S")
    if not os.path.exists(dir_nameGene+"\\"+dir_name):
        os.makedirs(dir_nameGene+"\\"+dir_name)  
    ruta_completa = os.path.abspath(dir_nameGene+"\\"+dir_name)
    return ruta_completa

contador = 0

def incrementar_contador():
    global contador
    contador += 1
    return contador

def screenshot(RutaDirectorio,NombreArchivo, self): 
    x=incrementar_contador()
    filename = os.path.join(RutaDirectorio, f"{x}_{NombreArchivo}.png")
    self.save_screenshot(filename)
    return filename

if not os.path.exists("log"):
    os.mkdir("log")
now = datetime.datetime.now()

log_filename = 'log\\AutoGX_{}.log'.format(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))


# Define un mapeo de tipos de log a niveles de registro
nivel_de_registro = {
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

# Configura el nivel de registro y el formato del mensaje
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def logINFO(message, tipodelog):
    nivel = nivel_de_registro.get(tipodelog, logging.INFO)
    logging.log(nivel, message)


def LeerArchivo():
    global Usuario
    global LoginPass
    global URLWEB
    global Userbd
    global PassBd
    global Hostbd
    global Puerto
    global NombreBD
    

    ruta_archivo = "config.config"
    if os.path.exists(ruta_archivo):

        with open(ruta_archivo, "r") as archivo:
            for linea in archivo:
                if linea.startswith("-Usuario"):
                    usuario = linea.split()[1]
                    Usuario=usuario
                elif linea.startswith("-LoginPass"):
                    password = linea.split()[1]
                    LoginPass=password
                elif linea.startswith("-URLWEB"):
                    URLWEB = linea.split()[1]
                    URLWEB=URLWEB    
                elif linea.startswith("-Userbd"):
                    Userbds = linea.split()[1]
                    Userbd=Userbds
                elif linea.startswith("-PassBd"):
                    PassBds = linea.split()[1]
                    PassBd=PassBds
                elif linea.startswith("-Hostbd"):
                    Hostbds = linea.split()[1]
                    Hostbd=Hostbds
                elif linea.startswith("-Puerto"):
                    Puertos = linea.split()[1]
                    Puerto=Puertos
                elif linea.startswith("-NombreBD"):
                    NombreBDs = linea.split()[1]
                    NombreBD=NombreBDs
    else:
        print("El archivo no existe.")
        return "Error"
def Bajar(self,veces):
    x = 0
    while x <= int(veces):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
        x += 1  # Incrementa x en 1 en cada iteración
    time.sleep(2)

def eliminar_registro(db_name, user, password, host, port, table_name, condition):
    try:
        # Conectar a la base de datos
        conexion = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = conexion.cursor()
        # Crear la consulta SQL para eliminar registros
        query = sql.SQL("DELETE FROM {table} WHERE {condition}").format(
            table=sql.Identifier(table_name),
            condition=sql.SQL(condition)
        )
        # Ejecutar la consulta
        cursor.execute(query)
        conexion.commit()
        #print(f"Registros eliminados de la tabla '{table_name}' donde {condition}.")    
    except Exception as e:
        print(f"Error al conectar o eliminar registros: {e}")
    
    finally:
        # Cerrar la conexión
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()


def Consultar_Registro_Unico(db_name, user, password, host, port, table_name, campo, order_by_field):
    try:
        # Conectar a la base de datos
        conexion = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = conexion.cursor()
        # Crear la consulta SQL para consultar un único registro
        query = sql.SQL("SELECT {campo} FROM {table} ORDER BY {order_by_field} DESC LIMIT 1").format(
            campo=sql.Identifier(campo),
            table=sql.Identifier(table_name),
            order_by_field=sql.Identifier(order_by_field)
        )

        # Ejecutar la consulta
        cursor.execute(query)        
        # Obtener el registro que cumple con la condición
        registro = cursor.fetchone()
        #print(f"Registro consultado de la tabla '{table_name}' con campo '{campo}' ordenado por '{order_by_field}' en orden descendente.")
        #print(registro)
        return registro    
    except Exception as e:
        print(f"Error al conectar o consultar el registro: {e}")
        return None    
    finally:
        # Cerrar la conexión
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
def GuardarArchivo(ruta,taxo):
        try:
            taxo_dir = os.path.join(ruta, "descargas", taxo)
            if not os.path.exists(taxo_dir):
                os.makedirs(taxo_dir)
                print(f"Carpeta creada: {taxo_dir}")
            else:
                print(f"La carpeta ya existe: {taxo_dir}")

            # Iniciar pywinauto Application
            app = application.Application().connect(title_re="Guardar como", timeout=20)
            # Conectarse a la ventana de "Guardar como"
            save_dialog = app["Guardar como"]                           
            # Obtener el nombre original del archivo desde el cuadro de texto "Nombre de archivo"
            nombre_original_archivo = save_dialog.child_window(class_name="Edit").window_text()
            # Especificar la ruta completa donde quieres guardar el archivo, manteniendo el nombre original
            save_path = os.path.join(taxo_dir, nombre_original_archivo)
            # Ingresar la ruta en el cuadro de texto "Nombre de archivo"
            save_dialog["Edit"].set_edit_text(save_path)
            # Hacer clic en el botón "Guardar"
            save_button = save_dialog["Guardar"]
            save_button.wait('enabled', timeout=10)  # Espera hasta que el botón esté habilitado
            save_button.click_input(double=True)  # Usar click_input para simular un clic más robusto
            time.sleep(2) 
        except Exception as e:
            print(f"Error al conectar o consultar el registro: {e}")
            return None  
        
def test_carga_web(self):
        NombrePrueba = 'Abrir Pagina'
        try:
            self.driver.get(URLWEB)
            time.sleep(3)
            self.driver.find_element(By.NAME, "usuario").send_keys(Usuario)
            self.driver.find_element(By.NAME, "password").send_keys(LoginPass)
            screenshot(self.Ruta, "PaginaPrincipal", self.driver)
            time.sleep(2)
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, ".k-button-solid-primary > .k-button-text").click()
            time.sleep(5)
            screenshot(self.Ruta, NombrePrueba, self.driver)
            loggin="Login "
            loggin+=NombrePrueba
            logINFO("Prueba OK " + loggin, "INFO")
            CorrInst=RescataCorr(self)
        except Exception as e:
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")


def test_CerrarSesion(self): 
        try:
            NombrePrueba = 'Cerrar Sesion'
            self.driver.find_element(By.XPATH, "//div[3]/div/div/button/span").click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, "//li[2]/span/span").click()
            time.sleep(2)
            screenshot(self.Ruta, NombrePrueba, self.driver)
            logINFO("Prueba OK " + NombrePrueba, "INFO")
        except Exception as e:
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")


def test_CrearInstancia(self,NombrePrueba,NombreTaxo,Pantalla,CorrInst): 
        try:
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Crear instancia\')]").click()            
            time.sleep(5)
            self.driver.find_element(By.XPATH, f"//label[contains(.,\'{Pantalla}')]").click() #Posibles valores pantalla=Circular 2275, Pantalla=Docs Fondos pantalla=Docs Financieros
            time.sleep(5)
            if Pantalla=="Docs Fondos":
                self.driver.find_element(By.ID, "taxonomia").click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, f"//span[contains(.,\'{NombreTaxo}')]").click() #Posibles Valores Nombretaxo cl-fi_20110430,cl-cp_20110822,cl-fc_20110606,cl-iv_20110430,cl-fm_20110430
                time.sleep(2)
            if Pantalla=="Docs Financieros":
                self.driver.find_element(By.ID, "categoria").click()
                time.sleep(1)
                self.driver.find_element(By.XPATH, f"//span[contains(.,\'{NombreTaxo}')]").click()#valores posibles Comercio Industria,Seguro,Holding Bancario,Holding Seguro,Cajas Compensación,Entidades informantes,Bancos y Seguros
                time.sleep(1)
            self.driver.find_element(By.ID, "descripcion").send_keys(f"{NombreTaxo} {CorrInst}")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Clasificado\')]").click()
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Directo\')]").click()
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Consolidado\')]").click()
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Por Función\')]").click()
            self.driver.find_element(By.XPATH, "//label[contains(.,\'Neto de Impuesto\')]").click()
            Bajar(self,20)
            time.sleep(2)
            r="Antes de crear "
            r+=NombrePrueba
            screenshot(self.Ruta, r, self.driver)
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Crear Instancia\')]").click()
            time.sleep(2)
            screenshot(self.Ruta, NombrePrueba, self.driver)
            logINFO("Prueba OK " + NombrePrueba, "INFO")
        except Exception as e:
            eliminar_registro(NombreBD,Userbd,PassBd,Hostbd,Puerto,"xbrl_inst_docu",f"corr_inst >{CorrInst}")   
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

def test_SubirArchivo(self,NombrePrueba,NombreDirTaxo):
        try:
            self.driver.find_element(By.XPATH, "//tr[1]/td[6]/div[2]/button/span/span").click() #Carga Archivo Principal
            time.sleep(3)
            screenshot(self.Ruta, "PaginaSubirArchivo", self.driver)
            input_archivo = self.driver.find_element(By.XPATH, "//input[@type='file']")
            directorio_actual = os.getcwd()
            ruta_archivo_relativa = os.path.join(directorio_actual, "taxos", NombreDirTaxo, "xls.zip")
            ruta_archivo = ruta_archivo_relativa  # Especifica la ruta completa del archivo
            input_archivo.send_keys(ruta_archivo)
            time.sleep(2)
            screenshot(self.Ruta, "SubeArchivo", self.driver)
            if  NombreDirTaxo=="BS" or NombreDirTaxo=="CC" or NombreDirTaxo=="CI" or NombreDirTaxo=="HB" or NombreDirTaxo=="HS": #La diferencia que este selecciona todos los archivos que aplica solo para los marcados
                self.driver.find_element(By.XPATH, "//label[contains(.,\'Seleccionar todos\')]").click() #check seleccionar todos 
            Bajar(self,20)
            time.sleep(3)
            screenshot(self.Ruta, "AntesdeSubirArchivo", self.driver)
            time.sleep(1)
            if NombreDirTaxo=="CS":
                self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div/form/div/div[7]/div/button/span").click()#Boton Subir Documento
            else:
                self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/form/div/div[8]/div/button/span").click()#Boton Subir Documento

            esperar_y_refrescar(self,"/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div/div[1]/button/span")

            time.sleep(2)
            screenshot(self.Ruta, "DetalleCarga", self.driver)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/button").click()#cerrar ver detalle
            time.sleep(2)
            screenshot(self.Ruta, "ArchivoSubido", self.driver)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[3]/div/div[2]/button/span").click()#Boton Generar XBRL
            time.sleep(2)
            screenshot(self.Ruta, "PresionaBotonGenerarXBRL", self.driver)

            esperar_y_refrescar(self,"/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div[1]/button/span")

            time.sleep(2)
            screenshot(self.Ruta, "DetalleXBRL", self.driver)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/button").click()#cerrar ver detalle
            time.sleep(2)
            screenshot(self.Ruta, "XBRLGenerado", self.driver)
            time.sleep(60)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div[2]/button/span").click()#Boton ver HTML
            time.sleep(10)
            screenshot(self.Ruta, "HTMLXBRL", self.driver)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/button").click()#cerrar ver Html
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[5]/div[3]/button/span").click()#Boton Descargar XBRL
            time.sleep(3)
            screenshot(self.Ruta, "PantallaDescargaXBRL", self.driver)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/button[2]/span").click()#Boton que si descarga el XBRL
            time.sleep(10)
            GuardarArchivo(self.Ruta,NombreDirTaxo)# Funcion que guarda XBRL de Ruta relativa mas nombre de la taxo
            time.sleep(10)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/button[1]/span").click()#cerrar Descargas
            time.sleep(5)
            logINFO("Prueba OK " + NombrePrueba, "INFO")
        except Exception as e:  
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")


def esperar_y_refrescar(self,xpath_button):
    max_espera = 900  # Tiempo máximo total de espera en segundos
    intervalo_refresco = 60  # Intervalo de refresco en segundos
    tiempo_inicial = time.time()

    while True:
        try:
            # Intentar encontrar el botón y esperar que sea clickeable
            VerDetalle = WebDriverWait(self.driver, intervalo_refresco).until(
                EC.element_to_be_clickable((By.XPATH, xpath_button))
            )
            # Si se encuentra, salir del bucle
            self.driver.find_element(By.XPATH, xpath_button).click()
            return VerDetalle
        
        except:
            # Si el botón no es clickeable después del intervalo, refrescar la página
            tiempo_transcurrido = time.time() - tiempo_inicial
            if tiempo_transcurrido >= max_espera:
                raise TimeoutException(f"El botón no apareció después de {max_espera} segundos.")
            #self.driver.refresh()
            # Puedes agregar un pequeño tiempo de espera después del refresh para que la página se cargue antes del próximo intento
            time.sleep(10)
            
def RescataCorr(self):
        Valor=1
        try:
                xpath_td_anterior = "/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[1]/td[1]"
                # Encuentra el elemento anterior
                elemento_td_anterior = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_td_anterior)))
                Valor= int(elemento_td_anterior.text)+1
                return Valor
        except Exception as e:
                return Valor

def BuscarParametroAbrirEditar(self, BuscarParametro):
    Valor = 1
    while True:
        try:
            # Construir el xpath para la celda en la columna 2 de la fila actual
            xpath_td = f"/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[{Valor}]/td[2]"
            
            # Esperar hasta que el elemento sea encontrado en la página
            elemento_td = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_td))
            )            
            # Obtener el texto del elemento
            Xpath = elemento_td.text
            #print (Xpath)
            if Valor==10:
                self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div/button[3]" ).click()
                Valor=0
            if Xpath == BuscarParametro:
                # Construir el xpath para el botón en la columna 5 de la fila actual
                boton_xpath = f"/html/body/div/div/div[2]/div/div[2]/div[1]/div[2]/div/div[1]/table/tbody/tr[{Valor}]/td[5]/div/button"                
                # Esperar hasta que el botón sea clickeable
                boton = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, boton_xpath))
                )
                boton.click()
                return Xpath
            Valor += 1
        except Exception as e:
            # Manejar el caso cuando se agotan las filas o ocurre un error
            if "no such element" in str(e):
                # No se encontró más filas en la tabla
                print("No se encontraron más filas en la tabla.")
                return None
            else:
                # Manejar otros tipos de errores
                print(f"Error al buscar el parámetro: {e}")
                return None

def test_ConsultaConceptos(self,NombrePrueba,TipoTaxo,Taxo,Buscar):
        try:
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Instancias\')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Herramientas\')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//li[2]/span/span").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//form/div/div/div/div/div/span/span/span").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, f"//span[contains(.,\'{TipoTaxo}')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//span[@id=\'taxonomy\']/button").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, f"//i[contains(.,\'{Taxo}')]").click() 
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[contains(.,\'Buscar\')]").click()
            time.sleep(2)
            screenshot(self.Ruta, f"BuscardorPreterminado{TipoTaxo}", self.driver)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'concept\']").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'concept\']").send_keys(f"{Buscar}")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[contains(.,\'Buscar\')]").click()
            time.sleep(5)
            screenshot(self.Ruta, NombrePrueba, self.driver)
            logINFO("Prueba OK " + NombrePrueba, "INFO")
        except Exception as e:
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")  


def test_CrearParaGene(self,NombrePrueba):
        try:         
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Mantenedores\')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//li[1]/span/span").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Crear Parámetro\')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'ParamName\']").send_keys("ParametroQA")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'ParamDesc\']").send_keys("1111")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'ParamValue\']").send_keys("2222")
            time.sleep(2)
            screenshot(self.Ruta, "Crear Parametro General", self.driver)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[4]/button[2]/span").click()
            time.sleep(4)
            #self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/button[4]").click()
            #time.sleep(5)
            BuscarParametroAbrirEditar(self,"ParametroQA")
            campo_texto = self.driver.find_element(By.XPATH, "//input[@id=\'ParamDesc\']")
            campo_texto.send_keys(Keys.BACKSPACE *10)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'ParamDesc\']").send_keys("4444")
            campo_textos=self.driver.find_element(By.XPATH, "//input[@id=\'ParamValue\']")
            campo_textos.send_keys(Keys.BACKSPACE *10)
            self.driver.find_element(By.XPATH, "//input[@id=\'ParamValue\']").send_keys("55555")
            time.sleep(2)
            screenshot(self.Ruta, "Editar Parametro General", self.driver)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[5]/button[2]/span").click()
            time.sleep(2)
            #self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/button[1]").click()
            #time.sleep(2)
            #self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/button[4]").click()
            #time.sleep(2)            
            BuscarParametroAbrirEditar(self,"ParametroQA")
            time.sleep(1)  
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[4]/button").click()
            time.sleep(2)
            screenshot(self.Ruta, "Eliminar Parametro General", self.driver)
            self.driver.find_element(By.XPATH, "//span[@class='k-button-text' and text()='Eliminar']")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[2]/button[2]/span").click()
            time.sleep(5)            
            screenshot(self.Ruta, NombrePrueba, self.driver)
            logINFO("Prueba OK " + NombrePrueba, "INFO")
        except Exception as e:
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

def test_CrearParamEmpr(self,NombrePrueba):
        try:
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Mantenedores\')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//li[2]/span/span").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//span[contains(.,\'Crear Parámetro\')]").click()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'CodiPaem\']").send_keys("ParametroQA")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'DescPaem\']").send_keys("22222")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'ValoPaem\']").send_keys("33333")
            time.sleep(2)
            screenshot(self.Ruta, "Crear Parametro General", self.driver)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[4]/button[2]/span").click()
            time.sleep(5)
            BuscarParametroAbrirEditar(self,"ParametroQA")
            time.sleep(2)
            campo_texto = self.driver.find_element(By.XPATH, "//input[@id=\'DescPaem\']")
            campo_texto.send_keys(Keys.BACKSPACE *10)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@id=\'DescPaem\']").send_keys("4444")
            campo_textos=self.driver.find_element(By.XPATH, "//input[@id=\'ValoPaem\']")
            campo_textos.send_keys(Keys.BACKSPACE *10)
            self.driver.find_element(By.XPATH, "//input[@id=\'ValoPaem\']").send_keys("55555")
            time.sleep(2)
            screenshot(self.Ruta, "Editar Parametro General", self.driver)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[5]/button[2]").click()
            time.sleep(2)
            BuscarParametroAbrirEditar(self,"ParametroQA")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div[4]/button").click()
            time.sleep(2)
            screenshot(self.Ruta, "Eliminar Parametro General", self.driver)
            self.driver.find_element(By.XPATH, "//span[@class='k-button-text' and text()='Eliminar']")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//div[2]/button[2]/span").click()
            time.sleep(5)
            screenshot(self.Ruta, NombrePrueba, self.driver)
            logINFO("Prueba OK " + NombrePrueba, "INFO")
        except Exception as e:
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

def test_NecesitoAyuda(self,NombrePrueba):
        try:
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div[3]/button/span/span").click()
            time.sleep(5)
            screenshot(self.Ruta, NombrePrueba, self.driver)
            self.driver.back() 
            time.sleep(5) 
            logINFO("Prueba OK " + NombrePrueba, "INFO")          
        except Exception as e:
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

def test_CambioEmpr(self,NombrePrueba):
        try:
                self.driver.find_element(By.XPATH, "//div[3]/span/span").click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//input").send_keys("ADMINISTRADORA GRAL DE FONDOS SURA S.A")
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//input").send_keys(Keys.ENTER)
                time.sleep(2)
                screenshot(self.Ruta, "Segunda Empresa", self.driver)
                self.driver.find_element(By.XPATH, "//div[3]/span/span").click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//input").send_keys(Keys.BACKSPACE *50)
                time.sleep(2)
                self.driver.find_element(By.XPATH, "//input").send_keys("Empresa de Prueba")
                time.sleep(5)
                self.driver.find_element(By.XPATH, "//input").send_keys(Keys.ENTER)
                screenshot(self.Ruta, "Empresa Principal", self.driver)
                time.sleep(10)
        except Exception as e:
            logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")