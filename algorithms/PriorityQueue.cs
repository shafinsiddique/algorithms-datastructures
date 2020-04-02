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
                string_rep += heap[x] += " ";
            }
        }

        return string_rep;
    }


    
}
