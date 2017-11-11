from django.core.mail import EmailMessage
from twilio.rest import Client as TwilioClient

def share_via_email(to_addr, place_id):
    # TODO: place_id or client-supplied json? When you put it that way though it's obvious
    # TODO [later]: personalize for sender (will need to authenticate user of website), and customize message depending on whether recipient is the same as sender (& always add to user profile)
    email = EmailMessage(
        subject='Your PlaceFindr Suggestion (Do Not Reply)',
        message='The following location has been shared to you:\n',
        recipient_list=[ to_addr ],
        #connection=,
    )

    return email.send(fail_silently=False)


twilio_client = TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def share_via_text(to_number, place_id):

    message = twilio_client.messages.create(
        to=to_number, 
        from_="+15017250604",
        body="Hello from Python!")

