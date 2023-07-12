from django.shortcuts import render

class TitleSearchMixin:
    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get('q')
        if q:
            return queryset.filter(title__icontains=q)
        return queryset
