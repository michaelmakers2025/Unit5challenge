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


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):


        self.todoli
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
