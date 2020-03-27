using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            LinkedList l  = new LinkedList();
            l.append(10);
            l.append(20);
            l.append(30);
            l.add(4);
            System.Console.WriteLine(l);
        }
    }
}
