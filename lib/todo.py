
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

        self.todo = task
        self.status = False
        pass

    def mark_complete(self):

        if self.status == False:
            self.status = True
        return

        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
