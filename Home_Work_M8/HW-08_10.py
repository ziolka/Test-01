from collections import deque

MAX_LEN = 3

fifo = deque(maxlen=MAX_LEN)
result = []

def push(element):
    print(f'Push: {element}')
    result = fifo.append(element)
    print(f'Result: {result}')


def pop():
    result = fifo.popleft()
    print(f'Pop: {result}')
    return result