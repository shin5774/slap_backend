from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from plants_section import views as board_views
from user import views as member_views
from disease import views as disease_views
from disease_by_section import views as plants_by_disease_views
from farm import views as plants_group_views
from section_by_time import views as section_by_time_views

router = routers.DefaultRouter()
router.register(r'user', member_views.MemberListAPI)
router.register(r'plants_section', board_views.BoardListAPI)
router.register(r'disease', disease_views.DiseaseListAPI)
router.register(r'disease_by_section', plants_by_disease_views.PlantsByDiseaseListAPI)
router.register(r'farm', plants_group_views.PlantsGroupListAPI)
router.register(r'seciton_by_time', section_by_time_views.SectionByTimeListAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)