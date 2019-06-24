from django.urls import path, re_path
from apps.user.views import RegisterView, ActiveView, LoginView

urlpatterns = [
    re_path(r'^register$', RegisterView.as_view(), name='register'),  # 注册
    re_path(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    re_path(r'^login$', LoginView.as_view(), name='login')


]
