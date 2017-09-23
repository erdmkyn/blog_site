from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'publishing_date', 'slug']
    list_display_links = ['title', 'publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['title', 'content']
    #  list_editable = ['content']
    #slug işlemi anlaşılır url yapısı için gerekli biz web sitesi üzerinden
    #ekleme işlemi yaptığımızda sıkıntı yok fakat admin panalinden eklemek
    #istersek ve slug alanı zorunlu olarak doldurmamız gerektiği için sorunla
    #karşılaşırız , bu sorunu çözmek için prepopulated_fields özelliğini kullanırız.
    #burada yapılan slug yapısına title i referans olarak vermemizdir.
    # prepopulated_fields = {'slug': ('title',)}

    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
