from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book')

urlpatterns = [
    #Route for the BookList view
    path('books/', BookList.as_view(), name='book-list'),
    
    #include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/', include('api.urls')),
    path('api-token-auth/', obtain_auth_token),  # <-- Token login endpoint
]
