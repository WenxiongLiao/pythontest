i = ['a', 'b']
l = [1, 2]
print(dict([i,l]))

a='AdfdFdd'
print(a.lower())


def cmp_ignore_case(s1, s2):
    if s1.lower() < s2.lower():
        return -1

    if s1.lower() > s2.lower():
        return 1
    return 0


print(sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case))


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print(sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))
