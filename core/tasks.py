from celery import shared_task
from core.models import Subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# from mysite.settings import EMAIL_HOST_USER
from django.conf import settings
from django.utils import timezone
from django.db.models import Count
from shop.models import product, product_version
from datetime import timedelta
from user.models import User

@shared_task
def send_mail_to_subscribers():
    startdate = timezone.now()
    enddate = startdate - timedelta(days=7)
    subscriber_emails = Subscriber.objects.values_list('email', flat=True)
    most_rev = product_version.objects.filter(created__gte=enddate).annotate(num_coms=Count('Reviews')).order_by('-num_coms')[0:2]
    for mail in subscriber_emails:
        body = render_to_string('email-subscribers.html', context={
            'email': mail,
            'most_rev': most_rev
        })
        msg = EmailMessage(subject='Subscriber mail', body=body,
                           from_email=settings.EMAIL_HOST_USER,
                           to=[mail,])
        msg.content_subtype = 'html'
        msg.send(fail_silently=True)
    return 'Done'