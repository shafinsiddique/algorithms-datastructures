using System;

namespace graphs_coursera_assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            WordNet wn = new WordNet("synsets.txt","hypernym.txt");

            foreach (String noun in wn.getNouns()) {
                System.Console.WriteLine(noun);
            }

        }
    }
}
