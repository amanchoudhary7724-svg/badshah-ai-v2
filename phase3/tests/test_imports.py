def test_brain_import():
    from badshah_ai.core.brain import Brain
    assert Brain is not None

def test_project_tool_import():
    from badshah_ai.tools.project_tools import create_static_website
    assert create_static_website is not None
