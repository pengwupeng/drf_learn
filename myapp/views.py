from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.renderers import BrowsableAPIRenderer,BrowsableAPIRenderer
from myapp.models import  Question
from myapp.serializers import  QuestionSerializer
from drfhumplib.parsers import SnakeJSONParser
from drfhumplib.renders import HumpJSONRenderer
from myapp.models import Snippet
from myapp.serializers import SnippetSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import renderers


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    parser_classes = (SnakeJSONParser,)
    renderer_classes = (HumpJSONRenderer,BrowsableAPIRenderer,)



class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user



class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)