import pymysql
import config

host = config.HOST
user = config.USER
password = config.PASSWORD
database_name = config.DATABASE_NAME


def initial():
    # Устанавливаем соединение с базой данных
    connection = pymysql.connect(host=host, user=user, password=password, database=database_name)

    # Создаем курсор для выполнения SQL-запросов
    cursor = connection.cursor()

    # Создаем таблицу "Users"
    users_table = """
        CREATE TABLE IF NOT EXISTS Users (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(255)
        )
    """

    # Создаем таблицу "Task_lists"
    taskList_table = """
        CREATE TABLE IF NOT EXISTS Task_lists (
            list_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            list_name VARCHAR(255),
            FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
    """

    cursor.execute(users_table)
    cursor.execute(taskList_table)
    # Закрываем соединение с базой данных
    connection.close()
    return

def new_table(id, new_usr):
    #   функция генерации названия
    if new_usr is not None and new_usr == 1:
        table_name = 'taskList_' + str(id) + '_0_0'
    else:
        #   Функция подсчета таблиц принадлежащих пользователю
        count = 1
        tag_list = 1
        table_name = 'taskList_' + str(id) + '_' + str(count) + '_' + str(tag_list)

    # Устанавливаем соединение с базой данных
    connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
    # Создаем курсор для выполнения SQL-запросов
    cursor = connection.cursor()

    # Создаем таблицу "Tasks"
    tasks_table = """
        CREATE TABLE IF NOT EXISTS %s (
            task_id INT PRIMARY KEY AUTO_INCREMENT,
            task_title VARCHAR(255)
        )
    """

    formatted_query = tasks_table.replace("%s", table_name)
    cursor.execute(formatted_query)
    # Закрываем соединение с базой данных
    connection.close()
    return

def new_user(usr_id, usr_name):
    connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
    cursor = connection.cursor()

    sql = "INSERT INTO users (user_id, username) VALUES (%s, %s)"

    cursor.execute(sql, (usr_id, usr_name))
    connection.commit()

def check_usr(usr_id, usr_name):
    # Устанавливаем соединение с базой данных
    connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
    # Создаем курсор для выполнения SQL-запросов
    cursor = connection.cursor()

    search_usr = """
        SELECT EXISTS(SELECT 1 FROM users WHERE user_id = %s AND username = %s)
    """

    cursor.execute(search_usr, (usr_id, usr_name))
    result = cursor.fetchone()
    # Закрываем соединение с базой данных
    connection.close()

    if result[0] > 0:
        # User существует
        return 1
    else:
        # User не существует
        new_user(usr_id, usr_name)
        new_table(usr_id, 1)
        return 0
