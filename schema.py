
from graphene import ObjectType, String, Schema

def predict(link):
    return "image_filename"


class Query(ObjectType):
    predict = String(link=String(default_value="http://www.google.com"))

    def resolve_predict(root, info, link):        
        return f'Hello {link}!'

schema = Schema(query=Query)