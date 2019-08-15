function insertNodeAtTail(head, data) {
  if (!head) {
    return new SinglyLinkedListNode(data);
  }

  let node = head;

  while (node.next) {
    node = node.next;
  }

  node.next = new SinglyLinkedListNode(data);

  return head;
}
