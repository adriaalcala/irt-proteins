from collections import Counter


def percent_intersection(functions_1, functions_2, min=0, max=1):
    intersection = [f for f in set(functions_1) if f in functions_2]
    if not functions_2:
        return False
    return min <= len(intersection) / len(set(functions_2)) <= max


def popular_function(functions_1, functions_2, order=0):
    functions_2_counter = Counter(functions_2)
    sorted_functions = sorted(functions_2_counter.items(), key=lambda x: x[1])
    if len(sorted_functions) > order:
        return sorted_functions[order] in functions_1
    return False
