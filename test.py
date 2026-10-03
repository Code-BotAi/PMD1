import unittest
from main import to_upper

class MyTestCase (unittest.TestCase):
    def Test_to_upper(self):
        name = "PRAVIN"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "PRAVIN")
        if __name__ == '__main__':
            unittest.main()
            