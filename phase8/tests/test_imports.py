def test_import():
    from badshah_ai.core.brain import Brain
    assert Brain

def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "0.8.0"
