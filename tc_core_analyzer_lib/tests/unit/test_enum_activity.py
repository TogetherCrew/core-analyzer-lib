from tc_core_analyzer_lib.utils.activity import BaseActivity, DiscordActivity


def test_enum_discord_activity():
    assert DiscordActivity.Mention == "mention"
    assert DiscordActivity.Reply == "reply"
    assert DiscordActivity.Reaction == "reaction"


def test_enum_base_activity():
    assert BaseActivity.Mention == "mention"
    assert BaseActivity.Reply == "reply"
