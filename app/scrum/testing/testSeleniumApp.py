
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class testSeleniumApp(unittest.TestCase):
    
    # FUNCIONES AUXILIARES

    def esperar(self):
        time.sleep(4)    
    
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
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VRegistro")
        self.esperar() 
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
        
        el = driver.find_element_by_id("fUsuario_actorScrum")
        for option in el.find_elements_by_tag_name('option'):
            if option.text == 'Dueño de producto':
                option.click()
                break
        
        self.esperar() 
        correo.submit()
        
        # LOGIN
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VLogin")
        self.esperar()     
        usuario = driver.find_element_by_name("usuario")
        usuario.send_keys("Joel1993")

        clave = driver.find_element_by_name("clave")
        clave.send_keys("Joe@12345")
        self.esperar() 
        clave.submit()
        
        # CREO UNA CATEGORIA 
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VCategorias")
        self.esperar() 
        
        nombreCategoria= driver.find_element_by_name("nombre")
        nombreCategoria.send_keys("Categoria Creada ")

        pesoCategoria = driver.find_element_by_name("peso")
        pesoCategoria.send_keys("2")
        self.esperar() 
                 
        pesoCategoria.submit()
        
        # CREO PRODUCTO
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VProductos")
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VCrearProducto")
        self.esperar() 
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
        self.esperar() 
        nombreProducto = driver.find_element_by_name("nombre")
        nombreProducto.clear()
        nombreProducto.send_keys("Producto 1 Modificado")

        descripcionProducto = driver.find_element_by_name("descripcion")
        descripcionProducto.clear()
        descripcionProducto.send_keys("Nueva Descripcion del Producto 1")
        
        self.seleccionarEtiqueta(driver,"fPila_escala","Alta/Media/Baja")
        self.esperar() 
                 
        descripcionProducto.submit()
        
        """
        # CREO Actores  
            
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VProducto/1")
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VCrearActor/1")
        self.esperar() 
        
        nombreActor1 = driver.find_element_by_name("nombre")
        nombreActor1.send_keys("Actor 1")

        descripcionActor1 = driver.find_element_by_tag_name("Descripción")
        descripcionActor1.send_keys("Descripcion Actor 1")
        self.esperar() 
                 
        descripcionActor1.submit()
             
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VCrearActor/1")
        self.esperar() 
        
        nombreActor2 = driver.find_element_by_name("nombre")
        nombreActor2.send_keys("Actor 2")

        descripcionActor2 = driver.find_element_by_id("fActor_descripcion")
        descripcionActor2.send_keys("Descripcion Actor 2")
        self.esperar() 
                 
        descripcionActor2.submit()
        
    """
        # CREO Objetivos     
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VProducto/1")
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VCrearObjetivo/1")
        self.esperar() 
        
        nombreObjetivo1 = driver.find_element_by_id("fObjetivo_descripcion")
        nombreObjetivo1.send_keys("Objetivo 1")
        
        self.seleccionarEtiqueta(driver,"fObjetivo_transversal","Si")

        self.esperar()                  
        nombreObjetivo1.submit()

        # CREO  OBJETIVO 2
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VCrearObjetivo/1")
        self.esperar() 
        
        nombreObjetivo2 = driver.find_element_by_id("fObjetivo_descripcion")
        nombreObjetivo2.send_keys("Objetivo 2")

        self.seleccionarEtiqueta(driver,"fObjetivo_transversal","No")
        self.esperar() 
                 
        nombreObjetivo2.submit()
        
        # ELIMINAR OBJETIVO 2
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VObjetivo/2")
        self.esperar()
        
        driver.find_element_by_link_text("-objetivo").click(); 
        
        # Modifico Objetivo 1  
          
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VObjetivo/1")
        self.esperar() 
        
        nombreObjetivo1 = driver.find_element_by_id("fObjetivo_descripcion")
        nombreObjetivo1.clear()
        nombreObjetivo1.send_keys("Objetivo 1 Modificado")
        
        self.seleccionarEtiqueta(driver,"fObjetivo_transversal","No")

        self.esperar()                  
        nombreObjetivo1.submit()

        # CREO Acciones  
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VCrearAccion/1")
        self.esperar() 
        
        nombreAccion1 = driver.find_element_by_id("fAccion_descripcion")
        nombreAccion1.send_keys("Accion 1")

        self.esperar()                  
        nombreAccion1.submit()

        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VCrearAccion/1")
        self.esperar() 
        
        nombreAccion2 = driver.find_element_by_id("fAccion_descripcion")
        nombreAccion2.send_keys("Accion 2")
        self.esperar() 
                 
        nombreAccion2.submit()
        
        # ELIMINAR Accion 2
        self.esperar() 
        driver.get("http://0.0.0.0:5000/#/VAccion/2")
        self.esperar()
        
        driver.find_element_by_link_text("-accion").click(); 
        
        # Modifico Accion 1    
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VAccion/1")
        self.esperar() 
        
        nombreAccion1 = driver.find_element_by_id("fAccion_descripcion")
        nombreAccion1.clear()
        nombreAccion1.send_keys("Accion 1 Modificada")

        self.esperar()                  
        nombreAccion1.submit()        
        
        # CREO HISTORIAS 
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VHistorias/1 ")
        self.esperar()  
        
        driver.get("http://0.0.0.0:5000/#/VCrearHistoria/1")
        self.esperar()  
        codigoHistoria = driver.find_element_by_name("codigo")
        codigoHistoria.send_keys("CodHist")
        self.seleccionarEtiqueta(driver,"fHistoria_super","Ninguna")
        self.seleccionarEtiqueta(driver,"fHistoria_actores","Developer")
        self.seleccionarEtiqueta(driver,"fHistoria_tipo","Opcional")   
        self.seleccionarEtiqueta(driver,"fHistoria_accion","Accion 1 Modificada")
        self.seleccionarEtiqueta(driver,"fHistoria_objetivos","Objetivo 1 Modificado")   
        self.seleccionarEtiqueta(driver,"fHistoria_prioridad","Alta")           
        
        self.esperar()     
        codigoHistoria.submit()
        
        # MODIFICO LA HISTORIA
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VHistoria/1")
        self.esperar()
        
        codigoHistoria = driver.find_element_by_name("codigo")
        codigoHistoria.clear()
        codigoHistoria.send_keys("CodHist")
        self.seleccionarEtiqueta(driver,"fHistoria_super","Ninguna")
        self.seleccionarEtiqueta(driver,"fHistoria_actores","Scrum Master")
        self.seleccionarEtiqueta(driver,"fHistoria_tipo","Obligatoria")
        self.seleccionarEtiqueta(driver,"fHistoria_prioridad","Baja")           
        
        self.esperar()     
        codigoHistoria.submit()
        
        # ELIMINO LA HISTORIA 
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VHistoria/1")
        self.esperar()
        
        driver.find_element_by_link_text("-historia").click(); 
        
        # VUELVO A CREAR LA HISTORIA
        
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VHistorias/1 ")
        self.esperar()  
        
        driver.get("http://0.0.0.0:5000/#/VCrearHistoria/1")
        self.esperar()  
        codigoHistoria = driver.find_element_by_name("codigo")
        codigoHistoria.send_keys("CodHist")
        self.seleccionarEtiqueta(driver,"fHistoria_super","Ninguna")
        self.seleccionarEtiqueta(driver,"fHistoria_actores","Developer")
        self.seleccionarEtiqueta(driver,"fHistoria_tipo","Opcional")   
        self.seleccionarEtiqueta(driver,"fHistoria_accion","Accion 1 Modificada")
        self.seleccionarEtiqueta(driver,"fHistoria_objetivos","Objetivo 1 Modificado")   
        self.seleccionarEtiqueta(driver,"fHistoria_prioridad","Alta")           
        
        self.esperar()     
        codigoHistoria.submit()
        
        # CREAR TAREAS
        
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VHistoria/1")
        self.esperar()  
        
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VCrearTarea/1")
        self.esperar()  
        
        descripcionTarea = driver.find_element_by_name("descripcion")
        descripcionTarea.send_keys("Tarea 1")
        self.seleccionarEtiqueta(driver,"fTarea_categoria","Categoria Creada")
        self.esperar()  
        descripcionTarea.submit()
        
        # MODIFICAR TAREA
        
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VTarea/1")
        self.esperar()  
        
        descripcionTarea = driver.find_element_by_name("descripcion")
        descripcionTarea.clear()
        descripcionTarea.send_keys("Tarea 1 modificada")
        self.seleccionarEtiqueta(driver,"fTarea_categoria","Crear un diagrama UML")
        self.esperar()  
        descripcionTarea.submit()
        
        # ELIMINAR TAREA
        
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VTarea/1")
        self.esperar()  
        
        driver.find_element_by_link_text("-tarea").click();
        
        # CAMBIAR PRIORIDAD DE LA HISTORIA 
        
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VHistorias/1 ")
        self.esperar()  
        
        self.esperar()
        driver.get("http://0.0.0.0:5000/#/VPrioridades/1")
        self.esperar()
        
        prioridad = driver.find_element_by_id("fPrioridades_prioridad")
        for option in prioridad.find_elements_by_tag_name('option'):
            if option.text in "Baja":
                option.click()
        self.esperar()
        
        prioridad.submit()
        
        self.esperar()
        
                  
    def tearDown(self):
        self.esperar()
        self.driver.close()

if __name__ == "__main__":
    unittest.main()