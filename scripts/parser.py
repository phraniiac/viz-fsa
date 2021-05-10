from .cfg_pb2 import *
from google.protobuf.text_format import Parse
from google.protobuf.json_format import MessageToJson, MessageToDict
import json

with open('scripts/cfg.json', 'r') as f:
    
    cfg: ContextFreeGrammar = ContextFreeGrammar()
    Parse(f.read(), cfg)
    # print(cfg)

    cfg_dict = MessageToDict(cfg)
    # print(cfg)


    nodes = []

    x_axis = 10

    y_axis_terminal = 100
    y_axis_normal = 0


    for node in cfg_dict['nodes']:
        # print(node)
        n_node = {}
        n_node['id'] = str(node['canonicalId'])
        x_loc = x_axis
        y_loc = y_axis_normal
        if 'possibleValues' in node:
            n_node['title'] = ' '.join(node['possibleValues'])
        else:
            n_node['title'] = node['name']
        # n_node['color'] = 'lightgreen'

        # if node['isTerminalNode']:
        #     y_loc = y_axis_terminal

        # x_axis += 100

        n_node['x'] = x_loc
        n_node['y'] = y_loc
        # n_node['type'] = 'SKINNY_TYPE'
        nodes.append(n_node)

    edges = []
    edge_key = 0
    for edge in cfg_dict['productionRules']:
        for adj_node in edge['adjacentNodes']:
            n_edge = {}
            edge_key -= 1
            # n_edge['key'] = edge_key
            n_edge['source'] = str(edge['node1'])
            n_edge['target'] = str(adj_node)
            n_edge['type'] = "EMPTY_EDGE_TYPE"

            edges.append(n_edge)




    final_js = {
        'nodes': nodes,
        'edges': edges
    }

        



    with open('/Users/pranavsharma/br/side-tools/viz-fsa/src/graph.json', 'w') as f2:

        json.dump(final_js, f2)
        # f2.write(MessageToJson(cfg))


    
