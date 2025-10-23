# File: lib/todo_list.py

class TodoList:
    def __init__(self):
        self._tasks = []

    def add(self, todo):
        self._tasks.append(todo)

    def all(self):
        return self._tasks
    
    def incomplete(self):
        
        if False in self._tasks:
            return self._tasks
        else:
            print("skejdbhjebeu")

    def complete(self):
        if True in self._tasks:
            return self._tasks
        return
        

    def give_up(self):
        if False in self._tasks:
            self._tasks = self._tasks
        elif True in self._tasks:
            return
        else:
            return "There Are No Tasks In Your Todo List"
        pass