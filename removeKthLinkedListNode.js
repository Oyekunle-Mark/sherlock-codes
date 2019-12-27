/*
 * Complete the 'removeKthLinkedListNode' function below.
 *
 * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
 * The function accepts following parameters:
 *  1. INTEGER_SINGLY_LINKED_LIST head
 *  2. INTEGER k
 *
 * * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function removeKthLinkedListNode(head, k) {
  // initialize the length to zero
  let len = 0;
  // set node to the head
  let node = head;
  // nodeArray will hold the nodes in the linked list
  let nodeArray = [];

  // first find the nodes in the linked list
  // push each node to the nodeArray as you visit each
  while (node !== null) {
    // push the current node to the nodeArray
    nodeArray.push(node);
    // set node to the next
    node = node.next;
    // increment length
    len++;
  }

  // if k is greater than length
  if (k > len) {
    // return the linked list unchanged
    return head;
  }

  // WHERE: node marked for deletion if indexed "len - k"

  // if the kth node from the tail is the current head
  // i.e, if the node to be removed is the current head
  if (len - k === 0) {
    // return the next node as the head
    return nodeArray[len - k + 1];
  }

  // otherwise, remove the kth node from the tail
  // set the node before the marked node to point to
  // the node after the marked node
  nodeArray[len - k - 1].next = nodeArray[len - k + 1];

  // return the head of nodeArray
  return nodeArray[0];
}
