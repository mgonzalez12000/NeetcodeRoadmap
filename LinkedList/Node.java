/* The following is an implementation of a node/LinkedList class.
 * A linkedlist is a datastructure that allows the collection of value
 * Each value is inserted into a box of a linkedlist. Aka a node of a linkedlist
 * Every node has TWO parts. The DATA anda POINTER to the next node in the LL
 */

package LinkedList;

public class Node{
    // fields of the box class
    int data; // data will return the value of given node in a linkedlist eg: head.data
    Node next; // will point to the next node in the given linkedlist eg: head.next
              // if you want to get the value of the next node in the linkedlist you can do head.next.data
    // define a constructor for the class
    Node(int data){
        this.data = data;
    }

    void Linkedlist (){
        // in order to populate our linkedlist in a way such that it reflects:
        // 6 -> 3 -> 4 -> 4 -> 2 -> 1
        // we need to instantiate our Node class
        Node nodeA = new Node(6);
        Node nodeB = new Node(3);
        Node nodeC = new Node(4);
        Node nodeD = new Node(2);
        Node nodeE = new Node(1);

        nodeA.next = nodeB;
        nodeB.next = nodeC;
        nodeC.next = nodeD;
        nodeD.next = nodeE;
    }
}

/* Knowledge to know abotu Linkedlist
 * A LinkedList data structure can ve really expensive becuase when comparing
 * because a LL is a "chain". Comparing it to an array, if you want to grav an
 * elemenet, an array automatically points to it's index. However, whith a LL
 * it HAS to go through the entire chain to retrieve such data
 */




