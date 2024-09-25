from django.db import models


class Joke(models.Model):
    """This class is mapping the joke table"""

    description = models.TextField()

    def __str__(self) -> str:
        return f"Chuck Norris says: {self.description}"
