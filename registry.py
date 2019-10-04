from questions import (popular_function, crucial, percent_intersection_value,
                       get_decil)


QUESTIONS = {
    "name": {
        "fnx": lambda x: x,
        "args": ["protein"],
        "kwargs": {},
        "description": "Nombre de la proteina"
    },
    "question_1": {
        "fnx": percent_intersection_value,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {},
        "post_fnx": int,
        "description":"Porcentaje de las funciones de los vecinos que las hace la proteina (En tanto por 10)"  # noqa
    },
    "question_2": {
        "fnx": percent_intersection_value,
        "args": ['neighbors_functions', 'protein_functions'],
        "kwargs": {},
        "post_fnx": int,
        "description": "Porcentaje de las funciones de la proteina que las hace los vecinos (En tanto por 10)"  # noqa
    },
    "question_4": {
        "fnx": popular_function,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'order': 0},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Hace la función más popular de sus vecinos"
    },
    "question_5": {
        "fnx": popular_function,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'order': 1},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Hace la segundo función más popular de sus vecinos"
    },
    "question_6": {
        "fnx": popular_function,
        "args": ['protein_functions', 'neighbors_functions'],
        "kwargs": {'order': 2},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Hace la tercera función más popular de sus vecinos"
    },
    "question_7": {
        "fnx": get_decil,
        "args": ['degree', 'degree_distribution'],
        "kwargs": {'sort': 'frequency'},
        "post_fnx": int,
        "description": "El grado de la proteina esta en el decil x ordenado por frequencia"  # noqa
    },
    "question_8": {
        "fnx": get_decil,
        "args": ['eccentricity', 'eccentricity_distribution'],
        "kwargs": {'reverse': True},
        "post_fnx": int,
        "description": "La eccentricidad de la proteina esta en el decil x ordenado en orden inverso"  # noqa

    },
    "question_9": {
        "fnx": lambda x: x,
        "args": ['is_cut'],
        "kwargs": {},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Es vertice de corte"
    },
    "question_10": {
        "fnx": lambda x, y, z, k: k and y < x <= z,
        "args": ['eccentricity', 'eccentricity_75',
                 'eccentricity_100', 'is_cut'],
        "kwargs": {},
        "post_fnx": lambda x: int(not x) * 10,
        "description": "Es de corte y la eccentricidad esta en el cuarto cuartil"  # noqa
    },
    "question_11": {
        "fnx": lambda x, y, z, k: k and y <= x < z,
        "args": ['eccentricity', 'eccentricity_0',
                 'eccentricity_25', 'is_cut'],
        "kwargs": {},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Es de corte y la eccentricidad esta en el primer cuartil"  # noqa
    },
    "question_12": {
        "fnx": lambda x, y, z, k: k and y <= x < z,
        "args": ['eccentricity', 'degree_75',
                 'degree_100', 'is_cut'],
        "kwargs": {},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Es de corte y el grado esta en el cuarto cuartil"
    },
    "question_13": {
        "fnx": lambda x, y, z, k: k and y <= x < z,
        "args": ['eccentricity', 'degree_0',
                 'degree_25', 'is_cut'],
        "kwargs": {},
        "post_fnx": lambda x: int(not x) * 10,
        "description": "Es de corte y el grado esta en el primer cuartil"
    },
    "question_14": {
        "fnx": percent_intersection_value,
        "args": ['neighbors_functions', 'protein_functions', 'is_cut'],
        "kwargs": {},
        "post_fnx": lambda x: 10 - int(x),
        "description": "Es de corte y el porcentaje de las funciones de la proteina las hacen los vecinos"  # noqa
    },
    "question_15": {
        "fnx": get_decil,
        "args": ['max_blast', 'max_blast_distribution'],
        "kwargs": {'reverse': True},
        "post_fnx": int,
        "description": "Decil del max blast (cuanto menos semejanza mejor)"
    },
    "question_16": {
        "fnx": get_decil,
        "args": ['mean_blast', 'mean_blast_distribution'],
        "kwargs": {'reverse': True},
        "post_fnx": int,
        "description": "Decil del mean blast (cuanto menos semejanza mejor)"
    },
    "question_17": {
        "fnx": crucial,
        "args": ['eccentricity', 'eccentricity_0',
                 'eccentricity_25', 'is_cut', 'protein_functions',
                 'neighbors_functions'],
        "kwargs": {'min_value': 0, 'max_value': 0},
        "post_fnx": lambda x: int(not x) * 10,
        "description": "Es de corte, la eccentricidad de la proteina esta en el cuarto cuartil y niguna de las funciones de los vecinos las hace la proteina"  # noqa
    },
    "question_18": {
        "fnx": crucial,
        "args": ['eccentricity', 'eccentricity_0',
                 'eccentricity_25', 'is_cut',
                 'neighbors_functions', 'protein_functions'],
        "kwargs": {'min_value': 1, 'max_value': 1},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Es de corte, la eccentricidad de la proteina esta en el cuarto cuartil y todas las funciones de la proteina las hacen los vecinos"  # noqa

    },
    "question_19": {
        "fnx": crucial,
        "args": ['eccentricity', 'eccentricity_75',
                 'eccentricity_100', 'is_cut', 'protein_functions',
                 'neighbors_functions'],
        "kwargs": {'min_value': 0, 'max_value': 0},
        "post_fnx": lambda x: int(not x) * 10,
        "description": "Es de corte, la eccentricidad de la proteina esta en el cuarto cuartil y niguna de las funciones de los vecinos las hace la proteina"  # noqa
    },
    "question_20": {
        "fnx": crucial,
        "args": ['eccentricity', 'eccentricity_75',
                 'eccentricity_100', 'is_cut',
                 'neighbors_functions', 'protein_functions'],
        "kwargs": {'min_value': 1, 'max_value': 1},
        "post_fnx": lambda x: int(x) * 10,
        "description": "Es de corte, la eccentricidad de la proteina esta en el cuarto cuartil y todas las funciones de la proteina las hacen los vecinos"  # noqa

    }
}
