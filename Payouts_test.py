import unittest
from Payouts import payout_classification
from Payouts import Payout


class PayoutsTestCase(unittest.TestCase):
    symbol_list = ['A', 'A', 'K', 'K', 'A']

    def test_payout_classification(self):
        actual_classification = payout_classification(self.symbol_list)
        expected_classification = {'K': 1, 'A': 2}
        self.assertEqual(actual_classification, expected_classification)

    def test_payout(self):
        actual_payout = Payout(3).payout_main(payout_classification(self.symbol_list))
        expected_payout = 14.66
        self.assertEqual(expected_payout, actual_payout)

    def test_payout_dict(self):
        actual_payout_dict = Payout(5).payout_dict()
        actual_EV = 0
        probs_dict = Payout(5).payout_calc()[1]
        for i in actual_payout_dict:
            actual_EV += actual_payout_dict[i] * probs_dict[i + 1]
        expected_EV = -0.07

        self.assertEqual(expected_EV, round(actual_EV, 3))

    def test_payout_calc(self):
        expected_x = 2.931
        actual_x = round(Payout(3).payout_calc()[0], 3)

        self.assertEqual(expected_x, actual_x)


if __name__ == '__main__':
    unittest.main()

