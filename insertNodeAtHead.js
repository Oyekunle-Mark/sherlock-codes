function insertNodeAtHead(head, data) {
  if (!head) {
    return new SinglyLinkedListNode(data);
  }

  const newHead = new SinglyLinkedListNode(data);

  newHead.next = head;

  return newHead;
}