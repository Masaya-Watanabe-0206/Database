from django.urls import path
from . import views

app_name = 'album'

urlpatterns = [
    # ファイルの一覧ページ
    path('file/', views.FileListView.as_view(), name='file_list'),

    # 通常のフォーム
    path('single/upload/', views.SingleUploadView.as_view(), name='single_upload'),

    # モデルフォーム
    path('single/upload/model/', views.SingleUploadWithModelView.as_view(), name='single_upload_with_model'),


    path('multi/upload/', views.MultiUploadView.as_view(), name='multi_upload'),


    path('multi/upload/model/', views.multi_upload_with_model, name='multi_upload_with_model'),


    path('input/multiple/upload/', views.InputMultiUploadView.as_view(), name='input_multi'),
]
