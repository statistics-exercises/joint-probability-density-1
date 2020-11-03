import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_variables(self) :
          f = k*(x**2*y**3 + x*y**3 ) 
          self.assertTrue( dfdx==sy.diff( f, x ), "the variable dfdx has not been set correctly" )
          self.assertTrue( dfdy==sy.diff( f, y ), "the variable dfdy has not been set correctly" )
          self.assertTrue( d2fdydx==sy.diff(sy.diff( f, x ), y), "the variable d2fdydx has not been set correctly" )
          self.assertTrue( d2fdxdy==sy.diff(sy.diff( f, x ), y), "the variable d2fdydx has not been set correctly" )
