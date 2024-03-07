class BaseActivity:
    """
    base enum class for activities in a server
    """

    Reply: str = "reply"
    Mention: str = "mention"
    Reaction: str = "reaction"


class DiscordActivity:
    """
    Discord activities
    """

    Reply: str = BaseActivity.Reply
    Mention: str = BaseActivity.Mention
    Reaction: str = BaseActivity.Reaction
    Thread_msg: str = "thr_message"
    Lone_msg: str = "lone_message"
