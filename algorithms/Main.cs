using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            UnionFind h = new QuickUnion(4);
            h.union(0,3);
            h.union(2,3);
            System.Console.WriteLine(h.connected(0,2));
        }
    }
}
