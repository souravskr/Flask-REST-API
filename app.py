from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Item 1", "price": 12.99}]}]

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# ---------------------- POST REQUEST ------------------------


@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>", methods=["POST"])
def create_store_name(name):
    pass


@app.route("/store/<string:name>/item", methods=["POST"])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_data = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_data)
            return jsonify(new_data)
    return jsonify({"message": "Store not found"})


# ---------------------- GET REQUEST ------------------------


@app.route("/store", methods=["GET"])
def send_store():
    return jsonify({"stores": stores})


@app.route("/store/<string:name>", methods=["GET"])
def send_store_name(name):
    for store in stores:

        if store["name"] == name:
            return jsonify(store)
        else:
            raise ValueError("Store Not Found")


@app.route("/store/<string:name>/item", methods=["GET"])
def send_store_item(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})
        else:
            raise ValueError("Item Not Found")


if __name__ == "__main__":
    app.run(debug=True)
