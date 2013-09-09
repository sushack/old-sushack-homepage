from django.contrib import messages
from django.views.generic import CreateView

from .forms import MailingListForm, SignUpForm
from .models import Event, Sponsor


class Home(CreateView):
    if Event.objects.current():
        form_class = SignUpForm
    else:
        form_class = MailingListForm
    model = MailingListPerson
    success_url = '/'
    template_name = 'home.html'

    def form_valid(self, form):
        if Event.objects.current():
            return self._signup_form_valid(form)
        else:
            return self._mailing_list_form_valid(form)

    def _mailing_list_form_valid(self, form):
        msg = "Thanks for signing up for emails, we'll send you deails about any future emails"
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
