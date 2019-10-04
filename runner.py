import sys

from csv import DictWriter
from data import (read_network, compute_basic_node_attributes, get_functions,
                  compute_functions_attributes, compute_graph_attributes,
                  read_blast_matrix, compute_blast_attributes)

from questions import compute_question

from registry import QUESTIONS

from logging import getLogger, Formatter, StreamHandler, INFO


logger = getLogger("IRT")
log_format = Formatter(
    '[%(asctime)s] --> %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S')

console_handler = StreamHandler(sys.stdout)
console_handler.setFormatter(log_format)

logger.addHandler(console_handler)

logger.setLevel(INFO)


def main():
    logger.info('start')
    # logger.info('reading network')
    # network = read_network()
    # logger.info('reading blast matrix')
    # matrix = read_blast_matrix()
    # logger.info('computing basic node attributes')
    # proteins = compute_basic_node_attributes(network)
    # logger.info('getting functions')
    # get_functions(proteins)
    # logger.info('computing functions attributes')
    # compute_functions_attributes(proteins)
    # logger.info('computing grah attributes')
    # compute_graph_attributes(network, proteins)
    # logger.info('computing blast attributes')
    # compute_blast_attributes(matrix, proteins)
    import pickle
    with open('proteins.pickle', 'rb') as f:
        proteins = pickle.load(f)
    logger.info('computing questions')
    
    responses = [
        {key: compute_question(value, protein)
         for key, value in QUESTIONS.items()}
        for protein in proteins.values()
    ]
    with open('responses_multiple2.csv', 'w') as fcsv:
        writer = DictWriter(fcsv, QUESTIONS)
        writer.writeheader()
        writer.writerows(responses)
    with open('questions_multiple2.csv', 'w') as fcsv:
        writer = DictWriter(fcsv, ["column", "description"])
        writer.writeheader()
        writer.writerows([{"column": key, "description": item['description']}
                         for key, item in QUESTIONS.items()])
    return responses


responses = main()
print(responses[0])
