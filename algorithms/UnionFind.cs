using System;

namespace algorithms
{
    interface UnionFind
    {
        public Boolean connected(int p1, int p2);
        public void union(int p1, int p2);
    }
    class QuickFind : UnionFind
    {
        int[] ids;
        public QuickFind(int n)
        {
            this.ids = new int[n];

            for (int x = 0; x < n; x++)
            {
                this.ids[x] = x;
            }
        }

        public Boolean connected(int p1, int p2)
        {
            return this.ids[p1] == this.ids[p2];
        }

        public void union(int p1, int p2)
        {
            int id1 = this.ids[p1];
            int id2 = this.ids[p2];

            for (int x = 0; x < this.ids.Length; x++)
            {
                if (this.ids[x] == id1)
                {
                    this.ids[x] = id2;
                }
            }
        }
    }
    class QuickUnion : UnionFind
    {
        int[] ids;

        public QuickUnion(int n) : base()
        {
            this.ids = new int[n];
            for (int x = 0; x < this.ids.Length; x++)
            {
                this.ids[x] = x;
            }
        }
        public Boolean connected(int p1, int p2)
        {
            return root(p1) == root(p2);
        }

        public void union(int p1, int p2)
        {
            this.ids[root(p1)] = root(p2);
        }

        protected int root(int p)
        {
            if (ids[p] == p)
            {
                return p;
            }
            ids[p] = ids[ids[p]];
            return root(ids[p]);


        }
    }

    class WeightedQuickUnion : QuickUnion
    {
        int[] ids;
        int[] sizes;
        public WeightedQuickUnion(int n) : base(n)
        {
            ids = new int[n];
            sizes = new int[n];
            for (int x = 0; x < n; x++)
            {
                ids[x] = x;
                sizes[x] = 1;
            }

        }
        public new void union(int p1, int p2)
        {
            int root1 = root(p1);
            int root2 = root(p2);

            if (root1 != root2)
            {
                if (sizes[root1] < sizes[root2])
                {
                    ids[root1] = ids[root2];
                    sizes[root2] += sizes[root1];
                }

                else
                {
                    ids[root2] = ids[root1];
                    sizes[root1] += sizes[root2];
                }
            }

        }
    }
}
