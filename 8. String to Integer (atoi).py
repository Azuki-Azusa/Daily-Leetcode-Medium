class Solution:
    def myAtoi(self, s: str) -> int:
        caseArray = [str(i) for i in range(10)]
        s = s.lstrip(' ')
        mark = '+'
        temp = ''
        for dig in s:
            if temp == '':
                if dig == '+' or dig == '-' or dig in caseArray:
                    temp += dig
                else:
                    return 0
            elif temp == '+' or temp == '-' or temp == '0':
                if dig == '0':
                    continue
                elif dig in caseArray:
                    mark = temp[0]
                    temp = temp[1:]
                    temp += dig
                else:
                    return 0
            else:
                if dig in caseArray:
                    temp += dig
                else:
                    break
        if len(temp) == 0 or temp == '+' or temp == '-' or temp == '0':
            return 0
        elif len(temp) > 10:
            if mark == '+':
                return 2147483647
            else:
                return -2147483648
        elif len(temp) == 10:
            if mark == '+' or mark == '0':
                for i in range(10):
                    if int(temp[i]) > int('2147483647'[i]):
                        return 2147483647
                    elif int(temp[i]) == int('2147483647'[i]):
                        continue
                    else:
                        break
            else:
                for i in range(10):
                    if int(temp[i]) > int('2147483648'[i]):
                        return -2147483648
                    elif int(temp[i]) == int('2147483648'[i]):
                        continue
                    else:
                        break
        return int(mark + temp)
        

solution = Solution()
print(solution.myAtoi("2147483646"))