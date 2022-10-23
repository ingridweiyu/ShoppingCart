import flask
import pymysql
import os


class ShoppingResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        conn = pymysql.connect(
            user='dbuser',
            password='dbuserdbuser',
            host='database-1.cgeyeawignkd.us-east-1.rds.amazonaws.com',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_cartid(key):

        sql = "SELECT * FROM Cart.carts WHERE Cart.carts.cart_id =%s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_itemids_by_cart(key):

        sql = "SELECT item_id FROM Cart.cart_item WHERE cart_id = %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_itemnames_by_cart(key):

        sql = "SELECT item_name FROM Cart.cart_item, Cart.items WHERE cart_id = %s AND Cart.cart_item.item_id = Cart.items.item_id"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_items_by_cart(key):

        sql = "SELECT i.item_id, i.item_name FROM Cart.cart_item AS c, Cart.items AS i WHERE c.cart_id = %s AND c.item_id = i.item_id"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def get_carts(size):
        sql = "SELECT * FROM Cart.carts LIMIT %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=size)
        result = cur.fetchall()

        l1 = []
        for r in result:
            l1.append(r)

        return l1

    @staticmethod
    def get_items(size):

        sql = "SELECT * FROM Cart.items LIMIT %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=size)
        result = cur.fetchall()

        return result


    @staticmethod
    def get_by_item_id(key):

        sql = "SELECT * FROM Cart.items WHERE Cart.items.item_id=%s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def get_by_item_name(name, size):

        sql = "SELECT * FROM Cart.items WHERE Cart.items.item_name=%s LIMIT %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (name, size))
        result = cur.fetchall()

        l1 = []
        for r in result:
            l1.append(r)

        return l1


    @staticmethod
    def create_item(item_id, description, name):

        sql = "INSERT INTO Cart.items(item_id, item_name, description) VALUES(%s, %s, %s)"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (item_id, name, description))
        conn.commit()

        return {'item_id': item_id, 'item_name': name, 'description': description}

    @staticmethod
    def create_cart(user_id, cart_id):
        sql = "INSERT INTO Cart.carts(user_id, cart_id) VALUES(%s, %s)"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (user_id, cart_id))
        conn.commit()

        return {'user_id': user_id, 'cart_id': cart_id}
