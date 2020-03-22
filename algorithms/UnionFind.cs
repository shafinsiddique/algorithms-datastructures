using System;

namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            InefficientUnionFind h = new InefficientUnionFind(4);
            h.union(0,3);
            h.union(2,3);
            System.Console.WriteLine(h.connected(1,2));
        }
    }
}
