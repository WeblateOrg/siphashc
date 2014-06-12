import unittest

def suite():
    from . import test_siphashc
    suite = unittest.TestSuite()
    suite.addTest(test_siphashc.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())