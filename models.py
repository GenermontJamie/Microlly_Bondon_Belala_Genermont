from peewee import *
import datetime

database = SqliteDatabase("data.sqlite3")


#Définition du Model de BDD

class BaseModel(Model):

    class Meta:
        database = database

#Définition de la table Utilisateur

class User(BaseModel):
    username = CharField()
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    birthday = DateField()
    password = CharField()


#Définition de la table Publication

class Publication(BaseModel):

    title = CharField()
    body = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    modified_at = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref="publications")


#Fonction de création de table

def create_tables():
    with database:
        database.create_tables([User,Publication ])

#Fonction de destruction de table

def drop_tables():
    with database:
        database.drop_tables([User,Publication ])

