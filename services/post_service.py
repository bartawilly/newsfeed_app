import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

class PostService:
    @staticmethod
    def create_post(user_id, content):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()
            insert_query = """
                INSERT INTO Post (user_id, content)
                VALUES (%s, %s)
            """
            cursor.execute(insert_query, (user_id, content))
            connection.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Error creating post: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def get_post(post_id):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor(dictionary=True)
            select_query = "SELECT * FROM Post WHERE post_id = %s"
            cursor.execute(select_query, (post_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error fetching post: {e}")
            return None
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def update_post(post_id, content):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()
            update_query = """
                UPDATE Post SET content = %s, updated_at = NOW() WHERE post_id = %s
            """
            cursor.execute(update_query, (content, post_id))
            connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error updating post: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def delete_post(post_id):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()
            delete_query = "DELETE FROM Post WHERE post_id = %s"
            cursor.execute(delete_query, (post_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Error as e:
            print(f"Error deleting post: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()