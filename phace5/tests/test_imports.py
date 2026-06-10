def test_import():
    from badshah_ai.core.brain import Brain
    assert Brain

def test_selfmod_import():
    from badshah_ai.tools.selfmod_tools import list_patches
    assert list_patches
