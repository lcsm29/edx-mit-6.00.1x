def bal_next_year(bal, payment):
    for _ in range(1, 13):    
        unpaid = bal - payment
        bal = unpaid + (annualInterestRate / 12.0) * unpaid
    return bal


def bisect():
    l = balance / 12
    h = balance * (1 + annualInterestRate / 12) ** 12 / 12
    m = (l + h) / 2
    while 1:
        tmp = bal_next_year(balance, m)
        if tmp < 0:
            m, h = (m + l) / 2, m
        if tmp > 0:
            m, l = (m + h) / 2, m
        if h - l < 0.01:
            return h


balance = 320000
annualInterestRate = 0.2
print('Lowest Payment: {:.2f}'.format(bisect()))

balance = 999999
annualInterestRate = 0.18
print('Lowest Payment: {:.2f}'.format(bisect()))