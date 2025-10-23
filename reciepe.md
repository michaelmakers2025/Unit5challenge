# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem 

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So I want to  have a todo list
I want to add todos so i know what i need todo

As a user
So I can know what needs to be done in todos
I want to be able to see todos that are incomplete

As a user
So I can know what needs to be done in todos
I want to be able to see todos that are complete

As a user
when i give up or have completed all my todos in one swoop
I want to be able to mark all the todos as complete


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

# Real

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
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


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
        # Returns:
        # Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python


# Real 
"""
A task can be set
"""

task = Todo()
assert task == {}


"""
A task can be set into the 'Todo list"
"""
todolist = Todolist()
task = Todo("Wash the Dishes", False)
todolist.append(task)
assert todolist == {task}

"""
Multiple tasks can be set into the 'Todo list"
"""
todolist = Todolist()
task = Todo("Wash the Dishes", False)
task2 = Todo("Eat Your Food", False)
todolist.append(task)
todolist.append(task2)
assert todolist == {task, task2}

"""
Given a task is complete i can mark it as such 
"""

task = Todo("Wash the Dishes", False)
task.mark_complete()
assert task == {"Wash the Dishes", True}



"""
Given a task is already complete i can mark it to complete
it will return message "This Task is Already Complete"
"""

task = Todo("Wash the Dishes", False)
task.mark_complete()
# raise exception thing?? or just if statement?
assert message == "This Task is Already Complete"


"""
Given a request a list of incomplete todo tasks
 is produced
"""

todolist = Todolist()
task = Todo("Wash the Dishes", False)
task2 = Todo("Eat Your Food", False)
todolist.append(task)
todolist.append(task2)
assert incomplete(todolist) == {"Wash the Dishes": False, "Eat Your Food": False }

"""
Given a request a list of complete todo tasks
 is produced
"""

todolist = Todolist()
task = Todo("Wash the Dishes", False)
task2 = Todo("Eat Your Food", False)
todolist.append(task)
todolist.append(task2)
task.mark_complete
task2.mark_complete
assert complete(todolist) == {"Wash the Dishes": True, "Eat Your Food": True }

"""
Given a request a list of incomplete and complete todo tasks
 is produced
"""

todolist = Todolist()
task = Todo("Wash the Dishes", False)
task2 = Todo("Eat Your Food", False)
task3 = Todo("Drink the Water", False)
task4 = Todo("Put Away Dry Dishes", False)
task5 = Todo("Smell your Shower Gel", False)
task6 = Todo("Rob the Bank", False)
todolist.append(task)
todolist.append(task2)
todolist.append(task3)
todolist.append(task4)
todolist.append(task5)
todolist.append(task6)
task.mark_complete
task2.mark_complete
task5.mark_complete
task6.mark_complete
assert complete(todolist) == {"Wash the Dishes": True, "Eat Your Food": True, "Smell your Shower Gel": True, "Rob the Bank": True}

assert incomplete(todolist) == {"Drink the Water": False, "Put Away Dry Dishes": False}

"""
Given a request all tasks on the todo list are marked
as complete
"""

todolist = Todolist()
task = Todo("Wash the Dishes", False)
task2 = Todo("Eat Your Food", False)

todolist.giveup()

assert todolist == {"Wash the Dishes": True, "Eat Your Food": True}


"""
Given a request all tasks on the todo list are marked
as complete and those aleary complete will stay as such
"""

todolist = Todolist()
task = Todo("Wash the Dishes", False)
task2 = Todo("Eat Your Food", False)
task3 = Todo("Eat Your Gravy", False)

todolist.giveup()

assert todolist == {"Wash the Dishes": True, "Eat Your Food": True, "Eat Your Gravy": True}

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
