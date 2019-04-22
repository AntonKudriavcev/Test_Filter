from queue      import Queue 

import filterr

FIFO_memory      = 128

q = Queue(FIFO_memory)

def put_to_queue(value):
	if q.full():
		filterr.send_to_filter(q.get())
	q.put(value)
def clear_buf():
	filterr.del_points()
	q.queue.clear()

