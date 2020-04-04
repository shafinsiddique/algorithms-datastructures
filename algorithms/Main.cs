using System;
namespace algorithms
{
    class Program
    {
        static void Main(string[] args)
        { 
            SymbolTable s = new LinkedListSymbolTable();
            s.insert("Hello",1);
            s.insert("Hello",4);
            System.Console.WriteLine(s);

        }
    }
}



