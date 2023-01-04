class Solution(object):
    def maximumWealth(self, accounts):
        all_money_per_acc = []
        for i in range(len(accounts)):
            sum = 0
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
            all_money_per_acc.append(sum)
    
        return max(all_money_per_acc)