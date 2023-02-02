from pymongo import MongoClient


def connect_with_mongodb():
    try:
        # Connect to a MongoDB database
        client = MongoClient(
            "mongodb+srv://muhammadahmed:AMeg90C7Ze8hhKC6@cluster0.iguhlhs.mongodb.net/?retryWrites=true&w=majority")
        db = client["database"]
        return {"message": db}
    except Exception as e:
        return {"error": str(e)}
