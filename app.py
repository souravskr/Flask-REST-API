from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):

        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": f"{name} already exist"}, 400

        request_data = request.get_json()
        new_item = {"name": name, "price": request_data["price"]}
        items.append(new_item)
        return new_item


api.add_resource(Item, "/item/<string:name>")


class Itemlist(Resource):
    def get(self):
        return {"items": items}


api.add_resource(Itemlist, "/items")


if __name__ == "__main__":
    app.run(debug=True)