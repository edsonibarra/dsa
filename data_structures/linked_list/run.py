import random
from linkedlist import LinkedList


def main():
    linked_list = LinkedList()

    for n in range(20):
        linked_list.append(n)
    
    linked_list.print_list()

    linked_list.prepend(-1)
    linked_list.print_list()

    linked_list.prepend(-2)
    linked_list.print_list()

    linked_list.delete_by_pos(0)
    linked_list.print_list()

    linked_list.delete_by_pos(0)
    linked_list.print_list()

    linked_list.delete_by_pos(9)
    linked_list.print_list()

    linked_list.delete_by_value(0)
    linked_list.print_list()

    linked_list.delete_by_value(16)
    linked_list.print_list()

    print(f"__len__ at this point = {len(linked_list)}")

    linked_list.reverse()
    linked_list.print_list()

    linked_list.reverse()
    linked_list.print_list()

    # Test merge method

    print("\n\tTesting merge method\t\n")
    ll1 = LinkedList()
    ll2 = LinkedList()

    ll1.append(-100)
    ll1.append(100)
    ll1.append(300)
    ll1.append(400)

    ll2.append(1)
    ll2.append(234)
    ll2.append(543)
    ll2.append(5533)
    ll2.append(44000)

    ll1.print_list()
    ll2.print_list()
    
    # merge l2 into l1
    print("Merging ll2 into ll1")
    ll1.merge(ll2)
    ll1.print_list()

    # Nth to last node testing
    print("\n\tNth to last node method\t\n")
    ll1.print_list()
    ll1.print_nth_from_last(2,1)
    ll1.print_nth_from_last(1,1)
    ll1.print_nth_from_last(0,1)

if __name__ == "__main__":
    main()
