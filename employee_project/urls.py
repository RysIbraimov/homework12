from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from emp_api import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = DefaultRouter()
emplyee_router = DefaultRouter()
router.register('position', views.PositionApiViewSet)
emplyee_router.register('employee', views.EmployeeApiViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Employee API",
      default_version='v0.1',
      description="API for employees ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/user/register/',views.UserRegisterView.as_view()),
    path('api/token/', obtain_auth_token),

    path('api/',include(router.urls)),
    path('api/', include(emplyee_router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='redoc_ui'),
]
