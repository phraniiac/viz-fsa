import GraphConfig, {
    edgeTypes,
    EMPTY_EDGE_TYPE,
    EMPTY_TYPE,
    NODE_KEY,
    nodeTypes,
    COMPLEX_CIRCLE_TYPE,
    POLY_TYPE,
    SPECIAL_CHILD_SUBTYPE,
    SPECIAL_EDGE_TYPE,
    SPECIAL_TYPE,
    SKINNY_TYPE,
  } from './graph-config'; // Configures

export default {
    processGraph: (graph) => {


        graph.nodes.map(element => {
            element['type'] = SKINNY_TYPE

            return element;
        });


        return graph;
    }
}