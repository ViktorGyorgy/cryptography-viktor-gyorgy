import unittest
import Knapsack
import math
import utils

class TestKnapsack(unittest.TestCase):

  def setUp(self):
    Knapsack.generateKeys()

  def test_KeysGeneration(self):
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

  def test_Encode(self):
    byte = bytes("h", 'utf8')[0]

    encodedByte = Knapsack.encodeByte(byte)

    bits = utils.byte_to_bits(byte)
    self.assertEqual(encodedByte, sum([x * y for x, y in zip(bits, Knapsack.b)]))


if __name__ == '__main__':
  unittest.main()