from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "main"
urlpatterns = [
    path('', views.index, name="home"), 
    path('show/<int:id>', views.show, name="show"),
    path('add/<int:id>', views.add, name="add"),
    path('update<int:id>', views.update_with_solution, name="add_solution"),
    path('add/explanation/<int:id>', views.add_explanation, name="add_explanation"),
    path('filter/<int:id>', views.filtered_errors, name="filter_errors"),
    # path('create', views.create, name="create"),
    # path('add_keyword/<int:error_id>/<int:keyword_id>', views.add_keyword, name="add_keyword"),
    # path('add_suggestion/<int:error_id>', views.add_suggestion, name="add_suggestion"),
    # path('updatephoto', views.update_photo, name="update_photo"),
    # path('autocomplete', views.get_autocomplete_errors, name="autocomplete"),
    # path('filtered/<str:keyword>', views.get_error_cards, name="filtered"),
    # path('remove_keyword/<int:error_id>/<int:keyword_id>', views.remove_keyword, name="remove_keyword")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)