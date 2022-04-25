import queue
import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def test_queue(self):
        self.assertEqual(Queue.enqueue('loc'), 'loc')