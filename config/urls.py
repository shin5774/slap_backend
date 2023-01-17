from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from board import views as board_views
from member import views as member_views
import models.urls

router = routers.DefaultRouter()
router.register(r'member', member_views.MemberListAPI)
router.register(r'board', board_views.BoardListAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('models/',include(models.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
