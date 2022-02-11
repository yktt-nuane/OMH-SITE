from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# --- 管理画面でUserを作成するにはここが必要 ---
from anestudy.forms import UserCreationForm
from anestudy.models.account import User
from anestudy.models.blog import Article, Category, Comment, PostArticle, Tag
from anestudy.models.profile import Profile

# ---------------------------------------


class PostArticleResource(resources.ModelResource):
    class Meta:
        model = PostArticle


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            None,
            {
                "fields": (
                    "is_active",
                    "is_admin",
                )
            },
        ),
    )

    list_display = ("email", "is_active")
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                ),
            },
        ),
    )
    add_form = UserCreationForm

    inlines = (
        ProfileInline,
    )  # ProfileモデルはUserモデルとOneToOneで紐づいているので、User情報をみる際に一緒に表示するために追記


class TagInline(admin.TabularInline):
    model = PostArticle.tags.through


class CategoryInline(admin.TabularInline):
    model = PostArticle.categories.through


class ArticleAdmin(admin.ModelAdmin):

    exclude = ["tags", "categories"]


class PostArticleAdmin(ImportExportModelAdmin):
    inlines = [TagInline, CategoryInline]
    exclude = ["tags", "slug", "categories"]
    resource_class = PostArticleResource


admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(PostArticle, PostArticleAdmin)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
