from django.contrib import admin
from blog.models import Post, Comment, Photo, Youtube
from embed_video.admin import AdminVideoMixin


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')


admin.site.register(Post, AuthorAdmin)
admin.site.register(Comment)


class ClientDetailsAdmin(admin.ModelAdmin):
    def get_changeform_initial_data(self, request):
        get_data = super(ClientDetailsAdmin, self).get_changeform_initial_data(request)
        get_data['created_by'] = request.user.pk
        return get_data


admin.site.register(Photo, ClientDetailsAdmin)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Youtube, MyModelAdmin)


