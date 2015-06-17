
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class testSeleniumApp(unittest.TestCase):
    
    # FUNCIONES AUXILIARES

    def esperar(self):
        time.sleep(3)    
    
    def seleccionarEtiqueta(self,driver, element_id, labels):
        el = driver.find_element_by_id(element_id)
        for option in el.find_elements_by_tag_name('option'):
            if option.text in labels:
                option.click()

    def setUp(self):
        self.driver = webdriver.Firefox()

    def testRegistrarUsuario(self):
        driver = self.driver
        
        # REGISTRO DE USUARIO
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
        self.esperar()   
        correo.submit()
        
        # LOGIN
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VLogin")
            
        usuario = driver.find_element_by_name("usuario")
        usuario.send_keys("Joel1993")

        clave = driver.find_element_by_name("clave")
        clave.send_keys("Joe@12345")
        self.esperar() 
        clave.submit()
        
        # CREO PRODUCTO
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VProductos")
      
        driver.get("http://0.0.0.0:5000/#/VCrearProducto")
        nombreProducto = driver.find_element_by_name("nombre")
        nombreProducto.send_keys("Producto 1")

        descripcionProducto = driver.find_element_by_name("descripcion")
        descripcionProducto.send_keys("Descripcion del Producto 1")
        
        self.seleccionarEtiqueta(driver,"fPila_escala","Entre 1 y 20")
        self.esperar() 
                 
        descripcionProducto.submit()

        # MODIFICO PRODUCTO
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VProducto/1")

        nombreProducto = driver.find_element_by_name("nombre")
        nombreProducto.clear()
        nombreProducto.send_keys("Producto 1 Modificado")

        descripcionProducto = driver.find_element_by_name("descripcion")
        descripcionProducto.clear()
        descripcionProducto.send_keys("Nueva Descripcion del Producto 1")
        
        self.seleccionarEtiqueta(driver,"fPila_escala","Alta/Media/Baja")
        self.esperar() 
                 
        descripcionProducto.submit()
        
                           
    def tearDown(self):
        self.esperar()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()