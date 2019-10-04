from collections import Counter


def between(x, y, z):
    return y <= x <= z


def percent_intersection(functions_1, functions_2, is_cut=True,
                         min_value=0, max_value=1):
    intersection = [f for f in set(functions_1) if f in functions_2]
    if not functions_2:
        return False
    if is_cut:
        return between(min_value, len(intersection) / len(set(functions_2)),
                       max_value)
    return False


def percent_intersection_value(functions_1, functions_2, is_cut=True,
                               min_value=0, max_value=1):
    intersection = [f for f in set(functions_1) if f in functions_2]
    if not functions_2:
        return False
    if is_cut:
        return (len(intersection) / len(set(functions_2))) * 10
    return False


def get_decil(value, distribution, sort='default', reverse=False):
    value_list = distribution
    if sort == 'frequency':
        counts = Counter(value_list)
        value_list = sorted(value_list, key=counts.get, reverse=reverse)
    elif reverse:
        value_list = sorted(distribution, reverse=reverse)
    n = len(value_list)-1
    if value not in value_list:
        if int(value) in value_list:
            value = int(value)
        elif (int(value) + 0.5) in value_list:
            value = int(value) + 0.5
        elif (int(value) + 1) in value_list:
            value = int(value) + 1
        else:
            print(value)
            return 1
    if value == value_list[-1]:
        return 10
    value_position = value_list.index(value)
    return (value_position * 10) // n


def popular_function(functions_1, functions_2, order=0):
    functions_2_counter = Counter(functions_2)
    sorted_functions = sorted(functions_2_counter.items(), key=lambda x: x[1])
    if len(sorted_functions) > order:
        return sorted_functions[order][0] in functions_1
    return False


def compute_question(question, input_values):
    fnx = question['fnx']
    args = [input_values[v] for v in question['args']]
    kwargs = question['kwargs']
    post_fnx = question.get('post_fnx', lambda x: x)
    return post_fnx(fnx(*args, **kwargs))


def crucial(x, y, z, is_cut, functions1, functions2, min_value=0, max_value=1):
    if y <= x < z:
        return percent_intersection(functions1, functions2, is_cut,
                                    min_value=min_value, max_value=max_value)
    return False
