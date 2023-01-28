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

    

if __name__ == "__main__":
    main()
