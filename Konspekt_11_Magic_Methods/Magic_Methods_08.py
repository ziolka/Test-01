class Session:
    def __init__(self, addr, port=8080):
        self.connected = True
        self.addr = addr
        self.port = port

    def __enter__(self):
        print(f'Connected to {self.addr}:{self.port}')
        return self
    
    def __exit__(self, exception_type, exception_value, traceback):
        self.connected = False
        if exception_type is not None:
            print("Some error!")
        else:
            print("No problem")

local_host_session = Session('localhost')

with local_host_session as session:
    print(session is local_host_session)
    print(local_host_session.connected)

print(local_host_session.connected)