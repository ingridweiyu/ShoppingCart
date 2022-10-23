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

@application.route("/carts", methods=["GET"])
def get_all_carts():

    size = request.args.get('size', 20)
    result = ShoppingResource.get_carts(int(size))

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/carts/<cart_id>", methods=["GET"])
def get_carts_by_id(cart_id):

    result = ShoppingResource.get_by_cartid(cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/carts/<cart_id>/item_ids", methods=["GET"])
def get_itemids_by_cartid(cart_id):

    result = ShoppingResource.get_itemids_by_cart(cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/carts/<cart_id>/item_names", methods=["GET"])
def get_itemnames_by_cartid(cart_id):

    result = ShoppingResource.get_itemnames_by_cart(cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@application.route("/carts/<cart_id>/items", methods=["GET"])
def get_items_by_cartid(cart_id):

    result = ShoppingResource.get_items_by_cart(cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/items", methods=["GET"])
def get_items():

    size = request.args.get('size', 20)
    result = ShoppingResource.get_items(int(size))

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/items_id/<item_id>", methods=["GET"])
def get_items_by_id(item_id):

    result = ShoppingResource.get_by_item_id(item_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/items_name/<name>", methods=["GET"])
def get_items_by_name(name):

    size = request.args.get('size', 20)
    result = ShoppingResource.get_by_item_name(name, size)
    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@application.route("/items/create", methods=["POST"])
def create_item():

    request_json = request.get_json()
    item_id = request_json.get('item_id')
    name = request_json.get('item_name')
    description = request_json.get('description')
    result = ShoppingResource.create_item(item_id, description, name)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("ITEM NOT CREATED", status=404, content_type="text/plain")

    return rsp


@application.route("/carts/create", methods=["POST"])
def create_cart():
    request_json = request.get_json()
    user_id = request_json.get('user_id')
    cart_id = request_json.get('cart_id')
    result = ShoppingResource.create_cart(user_id, cart_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("CART NOT CREATED", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5012)
