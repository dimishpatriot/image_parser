def yes_or_no(answer):
    d = ('y', 'Y', 'yes', 'Yes', 'YES')
    yes = False
    if d.count(answer):
        yes = True
    return yes


def is_num(num, min_value=0, max_value=100):
    min = min_value
    max = max_value
    ans = False
    try:
        if min <= int(num) <= max:
            ans = True
    except:
        ans = False
    return ans
