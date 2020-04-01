using System;
interface PriorityQueue {
    public void enqueue(int item);
    public void dequeue_max();
    public int get_max();

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

