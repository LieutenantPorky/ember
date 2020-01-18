import peewee

class User:
    username = CharField(unique=True)
    id = AutoField()
    schedule = JSONField()

    class Meta:
        database = usersDB
