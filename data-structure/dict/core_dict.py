import multiprocessing
import time

# Process class
class Process(multiprocessing.Process):
	def __init__(self, id):
		super(Process, self).__init__()
		self.id = id

	def run(self):
		time.sleep(1)
		print("I'm the process with id: {}".format(self.id))


if __name__ == '__main__':
    while True:
        p = Process(0)

        # Create a new process and invoke the
        # Process.run() method
        p.start()

        # Process.join() to wait for task completion.
        p.join()
        p = Process(1)
        p.start()
        p.join()
