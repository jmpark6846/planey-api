from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request


class BaseViewSet(ModelViewSet):
    serializer_class = None
    viewset_serializer_class = {
        'list': None,
        'retrieve': None,
        'update': None,
        'create': None,
    }

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """

        viewset_action = kwargs.pop('viewset_action', None)
        serializer_class = self.get_serializer_class(viewset_action=viewset_action)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self, viewset_action: str = None):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        serializer_class = self.viewset_serializer_class.get(viewset_action, None)

        assert self.serializer_class is not None, (
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method."
                % self.__class__.__name__
        )
        return serializer_class or self.serializer_class

    def list(self, request: Request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, viewset_action='list', many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, viewset_action='list', many=True)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "success": True,
                "message": "정상 처리되었습니다.",
                "body": serializer.data
            }
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, viewset_action='retrieve',)
        return Response(
            status=status.HTTP_200_OK,
            data={
                "success": True,
                "message": "정상 처리되었습니다.",
                "body": serializer.data
            }
        )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, viewset_action='create', )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "success": True,
                "message": "정상 생성되었습니다.",
                "body": serializer.data
            },
            headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, viewset_action='update', data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(
            status=status.HTTP_200_OK,
            data={
                "success": True,
                "message": "정상 처리되었습니다.",
                "body": serializer.data
            }
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data={
                "success": True,
                "message": "정상 처리되었습니다.",
            }
        )
