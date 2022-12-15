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
    def _get_carts(limit, offset):
        limit = min([limit, 80])
        sql = "SELECT * FROM Cart.carts LIMIT %s OFFSET %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (limit, offset))
        result = cur.fetchall()

        prev_page = 0 if offset == 0 else (offset - limit)
        obj = {'data': result, 'link': [{'href': '/carts' + '?offset=%d&limit=%d' % (prev_page, limit), 'rel': 'previous'},
                                        {'href': '/carts' + '?offset=%d&limit=%d' % (offset + limit, limit), 'rel': 'next'}]}

        return obj

    @staticmethod
    def _create_cart(user_id, cart_id):
        sql = "INSERT INTO Cart.carts(user_id, cart_id) VALUES(%s, %s)"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (user_id, cart_id))
        conn.commit()

        return {'user_id': user_id, 'cart_id': cart_id}

    @staticmethod
    def _get_by_cartid(key):
        sql = "SELECT * FROM Cart.carts WHERE Cart.carts.cart_id =%s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def _get_itemids_by_cartid(key):
        sql = "SELECT item_id FROM Cart.cart_item WHERE cart_id = %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def _get_itemnames_by_cartid(key):
        sql = "SELECT item_name FROM Cart.cart_item, Cart.items WHERE cart_id = %s AND Cart.cart_item.item_id = Cart.items.item_id"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def _get_items_by_cartid(key):
        sql = "SELECT i.item_id, i.item_name FROM Cart.cart_item AS c, Cart.items AS i WHERE c.cart_id = %s AND c.item_id = i.item_id"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()

        return result

    @staticmethod
    def _get_items(limit, offset):
        limit = min(limit, 80)
        sql = "SELECT * FROM Cart.items LIMIT %s OFFSET %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (limit, offset))
        result = cur.fetchall()

        prev_page = 0 if offset == 0 else (offset - limit)
        obj = {'data': result, 'link': [{'href': '/items' + '?offset=%d&limit=%d' % (prev_page, limit), 'rel': 'previous'},
                                        {'href': '/items' + '?offset=%d&limit=%d' % (offset + limit, limit), 'rel': 'next'}]}

        return obj

    @staticmethod
    def _create_item(item_id, description, name):
        sql = "INSERT INTO Cart.items(item_id, item_name, description) VALUES(%s, %s, %s)"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (item_id, name, description))
        conn.commit()

        return {'item_id': item_id, 'item_name': name, 'description': description}

    @staticmethod
    def _get_by_item_id(key):
        sql = "SELECT * FROM Cart.items WHERE Cart.items.item_id=%s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

    @staticmethod
    def _get_by_item_name(name, size):
        sql = "SELECT * FROM Cart.items WHERE Cart.items.item_name=%s LIMIT %s"
        conn = ShoppingResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, (name, size))
        result = cur.fetchall()

        return result



