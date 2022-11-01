from .base import BaseObject

class Update (BaseObject):
    """
    This object represents an incoming update.
    Only one of the optional parameters can be present in any given update.

    Args:
        update_id (int): The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using Webhooks, since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.

        message (Optional[telegram.objects.message.Message]): Optional. New incoming message of any kind — text, photo, sticker, etc.

        edited_message (Optional[telegram.objects.message.Message]): Optional. New version of a message that is known to the bot and was edited

        channel_post (Optional[telegram.objects.message.Message]): Optional. New incoming channel post of any kind — text, photo, sticker, etc.

        edited_channel_post (Optional[telegram.objects.message.Message]): Optional. New version of a channel post that is known to the bot and was edited

        inline_query (Optional[telegram.objects.inline_query.InlineQuery]): Optional. New incoming inline query

        chosen_inline_result (Optional[telegram.objects.inline_query.ChosenInlineResult]): Optional. The result of an inline query that was chosen by a user and 
        sent to their chat partner. Please see our documentation on the feedback collecting for details on how to enable these updates for your bot.

        callback_query (Optional[telegram.objects.callback_query.CallbackQuery]): Optional. New incoming callback query

        shipping_query (Optional[telegram.objects.shipping_query.ShippingQuery]): Optional. New incoming shipping query. Only for invoices with flexible price

        pre_checkout_query (Optional[telegram.objects.pre_checkout_query.PreCheckoutQuery]): Optional. New incoming pre-checkout query. Contains full information about checkout

        poll (Optional[telegram.objects.poll.Poll]): Optional. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot

        poll_answer (Optional[telegram.objects.poll.PollAnswer]): Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.

        my_chat_member (Optional[telegram.objects.chat_member_updated.ChatMemberUpdated]): Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.

        chat_member (Optional[telegram.objects.chat_member_updated.ChatMemberUpdated]): Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.

        chat_join_request (Optional[telegram.objects.chat_join_request.ChatJoinRequest]): Optional. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    """

    __slots__ = (
        'update_id',
        'message', 
        'edited_message', 
        'channel_post', 
        'edited_channel_post', 
        'inline_query', 
        'chosen_inline_result', 
        'callback_query', 
        'shipping_query', 
        'pre_checkout_query', 
        'poll', 
        'poll_answer', 
        'my_chat_member', 
        'chat_member', 
        'chat_join_request'
        )
    
    
    def __init__(self, update_id):
        self.update_id = update_id
        self.message = None
        self.edited_message = None
        self.channel_post = None
        self.edited_channel_post = None
        self.inline_query = None
        self.chosen_inline_result = None
        self.callback_query = None
        self.shipping_query = None
        self.pre_checkout_query = None
        self.poll = None
        self.poll_answer = None
        self.my_chat_member = None
        self.chat_member = None
        self.chat_join_request = None

