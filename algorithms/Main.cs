using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            DirectedGraph ug = new DirectedGraph(4);
            ug.addEdge(0, 1);
            ug.addEdge(1, 2);
            // ug.addEdge(1,2);
            // ug.addEdge(2,3);
            StrongComponents scc = new StrongComponents(ug);
            System.Console.WriteLine(scc.isConnected(2, 3));




        }
    }
}



