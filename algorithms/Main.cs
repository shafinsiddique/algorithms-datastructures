using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            TwoStackQueue q = new TwoStackQueue();
            q.enqueue(10);
            q.enqueue(20);
            System.Console.WriteLine(q.pop());
            System.Console.WriteLine(q.pop());
            
        }
    }
}



