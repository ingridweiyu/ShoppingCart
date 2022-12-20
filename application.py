from flask import Flask, Response, request
from flask_cors import CORS
import json
from resources.shopping_resource import ShoppingResource

application = Flask(__name__)
CORS(application)


@application.route("/", methods=["GET"])
def get_default():
    result = {"status": "success"}
    rsp = Response(json.dumps(result), status=200, content_type="application.json")
    return rsp


@application.route("/carts", methods=["GET", "POST", "DELETE"])
def get_all_carts():
    if request.method == "GET":
        limit = request.args.get('limit', 20)
        offset = request.args.get('offset', 0)
        result = ShoppingResource._get_carts(int(limit), int(offset))

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

    elif request.method == "POST":
        request_json = request.get_json()
        user_id = request_json['user_id']
        cart_id = request_json['cart_id']
        result = ShoppingResource._create_cart(user_id, cart_id)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("CART NOT CREATED, BAD PARAMETER", status=400, content_type="text/plain")

        return rsp

    elif request.method == "DELETE":
        request_json = request.get_json()
        user_id = request_json['user_id']
        cart_id = request_json['cart_id']
        result = ShoppingResource._delete_cart(user_id, cart_id)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type='application.json')
        else:
            rsp = Response("CART NOT DELETED, OR CART DOES NOT EXIST", status=400, content_type='text/plain')

        return rsp

@application.route("/carts/users/<user_id>", methods=["GET"])
def get_by_userid(user_id):
    result = ShoppingResource._get_by_userid(user_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/carts/<cart_id>", methods=["GET", "POST", "PUT", "DELETE"])
def get_by_cartid(cart_id):
    if request.method == "GET":
        result = ShoppingResource._get_by_cartid(cart_id)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

    elif request.method == "POST":
        request_json = request.get_json()
        item_id = request_json["item_id"]
        count = request_json["count"]
        result = ShoppingResource._insert_by_cartid(item_id, cart_id, count)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("ITEM NOT ADDED TO CART, OR ITEM EXISTS IN THE CART, USE UPDATE METHOD INSTEAD", status=400, content_type="text/plain")

        return rsp

    elif request.method == "PUT":
        request_json = request.get_json()
        item_id = request_json["item_id"]
        count = request_json["count"]
        result = ShoppingResource._update_by_cartid(item_id, cart_id, count)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response('ITEM IN CART NOT UPDATED', status=400, content_type="text/plain")

        return rsp

    elif request.method == "DELETE":
        request_json = request.get_json()
        item_id = request_json['item_id']
        result = ShoppingResource._delete_by_cartid(item_id, cart_id)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response('ITEM IN CART NOT DELETED, OR ITEM DOES NOT EXIST IN THE CART', status=400, content_type="text/plain")

        return rsp


@application.route("/carts/<cart_id>/item_ids", methods=["GET"])
def get_itemids_by_cartid(cart_id):
    result = ShoppingResource._get_itemids_by_cartid(cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/carts/<cart_id>/item_names", methods=["GET"])
def get_itemnames_by_cartid(cart_id):
    result = ShoppingResource._get_itemnames_by_cartid(cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/carts/<cart_id>/items", methods=["GET"])
def get_items_by_cartid(cart_id):
    result = ShoppingResource._get_items_by_cartid(cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/items", methods=["GET", "POST"])
def get_items():
    if request.method == "GET":
        offset = request.args.get('offset', 0)
        limit = request.args.get('limit', 20)
        result = ShoppingResource._get_items(int(limit), int(offset))

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

    else:
        request_json = request.get_json()
        item_id = request_json.get('item_id')
        name = request_json.get('item_name')
        description = request_json.get('description')
        price = request_json.get('price')
        result = ShoppingResource._create_item(item_id, name, description, price)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("ITEM NOT CREATED, BAD PARAMETER", status=404, content_type="text/plain")

        return rsp

@application.route("/items/<item_id>", methods=["GET", "DELETE"])
def get_items_by_id(item_id):
    if request.method == "GET":
        result = ShoppingResource._get_by_itemid(item_id)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("NOT FOUND", status=404, content_type="text/plain")

        return rsp

    elif request.method == "DELETE":
        result = ShoppingResource._delete_by_itemid(item_id)

        if result:
            rsp = Response(json.dumps(result), status=200, content_type="application.json")
        else:
            rsp = Response("ITEM NOT FOUND", status=404, content_type="text/plain")

        return rsp

@application.route("/items_name/<name>", methods=["GET"])
def get_items_by_name(name):
    size = request.args.get('size', 20)
    result = ShoppingResource._get_by_itemname(name, size)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    application.run(host="127.0.0.1", port=5020)

