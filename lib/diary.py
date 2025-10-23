# File: lib/todo_list.py

class TodoList:
    def __init__(self):
        self._tasks = []

    def add(self, todo):
        self._tasks.append(todo)

    def all(self):
        return self._tasks
    
    def incomplete(self):

        return [task for task in self._tasks if not task.status]
    
    def complete(self):

        return [task for task in self._tasks if task.status]

        

    def give_up(self):
        if False in self._tasks:
            self._tasks = self._tasks
        elif True in self._tasks:
            return
        else:
            return "There Are No Tasks In Your Todo List"
        pass