from functools import reduce


max_weight = 1000
inv = {
    'potatoes': [800, 1501600],
    'wheat_flour': [400, 1444000],
    'rice': [300, 1122000],
    'beans[can]': [300, 690000],
    'tomatoes[can]': [300, 237000],
    'stawberry_jam': [50, 130000],
    'peanut_butter': [20, 117800]
}

def output(inv, max_weight) :
    for k, v in inv.items():
        inv[k].append(round(v[1] / v[0], 2))
    
    total_w = reduce(lambda x, y: x + y, [v[0] for v in inv.values()])
    total_c = reduce(lambda x, y: x + y, [v[1] for v in inv.values()])
    total_c_w = reduce(lambda x, y: x + y, [v[2] for v in inv.values()])
    
    ratio = [(v, k) for k, v in sorted([(v[2], k) for k, v in inv.items()], reverse=True)]
    take_out = []
    y = 0
    z = 0
    for v, k in ratio:
        if (y+inv[v][0] > max_weight):
            break
        y += inv[v][0]
        z += inv[v][1]
        take_out.append(v)
    
    return {
        'iventory': inv,
        'total_calories_per_kg': total_c_w,
        'total_weight': total_w,
        'total_calories': total_c,
        'results': {
            'items': take_out,
            'total_calories': z,
            'total_weight': y,
            'ratio': ratio
        }
    }
    
results = output(inv, max_weight)
print(results['results'])
print()