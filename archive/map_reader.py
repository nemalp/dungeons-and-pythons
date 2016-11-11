def load_map(filename):
    with open(filename, 'r') as f:
        data = f.read().split('\n')
        map_ = [list(x) for x in data if x.strip() != '']

    return map_
