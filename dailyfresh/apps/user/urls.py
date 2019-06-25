from django.urls import path, re_path
from apps.user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

urlpatterns = [
    re_path(r'^register$', RegisterView.as_view(), name='register'),  # 注册
    re_path(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'),
    re_path(r'^login$', LoginView.as_view(), name='login'),
    re_path(r'^logout$', LogoutView.as_view(), name='logout'),  # 注销登录
    re_path(r'^$', UserInfoView.as_view(), name='user'),
    re_path(r'^order$', UserOrderView.as_view(), name='order'),
    re_path(r'^address$', AddressView.as_view(), name='address')

]
