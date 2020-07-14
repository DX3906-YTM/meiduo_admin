from django.urls import path
from meiduo_admin.views import users, statistical

urlpatterns = [
    path(r'authorizations/', users.AdminAuthorizeView.as_view()),
    path(r'statistical/day_active/', statistical.UserDayActiveView.as_view()),
    path(r'statistical/day_orders/', statistical.UserDayOrdersView.as_view()),
    path(r'statistical/month_increment/', statistical.UserMonthCountView.as_view()),
    path(r'users/', users.UserInfoView.as_view()),
]