from pyrogram.types import Message


def reply_id(msg: Message):
    """Take a Message and return the ID of the replied-to message, the message itself
    if it's not ours, or None if it's not a reply.

    Arguments:
        message (`Message`): A Pyrogram Message object
    """

    reply_id = None

    if msg.reply_to_message:
        reply_id = msg.reply_to_message.message_id

    elif not msg.from_user.is_self:
        reply_id = msg.message_id

    return reply_id
