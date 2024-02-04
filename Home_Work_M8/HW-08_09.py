from collections import deque

MAX_LEN = 4

lifo = deque(maxlen=MAX_LEN)
result = []

def push(element):
    print(element)
    result = lifo.appendleft(element)
    print(result)
    
def pop():
    result = lifo.popleft()

    return result