/*
 * Complete the 'removeKthLinkedListNode' function below.
 *
 * The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
 * The function accepts following parameters:
 *  1. INTEGER_SINGLY_LINKED_LIST head
 *  2. INTEGER k
 */

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */

function removeKthLinkedListNode(head, k) {
    let len = 0
    let node = head
    let nodeArray = []

    while (node !== null) {
        len++
        nodeArray.push(node)
        node =node.next
    }

    if (k > len) {
        return head
    }

    if (len - k === 0) {
        return nodeArray[len - k + 1]
    }

    nodeArray[len - k - 1].next = nodeArray[len - k + 1]

    return nodeArray[0]
}