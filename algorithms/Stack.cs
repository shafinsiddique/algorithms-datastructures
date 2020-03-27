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

public class FixedCapacityStack : Stack {
    private Object [] items;
    int current = 0;

    public FixedCapacityStack(int capacity) {
        items = new Object[capacity];
    }

    public void push(Object item) {
        if (current < items.Length) {
            items[current] = item;
            current += 1;
        }

    }

    public Object pop() {
        if (!isEmpty()) {
            Object temp = items[current-1];
            current -= 1;
            return temp;
        }
        return null;
    }

    public Boolean isEmpty(){
        return current <= 0;
    }
}