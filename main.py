import telebot
from telebot import types

import config
from entities import Tasks
import checker_database as cdb

bot = telebot.TeleBot(config.BOT)
dev_id = config.DEV_ID

to_del = 0

print('Initialization DB')
cdb.initial()
print('Success')

#   Все задачи
def reader(id):
    tasks = Tasks
    return(tasks.display_task(tasks, id))

#   Новая задача
def newTask(task, id):
    tasks = Tasks
    Tasks.create_task(tasks, task, id)

#   Удаление задачи
def delTask(toDel, id):
    tasks = Tasks
    task_count, all_tsk = read_norm(id)
    Tasks.delete_task(tasks, all_tsk[toDel - 1], id)
    print(all_tsk)

    return

#   Изменение задачи (soon)
def updateTask(taskList):
    tasks = Tasks
    pass

#   Нормализация полученных данных из бд (требует доработки)
def read_norm(id):
    task_list = reader(id)    #   Получение всех задач из БД
    task_count = str(len(task_list))    #   Подсчет кол-ва задач

    #   Нормализация полученного списка
    all_tsk = []
    for i in task_list:
        all_tsk.append(i[0])

    return task_count, all_tsk

#   Для тестирования
def testBD():
    pass



print("running")

#   Код для ТГ
@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    task_all = types.KeyboardButton('All tasks️')
    # task_upd = types.KeyboardButton('Update task')
    task_del = types.KeyboardButton('Delete tasks️')
    info = types.KeyboardButton('Info')
    # devs = types.KeyboardButton('For dev')

    markup.add(task_all, task_del, info)

    #   Проверка существования записи пользователя
    if cdb.check_usr(message.from_user.id, message.from_user.username) == True:
        bot.send_message(message.chat.id,
                         ("Welcome back " + message.from_user.username + '!')
                         , reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Welcome to Task Master!\n"
                                          "What do you want now?", reply_markup=markup)

    '''
    if message.chat.id == dev_id:
    '''

@bot.message_handler(content_types=['text'])
def get_link(message):

    global to_del

    if message.chat.type == 'private':

        if message.text == 'All tasks️':

            task_count, all_tsk1 = read_norm(message.chat.id)
            all_tsk = '\n'.join(f'{i + 1}. {item}' for i, item in enumerate(all_tsk1))
            bot.send_message(message.chat.id, "You have " + task_count + ' tasks\n')
            bot.send_message(message.chat.id, all_tsk)

        elif message.text == 'Delete tasks️':
            to_del = 1
            bot.send_message(message.chat.id, 'What do you want to delete?')

        elif message.text == 'Info':
            bot.send_message(message.chat.id, 'Task Master\nV_1.2.1')

        elif message.text == 'For dev':
            bot.send_message(message.chat.id, message.text)

        elif to_del == 1:
            delTask(int(message.text), message.chat.id)
            to_del = 0

            task_count, all_tsk1 = read_norm(message.chat.id)
            all_tsk = '\n'.join(f'{i + 1}. {item}' for i, item in enumerate(all_tsk1))
            bot.send_message(message.chat.id, "Task deleted\n"
                                              "Now you have " + task_count + ' tasks\n')
            bot.send_message(message.chat.id, all_tsk)

        else:
            newTask(message.text, message.chat.id)

            task_count, all_tsk1 = read_norm(message.chat.id)
            all_tsk = '\n'.join(f'{i + 1}. {item}' for i, item in enumerate(all_tsk1))
            bot.send_message(message.chat.id, "Task added\n"
                                              "Now you have " + task_count + ' tasks\n')
            bot.send_message(message.chat.id, all_tsk)


bot.polling(none_stop=True)
