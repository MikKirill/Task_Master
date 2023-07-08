import pymysql
import config

host = config.HOST
user = config.USER
password = config.PASSWORD
database_name = config.DATABASE_NAME

class Tasks:
    def __init__(self, id, title, description):
        self.taskId = id
        self.taskTitle = title
        self.dsc = description
        self.dateEnd = False

    #    Отображение всех задач
    def display_task(self, user_id):
        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        table_name = 'taskList_' + str(user_id) + '_0_0'

        # Выполните SQL-запрос для получения всех данных из таблицы
        bd_tasks = "SELECT task_title FROM " + table_name + ";"
        cursor.execute(bd_tasks)
        # Получите все строки данных из результата запроса
        rows_task = list(cursor.fetchall())

        # Выполните SQL-запрос для получения всех данных из таблицы
        bd_id = "SELECT task_id FROM " + table_name + ";"
        cursor.execute(bd_id)
        # Получите все строки данных из результата запроса
        rows_id = list(cursor.fetchall())
        connection.commit()

        return rows_task, rows_id

    #   Создание новой задачи
    def create_task(self, task, user_id):  #   Запись в БД
        table_name = 'taskList_' + str(user_id) + '_0_0'

        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        sql = "INSERT INTO " + table_name + " (task_title) VALUES (%s)"

        cursor.execute(sql, (task))
        connection.commit()
        return

    #   Удаление задачи
    def delete_task(self, tsk_del, user_id):
        table_name = 'taskList_' + str(user_id) + '_0_0'

        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        sql = "DELETE FROM " + table_name + " WHERE task_id = %s"

        cursor.execute(sql, (tsk_del,))
        connection.commit()
        cursor.close()
        connection.close()
        return

    #   Изменение задачи (soon)
    def update_task(self, task_list, task_id, task_title):
        pass

    #   Выполнение задачи (soon)
    def complete_task(self):
        pass

