#!/usr/bin/env python
"""
Django sample data script
"""
import os
import sys
import django

# Add the parent directory to the path so we can import Django modules
sys.path.append('/home/vedant/Desktop/django/mysite')

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Question, Choice
from django.utils import timezone

# Get the existing question or create a new one
question = Question.objects.first()
if not question:
    question = Question.objects.create(
        question_text="What's your favorite color?",
        pub_date=timezone.now()
    )
    print(f"Created question: {question.question_text}")
else:
    print(f"Using existing question: {question.question_text}")

# Add choices if they don't exist
if not question.choice_set.exists():
    choices = [
        "Red",
        "Blue", 
        "Green",
        "Yellow"
    ]
    
    for choice_text in choices:
        choice = Choice.objects.create(
            question=question,
            choice_text=choice_text,
            votes=0
        )
        print(f"Created choice: {choice.choice_text}")
else:
    print("Choices already exist for this question")

print(f"\nTotal Questions: {Question.objects.count()}")
print(f"Total Choices: {Choice.objects.count()}")
