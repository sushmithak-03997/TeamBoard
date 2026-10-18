from django.core.management.base import BaseCommand

from api.models import KBEntry

ENTRIES = [
    {
        'question': 'What is select_related in Django ORM?',
        'answer': 'select_related performs a SQL JOIN and fetches related '
                   'objects in the same query, reducing the number of '
                   'database hits for foreign key and one-to-one relations.',
        'category': KBEntry.Category.DATABASE,
    },
    {
        'question': 'How does prefetch_related differ from select_related?',
        'answer': 'prefetch_related runs a separate query per relation and '
                   'joins the results in Python, which works for '
                   'many-to-many and reverse foreign key relations where a '
                   'single SQL JOIN is not possible.',
        'category': KBEntry.Category.DATABASE,
    },
    {
        'question': 'How does transaction.atomic() work in Django?',
        'answer': 'transaction.atomic() wraps a block of database operations '
                   'so that they all succeed or all roll back together, '
                   'guaranteeing that partial writes never persist if an '
                   'exception is raised inside the block.',
        'category': KBEntry.Category.DATABASE,
    },
    {
        'question': 'What is a JWT and how does JWT authentication work?',
        'answer': 'A JSON Web Token (JWT) is a signed, self-contained token '
                   'that encodes claims about a user. JWT authentication lets '
                   'a client send the token with each request instead of a '
                   'session cookie, and the server verifies the signature to '
                   'trust the claims.',
        'category': KBEntry.Category.API,
    },
    {
        'question': 'When should I use Q objects in Django queries?',
        'answer': 'Q objects let you build complex WHERE clauses with OR, '
                   'AND, and NOT logic that plain keyword filtering cannot '
                   'express, such as searching across multiple fields with '
                   'a single search term.',
        'category': KBEntry.Category.DATABASE,
    },
    {
        'question': 'How do Django signals work?',
        'answer': 'Signals let decoupled parts of an application get '
                   'notified when actions occur elsewhere. A post_save '
                   'signal, for example, fires right after a model instance '
                   'is saved, which is useful for automatically creating a '
                   'related profile record.',
        'category': KBEntry.Category.FRAMEWORK,
    },
    {
        'question': 'What is the difference between authentication and authorization?',
        'answer': 'Authentication confirms who is making a request, usually '
                   'via a credential like an API key or JWT. Authorization '
                   'decides what that authenticated identity is allowed to '
                   'do, such as restricting an endpoint to admin roles only.',
        'category': KBEntry.Category.API,
    },
    {
        'question': 'What is an API key and why is it safer than a client-supplied ID?',
        'answer': 'An API key is a server-issued credential tied to a '
                   'specific account. It is safer than letting a client send '
                   'its own ID because a server-issued secret cannot be '
                   'forged or swapped for another company\'s identifier.',
        'category': KBEntry.Category.API,
    },
    {
        'question': 'How do I set up a Django REST Framework project with PostgreSQL?',
        'answer': 'Install djangorestframework and psycopg2-binary, add '
                   'rest_framework to INSTALLED_APPS, and point the DATABASES '
                   'setting at your PostgreSQL credentials, ideally loaded '
                   'from environment variables rather than hardcoded values.',
        'category': KBEntry.Category.FRAMEWORK,
    },
    {
        'question': 'What is horizontal scaling in cloud infrastructure?',
        'answer': 'Horizontal scaling adds more machines or instances to '
                   'handle increased load, as opposed to vertical scaling, '
                   'which increases the resources of a single machine. Cloud '
                   'platforms typically automate horizontal scaling with '
                   'auto-scaling groups.',
        'category': KBEntry.Category.CLOUD,
    },
    {
        'question': 'What is a load balancer used for?',
        'answer': 'A load balancer distributes incoming traffic across '
                   'multiple backend servers so no single instance is '
                   'overwhelmed, and it can also detect unhealthy instances '
                   'and stop routing traffic to them.',
        'category': KBEntry.Category.CLOUD,
    },
    {
        'question': 'What are Django migrations?',
        'answer': 'Migrations are version-controlled files that describe '
                   'changes to your database schema, generated with '
                   'makemigrations and applied with migrate, keeping the '
                   'database structure in sync with your models.',
        'category': KBEntry.Category.GENERAL,
    },
]


class Command(BaseCommand):
    help = 'Seeds the knowledge base with a starter set of Q&A entries.'

    def handle(self, *args, **options):
        created_count = 0
        for entry in ENTRIES:
            _, created = KBEntry.objects.get_or_create(
                question=entry['question'],
                defaults={
                    'answer': entry['answer'],
                    'category': entry['category'],
                },
            )
            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Seeding complete. {created_count} new entries created, '
                f'{KBEntry.objects.count()} total entries in the knowledge base.'
            )
        )
