using System;
public class DirectedGraph : Graph
{
    public DirectedGraph(int numVertices) : base(numVertices) {

    }

    public override void addEdge(int v1, int v2) {
        adj[v1].Add(v2);
    }


    public DirectedGraph reverse() {
        DirectedGraph reversed_graph = new DirectedGraph(vertices);
        for(int x=0; x<vertices; x++) {
            foreach(int edge in adj[x]) {
                reversed_graph.addEdge(edge, x);
            }
        }

        return reversed_graph;
    }


}