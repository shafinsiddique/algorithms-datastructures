using System;
using System.Collections.Generic;
public interface GraphAPI
{
    public void addEdge(int v1, int v2);
    public int Length();
    public String ToString();
    public HashSet<int>[] getAdj();


}

public abstract class Graph : GraphAPI
{
    protected int vertices;
    protected HashSet<int>[] adj;
    public Graph(int numVertices)
    {
        this.vertices = numVertices;
        this.adj = new HashSet<int>[vertices];

        for (int x = 0; x < vertices; x++)
        {
            adj[x] = new HashSet<int>();
        }

    }

    public override String ToString()
    {
        String string_rep = "";

        for (int x = 0; x < vertices; x++)
        {
            string_rep += x + ": ";

            foreach (int edge in adj[x])
            {
                string_rep += edge + " ";
            }

            string_rep += "\n";
        }

        return string_rep;
    }


    public int Length()
    {
        return this.vertices;
    }

    public HashSet<int>[] getAdj()
    {
        return this.adj;
    }

    public abstract void addEdge(int v1, int v2);
}