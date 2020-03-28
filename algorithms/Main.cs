using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            Queue q = new Queue();
            q.enqueue(10);
            q.enqueue(20);
            q.enqueue(30);
            System.Console.WriteLine(q);
            q.dequeue();
            System.Console.WriteLine(q);

        }
    }
}
