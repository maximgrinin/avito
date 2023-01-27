from django.urls import path

from ads.views import root, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, \
    CategoryDeleteView, AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, AdUploadImageView, \
    SelectionListView, SelectionDetailView, SelectionCreateView, SelectionUpdateView, SelectionDeleteView

urlpatterns = [
    path('', root, name='root-path'),
    path('cat/', CategoryListView.as_view(), name='categories-list'),
    path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('cat/create/', CategoryCreateView.as_view(), name='category-create'),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view(), name='user-delete'),
    path('ad/', AdListView.as_view(), name='ads-list'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('ad/create/', AdCreateView.as_view(), name='ad-create'),
    path('ad/<int:pk>/update/', AdUpdateView.as_view(), name='ad-update'),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='ad-delete'),
    path('ad/<int:pk>/upload_image/', AdUploadImageView.as_view(), name='ad-upload-image'),
    path('selection/', SelectionListView.as_view(), name='selections-list'),
    path('selection/<int:pk>/', SelectionDetailView.as_view(), name='selection-detail'),
    path('selection/create/', SelectionCreateView.as_view(), name='selection-create'),
    path('selection/<int:pk>/update/', SelectionUpdateView.as_view(), name='selection-update'),
    path('selection/<int:pk>/delete/', SelectionDeleteView.as_view(), name='selection-delete'),
]
