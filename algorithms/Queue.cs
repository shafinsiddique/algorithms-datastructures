using System;
public class Queue
{
    BackLinkedList items = new BackLinkedList();

    public void enqueue(object item)
    {
        items.add(item);
    }

    public Boolean isEmpty()
    {
        return items.isEmpty();
    }

    public Object dequeue()
    {
        Node n = items.pop();

        if (n != null)
        {
            return n.item;
        }

        return null;
    }

    public override String ToString()
    {
        return items.ToString();
    }
}

public class TwoStackQueue
{
    Stack inbox = new LinkedStack();
    Stack outbox = new LinkedStack();

    public void enqueue(Object item)
    {
        this.inbox.push(item);
    }

    public Object pop()
    {
        if (outbox.isEmpty())
        {
            while (!inbox.isEmpty())
            {
                outbox.push(inbox.pop());
            }

            if (outbox.isEmpty())
            {
                return null;

            }

            return outbox.pop();
        }

        return outbox.pop();
    }

}


