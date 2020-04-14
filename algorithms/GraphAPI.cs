using System;
using System.Collections.Generic;
public interface Graph {
    public void addEdge(int v1, int v2);

    public Boolean isAdjacent(int v1, int v2);

    public int Length();

    public String ToString();

    public HashSet<int>[] getAdj();


}