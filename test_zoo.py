import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_Unknown_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Invalid")
    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test_Teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_Adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    def test_Elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()