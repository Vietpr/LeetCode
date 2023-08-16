class Solution(object):
    def intToRoman(self, num):
        roman_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        result = ""

        if num < 1:
            return None

        for value in sorted(roman_dict.keys(), reverse=True):
            while num >= value:
                num -= value
                result += roman_dict[value]

        return result

# Example 
num= 1994
solution = Solution()
roman_numeral = solution.intToRoman(num)
print(roman_numeral)
