import sys
sys.path = ['..'] + sys.path

import recommendations
import unittest

class TestRecommendations(unittest.TestCase):
  def setUp(self):
    self.ratings = {
      'joe': {'Ford': 1.0}, 
      'jeff': {'Ford': 2.0} 
    }
    
  def testSimDistanceForDifferentRatings(self):
    actual = recommendations.sim_distance(self.ratings, 'joe', 'jeff')
    self.assertEqual(0.5, actual)

  def testSimDistanceForSameRatings(self):
    self.ratings['jeff']['Ford'] = 1
    actual = recommendations.sim_distance(self.ratings, 'joe', 'jeff')
    self.assertEqual(1, actual)

    
if __name__ == '__main__':
    unittest.main()

    
