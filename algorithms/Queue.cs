using System;
public class Queue {
    BackLinkedList items = new BackLinkedList();

    public void enqueue(object item) {
        items.add(item);
    }

    public Object dequeue() {
        Node n = items.pop();

        if (n != null) {
            return n.item;
        }

        return null;
    }

    public override String ToString()  {
        return items.ToString();
    }
}