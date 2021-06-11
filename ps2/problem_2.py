def bal_next_year(bal, pmnt, mo_rate):
    for _ in range(12):    
        bal += mo_rate * (bal - pmnt) - pmnt
    return bal


def bisect(bal, apr, eps):
    def set_high():
        h = 500
        while bal_next_year(bal, h, apr / 12) > 0:
            h *= 2
        return h

    l, h = 0, set_high()
    m = round((l + h) // 2, 1)
    while h - l > eps:
        tmp = bal_next_year(bal, m, apr / 12)
        if tmp < 0:
            m, h = round((m + l) // 2, -1), m
        elif tmp > 0:
            m, l = round((m + h) // 2, -1), m
        else: break
    return h


balance = 3329  # test case 1, expected 310
annualInterestRate = 0.2
print('Lowest Payment:', bisect(balance, annualInterestRate, 10))

balance = 4773  # test case 2, expected 440
annualInterestRate = 0.2
print('Lowest Payment:', bisect(balance, annualInterestRate, 10))

balance = 3926  # test case 3, expected 360
annualInterestRate = 0.2
print('Lowest Payment:', bisect(balance, annualInterestRate, 10))
