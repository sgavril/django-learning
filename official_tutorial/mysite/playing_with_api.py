# open `python manage.py shell`

from django.utils import timezone
from polls.models import Choice, Question

# Lookup by primary key:
Question.objects.get(pk=1)

# Filter on objects: id, startswith, 
Question.objects.filter(question_text__startswith="What")
Question.objects.filter(id=1)

current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

# Looking at custom methods
q = Question.objects.get(pk=1)
q.was_published_recently()

# Creating choices for q: 
#   because 'Choice' model has a ForeignKey field named 'question'
#   Django will create an attribute on 'Question' named choice_set
q.choice_set.all() # currently empty
q.choice_set.create(choice_text="Not much", votes=0)
c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Showing access to objects related by foreign key
c.question
c.choice_set.count()

# Lookups can span relationships: query the database for records
#   with properties in their related models
Choice.objects.filter(question__pub_date__year=current_year)

# Deletion
c = q.choice_set.filter(choice_text__startswith="Just hacking")
c.delete()