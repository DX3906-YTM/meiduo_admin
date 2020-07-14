from users.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from meiduo_admin.serializer.users import AdminAuthSerializer
from meiduo_admin.serializer.users import UserSerializer

# POST /meiduo_admin/authorizations/
class AdminAuthorizeView(CreateAPIView):
    """
    管理员登录API
    """
    serializer_class = AdminAuthSerializer

# GET /meiduo_admin/users/?keyword=<搜索内容>&page=<页码>&pagesize=<页容量>
class UserInfoView(CreateAPIView):
    """
    查询用户
    """
    # 指定认证方案
    permission_classes = [IsAdminUser]

    @staticmethod
    def get(request):
        """
         获取普通用户数据
        """
        # 提取查询字符串 <keyword:搜索内容><page:页码><pagesize:页容量>
        keyword = request.query_params.get('keyword')
        page = request.query_params.get('page')
        pagesize = request. query_params.get('pagesize')

        # 查询普通用户数据
        if keyword:
            users = User.objects.filter(is_staff=False, username__contains=keyword)
        else:
            users = User.objects.filter(is_staff=False)

        # 序列化数据:
        serializer = UserSerualizer(user, many=True)





















































