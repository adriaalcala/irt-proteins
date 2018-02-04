from goatools.obo_parser import GODag
from igraph import Graph
from json import load as json_load
from numpy import percentile


def read_network(net_path='hsa.tab'):
    return Graph.Read_Ncol(net_path, directed=False)


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
        proteins[protein].update(eccentricities_dict)
