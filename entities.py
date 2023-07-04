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
    def display_task(self):
        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        # Выполните SQL-запрос для получения всех данных из таблицы
        query = "SELECT * FROM tasks;"
        cursor.execute(query)

        # Получите все строки данных из результата запроса
        rows = list(cursor.fetchall())
        return rows

    #   Создание новой задачи
    def create_task(self, task):  #   Запись в БД
        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        sql = "INSERT INTO tasks (title) VALUES (%s)"

        cursor.execute(sql, (task))
        connection.commit()
        return

    #   Удаление задачи
    def delete_task(self, tsk_del):
        # Установка соединения с базой данных
        connection = pymysql.connect(host=host, user=user, password=password, database=database_name)
        cursor = connection.cursor()

        sql = "DELETE FROM tasks WHERE title = %s"

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

