using System;

interface Stack {
    public void push(Object item);
    public Object pop();
    public Boolean isEmpty();

}

public class LinkedStack : Stack {
    private LinkedList items = new LinkedList();
    public void push(Object item){ 
        this.items.add(item);
    }

    public Object pop() {
        return items.pop();
    }

    public Boolean isEmpty() {
        return items.isEmpty();
    }

}