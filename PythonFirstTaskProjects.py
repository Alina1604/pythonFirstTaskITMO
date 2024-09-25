class ToDoList:
    def __init__(self):
        self.tasks = {}  
        self.task_id = 1 

    def add_task(self, description):
        """Добавить новую задачу с описанием и статусом 'Не начата'."""
        self.tasks[self.task_id] = {'description': description, 'status': 'Не начата'}
        print(f"Задача '{description}' добавлена с ID: {self.task_id}")
        self.task_id += 1

    def remove_task(self, task_id):
        """Удалить задачу по её идентификатору."""
        if task_id in self.tasks:
            removed_task = self.tasks.pop(task_id)
            print(f"Задача '{removed_task['description']}' с ID: {task_id} удалена.")
        else:
            print(f"Задача с ID: {task_id} не найдена.")

    def update_status(self, task_id, status):
        """Изменить статус задачи на один из допустимых."""
        if task_id in self.tasks:
            if status in ["Не начата", "В процессе", "Завершена"]:
                self.tasks[task_id]['status'] = status
                print(f"Статус задачи ID: {task_id} обновлён на '{status}'.")
            else:
                print("Недопустимый статус. Доступные статусы: 'Не начата', 'В процессе', 'Завершена'.")
        else:
            print(f"Задача с ID: {task_id} не найдена.")

    def view_tasks(self):
        """Вывести список всех задач с их статусами."""
        if not self.tasks:
            print("Список задач пуст.")
        else:
            print("Текущие задачи:")
            for task_id, task_info in self.tasks.items():
                print(f"ID: {task_id}, Описание: '{task_info['description']}', Статус: {task_info['status']}")
                
if __name__ == "__main__":
    todo_list = ToDoList()

    todo_list.add_task("Написать отчёт")
    todo_list.add_task("Сделать презентацию")
    todo_list.add_task("Подготовиться к встрече")

    todo_list.update_status(2, "В процессе")

    todo_list.remove_task(3)

    todo_list.view_tasks()