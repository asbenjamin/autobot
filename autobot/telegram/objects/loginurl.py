from autobot.telegram.objects.base import BaseObject
from typing import Optional

class LoginUrl(BaseObject):
    """
    This object represents a parameter of the inline keyboard button used to automatically authorize a user. Serves as a great replacement for the Telegram Login Widget when the user is coming from Telegram. All the user needs to do is tap/click a button and confirm that they want to log in:

    Telegram apps support these buttons as of version 5.7.

    Args:
        url (str): An HTTP URL to be opened with user authorization data added to the query string when the button is pressed. If the user refuses to provide authorization data, the original URL without information about the user will be opened. The data added is the same as described in Receiving authorization data.

        forward_text (str): Optional. New text of the button in forwarded messages.

        bot_username (str): Optional. Username of a bot, which will be used for user authorization. See Setting up a bot for more details. If not specified, the current bot's username will be assumed. The url's domain must be the same as the domain linked with the bot. See Linking your domain to the bot for more details.

        request_write_access (bool): Optional. Pass True to request the permission for your bot to send messages to the user.
    """

    
    
    def __init__(self, url:str = None) -> None:
        self.url = url
        self.forward_text: Optional[str] = None
        self.bot_username: Optional[str] = None
        self.request_write_access: Optional[bool] = None
