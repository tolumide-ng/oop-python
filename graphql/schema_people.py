from graphene_sqlalchemy import SQLAlchemyObjectType
from database.model_people import ModelPeople
import graphene


# Create a generic class to mutualize description of people attributes for both queries and mutations
class PeopleAttribute:
    name = graphene.String(description="Name of the person.")
    height = graphene.String(description="Height of the person.")
    mass = graphene.String(description="Mass of the person.")
    hair_color = graphene.String(description="Hair color of the person.")
    skin_color = graphene.String(description="Skin color of the person.")
    eye_color = graphene.String(description="Eye color of the person.")
    birth_year = graphene.String(description="Birth year of the person.")
    gender = graphene.String(description="Gender of the person.")
    # planet_id = graphene.ID(description="Global Id of the planet from which the person comes from.")
    url = graphene.String(description="URL of the person in the Star Wars API.")


class People(SQLAlchemyObjectType, PeopleAttribute):
    """People node."""

    class Meta:
        model = ModelPeople
        interfaces = (graphene.relay.Node,)