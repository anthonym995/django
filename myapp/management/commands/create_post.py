from django.core.management.base import BaseCommand
from blog.models import Post
from faker import Faker


class Command(BaseCommand):
    help = 'Add initial posts to the database'

    def handle(self, *args, **kwargs):
        fake = Faker()
        posts = []

        for _ in range(10):  # Creates 10 post entries
            post = Post(
                title=fake.sentence(nb_words=6),
                body=fake.text(max_nb_chars=1000),
                created_at=fake.date_time_this_year()
            )
            posts.append(post)

        Post.objects.bulk_create(posts)
        self.stdout.write(self.style.SUCCESS('Successfully added initial posts'))
