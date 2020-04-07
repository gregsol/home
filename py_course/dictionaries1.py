d = {6:[10]}
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    else:
        if 2*key in d:
            d[2*key] += [value]
        if 2*key not in d:
            d[2*key] = [value]
    return d
print(update_dictionary(d,1,100))
