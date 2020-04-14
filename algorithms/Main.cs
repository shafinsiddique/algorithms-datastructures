using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        { 
            UndirectedGraph ug = new UndirectedGraph(5);
            ug.addEdge(2,3);
            ug.addEdge(1,2);
            System.Console.WriteLine(ug);

        }
    }
}



