from functools import reduce

max_weight = 1000
inv = {
    'potatoes': [800, 1501600],
    'wheat_flour': [400, 1444000],
    'rice': [300, 1122000],
    'beans[can]': [300, 690000],
    'tomatoes[can]': [300, 237000],
    'strawberry_jam': [50, 130000],
    'peanut_butter': [20, 117800]
}


def output(inventory, max_weight):
    """Outputs the inventory in the following format: {items: [...], ...}"""
    for k, v in inventory.items():
        inventory[k].append(round(v[1] / v[0], 2))

    total_w = reduce(lambda x, y: x + y, [v[0] for v in inventory.values()])
    total_c = reduce(lambda x, y: x + y, [v[1] for v in inventory.values()])
    total_c_w = reduce(lambda x, y: x + y, [v[2] for v in inventory.values()])

    ratio = [(v, k) for k, v in sorted([(v[2], k) for k, v in inventory.items()], reverse=True)]
    take_out = []
    y = 0
    z = 0
    for v, k in ratio:
        if y + inventory[v][0] > max_weight:
            break
        y += inventory[v][0]
        z += inventory[v][1]
        take_out.append(v)

    return {
        'inventory': inventory,
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

inv_2 = {
    'bananas': [300, 2122000],
    'apples': [250, 132000],
    'jackfruit': [200, 110800],
    'kiwi': [100, 80000],
    'oranges': [500, 524000],
    'grapes': [30, 300120],
    'peaches': [208, 200530],
    'pineapple': [140, 106000],
    'strawberries': [100, 170000],
}

results_2 = output(inv_2, max_weight)
print('\n\n', results_2['results'])
print()
