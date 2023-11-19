todo_amount = int(input("how many todos would you like to add today? "))

todos = []

for i in range(1, todo_amount+1):
    todo_text = input("todo #{}: ".format(i))
    todos.append(todo_text)

while not all(i == 'done' for i in todos):
    for i in range(len(todos)):
        print(f"#{i+1} {todos[i]}")

    finished_todo_index = int(input("enter a todo by numberto check it off: "))-1

    todos[finished_todo_index] = "done"

for i in range(len(todos)):
    print(f"#{i+1} {todos[i]}")
print('you have completed all of your todos for today')