from django.contrib import messages
from django.views.generic import CreateView

from .forms import MailingListForm
from .forms import SignUpForm
from .models import Event
from .models import Sponsor


class Home(CreateView):
    if Event.objects.current():
        form_class = SignUpForm
        success_url = '/#attendees'
    else:
        form_class = MailingListForm
        success_url = '/'

    template_name = 'home.html'

    def form_valid(self, form):
        if Event.objects.current():
            return self._signup_form_valid(form)
        else:
            return self._mailing_list_form_valid(form)

    def _mailing_list_form_valid(self, form):
        msg = "Thanks for signing up for emails, we'll send you details about any future SusHack events."
        messages.info(self.request, msg)
        return super(Home, self).form_valid(form)

    def _signup_form_valid(self, form):
        self.event = Event.objects.current()
        msg = "Thanks for signing up, we'll email you more details closer to the date."
        messages.info(self.request, msg)
        form.instance.event = self.event
        return super(Home, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['event'] = Event.objects.current()
        context['sponsors'] = Sponsor.objects.all()
        return context
