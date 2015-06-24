import unittest
from testAcciones import TestAccion
from testActores import TestActor
from testEnlace import TestEnlace
from testHistActor import TestHistActor
from testHistObj import TestHistObj
from testHistorias import TestHistoria
from testObjetivo import TestObjetivo
from testProducto import TestProducto
from testCategoria import TestCategoria
from testTareas import TestTareas


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestAccion))
suite.addTest(unittest.makeSuite(TestActor))
suite.addTest(unittest.makeSuite(TestEnlace))
suite.addTest(unittest.makeSuite(TestHistActor))
suite.addTest(unittest.makeSuite(TestHistObj))
suite.addTest(unittest.makeSuite(TestHistoria))
suite.addTest(unittest.makeSuite(TestObjetivo))
suite.addTest(unittest.makeSuite(TestProducto))
suite.addTest(unittest.makeSuite(TestCategoria))
suite.addTest(unittest.makeSuite(TestTareas))

unittest.TextTestRunner(verbosity=2).run(suite)