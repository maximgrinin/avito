from django.urls import path

from ads.views import root, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView, AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdUploadImageView, \
    SelectionListView, SelectionDetailView, SelectionCreateView, SelectionUpdateView, SelectionDeleteView

urlpatterns = [
    path('', root),
    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('ad/', AdListView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', AdUploadImageView.as_view()),
    path('selection/', SelectionListView.as_view()),
    path('selection/<int:pk>/', SelectionDetailView.as_view()),
    path('selection/create/', SelectionCreateView.as_view()),
    path('selection/<int:pk>/update/', SelectionUpdateView.as_view()),
    path('selection/<int:pk>/delete/', SelectionDeleteView.as_view()),
]
