using System;

public class LinkedList {
    Node first;
    private class Node {
        public Object item;
        public Node next;
        public Node(Object item) {
            this.item = item;
            this.next = null;
        }

        public override String ToString() {
            return this.item.ToString();
        }
    }

    public LinkedList() {
        this.first = null;
    }

    public Boolean isEmpty() {
        return this.first == null;
    }
    public void add(Object item) {
        Node new_node = new Node(item);
        new_node.next = this.first;
        this.first = new_node;
    }

    public Object pop()  {
        if (this.first != null) {
            Node first;
            first = this.first;
            this.first = this.first.next;

            return first;
        }
        return null;
    }

    public void append(Object item){ 
        Node new_node = new Node(item);
        if (isEmpty()) {
            this.first = new_node;
        }

        else { 
            Node curr = this.first;

            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = new_node;
        }
    }

    public override String ToString() {
        String string_rep = "";
        Node curr = this.first;

        while (curr != null) {
            string_rep += curr.item + " ";

            curr = curr.next;
        }

        return string_rep;
    }








}