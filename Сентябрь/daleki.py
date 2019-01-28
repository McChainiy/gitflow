import sys
replaced = ['"', '(', "'", '{', '[']
count = 0
for i in sys.stdin:
    for z in i.split():
        for jey in z:
            if jey in replaced:
                z = z.replace(jey, '')
        if z.lower().startswith('далек'):
            count += 1
            break
print(count)