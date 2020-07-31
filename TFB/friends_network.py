import collections

def friends_network(input_graph):
    flat_graph = [element for sub_list in input_graph for element in sub_list]
    C = collections.Counter(flat_graph)
    single_list = [element for sub_list in input_graph for element in sub_list if len(sub_list) == 1]
    for s in single_list:
        C[s] = 0
    return C

input_graph = [['A','B'], ['A','C'], ['A','D'], ['B','D'], ['E']]
ans = {'A': 3,  'B': 2, 'C': 1, 'D': 2, 'E': 0}
assert friends_network(input_graph) == ans
