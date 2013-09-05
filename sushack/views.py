from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView

from .forms import MailingListForm, SignUpForm
from .models import Attendee, Event, MailingListPerson


class Home(CreateView):
    form_class = MailingListForm
    model = MailingListPerson
    success_url = '/'
    template_name = 'home.html'

    def form_valid(self, form):
        msg = "Thanks for signing up for emails, we'll send you deails about any future emails"
        messages.info(self.request, msg)
        return super(Home, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['event'] = Event.objects.current()
        return context


class SignUp(CreateView):
    form_class = SignUpForm
    model = Attendee
    success_url = '/'
    template_name = 'signup.html'

    def dispatch(self, request, *args, **kwargs):
        self.event = Event.objects.current()
        if not self.event:
            return HttpResponseRedirect('/')
        return super(SignUp, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        msg = "Thanks for signing up, we'll email you more details closer to the date."
        messages.info(self.request, msg)
        form.instance.event = self.event
        return super(SignUp, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SignUp, self).get_context_data(**kwargs)
        context['event'] = self.event
        return context
