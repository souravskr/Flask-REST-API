from users import User

user = [User(1, "bob", "asdf")]


username_mapping = {u.username: u for u in user}

userid_mapping = {u.id: u for u in user}


def authenticate(username, password):

    input_username = username_mapping.get(username, None)
    # input_password = username_mapping.get(password, None)
    if input_username and input_username.password == password:
        return input_username


def indentity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
