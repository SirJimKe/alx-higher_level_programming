import unittest
from models.base import Base

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = Base(id=5)
        self.obj1 = Base()
        self.obj2 = Base(id=10)
        self.obj3 = Base(id=20)
        self.obj4 = Base()


    def test_id_assignment(self):
        self.assertEqual(self.obj.id, 5)
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 10)
        self.assertEqual(self.obj3.id, 20)
        self.assertEqual(self.obj4.id, 2)
