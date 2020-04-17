// using System;

// public interface SymbolTable {
//     public void insert(String key, Object value);
//     public Object get(String key); 
// }

// public class LinkedListSymbolTable : SymbolTable {
//     private class Node {
//         public String key;
//         public Object value;
//         public Node next;

//         public Node(String key, Object value) {
//             this.key = key;
//             this.value = value;
//             this.next = null;
//         }

//         public void setNext(Node next) {
//             this.next = next;
//         }

//     }

//     Node head;

//     public LinkedListSymbolTable() {
//         this.head= null;
//     }

//     public Object get(String key) {
//         Node curr = this.head;

//         while (curr != null) {
//             if (curr.key == key){
//                 return curr.value;
//             }
//             curr = curr.next;
//         }

//         return null;
//     }

//     private void replace(String key, Object value) {
//         Node curr = this.head;

//         while (curr != null) {
//             if (curr.key == key) {
//                 curr.value = value;
//                 break;
//             }

//             curr = curr.next;
//         }
//     }
//     public void insert(String key, Object value) {
//         if (search(key)!= null) {
//             replace(key, value);
//         }

//         else {
//             Node n = new Node(key, value);
//             n.next = this.head;
//             this.head = n;
//         }
//     }

//     public override String ToString() {
//         String string_rep = "";
//         Node curr = this.head;

//         while (curr != null) {
//             string_rep += "(" + curr.key + ", " + curr.value + ") ";
//             curr = curr.next; 
//         }

//         return string_rep;

//     }


// }