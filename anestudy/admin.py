from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from anestudy.models.account import User
from anestudy.models.profile import Profile
from anestudy.models.blog import Article, Comment, PostArticle, Tag, PostArticle

# --- 管理画面でUserを作成するにはここが必要 ---
from anestudy.forms import UserCreationForm
# ---------------------------------------


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        })
    )

    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password',),
        }),
    )
    add_form = UserCreationForm

    inlines = (ProfileInline,)  # ProfileモデルはUserモデルとOneToOneで紐づいているので、User情報をみる際に一緒に表示するために追記

class TagInline(admin.TabularInline):
    model = Article.tags.through

class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    exclude = ['tags',]

class PostArticleAdmin(admin.ModelAdmin):
    exclude = ['tags',]

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PostArticle, PostArticleAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
