using System;
public class DirectedGraph : Graph
{
    public DirectedGraph(int numVertices) : base(numVertices) {

    }

    public override void addEdge(int v1, int v2) {
        adj[v1].Add(v2);
    }

}