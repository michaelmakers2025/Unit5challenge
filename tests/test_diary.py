from lib.todo import Todo
from lib.diary import TodoList

# This is known as an integration test as Its not just
# testing one class it is testing both of them similtanio-
# usly as there is no other way for implementation



# A task can be set into the todo list
todolist = TodoList()
task = Todo("Kill John Lennon", False)
todolist.add(task)
assert task == {"Kill John Lennon", False}