class Solution(object):
    def romanToInt(self, s):
        roman_number = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        
        for char in reversed(s):
            value = roman_number[char]
            result += value if value >= prev_value else -value
            prev_value = value
        
        return result
         
My_solution = Solution()
roman_numeral = "II"
roman_numeral = "X"
print(My_solution.romanToInt(roman_numeral))