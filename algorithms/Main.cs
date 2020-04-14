using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        { 
            UndirectedGraph ug = new UndirectedGraph(3);
            ug.addEdge(0,1);
            ug.addEdge(1,2);
            DFSPathFinder dfs = new DFSPathFinder(ug, 0);
            System.Console.WriteLine(dfs.hasPath(2));


        }
    }
}



