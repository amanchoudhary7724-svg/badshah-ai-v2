def test_import():
    from badshah_ai.core.brain import Brain
    assert Brain

def test_plugins():
    from badshah_ai.plugins.manifest import list_plugins
    assert len(list_plugins()) > 0
