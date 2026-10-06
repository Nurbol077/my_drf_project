from django.urls import path, include
from .views import CategoryListCreateUpdateDeleteView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryListCreateUpdateDeleteView, basename='category')

urlpatterns = [
    path('category/', include(router.urls)),
    # path('category/', CategoryList.as_view()),
    # path('category/create/', CategoryCreateView.as_view()),
    # path('category/<int:pk>/', CategoryRetrieveView.as_view()),
    # path('category/<int:pk>/update/', CategoryUpdateView.as_view()),
    # path('category/get_post/', CategoryListCreateView.as_view()),
]