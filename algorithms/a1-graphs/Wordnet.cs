using System;

public class WordNet  {
    public WordNet(String synsets, String hypernyms);

    public Iterable<String> nouns();

    public Boolean isNoun(String word);

    public int distance(String nounA, String nounB);

    public String sap(String nounA, String nounB);

}