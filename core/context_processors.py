from core.forms import SubscriberForm


def get_subscriber_form(request):
    subscribe_form = SubscriberForm()
    if request.method == 'POST':
        subscribe_form = SubscriberForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
    else:
        subscribe_form = SubscriberForm()

    return {'subscriber_form': subscribe_form}