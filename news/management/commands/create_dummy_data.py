from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from news.models import Story, Comment
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Creates dummy data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating dummy data...')

        # Create users
        for i in range(5):
            username = f'user{i}'
            User.objects.create_user(username=username, password='password')

        users = User.objects.all()

        # Create stories
        for i in range(20):
            story = Story.objects.create(
                title=f'Test Story {i}',
                url=f'http://example.com/story{i}',
                points=random.randint(1, 100),
                user=random.choice(users),
                created_at=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
            )

            # Create comments for each story
            for j in range(random.randint(0, 5)):
                Comment.objects.create(
                    story=story,
                    user=random.choice(users),
                    text=f'This is a test comment {j} for story {i}',
                    created_at=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
                )

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data'))

