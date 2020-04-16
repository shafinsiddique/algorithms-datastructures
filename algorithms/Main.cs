using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        { 
            UndirectedGraph ug = new UndirectedGraph(5);
            ug.addEdge(0,1);
            ug.addEdge(1,2);
            ug.addEdge(3,4);
            ConnectedComponents cc = new ConnectedComponents(ug);
            int[] arr = cc.getIDs();
            for (int x=0;x<arr.Length; x++) {
                System.Console.WriteLine(arr[x]);
            }
        }
    }
}



