from django.core.mail import EmailMessage
from twilio.rest import Client as TwilioClient
from django.conf import settings

def share_via_email(to_addr, place_id):
    '''
    Sends an email containing a Google Maps link for the location suggestion.

    :param to_addr: string of the recipient's email address
    :param place_id: a string that uniquely identifies a location to Google Maps
    :return: 1 if email is sent, or 0 if not
    '''
    # TODO: place_id or client-supplied json? When you put it that way though it's obvious
    # TODO [later]: personalize for sender (will need to authenticate user of website), and customize message depending on whether recipient is the same as sender (& always add to user profile)
    email = EmailMessage(
    'Hello',
    'Body goes here',
    'from@example.com',
    ['to1@example.com', 'to2@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)
    email = EmailMessage(
        'Your PlaceFindr Suggestion (Do Not Reply)',
        'The following location has been shared with you: \n',
        'from@example.com',
        ['to1@example.com', 'to2@example.com'],
        )
    return email.send(fail_silently=True)


twilio_client = TwilioClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

def share_via_text(to_number, place_id):
    '''
    Sends a text message (via Twilio) containing a Google Maps link for the location suggestion.

    :param to_number: string of the recipient's phone number
    :param place_id: a string that uniquely identifies a location to Google Maps
    :return: <TODO>
    '''
    message = twilio_client.messages.create(
        to=to_number, 
        from_="+15017250604",
        body="Hello from Python!")
    
    # TODO: Twilio's message status response is ridiculously complicated (https://www.twilio.com/docs/guides/how-to-confirm-delivery-in-python). Let's worry abot that after we've got a database.

    return 1

