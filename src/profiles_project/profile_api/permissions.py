from rest_framework import permissions

class UpdateUserProfile(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            print("SAFE")
            return True
        print(" NOT SAFE\n serializer_class = serializers.UserProfileSerializer ")
        return request.user.id == obj.id
