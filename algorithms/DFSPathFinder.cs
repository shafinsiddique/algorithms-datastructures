using System;
public class DFSPathFinder {
    private int[]edgeTo;
    private Boolean[] marked;

    int vertex;

    public DFSPathFinder(Graph graph, int vertex) {
        edgeTo = new int[graph.Length()];
        this.vertex = vertex;
        marked = new Boolean[graph.Length()];
        for (int x=0; x<graph.Length(); x++) {
            marked[x] = false;
        }
        DFS(graph, vertex);
    }

    private void DFS(Graph graph, int vertex){
        marked[vertex] = true;

        foreach (int e in graph.getAdj()[vertex]) {
            if (!marked[e]) {
                edgeTo[e] = vertex;
                DFS(graph, e);
            }
        }

    }

    public Boolean hasPath(int v2) {
        return this.marked[v2];
    }

    public LinkedStack getPath(int v2) {

        if(hasPath(v2)) {
            LinkedStack stack = new LinkedStack();

            stack.push(v2);

            int curr = v2;

            while (edgeTo[curr] != vertex) {
                stack.push(edgeTo[curr]);
                curr = edgeTo[curr];
            }

            stack.push(vertex);
            return stack;

        }
        return null;
        
    }
    public Boolean[] getMarked() {
        return marked;
    }

    public int[] getEdgeTo() {
        return edgeTo;
    }

    }

