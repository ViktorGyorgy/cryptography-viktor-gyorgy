import unittest
import Knapsack
import math

class TestKnapsack(unittest.TestCase):

  def testKeysGeneration(self):
    Knapsack.generateKeys()

    total = 0
    
    self.assertEqual(Knapsack.n, len(Knapsack.w))
    self.assertEqual(Knapsack.n, len(Knapsack.b))

    for i in Knapsack.w:
      self.assertGreater(i, total)
      total += i

    self.assertGreater(Knapsack.q, total)

    self.assertEqual(1, math.gcd(Knapsack.r, Knapsack.q))

    for i in range(Knapsack.n):
      self.assertEqual(Knapsack.b[i], Knapsack.w[i] * Knapsack.r % Knapsack.q)


if __name__ == '__main__':
  unittest.main()