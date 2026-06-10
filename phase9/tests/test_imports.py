def test_import():
    from badshah_ai.core.brain import Brain
    assert Brain

def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "0.9.0"

def test_smoke():
    from badshah_ai.tools.health_tools import smoke_test
    assert "SMOKE" in smoke_test()
