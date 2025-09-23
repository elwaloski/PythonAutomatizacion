import funciones
import LeerArchivo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from retrying import retry
from selenium.common.exceptions import TimeoutException
import unittest
""""
a=funciones.logINFO("estoy es una prueba de log","INFO")
b=funciones.logINFO("a","DEBUG")
c=funciones.logINFO("v","WARNING")
d=funciones.logINFO("e","ERROR")
f=funciones.logINFO("r","CRITICAL")

x=LeerArchivo.LeerArchivo()
print(LeerArchivo.IPCLOUD +"  "+LeerArchivo.BasedatoCLOUD+"  "+LeerArchivo.UsuarioCLOUD+"  "+LeerArchivo.PassCLOUD)
"""



class TestExample(unittest.TestCase):

    @classmethod 
    def setUpClass(cls):
        cls.chrome_options = webdriver.ChromeOptions()            
        cls.chrome_options.add_argument("--incognito") 
        cls.chrome_options.add_argument("--start-maximized")               
        cls.driver = webdriver.Chrome(options=cls.chrome_options)        
        funciones.logINFO("SE agregan los argunmento del web de forma correcta","INFO")
        LeerArchivo.LeerArchivo()


    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda e: isinstance(e, TimeoutException))
    def test1_Prueba1CargaWeb(cls):
        try:
            cls.driver.get(LeerArchivo.URLWEBAUT)
            time.sleep(2)
            funciones.screenshot("Cargo_WEB",cls.driver)
            time.sleep(2)
            funciones.logINFO("Prueba de carga de web es exitosa","INFO")
        except:
            funciones.logINFO("Error en la prueba de carga de web","ERROR")
            cls.fail("Prueba mala")
    
    
    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda e: isinstance(e, TimeoutException))
    def test2_Prueba2IngresaUsuario(cls):
        try:
            cls.driver.find_element(By.ID, "p_Usuario").send_keys("prod_0277")
            time.sleep(2)
            funciones.screenshot("Ingresa_Usuario",cls.driver)
            time.sleep(2)
            funciones.logINFO("Prueba de ingresar usuario es exitosa","INFO")
        except:
            funciones.logINFO("Error al ingresar usuario","ERROR")
            cls.fail("Prueba mala")

    @retry(stop_max_attempt_number=3, wait_fixed=2000, retry_on_exception=lambda e: isinstance(e, TimeoutException))
    def test3_Prueba3IngresaPass(cls):
        try:
            cls.driver.find_element(By.ID, "p_Clave").send_keys("wsx678S")
            time.sleep(2)
            funciones.screenshot("Ingresa_Pass",cls.driver)
            time.sleep(2)
            funciones.logINFO("Prueba de ingresar Pass es exitosa","INFO")
        except:
            funciones.logINFO("Error al ingresar Pass","ERROR")
            cls.fail("Prueba mala")

    @retry(stop_max_attempt_number=3)
    def test4_Prueba4IngresaPass(cls):
        
        try:
            cls.driver.find_element(By.CSS_SELECTOR, ".btn").click()
            time.sleep(2)
            funciones.screenshot("Ingreso_Loggin",cls.driver)
            funciones.logINFO("Prueba de ingresar al menu exitosa","INFO")
        except:
            funciones.logINFO("Error al ingresar al Menu","ERROR")
            cls.fail("Prueba mala")

@classmethod   
def tearDown(cls):
    # Cerrar el driver del navegador
    cls.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExample)
    corredor = unittest.TextTestRunner()
    resultados = corredor.run(suite)
    print(resultados)

