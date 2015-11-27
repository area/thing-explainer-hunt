import unittest
import main
import math
class TestThingExplainer(unittest.TestCase):

  def test_elements(self):
	self.assertEqual(main.elements("H HE LIBE C".lower()), math.log(118) * 2)
	self.assertEqual(main.elements("H HE LIB EC adfadf".lower()), math.log(118) * 2)
	self.assertEqual(main.elements("H HE LIB ECadfadf".lower()), math.log(118) * math.sqrt(3))
	self.assertEqual(main.elements("HE LIB ECadfadf".lower()), math.log(118) * math.sqrt(2))
	self.assertEqual(main.elements("HE L IL iECadfadf".lower()), math.log(118) * math.sqrt(1))


if __name__ == '__main__':
    unittest.main()
