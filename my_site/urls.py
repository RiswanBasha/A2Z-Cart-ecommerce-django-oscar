"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.apps import apps
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#from paypal.express.dashboard.app import application as express_dashboard
admin.site.site_header="A2Z Cart"
admin.site.site_title= "A2Z Cart"
admin.site.index_title= "Manage A2Z Cart Admin Panel"

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('admin/', admin.site.urls),
    path ( 'checkout/paypal/' , include ( 'paypal.express.urls' )),
     # Dashboard views for Express 
    path('dashboard/paypal/express/', apps.get_app_config("express_dashboard").urls),
    path('dashboard/paypal/payflow/', apps.get_app_config("payflow_dashboard").urls),
     # Custom functionality to allow dashboard users to be created 
    #path ( 'gateway /' , include ( 'apps.gateway.urls' )),
    path('', include(apps.get_app_config('oscar').urls[0])),
] 

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)