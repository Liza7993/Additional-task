deque = []
work = True

def push_front(deque, x):
    deque.insert(0, x)
    print('ok')

def push_back(deque, x):
    deque.append(x)
    print('ok')

def pop_front(deque):
    if deque:
        print(deque.pop(0))
    else:
        print('error')

def pop_back(deque):
    if deque:
        print(deque.pop())
    else:
        print('error')

def front(deque):
    if deque:
        print(deque[0])
    else:
        print('error')

def back(deque):
    if deque:
        print(deque[-1])
    else:
        print('error')

def size(deque):
    print(len(deque))

def clear(deque):
    deque.clear()
    print('ok')

def find(deque, x):
    if x in deque:
        print(f'{x} found in deque')
    else:
        print(f'{x} not found in deque')

def exit():
    global work
    work = False
    print('bye')

while work:
    command_get = input()

    if 'push_front' in command_get:
        push_front(deque, int(command_get.split()[1]))
    elif 'push_back' in command_get:
        push_back(deque, int(command_get.split()[1]))
    elif 'pop_front' in command_get:
        pop_front(deque)
    elif 'pop_back' in command_get:
        pop_back(deque)
    elif 'front' in command_get:
        front(deque)
    elif 'back' in command_get:
        back(deque)
    elif 'size' in command_get:
        size(deque)
    elif 'clear' in command_get:
        clear(deque)
    elif 'find' in command_get:
        find(deque, int(command_get.split()[1]))
    elif 'exit' in command_get:
        exit()