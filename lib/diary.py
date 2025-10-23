# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        not_done_list = ??.appened(not_done)
        return list(not_done_list)
        

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete

        done_list = ??.appened(done)
        return list(done_list)
        

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete

        for False in self.task:
            if False not in self.task:
                return
            else:
                self.task.mark_complete()
