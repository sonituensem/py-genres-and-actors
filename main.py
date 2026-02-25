import init_django_orm  # noqa: F401
from django.db.models import QuerySet
from db.models import Actor, Genre
from django.db import transaction


def main() -> QuerySet:
    with transaction.atomic():
        # ---- Create or update genres ----
        target_genres = ["Western", "Drama"]
        for g_name in target_genres:
            Genre.objects.update_or_create(
                name=g_name, defaults={"name": g_name})
        # Fix any old typo
        Genre.objects.filter(name="Dramma").update(name="Drama")

        # ---- Create or update actors ----
        target_actors = [
            ("George", "Clooney"),
            ("Keanu", "Reeves"),
            ("Will", "Smith"),
            ("Jaden", "Smith"),
        ]
        for first, last in target_actors:
            Actor.objects.update_or_create(
                first_name=first,
                last_name=last,
                defaults={"first_name": first, "last_name": last},
            )
        # ---- Return actors with last name "Smith", ordered by first name ----
        smith_actors: QuerySet = Actor.objects.filter(
            last_name="Smith"
        ).order_by("first_name")
        return smith_actors
