import init_django_orm  # noqa: F401

from django.db.models import QuerySet

from db.models import Actor, Actress, Genre

def main() -> QuerySet:
    #Create 

    Genre.objects.bulk_create([
        Genre(Name="Action"),
        Genre(Name="Comedy"),
        Genre(Name="Dramma"),
    ])

    Actor.objects.bulk_create([
        Actor(first_name="George, last_name = ""),
        Actor(first_name="Kianu" last_name="Reaves"),
        Actor(first_name="Will", last_name="Smith")
    ])

    Actress.objects.bulk_create([
        Actress(first_name="Scarlett", last_name="Keegan"),
        Actress(first_name="Scarlett", last_name="Johansson")
    ])

    #Update

    Genre.objects.filter(Name="Dramma").update(Name="Drama")
    Actor.objects.filter(first_name="George").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu").update(first_name="Keanu", last_name="Reeves")


    #Delete
    Genre.objects.filter(Name="Action").delete()
    Actress.objects.filter(first_name="Scarlett").delete()

    #Return
    smith_actors: QuerySet = Actor.objects.filter(last_name="Smith").order_by("first_name")
    return smith_actors