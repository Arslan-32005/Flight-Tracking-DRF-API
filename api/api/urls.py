# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('app.urls')),
# ]
# from django.contrib import admin
# from django.urls import path, include
# from django.views.generic import TemplateView
# from django.conf import settings
# from django.conf.urls.static import static
# import os

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('app.urls')),
# ]

# # Serve HTML file
# from django.http import FileResponse
# def serve_html(request):
#     return FileResponse(open('flight_search.html', 'rb'), content_type='text/html')

# urlpatterns += [
#     path('', serve_html),
# ]
