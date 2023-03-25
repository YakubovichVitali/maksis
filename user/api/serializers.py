from rest_framework import serializers

from user.models import MaksisUser


class FilterChildrenListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ChildrenListSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)

        return serializer.data


class ReferralUserListSerializer(serializers.ModelSerializer):

    children = ChildrenListSerializer(many=True)

    class Meta:
        list_serializer_class = FilterChildrenListSerializer
        model = MaksisUser
        fields = (
            'ref_id',
            'ref_level',
            'children',
        )


class ReferralUserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaksisUser
        fields = (
            'ref_id',
            'ref_level',
        )
