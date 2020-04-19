using System;
public class GraphProblems
{
    Graph graph;
    Boolean[] marked;
    public GraphProblems(Graph graph)
    {
        this.graph = graph;
        marked = new Boolean[graph.Length()];

        for (int x = 0; x < marked.Length; x++)
        {
            marked[x] = false;
        }

  
    }

    /* 
    Find if there is cycle in directed graph.
    */
    public Boolean hasCycle()
    {
        Boolean foundCycle = false;
        for (int x=0;x<marked.Length; x++) {
            if(!marked[x]) {
                if (cycleDetected(x)) {
                    foundCycle = true;
                    break;
                }
            }
        }

        unmarkVisited();

        return foundCycle;

    }


    private void unmarkVisited() {
        for (int x=0; x<marked.Length; x++) {
            marked[x] = false;
        }
    }
    private Boolean cycleDetected(int vertex){ 
        marked[vertex] = true;

        foreach (int edge in graph.getAdj()[vertex]) {
            if (marked[edge]) {
                return true;
            }

            else {
                return cycleDetected(edge);
            }
        }

        return false;

    }

}