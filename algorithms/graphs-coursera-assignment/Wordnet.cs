using System;
using System.Collections.Generic;
using System.IO;
public class WordNet
{
    HashSet<String> nouns = new HashSet<string>();
    public WordNet(String synsets, String hypernyms)
    {
        addAllNouns(synsets);


    }
    private void addAllNouns(String synsets)
    {
        char[] lineseperators = new char[] { ',' };
        char[] nounseperators = new char[] {' '};
        using (StreamReader synsetsFile = File.OpenText(synsets))
        {
            String line;

            while ((line = synsetsFile.ReadLine()) != null)
            {
                String nouns = line.Split(lineseperators, StringSplitOptions.None)[1];
                String[] nounsSplit = nouns.Split(nounseperators, StringSplitOptions.None);

                for (int x=0; x<nounsSplit.Length; x++) {
                    this.nouns.Add(nounsSplit[x]);
                }
                
            }
        }
    }

    public HashSet<String> getNouns() {
        return nouns;
    }
    public Boolean isNoun(String word) {
        return nouns.Contains(word);
    }
}