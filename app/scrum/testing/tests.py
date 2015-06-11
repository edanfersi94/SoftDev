import unittest
from testAcciones import TestAccion
from testActores import TestActor
from testEnlace import TestEnlace
from testHistActor import TestHistActor
from testHistObj import TestHistObj
from testHistorias import TestHistoria
from testObjetivo import TestObjetivo
from testProducto import TestProducto


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestAccion))
suite.addTest(unittest.makeSuite(TestActor))
suite.addTest(unittest.makeSuite(TestEnlace))
suite.addTest(unittest.makeSuite(TestHistActor))
suite.addTest(unittest.makeSuite(TestHistObj))
suite.addTest(unittest.makeSuite(TestHistoria))
suite.addTest(unittest.makeSuite(TestObjetivo))
suite.addTest(unittest.makeSuite(TestProducto))

unittest.TextTestRunner(verbosity=2).run(suite)