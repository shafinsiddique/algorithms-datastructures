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
            Stack s = new FixedCapacityStack(5);
            s.push(10);
            s.push(20);
            s.push(30);
            System.Console.WriteLine(s.pop());
            System.Console.WriteLine(s.pop());
            System.Console.WriteLine(s.pop());
            System.Console.WriteLine(s.isEmpty());



        }
    }
}
