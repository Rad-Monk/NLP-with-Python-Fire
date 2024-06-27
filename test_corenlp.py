from nlplogic.corenlp import get_phrases


def test_get_phrase():
    assert "microsoft" in get_phrases("Microsoft")
