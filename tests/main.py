import sys
import unittest
sys.path.append("..")

from models.map import Map


class Test(unittest.TestCase):

    def setUp(self):
        self.map_obj = Map()
        self.valid_map = ['START: (0, 0)', 'GO (1000)']
        self.not_valid_map = ['START: (0, 0)', 'FLY']

    def test_not_valid_map(self):
        self.assertNotEqual(True, self.map_obj.is_valid(self.not_valid_map))

    def test_valid_map(self):
        self.assertEqual(True, self.map_obj.is_valid(self.valid_map))

    def test_valid_map_interpret(self):
        self.assertEqual([('START', ['0', '0']), ('GO', ['1000'])],
                         self.map_obj.interpret(self.valid_map))


if __name__ == '__main__':
    unittest.main()
