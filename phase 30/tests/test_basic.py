def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "3.0.0"

def test_brain_help():
    from badshah_ai.core.brain import Brain
    assert "build exe guide" in Brain().run("help")

def test_smoke():
    from badshah_ai.tools.qa_tools import smoke_test
    assert "workspace" in smoke_test().lower()
