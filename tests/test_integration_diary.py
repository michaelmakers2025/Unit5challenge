from lib.todo import Todo
from lib.diary import TodoList

# This is known as an integration test as Its not just
# testing one class it is testing both of them similtanio-
# usly as there is no other way for implementation

def test_add_task_and_list_is_created():
    t_list = TodoList()
    todo = Todo("todo")
    t_list.add(todo)
    assert t_list.all() == [todo]

def test_add_multiple_tasks_and_list_is_created():
    t_list = TodoList()
    todo = Todo("todo")
    todo2 = Todo("todo list")
    t_list.add(todo)
    t_list.add(todo2)
    assert t_list.all() == [todo, todo2]

def test_a_task_can_be_marked_as_complete():
    t_list = TodoList()
    todo = Todo("todo")
    todo.mark_complete()
    assert todo.status == True

def test_multiple_task_can_be_marked_as_complete():
    t_list = TodoList()
    todo = Todo("todo")
    todo2 = Todo("todo2")
    todo3 = Todo("todo3")
    todo.mark_complete()
    todo2.mark_complete()
    todo3.mark_complete()
    assert todo.status == True
    assert todo2.status == True
    assert todo3.status == True

def test_get_todos_that_are_not_complete():
    t_list = TodoList()
    todo = Todo("todo")
    todo2 = Todo("todo2")
    todo.mark_complete()
    t_list.add(todo)
    t_list.add(todo2)
    assert t_list.incomplete() == [todo2]

def test_get_multiple_todos_that_are_not_complete():
    t_list = TodoList()
    todo = Todo("todo")
    todo2 = Todo("todo2")
    todo3 = Todo("todo3")
    todo.mark_complete()
    t_list.add(todo)
    t_list.add(todo2)
    t_list.add(todo3)
    assert t_list.incomplete() == [todo2, todo3]

def test_get_todos_that_are_complete():
    t_list = TodoList()
    todo = Todo("todo")
    todo2 = Todo("todo2")
    todo.mark_complete()
    t_list.add(todo)
    t_list.add(todo2)
    assert t_list.complete() == [todo]

def test_get_multiple_todos_that_are_complete():
    t_list = TodoList()
    todo = Todo("todo")
    todo2 = Todo("todo2")
    todo3 = Todo("todo3")
    todo2.mark_complete()
    todo3.mark_complete()
    t_list.add(todo)
    t_list.add(todo2)
    t_list.add(todo3)
    assert t_list.complete() == [todo2, todo3]
