import unittest
import day3

class TestDay3(unittest.TestCase):

	bank1 = [int(c) for c in "987654321111111"]
	bank2 = [int(c) for c in "811111111111119"]
	bank3 = [int(c) for c in "234234234234278"]
	bank4 = [int(c) for c in "818181911112111"]
	banks = [bank1, bank2, bank3, bank4]

	def test_bank_joltage_naive(self):
		self.assertEqual(day3.bank_joltage_naive(self.bank1), 98)
		self.assertEqual(day3.bank_joltage_naive(self.bank2), 89)
		self.assertEqual(day3.bank_joltage_naive(self.bank3), 78)
		self.assertEqual(day3.bank_joltage_naive(self.bank4), 92)

	def test_part_1_naive(self):
		self.assertEqual(day3.part_1_naive(self.banks), 357)

	def test_bank_joltage_linear(self):
		self.assertEqual(day3.bank_joltage_linear(self.bank1), 98)
		self.assertEqual(day3.bank_joltage_linear(self.bank2), 89)
		self.assertEqual(day3.bank_joltage_linear(self.bank3), 78)
		self.assertEqual(day3.bank_joltage_linear(self.bank4), 92)

if __name__ == '__main__':
    unittest.main()