from braces.views import SetHeadlineMixin
from django.conf import settings
from django.views.generic import ListView

from bulletin.models import Category
from bulletin.views import PostSubmitView, PostUpdateView, SidebarView
from bulletin.tools.plugins.forms import opportunity as forms
from bulletin.tools.plugins.models import Opportunity


class OpportunitySubmitView(PostSubmitView):

    model = Opportunity
    form_class = forms.OpportunitySubmitForm
    headline = 'Submit an Opportunity'


class OpportunityUpdateView(PostUpdateView):

    model = Opportunity
    form_class = forms.OpportunityUpdateForm
    headline = 'Update Opportunity'


class OpportunityListView(SetHeadlineMixin,
                          ListView,
                          SidebarView):

    model = Opportunity
    queryset = Opportunity.objects.filter(approved=True).order_by('-pub_date')
    template_name = 'plugins/opportunity_list.html'
    paginate_by = settings.NUM_POSTS_ON_FRONT_PAGE
    headline = 'Opportunities'

    def get_queryset(self):
        queryset = super(OpportunityListView, self).get_queryset()
        if 'category' in self.request.GET:
            category = Category.objects.get(name=self.request.GET['category'])
            queryset.filter(category_id=category.id)
        return queryset
