import threading
import time 

def thread(thread_id) -> None:
    elapsed_time = 0
    while(thread_state[thread_id-1]):
         print(f'** thread {thread_id} is running at {elapsed_time}')
         time.sleep(5)
         elapsed_time += 5

if __name__ == '__main__':
    # thread states for t1, t2 and t3
    thread_state = [True] * 3
    # starting thread 1
    thread_state[0] = True
    t1 = threading.Thread(target=thread, daemon=True, args=(1,))
    t1.start()
    # starting thread 3
    thread_state[2] = True
    t3 = threading.Thread(target=thread, daemon=True, args=(3,))
    t3.start()
    # waiting for 20 seconnds and stopping thread 1
    time.sleep(20)
    thread_state[0] = False
    # starting thread 2
    thread_state[1] = True
    t2 = threading.Thread(target=thread, daemon=True, args=(2,))
    t2.start()
    # waiting for 18 seconnds and stopping thread 3
    time.sleep(18)
    thread_state[2] = False
    # restarting thread 1
    thread_state[0] = True
    t1 = threading.Thread(target=thread, daemon=True, args=(1,))
    t1.start()
