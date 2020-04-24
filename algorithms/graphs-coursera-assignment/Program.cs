using System;

namespace graphs_coursera_assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            WordNet wn = new WordNet("synsets.txt","hypernym.txt");

            System.Console.WriteLine(wn.isNoun("Computer"));

        }
    }
}
