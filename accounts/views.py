from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MypageView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/mypage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.request.user
        return context