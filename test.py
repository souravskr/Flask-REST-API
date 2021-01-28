request_data = request.get_json()
    for store in stores:
        store["name"] = request_data[name]
    return jsonify({"stores": stores})