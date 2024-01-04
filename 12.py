def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

# Örnek kullanım
lst = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(lst))