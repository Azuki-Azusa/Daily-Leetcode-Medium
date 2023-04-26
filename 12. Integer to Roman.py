class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        dig = [0 for i in range(4)]
        dig[0] = num // 1000
        dig[1] = num % 1000 // 100
        dig[2] = num % 100 // 10
        dig[3] = num % 10
        if dig[0]:
            res += 'M' * dig[0]

        if dig[1]:
            if dig[1] <= 3:
                res += 'C' * dig[1]
            elif dig[1] == 4:
                res += 'CD'
            elif dig[1] <= 8:
                res += 'D'
                res += 'C' * (dig[1] - 5)
            else:
                res += 'CM'
        
        if dig[2]:
            if dig[2] <= 3:
                res += 'X' * dig[2]
            elif dig[2] == 4:
                res += 'XL'
            elif dig[2] <= 8:
                res += 'L'
                res += 'X' * (dig[2] - 5)
            else:
                res += 'XC'

        if dig[3]:
            if dig[3] <= 3:
                res += 'I' * dig[3]
            elif dig[3] == 4:
                res += 'IV'
            elif dig[3] <= 8:
                res += 'V'
                res += 'I' * (dig[3] - 5)
            else:
                res += 'IX'
        return res


solution = Solution()
print(solution.intToRoman(1994))