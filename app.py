from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, indentity

app = Flask(__name__)
app.secret_key = "secret"
api = Api(app)

jwt = JWT(app, authenticate, indentity)


items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return item, 404 if None else 200

    def post(self, name):

        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": f"{name} already there"}

        parser = reqparse.RequestParser()
        parser.add_argument(
            "price", type=float, required=True, help="This field can't be empty"
        )

        request_data = parser.parse_args()

        new_item = {"name": name, "price": request_data["price"]}
        items.append(new_item)
        return new_item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        return {"message": "Item Deleted"}

    def put(self, name):

        parser = reqparse.RequestParser()
        parser.add_argument(
            "price", type=float, required=True, help="This field can't be empty"
        )

        request_data = parser.parse_args()

        item = next(filter(lambda x: x["name"] == name, items), None)
        if item:
            item.update(request_data)
        else:
            item = {"name": name, "price": request_data["price"]}
            items.append(item)
        return item


api.add_resource(Item, "/item/<string:name>")


class Itemlist(Resource):
    def get(self):
        return {"items": items}, 200


api.add_resource(Itemlist, "/items")

if __name__ == "__main__":
    app.run(debug=True)