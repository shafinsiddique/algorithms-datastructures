using System;
public class ConnectedComponents {
    int[] ids;
    Boolean[] marked;
    int count;
    public ConnectedComponents(Graph graph) {
        ids = new int[graph.Length()];
        marked = new Boolean[graph.Length()];

        for (int x=0; x<graph.Length(); x++) {
            marked[x] = false;
        }

        for (int x=0; x<graph.Length(); x++) {
            if (!marked[x]) {
                DFS(graph, x);
                count++;
            }
        }


    }

    public void DFS(Graph graph, int cur_vertex) {
        marked[cur_vertex] = true;
        ids[cur_vertex] = count;

        foreach (int edge in graph.getAdj()[cur_vertex]) {
            if (!marked[edge])  {
                DFS(graph, edge);
            }

        }
    }

    public Boolean connected(int v1, int v2) {
        return ids[v1] == ids[v2];
    }

    public int[] getIDs() {
        return ids;
    }
}