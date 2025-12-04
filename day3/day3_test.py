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

	def test_part_2_joltage_recursive(self):
		self.assertEqual(day3.part_2_joltage_recursive(self.bank1, 12, {}), 987654321111)
		self.assertEqual(day3.part_2_joltage_recursive(self.bank2, 12, {}), 811111111119)
		self.assertEqual(day3.part_2_joltage_recursive(self.bank3, 12, {}), 434234234278)
		self.assertEqual(day3.part_2_joltage_recursive(self.bank4, 12, {}), 888911112111)

	def test_part_2_recursive(self):
		self.assertEqual(day3.part_2_recursive(self.banks), 3121910778619)

if __name__ == '__main__':
    unittest.main()