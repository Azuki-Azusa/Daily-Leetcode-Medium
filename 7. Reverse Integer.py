class Solution:
    def reverse(self, x: int) -> int:
        mark = '+'
        x = str(x)
        if x[0] == '-':
            mark = '-'
            x = x[1:]
        temp = ''
        for dig in x:
            temp = dig + temp
        if len(temp) >= 10:
            if mark == '+':
                for i in range(10):
                    if int(temp[i]) > int('2147483647'[i]):
                        return 0
                    elif int(temp[i]) == int('2147483647'[i]):
                        continue
                    else:
                        break
            else:
                for i in range(10):
                    if int(temp[i]) > int('2147483648'[i]):
                        return 0
                    elif int(temp[i]) == int('2147483648'[i]):
                        continue
                    else:
                        break
        return int(mark + temp)

solution = Solution()
print(solution.reverse(-2147483412))