def bal_next_year(bal, pmnt, mo_rate):
    for _ in range(12):    
        bal += mo_rate * (bal - pmnt) - pmnt
    return bal


def bisect(bal, apr, eps):
    l = bal / 12
    h = bal * (1 + apr / 12)**12 / 12
    m = (l + h) / 2
    while h - l > eps:
        tmp = bal_next_year(bal, m, apr / 12)
        if tmp < 0:
            m, h = (m + l) / 2, m
        if tmp > 0:
            m, l = (m + h) / 2, m
    return h


balance = 320000  # test case 1, expected 29,157.09
annualInterestRate = 0.2
print('Lowest Payment: {:.2f}'.format(bisect(balance, annualInterestRate, 0.01)))

balance = 999999  # test case 2, expected 90,325.03
annualInterestRate = 0.18
print('Lowest Payment: {:.2f}'.format(bisect(balance, annualInterestRate, 0.01)))
