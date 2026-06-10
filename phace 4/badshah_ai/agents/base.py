class BaseAgent:
    name="base"
    def can_handle(self,q): return True
    def handle(self,q): raise NotImplementedError
