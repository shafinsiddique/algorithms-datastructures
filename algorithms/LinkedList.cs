using System;

public class Node
{
    public Object item;
    public Node next;
    public Node(Object item)
    {
        this.item = item;
        this.next = null;
    }

    public override String ToString()
    {
        return this.item.ToString();
    }
}
public class LinkedList
{
    Node first;


    public LinkedList()
    {
        this.first = null;
    }

    public Boolean isEmpty()
    {
        return this.first == null;
    }
    public void add(Object item)
    {
        Node new_node = new Node(item);
        new_node.next = this.first;
        this.first = new_node;
    }

    public Object pop()
    {
        if (this.first != null)
        {
            Node first;
            first = this.first;
            this.first = this.first.next;

            return first.item;
        }
        return null;
    }

    public void append(Object item)
    {
        Node new_node = new Node(item);
        if (isEmpty())
        {
            this.first = new_node;
        }

        else
        {
            Node curr = this.first;

            while (curr.next != null)
            {
                curr = curr.next;
            }
            curr.next = new_node;
        }
    }

    public override String ToString()
    {
        String string_rep = "";
        Node curr = this.first;

        while (curr != null)
        {
            string_rep += curr.item + " ";

            curr = curr.next;
        }

        return string_rep;
    }

    public int getMax()
    {
        Node curr = this.first;
        if (curr == null)
        {
            return 0;
        }

        else
        {
            int max = (int)curr.item;
            while (curr != null)
            {
                if ((int)curr.item > max)
                {
                    max = (int)curr.item;
                }
                curr = curr.next;
            }

            return max;


        }
    }

    public void deleteOccurences(int item)
    {
        Node curr = this.first;

        while (curr != null && curr.next != null)
        {
            if ((int)curr.next.item == item)
            {
                curr.next = curr.next.next;
            }

            curr = curr.next;
        }

    }



}

public class BackLinkedList
{
    Node head;
    Node tail;

    public Boolean isEmpty()
    {
        return head == null;
    }
    public void add(Object item)
    {
        Node new_node = new Node(item);
        if (head == null)
        {
            head = new_node;
            tail = head;
        }
        else
        {
            tail.next = new_node;
            tail = new_node;
        }
    }
    public Node pop()
    {
        if (head != null)
        {
            Node temp = head;
            head = head.next;
            return temp;
        }
        return null;
    }

    public override String ToString()
    {
        String string_rep = "";
        Node curr = this.head;

        while (curr != null)
        {
            string_rep += curr.item + " ";

            curr = curr.next;
        }

        return string_rep;
    }

}

