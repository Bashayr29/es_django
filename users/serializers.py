from __future__ import unicode_literals

from rest_framework import serializers

from users.models import Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('username', 'first_name', 'last_name', 'id', 'email')
