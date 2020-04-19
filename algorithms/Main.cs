using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            DirectedGraph ug = new DirectedGraph(5);
            ug.addEdge(0, 1);
            ug.addEdge(1, 2);
            ug.addEdge(3, 4);
            ug.addEdge(4,1);

            GraphProblems gp = new GraphProblems(ug);
            System.Console.WriteLine(gp.hasCycle());
            
 
           
        }
    }
}



