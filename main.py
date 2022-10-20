from fastapi import FastAPI
from DataService import *

app = FastAPI()
DB_data = krri_dataservice()

# web server activation: uvicorn main:app --reload
# local host: http://127.0.0.1:8000/

@app.get("/{value}")
def read_root():
    return {"Hello": "World"}

@app.get("/train_and_predict/{value},{name}")
def train_and_predict(value: int, name: str):
    df = DB_data.data_select(value)
    print('Now {} data is loading...'.format(name))
    df = df.values.tolist()
    print(df)
    # DB_data.data_insert()

    # ML - weights
    # model()
    # model.weight()
    # import pickle as pkl
    # pkl.save('d:/gru/'+str(time)+'/.weight')

    # r2 = model.predict()
    # DB_data.data_insert(r2)
    # monthly training

    # DB_data.data_insert()
    return df

def predict(value: int, name: str):
    df = DB_data.data_select(value)
    print('Now {} data is loading...'.format(name))
    df = df.values.tolist()
    print(df)
    # DB_data.data_insert()

    # ML - weights
    #import pickle as pkl
    #pkl.load('d:/gru/'+str(time)+'/.weight')

    #r2 = model.predict()
    #DB_data.data_insert(r2)
    # monthly training

    # DB_data.data_insert()
    return

if __name__ =="__main__":
    train_and_predict(30, 'krri')