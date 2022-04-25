class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

class Queue:

    def __init__(self):
        self.queue = []

    def __repr__(self):
        return f'Queue: {self.queue}'

    def enqueue(self, person):
        self.queue.append(person)

    def dequeue(self):
        return self.queue.pop(0)

class Game(Person, Queue):

    def run():
        x = input('what is the first name? ')
        y = input('what is the last name? ')
        person = Person(x, y)

        Queue.enqueue(person)


# Game.run()



