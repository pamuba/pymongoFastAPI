from models.todos_model import Todo


def todo_serializer(todo) -> dict:
    return {
        "id": str(todo["_id"]), #ObjectId
        "name": todo["name"],
        "description": todo["description"],
        "completed" : todo["completed"],
        "date" : todo["date"]
    }

def todos_serializer(todos)-> list:
    return [todo_serializer(todo) for todo in todos]

def todo_single_serializer(todo) -> list:
    return [{
        "id": str(todo["_id"]), #ObjectId
        "name": todo["name"],
        "description": todo["description"],
        "completed" : todo["completed"],
        "date" : todo["date"]
    }]