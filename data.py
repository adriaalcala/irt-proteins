from csv import reader as csv_reader
from collections import defaultdict
from goatools.obo_parser import GODag
from igraph import Graph
from json import load as json_load
from numpy import percentile


def read_network(net_path='hsa.tab'):
    return Graph.Read_Ncol(net_path, directed=False)


def read_blast_matrix(matrix_path='hsa-blast.tab'):
    blast_matrix = defaultdict(dict)
    with open(matrix_path, 'r') as fcsv:
        reader = csv_reader(fcsv, delimiter='\t')
        for prot1, prot2, blast in reader:
            if prot1 != prot2:
                blast_matrix[prot1][prot2] = float(blast)
                blast_matrix[prot2][prot1] = float(blast)
    return blast_matrix


def compute_basic_node_attributes(network):
    def _compute_basic_attributes(v):
        degree = network.degree(v)
        eccentricity = network.eccentricity(v)
        neighbors = [network.vs(n)['name'][0] for n in network.neighbors(v)]
        return {'degree': degree, 'eccentricity': eccentricity,
                'neighbors': neighbors, 'is_cut': v['name'] in cut_vertices,
                'protein': v['name']}
    cut_vertices = [network.vs(v)['name'][0] for v in network.cut_vertices()]
    proteins = {v['name']: _compute_basic_attributes(v) for v in network.vs()}
    return proteins


def get_functions(proteins):
    functions = json_load(open('go.json'))
    for protein in proteins:
        proteins[protein]['protein_functions'] = functions.get(protein, [])
        neighbors = proteins[protein]['neighbors']
        proteins[protein]['neighbors_functions'] = \
            [f for neighbor in neighbors for f in functions.get(neighbor, [])]


def compute_functions_attributes(proteins):
    def _get_namespace(go):
        res = g.query_term(go)
        if not res:
            return ''
        return g.query_term(go).namespace
    g = GODag()
    for protein in proteins:
        proteins[protein]['protein_category_functions'] = \
            [_get_namespace(go)
             for go in proteins[protein]['protein_functions']]


def compute_graph_attributes(network, proteins):
    degrees = network.degree()
    degree_dict = {f'degree_{p}': percentile(degrees, p)
                   for p in [0, 25, 50, 75, 100]}

    eccentricities = network.eccentricity()
    eccentricities_dict = {f'eccentricity_{p}': percentile(eccentricities, p)
                           for p in [0, 25, 50, 75, 100]}
    for protein in proteins:
        proteins[protein].update(degree_dict)
        proteins[protein]['degree_distribution'] = sorted(degrees)
        proteins[protein].update(eccentricities_dict)
        proteins[protein]['eccentricity_distribution'] = sorted(eccentricities)


def compute_blast_attributes(matrix, proteins):
    for protein in proteins:
        blasts = list(matrix[protein].values())
        if blasts:
            blasts = list(matrix[protein].values())
            proteins[protein]['max_blast'] = max(blasts)
            proteins[protein]['min_blast'] = min(blasts)
            proteins[protein]['mean_blast'] = sum(blasts) / len(blasts)
        else:
            proteins[protein]['max_blast'] = 0
            proteins[protein]['min_blast'] = 0
            proteins[protein]['mean_blast'] = 0

    max_blast_list = [protein['max_blast'] for protein in proteins.values()]
    min_blast_list = [protein['max_blast'] for protein in proteins.values()]
    mean_blast_list = [protein['max_blast'] for protein in proteins.values()]
    max_blast_dict = {f'max_blast_{p}': percentile(max_blast_list, p)
                      for p in [0, 25, 50, 75, 100]}
    min_blast_dict = {f'min_blast_{p}': percentile(min_blast_list, p)
                      for p in [0, 25, 50, 75, 100]}
    mean_blast_dict = {f'mean_blast_{p}': percentile(mean_blast_list, p)
                       for p in [0, 25, 50, 75, 100]}

    for protein in proteins:
        proteins[protein].update(max_blast_dict)
        proteins[protein]['max_blast_distribution'] = sorted(max_blast_list)
        proteins[protein].update(min_blast_dict)
        proteins[protein].update(mean_blast_dict)
        proteins[protein]['mean_blast_distribution'] = sorted(mean_blast_list)
