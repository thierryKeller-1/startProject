from django.views.generic import TemplateView, View




class BaseHomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context






class LogoutView():
    pass