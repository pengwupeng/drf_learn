# -*- coding:utf-8  -*-
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from myapp.views import QuestionViewSet,SnippetViewSet
from system.views import UserViewSet

__doc__ = u"""
    rest API测试
"""

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"questions",QuestionViewSet)
router.register(r"snippetviewset",SnippetViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

from rest_framework.views import APIView
from rest_framework.response import  Response
from myapp.models import Question
from myapp.serializers import QuestionSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def question_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        qs = Question.objects.all()
        serializer = QuestionSerializer(qs,many=True)
        return Response(serializer.data)

class QuestionList(APIView):
    def get(self,request,format=None):
        qs = Question.objects.all()
        serializer = QuestionSerializer(qs,many=True)
        return Response(serializer.data)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
    path('', include(router.urls)),
    path("test",QuestionList.as_view()),
    path("test2",question_list),
    path('docs', include_docs_urls(title="项目开发文档",description="所有项目API"),),
]
