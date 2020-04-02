using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        { 
            BinaryHeap b = new BinaryHeap();
            b.enqueue(1);
            b.enqueue(2);
            b.enqueue(3);
            b.enqueue(0);
            b.sink(1); 
            System.Console.WriteLine(b);
            b.del_max();
            System.Console.WriteLine(b);
        }
    }
}



