from django.urls import path

from references.article import views as article_views
from references.contragent import views as contragent_views
from references.measure import views as measure_views
from references.stock import views as stock_views
from references.views import ReferencesView

app_name = 'references'

urlpatterns = [
    path('', ReferencesView.as_view(), name='main'),
    path('article/', article_views.article_list, name='article_list'),
    path('article/<int:group_id>/', article_views.article_list,
         name='article_list_by_group'),
    path('article/<int:group_id>/edit/', article_views.article_group_edit,
         name='article_group_edit'),
    path('article/new/', article_views.article_group_edit,
         name='article_group_new'),
    path('article/element/<int:article_id>/', article_views.article_detail,
         name='article_detail'),
    path('article/element/new/', article_views.article_detail,
         name='article_new'),
    path('contragent/', contragent_views.ContragentListView.as_view(),
         name='contragent_list'),
    path('contragent/new/', contragent_views.ContragentCreateView.as_view(),
         name='contragent_new'),
    path('contragent/<int:pk>/edit',
         contragent_views.ContragentUpdateView.as_view(),
         name='contragent_detail'),
    path('contragent/<int:pk>/delete',
         contragent_views.ContragentDeleteView.as_view(),
         name='contragent_delete'),
    path('measure/', measure_views.MeasureListView.as_view(),
         name='measure_list'),
    path('measure/new/', measure_views.MeasureCreateView.as_view(),
         name='measure_new'),
    path('measure/<int:pk>/edit',
         measure_views.MeasureUpdateView.as_view(),
         name='measure_detail'),
    path('measure/<int:pk>/',
         measure_views.MeasureUpdateView.as_view(),
         name='measure_detail'),
    path('measure/<int:pk>/delete',
         measure_views.MeasureDeleteView.as_view(),
         name='measure_delete'),
    path('stock/', stock_views.StockListView.as_view(),
         name='stock_list'),
    path('stock/new/', stock_views.StockCreateView.as_view(),
         name='stock_new'),
    path('stock/<int:pk>/edit', stock_views.StockUpdateView.as_view(),
         name='stock_detail'),
    path('stock/<int:pk>/delete', stock_views.StockDeleteView.as_view(),
         name='stock_delete'),
]
