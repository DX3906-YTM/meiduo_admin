from users.models import User
from rest_framework import serializers


class AdminAuthSerializer(serializers.ModelSerializer):
    """
    管理员序列化器:
    AdminAuthSerializer():
    id = IntegerField(label='ID', read_only=True)
    username = CharField(label='用户名')
    password = CharField(max_length=128, write_only=True)
    token = CharField(label='JWT Token', read_only=True)
    """
    username = serializers.CharField(label='用户名')
    token = serializers.CharField(label='JWT Token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'token')

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate(self, attrs):  # validate 方法用于补充验证
        """
        获取username 和 password
        """
        username = attrs['username']
        password = attrs['password']

        # 校验用户名和密码
        try:
            user = User.objects.get(username=username, is_staff=True)
        except User.DoesNotExist:
            raise serializers.ValidationError('用户名或密码错误')
        else:
            if not user.check_password(password):
                raise serializers.ValidationError('用户名或密码错误')
            # 保存登录用户
            attrs['user'] = user
        return attrs

    def create(self, validated_data):
        """
        获取登录用户user
        validated_data：校验之后的数据
        """
        # 获取登录用户user
        user = validated_data['user']
        # 生成jwt token
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    普通用户序列化器:

    """
    print("*测试*" * 50)
    class Meta:
        model = User
        fields=('id', 'username', 'mobile', 'email')