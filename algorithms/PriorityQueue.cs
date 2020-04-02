using System;
using System.Collections;
interface PriorityQueue {
    // public void enqueue(int item);
    // public void dequeue_max();
    // public int get_max();

}
public class ArrayPriorityQueue: PriorityQueue {
    LinkedList priorityLinky = new LinkedList();
    public void enqueue(int item) {
        priorityLinky.add(item);

    }

    public void dequeue_max() {
        priorityLinky.deleteOccurences(get_max());

    }

    public int get_max() {
        return priorityLinky.getMax();
    }

    public override String ToString() {
        return priorityLinky.ToString();

    } 
}

public class BinaryHeap : PriorityQueue  {
    ArrayList heap = new ArrayList();
        public BinaryHeap() {
        this.heap.Add(-1);
    }

    public void enqueue(int item) {
        this.heap.Add(item);
        if (this.heap.Count > 1) {
            swim(this.heap.Count-1);
        }
    }

    private void swim(int cur_position) {
        int temp = (int) this.heap[cur_position/2];
        if (cur_position > 1 && temp < (int) this.heap[cur_position]){ 
            this.heap[cur_position/2] = (int) this.heap[cur_position];
            this.heap[cur_position] = temp;
            swim(cur_position/2);
        }
    }

    public override String ToString() {
        String string_rep = "";

        for (int x=0; x<heap.Count; x++) {
            if (x > 0) {
                string_rep += heap[x] + " ";
            }
        }

        return string_rep;
    }

    public void sink(int cur_position) {
        if (cur_position*2 < this.heap.Count) {
            int left_child = (int) this.heap[cur_position];
            int right_child = (int) this.heap[(cur_position*2) + 1];
            int parent = (int) this.heap[cur_position];
            
            if (parent < left_child || parent < right_child) {
                if (left_child > right_child) {
                    this.heap[cur_position*2] = parent;
                    this.heap[cur_position] = left_child;
                    sink(cur_position*2);
                }
                else {
                    this.heap[(cur_position*2)+1] = parent;
                    this.heap[cur_position] = right_child;
                    sink((cur_position*2)+1);
                }
            }
        }
    }

    public int del_max() {
        if (this.heap.Count > 1) {
            int max = (int) this.heap[1];
            int last_leaf = (int) this.heap[this.heap.Count-1];
            this.heap.RemoveAt(this.heap.Count-1);
            this.heap[1] = last_leaf;
            sink(1);
            return max;
        }

        return 0;
    }
    
}
