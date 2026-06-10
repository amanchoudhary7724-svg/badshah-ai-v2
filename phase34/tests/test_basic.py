def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "3.4.0"

def test_repo_validate():
    from badshah_ai.tools.migration_tools import repo_validate
    assert "Repo status" in repo_validate()

def test_brain_help():
    from badshah_ai.core.brain import Brain
    assert "migration guide" in Brain().run("help")
