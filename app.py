from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('chickens', user='postgres', password='', host='localhost', port=5432)

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



app.run(debug=True, port=9000)
