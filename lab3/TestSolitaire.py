import unittest
import solitaire

class solitaireTester(unittest.TestCase):

  #feher 53, fekete -53

  #Test MoveJokers
  def testMoveJokers(self):
    l = [1, 53, 2, 3, -53, 4, 5]
    solitaire.moveJokers(l)
    self.assertListEqual(l, [1,2, 53, 3, 4, 5, -53])

    #when jokers get swapped
    l = [1, 53, -53, 1]
    solitaire.moveJokers(l)
    self.assertListEqual(l, [1, 53, 1, -53])

    #when joker moves over edge
    l = [53, 1, -53, 1]
    solitaire.moveJokers(l)
    self.assertListEqual(l, [-53, 53, 1, 1])


  #Test SwapCardsBehindAndAfterJokers
  def testSwapCardsBehindAndAfterJokers(self):
    l = [53, 1, 1, 1, -53, 1, 1]
    solitaire.swapCardsBehindAndAfterJokers(l)
    self.assertListEqual(l, [1, 1, 53, 1, 1, 1, -53])

  def test(self):

    #nem cserelodnek fel
    l = [1, 53, 4, -53, 2, 3, 6]
    solitaire.swapWithN(l)
    self.assertListEqual(l, l)

    l = [1, 53, 4, -53, 2, 4]
    solitaire.swapWithN(l)
    self.assertListEqual(l, [2, 1, 53, 4, -53, 4])


if __name__ == '__main__':
    unittest.main()