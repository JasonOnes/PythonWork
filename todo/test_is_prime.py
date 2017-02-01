import unittest
import is_prime


class TestforPrime(unittest.TestCase):

    def test_really_prime(self):
        for i in range(0, is_prime.is_prime(x)):
            self.assertNotEqual(i % 2, 0)



if __name__ == '__main__':
    unittest.main()
