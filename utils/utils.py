def validate_cpf(cpf):
    ''' Expects a numeric-only CPF string. '''
    if len(cpf) < 11:
        return False    
    
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    
    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
    d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
    return str(d1) == cpf[-2] and str(d2) == cpf[-1]

def verify_age(born,today):
    born_year = born.year
    born_day = born.day
    born_month = born.month
    this_year = today.year
    this_month = today.month
    this_day = today.day
    if this_month > born_month:
        age = this_year - born_year
    elif this_month == born_month and this_day >= born_day:
        age = this_year - born_year
    else:
        age = (this_year - born_year) - 1
    return age
def verify_age_is_more_than_18(born,today):
    born_year = born.year
    born_day = born.day
    born_month = born.month
    this_year = today.year
    this_month = today.month
    this_day = today.day
    if this_year - born_year >= 19:
        return True
    elif this_year - born_year == 18 and this_month > born_month:
        return True
    elif this_year - born_year == 18 and this_month == born_month and this_day >= born_day:
        return True
    else:
        return  False