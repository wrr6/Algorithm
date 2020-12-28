class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if five >= 1:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif i == 20:
                if ten >= 1 and five >= 1:
                    twenty += 1
                    ten -= 1
                    five -= 1
                elif ten == 0 and five >= 3:
                    twenty += 1
                    five -= 3
                else:
                    return False
        return True