import threading

class TestMessager(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            
im1 = TestMessager(name = 'Send out messages')
im2 = TestMessager(name = 'Receive messages')
im1.start()
im2.start()