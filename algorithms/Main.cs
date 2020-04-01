using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            PriorityQueue p = new ArrayPriorityQueue();
            p.enqueue(1);
            p.enqueue(2);
            p.enqueue(4);
            p.enqueue(-1);
            p.enqueue(5);
            p.dequeue_max();
            System.Console.WriteLine(p);
            
        }
    }
}



