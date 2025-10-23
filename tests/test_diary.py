from lib.diary import Todo
from lib.diary import TodoList

# A task can be set into the todo list
todolist = TodoList()
task = Todo("Kill John Lennon", False)
todolist.add(task)
assert task == {"Kill John Lennon", False}