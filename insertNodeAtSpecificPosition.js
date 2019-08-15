function insertNodeAtPosition(head, data, position) {
  let node = head;

  for (let i = 0; i < position - 1; i++) node = node.next;

  const next = node.next;
  const newNode = new SinglyLinkedListNode(data);
  node.next = newNode;
  newNode.next = next;

  return head;
}
