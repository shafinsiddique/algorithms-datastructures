using System;
public class ConnectedComponents {
    Graph graph;
    int[] ids;
    Boolean[] marked;

    public ConnectedComponents(Graph g) {
        graph = g;
        ids = new int[graph.Length()];
        marked = new Boolean[graph.Length()];
        for (int x=0; x<graph.Length(); x++) {
            marked[x] = false;
            ids[x] = -1;
        }
        
        for (int x=0; x<graph.Length(); x++) {
                DFS(graph, x);
            
        }
    }

    public int[] getIDs() {
        return ids;
    }

    private void DFS(Graph graph, int cur_vertex) {

        if (!marked[cur_vertex]) {
             marked[cur_vertex] = true;

            if (ids[cur_vertex] == -1) {
                ids[cur_vertex] = cur_vertex;
            }
            foreach (int edge in graph.getAdj()[cur_vertex]) {
                    ids[edge] = ids[cur_vertex];
                    DFS(graph,edge);
            }

        }
       
    }

}