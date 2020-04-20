using System;
public abstract class PathFinder
{
    protected int[] edgeTo;
    protected Boolean[] marked;

    protected int vertex;

    public PathFinder(Graph graph, int vertex)
    {
        edgeTo = new int[graph.Length()];
        this.vertex = vertex;
        marked = new Boolean[graph.Length()];
        for (int x = 0; x < graph.Length(); x++)
        {
            marked[x] = false;
        }
        traverse(graph, vertex);
    }

    public Boolean hasPath(int v2)
    {
        return this.marked[v2];
    }
    protected abstract void traverse(Graph graph, int vertex);
    public LinkedStack getPath(int v2)
    {

        if (hasPath(v2))
        {
            LinkedStack stack = new LinkedStack();

            stack.push(v2);

            int curr = v2;

            while (edgeTo[curr] != vertex)
            {
                stack.push(edgeTo[curr]);
                curr = edgeTo[curr];
            }

            stack.push(vertex);
            return stack;

        }
        return null;

    }
    public Boolean[] getMarked()
    {
        return marked;
    }
    
    public int[] getEdgeTo()
    {
        return edgeTo;
    }
}