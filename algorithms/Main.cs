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
            PathFinder bfs = new BFSPathFinder(ug, 1);
            System.Console.WriteLine(bfs.getPath(2));
        }
    }
}



