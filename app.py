from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('chickens', user='zacklay', password='', host='localhost', port=5432)

class BaseModel(Model):
  class Meta:
    database = db

class Chicken(BaseModel):
  name = CharField()
  breed = CharField()

db.connect()
db.drop_tables([Chicken])
db.create_tables([Chicken])

Chicken(name='Speckles', breed='Rhode Island Red').save()
Chicken(name='Gertie', breed='Barred Plymouth Rock').save()

app = Flask(__name__)

@app.route('/chicken/', methods=['GET', 'POST'])
@app.route('/chicken/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
  if request.method == 'GET':
    if id:
        return jsonify(model_to_dict(Chicken.get(Chicken.id == id)))
    else:
        chickens_list = []
        for chicken in Chicken.select():
            chickens_list.append(model_to_dict(chicken))
        return jsonify(chickens_list)

  if request.method =='PUT':
    body = request.get_json()
    Chicken.update(body).where(Chicken.id == id).execute()
    return "Chicken " + str(id) + " has been updated."

  if request.method == 'POST':
    new_chicken = dict_to_model(Chicken, request.get_json())
    new_chicken.save()
    return jsonify({"success": True})

  if request.method == 'DELETE':
    Chicken.delete().where(Chicken.id == id).execute()
    return "Chicken " + str(id) + " deleted."

app.run(debug=True, port=9000)
