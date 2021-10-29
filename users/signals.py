from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user=instance
        profile= Profile.objects.create(user=user, username=user.username, email=user.email, firstName=user.first_name, lastName=user.last_name)

        with open(settings.WELCOME_EMAIL_DIR, 'r') as file:
            data = file.read()
        subject= "Linkr | Welcome to the service!"
        message= f"""<div>
    <div style="text-align:center; mid-width:375px; min-height:50px; padding-left:20px; padding-right:20px; max-width:600px; margin:auto; padding-top:10px">
        <img src="https://i.imgur.com/e3ExQlz.png" alt="CompanyLogo" style="max-width:150px; border:5px; border-color:white; margin:20px;">
    </div>
    <div align="center" style="background-color:#FFFFFF; padding-left:20px; padding-right:20px; max-width:550px; margin:auto; border-radius:5px; padding-bottom:5px; text-align:left; margin-bottom:40px; width:80%"> 
        <h2 style="padding-top:25px; min-width:600; align:center; font-family:Roboto">Hi, {Profile.firstName}</h2>
        <p style="max-width:500px; text-align: justify; align:center; font-family:Roboto; padding-bottom:0px; wrap:hard; line-height:25px">Thanks for creating an account with Linkr We're so happy to have you on board!</p>
        <p style="max-width:500px; text-align: justify; align:center; font-family:Roboto; padding-bottom:0px; wrap:hard">Should you have any issues or suggestions for this product. Don't hesitate in emailing us at <a href="mailto:info@devlg.com">info@devlg.com</a></p style="color:black">
        <p style="max-width:500px; text-align: justify; align:center; font-family:Roboto; padding-bottom:0px; wrap:hard">We are always aiming to improve.</p style="color:black">
        <p style="max-width:500px; text-align: justify; align:center; font-family:Roboto; padding-bottom:0px; wrap:hard">Thank you,</p>
        <p style="max-width:500px; text-align: justify; align:center; font-family:Roboto; padding-bottom:20px; wrap:hard">DEVLG</p style="color:black">
        <hr>
        <p style="max-width:100%; align:center; font-family:Roboto; padding-bottom:10px; wrap:hard; padding-top: 0px; font-size:10px">You’re receiving this email because you recently created a new Linkr account. If this wasn’t you, please ignore this email.</p>
    </div>
</div>"""

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
            html_message=message
        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.profileImage = profile.profileImage
        user.firstName = profile.firstName
        user.lastName = profile.lastName
        user.username = profile.username
        user.email = profile.email
        user.socialTitle1 = profile.socialTitle1
        user.socialLink1 = profile.socialLink1
        user.socialTitle2 = profile.socialTitle2
        user.socialLink2 = profile.socialLink2
        user.socialTitle3 = profile.socialTitle3
        user.socialLink3 = profile.socialLink3
        user.socialTitle4 = profile.socialTitle4
        user.socialLink4 = profile.socialLink4
        user.socialTitle5 = profile.socialTitle5
        user.socialLink5 = profile.socialLink5
        user.save()

def deleteUser(sender, instance, **kwargs):
    user=instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)