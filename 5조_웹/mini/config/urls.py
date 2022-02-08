from django.contrib import admin
from django.urls import path, include
from pybo import views

urlpatterns = [
    path('', views.main, name='main'),

    path('common/', include('common.urls')),

    path('marker/', views.marker, name='marker'),

    path('info/', views.info, name='info'),

    path('gw/', views.gw, name='gw'),
    path('gb/', views.gb, name='gb'),
    path('gg/', views.gg, name='gg'),
    path('gj/', views.gj, name='gj'),
    path('dg/', views.dg, name='dg'),
    path('gn/', views.gn, name='gn'),
    path('us/', views.us, name='us'),
    path('jn/', views.jn, name='jn'),
    path('jb/', views.jb, name='jb'),
    path('sj/', views.sj, name='sj'),
    path('so/', views.so, name='so'),
    path('bs/', views.bs, name='bs'),
    path('jj/', views.jj, name='jj'),
    path('dj/', views.dj, name='dj'),
    path('ic/', views.ic, name='ic'),
    path('cb/', views.cb, name='cb'),
    path('cn/', views.cn, name='cn'),

    path('wcl/', views.wcl, name='wcl'),
    path('wcl/gw', views.wcl_gw, name='wcl_gw'),
    path('wcl/gg', views.wcl_gg, name='wcl_gg'),
    path('wcl/gn', views.wcl_gn, name='wcl_gn'),
    path('wcl/gb', views.wcl_gb, name='wcl_gb'),
    path('wcl/dg', views.wcl_dg, name='wcl_dg'),
    path('wcl/dj', views.wcl_dj, name='wcl_dj'),
    path('wcl/bs', views.wcl_bs, name='wcl_bs'),
    path('wcl/so', views.wcl_so, name='wcl_so'),
    path('wcl/sj', views.wcl_sj, name='wcl_sj'),
    path('wcl/us', views.wcl_us, name='wcl_us'),
    path('wcl/ic', views.wcl_ic, name='wcl_ic'),
    path('wcl/jn', views.wcl_jn, name='wcl_jn'),
    path('wcl/jb', views.wcl_jb, name='wcl_jb'),
    path('wcl/jj', views.wcl_jj, name='wcl_jj'),
    path('wcl/cn', views.wcl_cn, name='wcl_cn'),
    path('wcl/cb', views.wcl_cb, name='wcl_cb'),
    path('wcl/gj', views.wcl_gj, name='wcl_gj'),

    path('graph/', views.graph, name='graph'),
    path('graph/2019_c', views.graph1, name='graph1'),
    path('graph/2020_c', views.graph2, name='graph2'),
    path('graph/2019_m', views.graph3, name='graph3'),
    path('graph/2020_m', views.graph4, name='graph4'),
    ]