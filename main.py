import pymysql
import telebot
from telebot import types
import config

host = config.HOST
user = config.USER
password = config.PASSWORD
database_name = config.DATABASE_NAME

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
        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        title = task
        sql = "INSERT INTO tasks (title) VALUES (%s)"

        cursor.execute(sql, (title))

        connection.commit()


#        with open("bd.txt", "r") as file:
#            lines = file.read()

#        allText = lines + '\n' + task

#        with open("bd.txt", "w") as file:
#            file.write(allText)


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

        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)

        cursor = connection.cursor()

        # Выполните SQL-запрос для получения всех данных из таблицы
        query = "SELECT * FROM tasks;"
        cursor.execute(query)

        # Получите все строки данных из результата запроса
        rows = list(cursor.fetchall())

        return rows

#        with open("bd.txt", "r") as file:
#            lines = file.readlines()
#            print(lines)
#            print(lines[0][:-1], len(lines) - 1, 'tasks')
#            return(lines)

#task1 = Task(1, "test", "1st test")

def reader():
    tasks = Tasks
    allTasks = tasks.display_task(tasks)
    return(allTasks)

def newTask(task):
    tasks = Tasks
    #task = input("Input your task:\n")
    Tasks.create_task(tasks, task)

def updateTask(taskList):
    tasks = Tasks
    toChange = int(input("What task to change?\n"))
    newText = input("What will we do with the drunken sailor?\n")
    Tasks.update_task(tasks, taskList, toChange, newText)

def delTask(toDel):
    task_count, all_tsk = read_norm()
    tsk_del = all_tsk[toDel - 1]

    connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
    cursor = connection.cursor()

    sql = "DELETE FROM tasks WHERE title = %s"

    cursor.execute(sql, (tsk_del,))
    connection.commit()
    cursor.close()
    connection.close()

def resetTaskList():
    with open("bd.txt", "w") as file:
        file.write("You have ")

def read_norm():
    task_list = reader()
    task_count = str(len(task_list) - 1)

    del task_list[0]
    all_tsk1 = []
    for i in task_list:
        all_tsk1.append(i[0])
    return task_count, all_tsk1

def testBD():
    # Установка соединения с базой данных
    connection = pymysql.connect(host=host, user=user, password=password, database=database_name)

    cursor = connection.cursor()

    # Выполните SQL-запрос для получения всех данных из таблицы
    query = "SELECT * FROM tasks;"
    cursor.execute(query)

    # Получите все строки данных из результата запроса
    rows = list(cursor.fetchall())

    return rows


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


#navigation()


bot = telebot.TeleBot(config.BOT)

print("running")

#   Код для ТГ
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    task_all = types.KeyboardButton('All tasks️')
    #task_upd = types.KeyboardButton('Update task')
    task_del = types.KeyboardButton('Delete tasks️')
    #devs = types.KeyboardButton('For dev')

    markup.add(task_all, task_del)

    bot.send_message(message.chat.id, "Welcome to Task Master V_1.1.3\n"
                                      "What do you want now?", reply_markup=markup)

to_del = 0

@bot.message_handler(content_types=['text'])
def get_link(message):
    global to_del


    if message.chat.type == 'private':

        if message.text == 'All tasks️':

            task_count, all_tsk1 = read_norm()
            all_tsk = '\n'.join(f'{i + 1}. {item}' for i, item in enumerate(all_tsk1))

            bot.send_message(message.chat.id, "You have " + task_count + ' tasks\n')
            bot.send_message(message.chat.id, all_tsk)

        elif message.text == 'Delete tasks️':
            to_del = 1
            bot.send_message(message.chat.id, 'What do you want to delete?')

        elif message.text == 'For dev':
            bot.send_message(message.chat.id, message.text)

            to_dd = 2

            task_count, all_tsk = read_norm()
            tsk_del = all_tsk[to_dd-1]

            connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
            cursor = connection.cursor()

            sql = "DELETE FROM tasks WHERE title = %s"

            cursor.execute(sql, (tsk_del,))
            connection.commit()
            cursor.close()
            connection.close()
            '''
            if tt == 1:
                bot.send_message(message.chat.id, "Good 4 U")
            elif tt:
                bot.send_message(message.chat.id, "So sad")
            else:
                bot.send_message(message.chat.id, "Somethng wrong")
            '''


        elif to_del == 1:
            delTask(int(message.text))
            to_del = 0
            bot.send_message(message.chat.id, "Deleted")

        else:
            newTask(message.text)
            bot.send_message(message.chat.id, "Ready")


bot.polling(none_stop=True)


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

