import csv

from django.core.management.base import BaseCommand
from textaudio.models import ProfanityWord



# Django allows to create custom command to run one time db opeartion
class Command(BaseCommand):
    help = "Import profanity words from CSV"

    def handle(self, *args, **kwargs):

        file_path = "textaudio/profanity/profanity.csv"

        objects = []

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                word = row["text"].strip().lower()

                if word:
                    objects.append(
                        ProfanityWord(word=word)
                    )

        ProfanityWord.objects.bulk_create(
            objects,
            ignore_conflicts=True
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(objects)} words imported successfully."
            )
        )