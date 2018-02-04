import sys

from csv import DictWriter
from data import (read_network, compute_basic_node_attributes, get_functions,
                  compute_functions_attributes, compute_graph_attributes)

from questions import percent_intersection, popular_function

from logging import getLogger, Formatter, StreamHandler, INFO


logger = getLogger("IRT")
log_format = Formatter(
    '[%(asctime)s] --> %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S')

console_handler = StreamHandler(sys.stdout)
console_handler.setFormatter(log_format)

logger.addHandler(console_handler)

logger.setLevel(INFO)


questions = {
    "name": {
        "fnx": lambda x: x,
        "args": ["protein"],
        "kwargs": {}
    },
    "question_1": {
        "fnx": percent_intersection,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'min': 1, 'max': 1}
    },
    "question_2": {
        "fnx": percent_intersection,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'min': 0, 'max': 0.25}
    },
    "question_3": {
        "fnx": percent_intersection,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'min': 0.25, 'max': 0.5}
    },
    "question_4": {
        "fnx": percent_intersection,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'min': 0.5, 'max': 0.75}
    },
    "question_5": {
        "fnx": percent_intersection,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'min': 0.75, 'max': 1}
    },
    "question_6": {
        "fnx": percent_intersection,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'min': 0, 'max': 0}
    },
    "question_7": {
        "fnx": percent_intersection,
        "args": ['neighbors_functions', 'protein_functions'],
        "kwargs": {'min': 1, 'max': 1}
    },
    "question_8": {
        "fnx": percent_intersection,
        "args": ['neighbors_functions', 'protein_functions'],
        "kwargs": {'min': 0, 'max': 0.25}
    },
    "question_9": {
        "fnx": percent_intersection,
        "args": ['neighbors_functions', 'protein_functions'],
        "kwargs": {'min': 0.25, 'max': 0.5}
    },
    "question_10": {
        "fnx": percent_intersection,
        "args": ['neighbors_functions', 'protein_functions'],
        "kwargs": {'min': 0.5, 'max': 0.75}
    },
    "question_11": {
        "fnx": percent_intersection,
        "args": ['neighbors_functions', 'protein_functions'],
        "kwargs": {'min': 0.75, 'max': 1}
    },
    "question_12": {
        "fnx": percent_intersection,
        "args": ['neighbors_functions', 'protein_functions'],
        "kwargs": {'min': 0, 'max': 0}
    },
    "question_13": {
        "fnx": popular_function,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'order': 0}
    },
    "question_14": {
        "fnx": popular_function,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'order': 1}
    },
    "question_15": {
        "fnx": popular_function,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'order': 2}
    },
    "question_16": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['degree', 'degree_0', 'degree_25'],
        "kwargs": {}
    },
    "question_17": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['degree', 'degree_25', 'degree_50'],
        "kwargs": {}
    },
    "question_18": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['degree', 'degree_50', 'degree_75'],
        "kwargs": {}
    },
    "question_19": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['degree', 'degree_75', 'degree_100'],
        "kwargs": {}
    },
    "question_20": {
        "fnx": lambda x: 'celular_component' in x,
        "args": ['protein_category_functions'],
        "kwargs": {}
    },
    "question_21": {
        "fnx": lambda x: 'molecular_function' in x,
        "args": ['protein_category_functions'],
        "kwargs": {}
    },
    "question_22": {
        "fnx": lambda x: 'biological_process' in x,
        "args": ['protein_category_functions'],
        "kwargs": {}
    },
    "question_23": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['eccentricity', 'eccentricity_0',
                 'eccentricity_25'],
        "kwargs": {}
    },
    "question_24": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['eccentricity', 'eccentricity_25',
                 'eccentricity_50'],
        "kwargs": {}
    },
    "question_25": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['eccentricity', 'eccentricity_50',
                 'eccentricity_75'],
        "kwargs": {}
    },
    "question_26": {
        "fnx": lambda x, y, z: y <= x <= z,
        "args": ['eccentricity', 'eccentricity_75',
                 'eccentricity_100'],
        "kwargs": {}
    },
    "question_27": {
        "fnx": lambda x: x,
        "args": ['is_cut'],
        "kwargs": {}
    }
}


def main():
    logger.info('start')
    network = read_network()
    logger.info('computing basic node attributes')
    proteins = compute_basic_node_attributes(network)
    logger.info('getting functions')
    get_functions(proteins)
    logger.info('computing functions attributes')
    compute_functions_attributes(proteins)
    logger.info('computing grah attributes')
    compute_graph_attributes(network, proteins)
    logger.info('computing questions')
    responses = [
        {key: value['fnx'](*[protein[v] for v in value['args']],
                           **value['kwargs'])
         for key, value in questions.items()}
        for protein in proteins.values()
    ]
    with open('responses.csv', 'w') as fcsv:
        writer = DictWriter(fcsv, questions)
        writer.writeheader()
        writer.writerows(responses)

    return responses


responses = main()
print(responses[0])
