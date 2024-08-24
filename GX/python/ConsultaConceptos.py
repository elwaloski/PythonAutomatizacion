from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import funciones
import unittest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestExample(unittest.TestCase):
    Ruta = funciones.CrearRutaEvidencia("ConsultaConceptos")

    @classmethod 
    def setUpClass(cls):        
        funciones.LeerArchivo()     
        chrome_options = webdriver.ChromeOptions()            
        chrome_options.add_argument("--incognito") 
        chrome_options.add_argument("--start-maximized")     
        # Usar webdriver-manager para manejar el driver de Chrome
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    def test_A1_carga_de_web(self):
        NombrePrueba = 'Iniciar Sesion'
        try:
            funciones.test_carga_web(self)
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")   
            
    def test_A2_ConsultaConceptosCS(self):
        NombrePrueba = 'BuscarConceptoCS'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Seguro","cl-cs-2017-11-30","activo")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")    

    def test_A3_ConsultaConceptosHB(self):
        NombrePrueba = 'BuscarConceptoHB'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Holding Bancario","cl-hb-2024-01-02","Patrimonio")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")  

    def test_A4_ConsultaConceptosHS(self):
        NombrePrueba = 'BuscarConceptoHS'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Holding Seguro","cl-hs-2024-01-02","Patrimonio")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")  

    def test_A5_ConsultaConceptosCC(self):
        NombrePrueba = 'BuscarConceptoCC'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Cajas Compensación","svs-cl-cc-2024-01-02","Patrimonio")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")  

    def test_A6_ConsultaConceptosEI(self):
        NombrePrueba = 'BuscarConceptoEI'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Entidades informantes","svs-cl-ei-2024-01-02","Aplicacion")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

    def test_A7_ConsultaConceptosBS(self):
        NombrePrueba = 'BuscarConceptoBS'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Bancos y Seguros","svs-cl-bs-2024-01-02","Negocios")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

    def test_A8_ConsultaConceptosTX(self):
        NombrePrueba = 'BuscarConceptoTX'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Taxo Fondos","cl-iv_20110430","Aumento")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

    def test_A9_ConsultaConceptosCircular(self):
        NombrePrueba = 'BuscarConceptoCircular'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Circ2275","cs-im-2020-03-15","Cuentas")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")
    def test_B1_ConsultaConceptosCI(self):
        NombrePrueba = 'BuscarConceptoCI'
        try:
            funciones.test_ConsultaConceptos(self,NombrePrueba,"Comercio Industria","svs-cl-ci-2024-01-02","Total")
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}")

    def test_C1_CerrarSesion(self): 
        NombrePrueba = 'Cerrar Sesion'
        try:
            funciones.test_CerrarSesion(self)
        except Exception as e:
            funciones.logINFO(f"Error {NombrePrueba}: {str(e)}", "ERROR")
            self.fail(f"Error {NombrePrueba}: {str(e)}") 

    @classmethod   
    def tearDownClass(cls):    
        cls.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExample)
    corredor = unittest.TextTestRunner()
    resultados = corredor.run(suite)
    print(resultados)
