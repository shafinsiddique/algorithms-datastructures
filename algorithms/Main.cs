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
            DepthFirstPaths d = new DepthFirstPaths(ug, 0);
            System.Console.WriteLine(d.hasPath(2));
            d.findPath(2);


        }
    }
}



