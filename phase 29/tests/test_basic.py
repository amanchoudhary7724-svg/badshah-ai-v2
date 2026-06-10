def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "2.9.0"

def test_smoke():
    from badshah_ai.tools.qa_tools import smoke_test
    assert "workspace" in smoke_test().lower()

def test_brain_help():
    from badshah_ai.core.brain import Brain
    assert "test smoke" in Brain().run("help")
