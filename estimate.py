import math
import unittest
import random

def wallis(n):
	pi = 0.0
	for i in range(1,n+1):
		equ= float(4*i*i/(4*i*i - 1))
		if i==1:
			pi=equ
		else:
			pi=pi*equ
	pi= 2*pi
	return pi
	

def monte_carlo(n):
	inside_cir = 0
	pi = 0.0
	for i in range(n):
		x =  random.random()
		y =  random.random()
		distance = math.sqrt(x*x + y*y) 
		if distance <= 1:
			inside_cir += 1
	pi = 4*inside_cir/n
	return pi

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
