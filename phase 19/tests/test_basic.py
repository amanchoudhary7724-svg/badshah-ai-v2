def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "1.9.0"
def test_brain():
    from badshah_ai.core.brain import Brain
    assert Brain().run("version").startswith("BADSHAH-AI")
def test_safety():
    from badshah_ai.tools.safety_tools import safety_policy
    assert "Safety" in safety_policy()
