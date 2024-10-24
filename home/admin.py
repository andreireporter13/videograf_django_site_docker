from django.contrib import admin
from .models import Event, Review


admin.site.register(Event)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at')
    list_filter = ('status',)
    actions = ['approve_reviews', 'deny_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(status=Review.APPROVED)

    def deny_reviews(self, request, queryset):
        queryset.update(status=Review.DENIED)

    approve_reviews.short_description = "Approve selected reviews"
    deny_reviews.short_description = "Deny selected reviews"

admin.site.register(Review, ReviewAdmin)
