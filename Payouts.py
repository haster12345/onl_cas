from math import comb


class Payout:

    def __init__(self, n):
        self.list_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']
        self.number_of_symbols = n

    def payout_calc(self):

        probs = dict()

        for k_pairs in range(2, self.number_of_symbols + 1):
            prob_of_k_same = comb(self.number_of_symbols, k_pairs) * 13 * (1 / 13) ** k_pairs * (12 / 13) ** (
                    self.number_of_symbols - k_pairs)
            probs[k_pairs] = prob_of_k_same

        sum_probs = 0
        for prob in probs:
            sum_probs += probs[prob]

        probs[1] = 1 - sum_probs

        Ex = 0
        for i in probs:
            if i > 1:
                Ex += probs[i] * (5 ** (i - 2))

        x = (probs[1] - 0.07) / Ex

        return x, probs

    def ev_function(self, x):
        return round(self.payout_calc()[0], 3)*(5**(x-1))

    def payout_dict(self) -> dict:

        payout_dict = {x: self.ev_function(x) for x in range(1, self.number_of_symbols)}
        payout_dict[0] = -1

        return payout_dict

    def payout_main(self, payout_class):
        classification_map = payout_class
        payout_dict = self.payout_dict()

        payout = -1
        for i in classification_map:
            if payout_dict[classification_map[i]] > payout:
                payout = payout_dict[classification_map[i]]

        return round(payout, 2)


def payout_classification(symbol_list) -> dict:
    hash_map = {}

    for i in symbol_list:
        if i not in hash_map:
            hash_map[i] = 0
        else:
            hash_map[i] = hash_map[i] + 1

    return hash_map

