import unittest
from main import suma

class TestSuma(unittest.TestCase):
    def test_suma_correcta(self):
        self.assertEqual(suma(2, 3), 5)

if __name__ == '__main__':
    document_type = "GOOGLE_DOC"
    unittest.main()
