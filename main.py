import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Actor, Genre
from django.db import transaction


def main() -> QuerySet:
    with transaction.atomic():
        # ---- Create Genres using a for loop ----
        genres_to_create = ["Western", "Comedy", "Dramma"]
        for g_name in genres_to_create:
            Genre.objects.get_or_create(name=g_name)

        # Fix typo "Dramma" -> "Drama"
        Genre.objects.filter(name="Dramma").update(name="Drama")

        # Remove unwanted genre "Action" if present
        # Delete unwanted genres
        Genre.objects.filter(name="Action").delete()
        Genre.objects.filter(name="Comedy").delete()

        # ---- Create Actors using a for loop ----
        actors_to_create = [
            ("George", ""),  # will update last_name later
            ("Keanu", "Reeves"),
            ("Will", "Smith"),
            ("Jaden", "Smith"),
            ("Scarlett", "Keegan"),  # will delete later
            ("Scarlett", "Johansson")  # will delete later
        ]
        for first, last in actors_to_create:
            Actor.objects.get_or_create(first_name=first, last_name=last)

        # Update missing/corrected fields
        Actor.objects.filter(first_name="George").update(last_name="Clooney")

        # Delete unwanted actors
        Actor.objects.filter(first_name="Scarlett").delete()

        # Return actors with last_name="Smith" in order
        smith_actors: QuerySet = Actor.objects.filter(
            last_name="Smith"
        ).order_by("first_name")
        return smith_actors
