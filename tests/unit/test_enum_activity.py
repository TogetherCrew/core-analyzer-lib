from analyzer.utils.activity import Activity


def test_enum_activity():
    assert Activity.Mention == "mention"
    assert Activity.Reply == "reply"
    assert Activity.Reaction == "reaction"
