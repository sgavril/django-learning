# IN: python manage.py shell

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# Create Snippet objects
snippet = Snippet(code='foo = "bar"\n')
snippet.save()

snippet = Snippet(code='print("hello, world")\n')
snippet.save()

# Serialize a Snippet instance
serializer = SnippetSerializer(snippet)
serializer.data

# Finalize serialization: render the data into JSON
content = JSONRenderer().render(serializer.data)
content

# Deserialization: parse a stream into Python native datatypes
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

# Restore native datatypes into fully populated object instance
serializer = SnippetSerializer(data = data)
serializer.is_valid()
serializer.validated_data
serializer.save()

# Can serialize queryset instead of model instances
serializer = SnippetSerializer(Snippet.objects.all(), many=True)
serializer.data