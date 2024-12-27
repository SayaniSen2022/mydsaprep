class ListNode<T> {
    val: T;
    next: ListNode<T> | null;

    constructor(val: T) {
        this.val = val;
        this.next = null;
    }
}

class LinkList<T> {
    head: ListNode<T> | null;
    size: number;

    constructor() {
        this.head = null;
        this.size = 0;
    }

    insertAtHead(val: T): void {
        const node = new ListNode(val);

        node.next = this.head;
        this.head = node;
        this.size++;
    }

    insertAtTail(val: T): void {
        const node = new ListNode(val);
        
        if (this.head === null) {
            this.head = node;
            this.size++;
            return;
        }

        let curr: ListNode<T> = this.head;
        while (curr.next) {
            curr = curr.next;
        }

        curr.next = node;
        this.size++;
    }

    insertAtIndex(val: T, index: number): void {
        // Validate index
        if (index < 0 || index > this.size) {
            return;
        }

        // If inserting at the head
        if (index === 0) {
            this.insertAtHead(val);
            return;
        }

        const node = new ListNode(val);
        let curr: ListNode<T> | null = this.head;
        let count = 0;

        // Traverse to the node before the insertion point
        while (curr && count < index - 1) {
            curr = curr.next;
            count++;
        }

        if (!curr) return;

        node.next = curr.next;
        curr.next = node;
        this.size++;
    }

    printList(): void {
        let curr = this.head;
        while (curr) {
            console.log(curr.val);
            curr = curr.next;
        }
    }
}

// Example usage
const List1 = new LinkList<number>();

List1.insertAtHead(5);
List1.insertAtHead(55);
List1.insertAtHead(555);
List1.insertAtHead(5555);
List1.insertAtTail(100);
List1.insertAtIndex(2, 3);
List1.printList();