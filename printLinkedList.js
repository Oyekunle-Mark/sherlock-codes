function printLinkedList(head) {
  let node = head;

  while (node !== null) {
    console.log(node.data);
    node = node.next;
  }
}
