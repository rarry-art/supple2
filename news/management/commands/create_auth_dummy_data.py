from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from news.models import Story, Comment
from django.utils import timezone
import random
from django.db import transaction

class Command(BaseCommand):
    help = 'Creates dummy data for testing, utilizing the authentication system'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Creating dummy data with authentication...')

        # Create users
        users = []
        for i in range(10):
            username = f'testuser{i}'
            email = f'testuser{i}@example.com'
            password = 'testpass123'
            user = User.objects.create_user(username=username, email=email, password=password)
            users.append(user)
            self.stdout.write(f'Created user: {username}')

        # Create stories
        for i in range(30):
            author = random.choice(users)
            story = Story.objects.create(
                title=f'Auth Test Story {i}',
                url=f'http://example.com/auth-story{i}',
                points=random.randint(1, 200),
                user=author,
                created_at=timezone.now() - timezone.timedelta(days=random.randint(0, 60))
            )
            self.stdout.write(f'Created story: {story.title} by {author.username}')

            # Create comments for each story
            for j in range(random.randint(0, 10)):
                commenter = random.choice(users)
                Comment.objects.create(
                    story=story,
                    user=commenter,
                    text=f'This is an authenticated test comment {j} for story {i}',
                    created_at=timezone.now() - timezone.timedelta(days=random.randint(0, 30))
                )
            self.stdout.write(f'Created {j+1} comments for story: {story.title}')

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data with authentication'))