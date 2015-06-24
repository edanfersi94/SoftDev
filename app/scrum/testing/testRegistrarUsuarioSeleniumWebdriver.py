import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class testRegistrarUsuarioSeleniumWebdriver(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def testRegistrarUsuario(self):
        driver = self.driver
        driver.get("http://0.0.0.0:5000/#/VRegistro")
   
        nombreCompleto = driver.find_element_by_name("nombre")
        nombreCompleto.send_keys("Joel Rivas")
        
        usuario = driver.find_element_by_name("usuario")
        usuario.send_keys("Joel1993")

        clave = driver.find_element_by_name("clave")
        clave.send_keys("Joe@12345")

        claveRepetida = driver.find_element_by_name("clave2")
        claveRepetida.send_keys("Joe@12345")
        
        correo = driver.find_element_by_name("correo")
        correo.send_keys("rivasjoel004@gmail.com")    
        correo.submit()

        assert "No results found." not in driver.page_source

    def tearDown(self):
        time.sleep(5)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()