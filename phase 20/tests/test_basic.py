def test_version():
    import badshah_ai
    assert badshah_ai.__version__ == "2.0.0"
def test_planner():
    from badshah_ai.agents.planner import MultiAgentPlanner
    p = MultiAgentPlanner()
    assert p.make_plan("create website and export workspace")
def test_brain_plan():
    from badshah_ai.core.brain import Brain
    assert "Multi-Agent Plan" in Brain().run("plan create website")
