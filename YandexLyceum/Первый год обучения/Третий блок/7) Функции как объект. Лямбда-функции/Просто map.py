def simple_map(transformation, values):
    result = []
    for item in values:
        result.append(transformation(item))
    return result
