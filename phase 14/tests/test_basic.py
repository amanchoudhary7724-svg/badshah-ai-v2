def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "1.4.0"

def test_brain():
    from badshah_ai.core.brain import Brain
    assert Brain().run("version").startswith("BADSHAH-AI")
