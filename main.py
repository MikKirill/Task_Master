import telebot
from telebot import types
import config
from entities import Tasks

bot = telebot.TeleBot(config.BOT)

def add_newUser():
    pass

#   Все задачи
def reader():
    tasks = Tasks
    return(tasks.display_task(tasks))

#   Новая задача
def newTask(task):
    tasks = Tasks
    Tasks.create_task(tasks, task)

#   Удаление задачи
def delTask(toDel):
    tasks = Tasks
    task_count, all_tsk = read_norm()
    Tasks.delete_task(tasks, all_tsk[toDel - 1])

    return

#   Изменение задачи (soon)
def updateTask(taskList):
    tasks = Tasks
    pass

#   Нормализация полученных данных из бд (требует доработки)
def read_norm():
    task_list = reader()    #   Получение всех задач из БД
    task_count = str(len(task_list) - 1)    #   Подсчет кол-ва задач

    del task_list[0]    #   Удаление служебной строки

    #   Нормализация полученного списка
    all_tsk1 = []
    for i in task_list:
        all_tsk1.append(i[0])

    return task_count, all_tsk1

#   Для тестирования
def testBD():
    pass



print("running")

#   Код для ТГ
@bot.message_handler(commands=['start'])
def welcome(message):
    add_newUser()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    task_all = types.KeyboardButton('All tasks️')
    #task_upd = types.KeyboardButton('Update task')
    task_del = types.KeyboardButton('Delete tasks️')
    info = types.KeyboardButton('Info')
    #devs = types.KeyboardButton('For dev')

    markup.add(task_all, task_del, info)

    bot.send_message(message.chat.id, "Welcome to Task Master\n"
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

        elif message.text == 'Info':
            bot.send_message(message.chat.id, 'Task Master\nV_1.1.6')

        elif message.text == 'For dev':
            bot.send_message(message.chat.id, message.text)

        elif to_del == 1:
            delTask(int(message.text))
            to_del = 0
            bot.send_message(message.chat.id, "Deleted")

        else:
            newTask(message.text)
            bot.send_message(message.chat.id, "Ready")


bot.polling(none_stop=True)
