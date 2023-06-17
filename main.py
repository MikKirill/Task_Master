#   This is main
'''
Класс Task:
- Атрибуты:
  - id: int - идентификатор задачи
  - title: str - заголовок задачи
  - description: str - описание задачи
  - due_date: str - дата выполнения задачи

  - Методы:
    - create_task(): создание новой задачи
    - update_task(): обновление информации о задаче
    - delete_task(): удаление задачи
    - complete_task(): отметить задачу как выполненную
    - display_task(): отображение задачи

'''
class Tasks:
    def __init__(self, id, title, description):
        self.taskId = id
        self.taskTitle = title
        self.dsc = description
        self.dateEnd = False

    def create_task(self, task):  #   Запись в БД

        with open("bd.txt", "r") as file:
            lines = file.read()

        allText = lines + '\n' + task

        with open("bd.txt", "w") as file:
            file.write(allText)

    def update_task(self, taskList, taskId, taskTitle):  #   Изменение записи
        taskList[taskId] = taskTitle

        toBd = '\n'.join([item.rstrip() for item in taskList])

        with open("bd.txt", "w") as file:
            file.write(toBd)

    def delete_task(self, taskList, taskId):  #   Удаление записи
        del taskList[taskId]

        toBd = '\n'.join([item.rstrip() for item in taskList])

        with open("bd.txt", "w") as file:
            file.write(toBd)

    def complete_task(self):#   Выполнение записи
        print("complete method")

    def display_task(self):#    Отображение записи
        with open("bd.txt", "r") as file:
            lines = file.readlines()
            print(lines)
            print(lines[0][:-1], len(lines) - 1, 'tasks')
            return(lines)

#task1 = Task(1, "test", "1st test")

def reader():
    tasks = Tasks
    allTasks = tasks.display_task(tasks)
    return(allTasks)

def newTask():
    tasks = Tasks
    task = input("Input your task:\n")
    Tasks.create_task(tasks, task)

def updateTask(taskList):
    tasks = Tasks
    toChange = int(input("What task to change?\n"))
    newText = input("What will we do with the drunken sailor?\n")
    Tasks.update_task(tasks, taskList, toChange, newText)

def delTask(taskList):
    tasks = Tasks
    toDel = int(input("What task to remove?\n"))
    Tasks.delete_task(tasks, taskList, toDel)

def resetTaskList():
    with open("bd.txt", "w") as file:
        file.write("You have ")

def navigation():
    allTasks = reader()
    vib = input('\nChose fun:\n'
                '1.\tNew task\n'
                '2.\tChange task\n'
                '3.\tDel task\n'
                '0.\tReset system\n'
                '00.\tSkip\n')

    if vib == '1':
        newTask()
    elif vib == '2':
        updateTask(allTasks)
    elif vib == '3':
        delTask(allTasks)
    elif vib == '0':
        resetTaskList()
    elif vib == '00':
        return(0)
    print("Ready")


navigation()

'''
Класс Idea:
- Атрибуты:
  - id: int - идентификатор идеи
  - title: str - заголовок идеи
  - description: str - описание идеи

  - Методы:
    - create_idea(): создание новой идеи
    - update_idea(): обновление информации о идее
    - delete_idea(): удаление идеи
'''

'''
Класс Birthday:
- Атрибуты:
  - id: int - идентификатор дня рождения
  - name: str - имя человека, у которого день рождения
  - date: str - дата дня рождения

  - Методы:
    - create_birthday(): создание нового дня рождения
    - update_birthday(): обновление информации о дне рождения
    - delete_birthday(): удаление дня рождения
'''

'''
Класс TodoApp:
- Атрибуты:
  - tasks: list - список задач
  - ideas: list - список идей
  - birthdays: list - список дней рождения

  - Методы:
    - add_task(): добавление новой задачи в список
    - add_idea(): добавление новой идеи в список
    - add_birthday(): добавление нового дня рождения в список
    - get_all_tasks(): получение списка всех задач
    - get_all_ideas(): получение списка всех идей
    - get_all_birthdays(): получение списка всех дней рождения
'''

