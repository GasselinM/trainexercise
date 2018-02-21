import unittest
from trainexercise import *

class TrainTest(unittest.TestCase):
    def setUp(self):
        string ="AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7"
        self.TrainExercise = TrainExercise(string)
        self.TrainExercise.parseInput()
        
    def test_distanceBetweenCities(self):

		# Test 1:
	    self.assertEqual(self.TrainExercise.distanceBetweenCities('A-B-C'),9)

		# Test 2:
	    self.assertEqual(self.TrainExercise.distanceBetweenCities('A-D'),5)

		# Test 3:
	    self.assertEqual(self.TrainExercise.distanceBetweenCities('A-D-C'),13)

		# Test 4:
	    self.assertEqual(self.TrainExercise.distanceBetweenCities('A-E-B-C-D'),22)

		# Test 5:
	    self.assertEqual(self.TrainExercise.distanceBetweenCities('A-E-D'),'NO SUCH ROUTE')
        
    def test6(self):
        self.assertEqual(self.TrainExercise.numberOfTrip('C-C', 3),2)

	# Test 7 :
    def test7(self):
        self.assertEqual(self.TrainExercise.numberOfTripWithMaxStep('A-C', 4),3)

	# Test 8 :
    def test8(self):
        self.assertEqual(self.TrainExercise.shortestRoute('A-C'),9)


	# Test 9 :
    def test9(self):
        self.assertEqual(self.TrainExercise.shortestRoute('C-C'),9)

	# Test 10 :
    def test10(self):
        self.assertEqual(self.TrainExercise.numberOfPossibleRoad('C-C',30),7)




if __name__ == '__main__':
    unittest.main()
