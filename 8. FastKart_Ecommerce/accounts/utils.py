from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def send_verification_email(request, user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.id))

    current_site = get_current_site(request)
    # use reverse()
    verification_link = f"http://{current_site.domain}/accounts/verify/{uid}/{token}"

    email_subject = "Verify Your Email Address"
    email_body = render_to_string(
        "accounts/verification_email.html",
        {"user": user, "verification_link": verification_link},
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email],
    )

    email.content_subtype = "html"
    email.send()
