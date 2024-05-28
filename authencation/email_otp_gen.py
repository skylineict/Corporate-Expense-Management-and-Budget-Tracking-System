import pyotp
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
from .models import User



def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32(), interval=240)  # OTP expires in 30 minutes
    return totp.now()



def send_otp(email):
    subject = "One Time Password (OTP) Generation"
    otp = generate_otp()
    user = User.objects.get(email=email)
    user.otp_code = otp
    user.otp_sent_time = timezone.now()  # Record the timestamp when OTP was sent
    user.save()
    body = f"Hi {user.username}, your OTP verification code is: {otp}. This code expires in 30 minutes."
    email_from = settings.DEFAULT_EMAIL_FROM
    email_sent = EmailMessage(subject=subject, from_email=email_from, body=body, to=[email])
    email_sent.send(fail_silently=True)

def send_password_reset_email(user, verification_code):
    subject = 'Password Reset'
    message = f'Hello {user.username},\r\n\r\nPlease use the following verification code to reset your password: {verification_code}'
    from_email = settings.DEFAULT_EMAIL_FROM
    to_email = user.email

    email = EmailMessage(subject, message, from_email, [to_email])
    email.send(fail_silently=True)

# def sentpasswordemail(data):
#     required_keys = ['email_subject', 'email_body', 'email_to']
#     if all(key in data for key in required_keys):
#         sent_emails = EmailMessage(
#             subject=data['email_subject'],
#             body=data['email_body'],
#             from_email=settings.EMAIL_HOST_USER,
#             to=[data['email_to']],
#         )
#         sent_emails.send(fail_silently=True)
#     else:
#         print("Missing required keys in data dictionary")

def sentpasswordemail(data):
    sent_emails = EmailMessage(
        subject=data['email_subject'],
        body = data['email_body'],
        from_email =  settings.DEFAULT_EMAIL_FROM,
        to = [data['email_to']],
    )

    sent_emails.send(fail_silently=True)



 