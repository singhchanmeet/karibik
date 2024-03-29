from react.views import serve_react
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('form.urls')),
    re_path(r"^(?P<path>.*)$", serve_react, {"document_root": settings.REACT_APP_BUILD_PATH}),
]
