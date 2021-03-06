"""PDT core case category admin interface."""
from django.contrib import admin

from ..models import CaseCategory

from .columns import tags

from taggit_helpers import TaggitListFilter


class CaseCategoryAdmin(admin.ModelAdmin):

    """Case category admin interface class."""

    list_display = ('id', 'position', 'title', tags, 'is_hidden', 'is_default')
    list_filter = (TaggitListFilter,)
    sortable_field_name = "position"


admin.site.register(CaseCategory, CaseCategoryAdmin)
