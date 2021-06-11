balance = 42  # test 1, expected 31.38 (test 2, balance 484, expected 361.61)
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(1, 13):    
    unpaid = balance - balance * monthlyPaymentRate
    balance = unpaid + annualInterestRate / 12.0 * unpaid
    # print('Month {} Remaining balance: {:.2f}'.format(i, balance)) 
print('Remaining Balance: {:.2f}'.format(balance))
