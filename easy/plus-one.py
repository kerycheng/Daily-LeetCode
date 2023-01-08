class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_len = len(digits)
        digits_last = digits_len - 1

        if digits[digits_len - 1] != 9:
            digits[digits_len - 1] += 1
            return digits

        while digits[digits_last] == 9:
            digits[digits_last] = 0
            digits_last -= 1

        if digits_last < 0:
            digits.insert(0 ,1)
            return digits

        digits[digits_last] += 1
        return digits