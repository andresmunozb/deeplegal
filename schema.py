
from graphene import ObjectType, String, Schema
from ocr.predictor import Predictor
import urllib

predictor = Predictor('prediction_model.hdf5')

def predict(link):
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    filename = 'pare.png'
    urllib.request.urlretrieve(link, filename)
    return predictor.predict(filename)


class Query(ObjectType):
    predict = String(link=String(default_value="http://www.google.com"))

    def resolve_predict(root, info, link):        
        return predict(link)

schema = Schema(query=Query)