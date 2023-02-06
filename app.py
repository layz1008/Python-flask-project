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
Chicken(name='Rosie', breed='Leghorn').save()
Chicken(name='Peggy', breed='Orpington').save()
Chicken(name='Lila', breed='Sussex').save()
Chicken(name='Nora', breed='Wyandotte').save()
Chicken(name='Maggie', breed='Jersey Giant').save()
Chicken(name='Daisy', breed='Marans').save()
Chicken(name='Tina', breed='Hamburg').save()
Chicken(name='Luna', breed='Silkie').save()
Chicken(name='Bella', breed='Araucana').save()
Chicken(name='Lucy', breed='Brahma').save()
Chicken(name='Izzy', breed='Buff Orpington').save()
Chicken(name='Sadie', breed='Cochin').save()
Chicken(name='Riley', breed='Cornish').save()
Chicken(name='Ava', breed='Dominique').save()
Chicken(name='Sophie', breed='Easter Egger').save()
Chicken(name='Lily', breed='Faverolle').save()
Chicken(name='Chloe', breed='Fayoumi').save()
Chicken(name='Ella', breed='Langshan').save()
Chicken(name='Nina', breed='Lakenvelder').save()
Chicken(name='Mia', breed='Light Brahma').save()
Chicken(name='Emma', breed='Minorcana').save()
Chicken(name='Hazel', breed='Naked Neck').save()
Chicken(name='Ruby', breed='New Hampshire').save()
Chicken(name='Willow', breed='Old English Game').save()
Chicken(name='Piper', breed='Plymouth Rock').save()
Chicken(name='Abby', breed='Poulet de Bresse').save()
Chicken(name='Ellie', breed='Rhode Island White').save()
Chicken(name='Maddie', breed='Sebright').save()
Chicken(name='Harper', breed='Sultan').save()
Chicken(name='Samantha', breed='Sussex Spangled').save()
Chicken(name='Avery', breed='Welsummer').save()
Chicken(name='Evelyn', breed='Yokohama').save()
Chicken(name='Aurora', breed='Zhongshan').save()
Chicken(name='Audrey', breed='Ancona').save()
Chicken(name='Aurora', breed='Andalusian').save()
Chicken(name='Bridgette', breed='Araucana').save()
Chicken(name='Carly', breed='Black Cochin').save()
Chicken(name='Cora', breed='Black Leghorn').save()
Chicken(name='Daphne', breed='Black Minorca').save()
Chicken(name='Esme', breed='Black Rosecomb').save()
Chicken(name='Fay', breed='Black Star').save()


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
