from rest_framework import generics, mixins, permissions, authentication, pagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from api.authentication import TokenAuthentication

class IsOwner(permissions.BasePermission):
    """
    Кастомное разрешение - разрешает доступ только владельцу объекта.
    """
    def has_object_permission(self, request, view, obj):
        # Проверяем, что владелец продукта - это текущий пользователь
        return obj.owner == request.user

class MyPagination(pagination.PageNumberPagination):
    page_size = 10

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]
    paginator_classes = [MyPagination]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        print(self.request.user)
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class ProductSearchAPIView(APIView):
#     def get(self, request):
#         search_query = request.GET.get('q', '')
#         products = Product.objects.search(search_query)
#         serializer = ProductSerializer(products, many=True)
#         return Response({'search_query': search_query,
#                          'count': products.count(),
#                          'results': serializer.data})

class ProductDetailAPIView(generics.RetrieveAPIView, IsOwner):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def perform_update(self, serializer):
        # здесь сохраняем
        instance = serializer.save()
        # здесь делаем доп действия которые хотим
        if not instance.content:
            print('no content yet. updating it to', instance.title)
            instance.content = instance.title

class ProductMixinView(generics.GenericAPIView,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin):
    '''
    Вью для GET - и list, и detail
    + POST create
    при помощи МИКСИНОВ
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)