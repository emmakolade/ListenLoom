from ListenLoom.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def send_otp(email, otp, expiration_time):
  subject = f"Kindly Veryfiy your account with this {otp}"
  message = f"your OTP for registration is {otp}, it will expire in {expiration_time} minutes"
  from_email = EMAIL_HOST_USER
  recipient_list = [email]
  send_mail(subject, message, from_email, recipient_list, fail_silently=False)