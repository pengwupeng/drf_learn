from rest_framework import routers, serializers, viewsets
from myapp.models import Question
from myapp.models import Snippet


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id','question_text', 'pub_date', ]



class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style','highlighted','owner',]