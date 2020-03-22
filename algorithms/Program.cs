using System;

namespace algorithms
{
   class InefficientUnionFind {
       int[]ids;
       public InefficientUnionFind(int n) {
           this.ids = new int[n];

           for (int x=0; x<n;x++) {
               this.ids[x] = x;
           }
       }

       public Boolean connected(int p1, int p2){
           return this.ids[p1] == this.ids[p2];
       }

       public void union(int p1, int p2){
           int id1 = this.ids[p1];
           int id2 = this.ids[p2];

           for (int x=0; x<this.ids.Length; x++) {
               if (this.ids[x] == id1) {
                   this.ids[x] = id2;
               }
           }

       }

       
   }
}
