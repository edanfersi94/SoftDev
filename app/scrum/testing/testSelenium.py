import unittest
from testRegistrarUsuarioSeleniumWebdriver import testRegistrarUsuarioSeleniumWebdriver
from testLoginSeleniumWebdriver import testLoginSeleniumWebdriver


suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(testRegistrarUsuarioSeleniumWebdriver))
suite.addTest(unittest.makeSuite(testLoginSeleniumWebdriver))


unittest.TextTestRunner(verbosity=2).run(suite)