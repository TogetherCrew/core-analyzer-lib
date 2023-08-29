class BaseActivity:
    """
    base enum class for activities in a server
    """

    Reply: str = "reply"
    Mention: str = "mention"


class DiscordActivity:
    """
    Discord activities
    """

    Reply: str = BaseActivity.Reply
    Mention: str = BaseActivity.Mention
    Reaction: str = "reaction"
