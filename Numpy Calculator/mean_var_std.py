import numpy as np

def calculate(l):
    if len(l)!=9:
        raise ValueError("List must contain nine numbers.")
    result = {}
    m = []

    while l!=[]:
        m.append(l[:3])
        l = l[3:]
    m = np.matrix(m)

    result['mean'] = [m.mean(axis=0).flatten().tolist()[0],
                        m.mean(axis=1).flatten().tolist()[0],
                        m.mean().flatten().tolist()[0]
                        ]

    result['variance'] = [m.var(axis=0).flatten().tolist()[0],
                        m.var(axis=1).flatten().tolist()[0],
                        m.var().flatten().tolist()[0]
                        ]

    result['standard deviation'] = [m.std(axis=0).flatten().tolist()[0],
                        m.std(axis=1).flatten().tolist()[0],
                        m.std().flatten().tolist()[0]
                        ]

    result['max'] = [m.max(axis=0).flatten().tolist()[0],
                        m.max(axis=1).flatten().tolist()[0],
                        m.max().flatten().tolist()[0]
                        ]

    result['min'] = [m.min(axis=0).flatten().tolist()[0],
                        m.min(axis=1).flatten().tolist()[0],
                        m.min().flatten().tolist()[0]
                        ]

    result['sum'] = [m.sum(axis=0).flatten().tolist()[0],
                        m.sum(axis=1).flatten().tolist()[0],
                        m.sum().flatten().tolist()[0]
                        ]

    return result