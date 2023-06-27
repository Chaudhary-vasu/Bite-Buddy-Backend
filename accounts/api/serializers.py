from django.contrib.auth.models import User
from rest_framework import serializers, validators


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")

        # defining email and password properties
        extra_kwargs = {
            "password": {"write_only": True},
            # "email": {
            #     "required": True,
            #     "allow_blank": False,
            #     "validators": [
            #         validators.UniqueValidator(
            #             User.objects.all(), "A user with email already exists."
            #         )
            #     ],
            # },
        }

    def create(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")

        user = User.objects.create_user(username=username, password=password)
        return user