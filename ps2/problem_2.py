def bal_next_year(bal, payment):
    for _ in range(1, 13):    
        unpaid = bal - payment
        bal = unpaid + (annualInterestRate / 12.0) * unpaid
    return bal


def set_high(bal):
    h = 500
    while bal_next_year(bal, h) > 0:
        h *= 2
    return h


def bisect():
    l, h = 0, set_high(balance)
    m = round(((l + h) // 2) / 10) * 10
    while 1:
        tmp = bal_next_year(balance, m)
        if tmp < 0:
            m, h = round(((m + l) // 2) / 10) * 10, m
        if tmp > 0:
            m, l = round(((m + h) // 2) / 10) * 10, m
        if h - l < 20:
            return h


balance = 3329
annualInterestRate = 0.2
print('Lowest Payment:', bisect())

balance = 4773
annualInterestRate = 0.2
print('Lowest Payment:', bisect())

balance = 3926
annualInterestRate = 0.2
print('Lowest Payment:', bisect())
