a = []


def recurs(lst, rng):
    global a
    recurs(lst + ['-'], rng)
    recurs(lst + ['+'], rng)
    if len(lst) == rng:
        a.append(lst)
        return


recurs([], 3)