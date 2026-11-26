import falcon;
from bson.objectid import ObjectId

class UsersResource:
    def __init__(self, db):
        self.db = db

    async def on_post(self, req, resp):
        data = await req.media
        data = validate_data(data, users_types)
        result = self.db.users.insert_one(data)
        data['_id'] = str(result.inserted_id)
        resp.media = data
        resp.status = falcon.HTTP_201

    async def on_get(self, req, resp, user_id):
        user = self.db.users.find_one({'_id': ObjectId(user_id)})
        if user:
            user['_id'] = str(user['_id'])
            resp.media = user
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404


users_types = {
    "name": str,
    "email": str,
    "city": str,
    "bio": str,
    "current_streak": int,
    "created_at": str,
    "last_logs": str,
    "habits_ids": list,
    "challenge_ids": list,
    "friends": list
}

habits_types = {
    "title": str,
    "description": str,
    "category_id": str,
    "frequency_type": str,
    "satatus": str,
    "enrolled_date": str,
    "last_checked_date": str,
    "completed_date": str,
}

challenge_types = {
    "title": str,
    "description": str,
    "habit_id": str,
    "category_id": str,
    "start_date": str,
    "end_date": str,
    "time": int,
    "created_at": str
}

category_types = {
    "name": str,
    "description": str,
    "icon": str,
    "created_at": str
}

activity_logs_types = {
    "user_id": str,
    "type": str,
    "external_id": str,
    "increment": str, 
    "notes": str,
    "datetime": str,
}

def validate_data(data,type):
    for property in type:
        if property not in data: 
            raise falcon.HTTPBadRequest(f"Invalid data: {property} is required.")
        if type[property] != str:
            try:
                data[property] = type[property](data[property])
            except ValueError:
                raise falcon.HTTPBadRequest(f"Invalid data: {property} must be {type[property]}.")
    return data
