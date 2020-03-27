using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        {
            ResizableArray r = new ResizableArray();
            r.append(20);
            System.Console.WriteLine("Array: " + r + "\nLength: " + r.getLength());
            r.append(30);
            System.Console.WriteLine("Array: " + r + "\nLength: " + r.getLength());

            r.append(40);
            System.Console.WriteLine("Array: " + r + "\nLength: " + r.getLength());

            r.append(50);
            System.Console.WriteLine("Array: " + r + "\nLength: " + r.getLength());

            r.pop();
            System.Console.WriteLine("Array: " + r + "\nLength: " + r.getLength());

            r.pop();
            System.Console.WriteLine("Array: " + r + "\nLength: " + r.getLength());




        }
    }
}
