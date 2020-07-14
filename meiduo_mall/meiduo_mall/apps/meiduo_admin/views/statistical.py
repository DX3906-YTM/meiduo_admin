from users.models import User
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

# GET /meiduo_admin/statistical/day_active/
class UserDayActiveView(APIView):
    """
    日活跃用户统计
    """
    # 指定认证方案
    permission_classes = [IsAdminUser]

    @staticmethod
    def get(request):
        """
        查询日活用户量
        """
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        count = User.objects.filter(last_login__gte=now_date).count()
        return Response({'date': now_date.date(), 'count': count})

# GET /meiduo_admin/statistical/day_orders/
class UserDayOrdersView(APIView):
    """
    日下单用户统计
    """
    # 指定认证方案
    permission_classes = [IsAdminUser]

    @staticmethod
    def get(request):
        """
        查询日下单用户数量
        """
        now_date = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        # 核心: 使用反向查询外键
        count = User.objects.filter(orders__create_time__gte=now_date).distinct().count()
        return Response({'date': now_date.date(), 'count': count})

# GET /meiduo_admin/statistical/month_increment/
class UserMonthCountView(APIView):
    """
    近30天每日新增用户统计
    """
    # 指定认证方案
    permission_classes = [IsAdminUser]

    @staticmethod
    def get(request):
        """
        查询近30天网站每日新增用户数据
        """
        # end:
        now_date = timezone.now().replace(hour=0,  minute=0, second=0, microsecond=0)
        # begin:
        begin_date = now_date - timezone.timedelta(days=29)

        current_date = begin_date

        month_li = []
        while current_date <= now_date:
            next_date = current_date + timezone.timedelta(days=1)
            # 核心代码: 查询当前时间与明天时间端内创建的用用户数量
            count = User.objects.filter(date_joined__gte=current_date, date_joined__lt=next_date).count()
            # 报存每日信息:
            month_li.append({
                'count': count,
                'date': current_date.date()
            })
            # 更新当前时间:
            current_date += timezone.timedelta(days=1)

        return Response(month_li)


















