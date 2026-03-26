if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        command_parts = input().split()
        cmd = command_parts[0]
        args = command_parts[1:]
        if cmd == "insert":
            my_list.insert(int(args[0]), int(args[1]))
        elif cmd == "print":
            print(my_list)
        elif cmd == "remove":
            my_list.remove(int(args[0]))
        elif cmd == "append":
            my_list.append(int(args[0]))
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "pop":
            my_list.pop()
        elif cmd == "reverse":
            my_list.reverse()
