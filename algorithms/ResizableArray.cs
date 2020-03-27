using System;

public class ResizableArray {
    Object[]array = new Object[1];
    int items = 0;


    public void append(Object item) {
        array[items++] = item;
        if (items == array.Length) {
            resize(array.Length*2);
        }
    }
    private void resize(int capacity) {
        Object[] temp = new Object[capacity];
        for (int x=0; x<items; x++)  {
            temp[x] = array[x];
        }

        this.array = temp;

    }
    public Object pop() {
        if (items > 0) {
            Object temp = this.array[items-1];
            this.array[items-1] = null;
            items--;

            if (items > 0 && items == array.Length/4){ 
                resize(array.Length/2);
            }

            return temp;
        }
        return null;
    }

    public int getLength(){
        return array.Length;
    }

    public override String ToString() {
        String string_rep = "";

        for (int x=0;x<items;x++) {
            string_rep += array[x] + " ";
        }

        return string_rep;
    }


}