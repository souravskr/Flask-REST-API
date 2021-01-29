test = [{"name": "book", "price": 12.99}, {"name": "pen", "price": 12.99}]

item = next(filter(lambda x: x["name"] == "book", test))

print(item)
