from connect import ConnectDatabase
from peewee import *


class Story(Model):
    story_title = CharField()
    user_story = TextField()
    acceptance_criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

    class Meta:
        database = ConnectDatabase.db

