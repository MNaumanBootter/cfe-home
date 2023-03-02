from api.permissions import IsStaffEditorPermission
from rest_framework.permissions import IsAdminUser


class StaffEditorPermissionMixin():
    permission_classes = [IsStaffEditorPermission, IsAdminUser]


class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        print(lookup_data)
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)