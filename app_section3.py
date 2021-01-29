from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

stores = [{"name": "KFC", "items": [{"name": "Drum Sticks", "price": 6.99}]}]


@app.route("/")
def home():
    return render_template("index.html")


# GET REQUEST
@app.route("/store", methods=["GET"])
def send_store_info():
    for store in stores:
        return jsonify({"store_name": store})


@app.route("/store/<string:name>", methods=["GET"])
def send_certain_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"item_info": store["items"]})
    return ValueError("Store Not Found!")


@app.route("/store/<string:name>/item")
def send_item_info(name):
    for store in stores:
        if store["name"] == name:
            return jsonify({"item_info": store["items"][0]})

    return ValueError("Store Not Found!")


# POST REQUEST
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_data = {"name": request_data["name"], "items": []}
    stores.append(new_data)
    return jsonify(new_data)


@app.route("/store/<string:name>/item", methods=["POST"])
def create_new_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            stores["items"].append(new_item)
            return jsonify(new_item)

    return ValueError("Store Not Found")


if __name__ == "__main__":
    app.run(debug=True)
