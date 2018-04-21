import datetime
from mongoengine import EmbeddedDocument, Document, StringField, DateTimeField, ListField, EmbeddedDocumentListField, \
    IntField, FloatField, BooleanField, ReferenceField, DictField, URLField, EmailField, EmbeddedDocumentField


class User(Document):
    email = EmailField()
########################################################################################################################

class CocktailIngredient(EmbeddedDocument):
    "e.g. 50 ml of Musicality"
    ingredient = StringField(required=True)
    amount = IntField()
    units = StringField()


class CocktailInfo(EmbeddedDocument):
    recipe = EmbeddedDocumentListField(CocktailIngredient)
    short_info = StringField()
    full_info = StringField()
    teachers_info = StringField()
    video_link = URLField()


class CocktailClassDetails(EmbeddedDocument):
    imbalance_ratio = FloatField()
    max_people = IntField()
    min_people = IntField()
    partnered = BooleanField()
    sessions_number = IntField()
    hours_per_session = FloatField()


class CocktailRecipe(Document):
    "A course definition"
    title = StringField(max_length=200, required=True, unique=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
    author = StringField()
    info = EmbeddedDocumentField(CocktailInfo)
    class_details = EmbeddedDocumentField(CocktailClassDetails)
    price = FloatField()

########################################################################################################################

class Cocktail(Document):
    "A course that is about to happen"
    cocktail_recipe = ReferenceField(CocktailRecipe)
    start_date = DateTimeField()
    end_date = DateTimeField()


########################################################################################################################

class CocktailsMenu(Document):
    cocktails = ListField(ReferenceField(Cocktail))
    start_date = DateTimeField()

########################################################################################################################

class Payment(EmbeddedDocument):
    stripe_response = DictField()
    amount = FloatField()



class Registration(Document):
    user = ReferenceField(User)
    location = DictField() # comes from a geo service
    payments = EmbeddedDocumentListField(Payment)



########################################################################################################################

class Teacher(Document):
    user = StringField()
