using System;

namespace algorithms
{
    interface UnionFind {
        public Boolean connected(int p1, int p2);
        public void union(int p1, int p2);
     }
   class QuickFind : UnionFind {
       int[]ids;
       public QuickFind(int n) {
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
   class QuickUnion : UnionFind{
       int[]ids;

       public QuickUnion(int n) {
           this.ids = new int[n];
           for (int x=0; x<this.ids.Length; x++) {
               this.ids[x] = x;
           }
       }
       public Boolean connected(int p1, int p2) {
           return root(p1) == root(p2);
       }

       public void union(int p1, int p2) {
            this.ids[root(p1)] = root(p2);
       }

       private int root(int p) {
           if (ids[p] == p){ 
               return p;
           }
           return root(ids[p]);

       }


    
   }
}
