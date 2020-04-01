using System;
using System.Collections;
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

public class MaxStack : Stack {
    ArrayList stack = new ArrayList();
    ArrayList max_with_state = new ArrayList();

    public void push(Object item) {
        stack.Add(item);
        if ((int)item > (int)max_with_state[max_with_state.Count-1]) {
            max_with_state.Add((int)item);
        }

        else {
            max_with_state.Add(max_with_state[max_with_state.Count-1]);
        }
    }
    public Boolean isEmpty(){ 
        return stack.Count == 0;
    }
    public Object pop() {
        if (!isEmpty()) {
            int item = (int)stack[stack.Count-1];
            stack.RemoveAt(stack.Count-1);
            max_with_state.RemoveAt(max_with_state.Count-1);

            return item;
        }
        return null;
    }

    public int max() {
        return (int) max_with_state[max_with_state.Count-1];
    }
}