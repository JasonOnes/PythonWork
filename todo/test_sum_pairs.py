import unittest
import re
from sum_pairs import find_sum_pairs


class TestSumSums(unittest.TestCase):

    def setUp(self):
        self.pairs_list = []
        self.good_result = find_sum_pairs([2, 2, 5, 7, 4, 3], 7)

    #def test_pairs_sum_is_correct(self):
    #    self.assertEqual(self.pairs_list, self.good_result)
    def test_result_is_a_list_of_pairs(self):

        # pattern = re.compile(r"[\d+, \d+]")
        # patmatch =

        for pair_group in self.good_result:
            assert len(pair_group) == 2
            assert isinstance(pair_group[0], int)
            

        #import pdb; pdb.set_trace()

        assert bool(pattern.match(patmatch)) == True
        #assert pattern.match(self.good_result)

    def test_pairs_sum_are_numbers(self):
        for n in range(len(self.pairs_list)):
            assert self.pairs_list[n].isadigit() == True

    def test_pairs_are_probably_pairs(self):
        self.assertEqual((len(self.pairs_list) % 2), 0)



if __name__ == '__main__':
    unittest.main()
