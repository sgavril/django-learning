from django.views.generic import TemplateView

class FreshFruitMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_fresh_fruit'] = True
        return context

class FavoriteMixin:
    @cached_property
    def likes_and_favorites(self):
        """ Returns a dict of likes and favorites. """
        likes = self.object.likes()
        favourites = self.object.favorites()
        return {
            "likes": likes,
            "favorites": favorites,
            "favorites_count": favorites.count(),
        }

class FlavorActionMixin:
    model = Flavor

    fields = ['title', 'slug', 'scoops_remaining']

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super().form_valid(form)