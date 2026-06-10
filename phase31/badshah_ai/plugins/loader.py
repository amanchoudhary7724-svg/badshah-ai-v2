import json
import importlib.util
from pathlib import Path
from badshah_ai.config.settings import settings

class PluginLoader:
    def __init__(self):
        self.plugin_dir = settings.plugin_dir
        self.config_file = settings.plugin_config
        if not self.config_file.exists():
            self.config_file.write_text(json.dumps({"enabled": []}, indent=2), encoding="utf-8")

    def _config(self):
        try:
            return json.loads(self.config_file.read_text(encoding="utf-8"))
        except Exception:
            return {"enabled": []}

    def _save_config(self, data):
        self.config_file.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def available(self):
        out = []
        for manifest in self.plugin_dir.glob("*/plugin.json"):
            try:
                data = json.loads(manifest.read_text(encoding="utf-8"))
                data["path"] = str(manifest.parent)
                data["enabled"] = data.get("name") in self._config().get("enabled", [])
                out.append(data)
            except Exception:
                pass
        return out

    def marketplace_text(self):
        items = self.available()
        return "\n".join([f"{p['name']} | enabled={p['enabled']} | {p.get('description','')}" for p in items]) or "No plugins found."

    def enable(self, name):
        if not any(p["name"] == name for p in self.available()):
            return "Plugin not found: " + name
        data = self._config()
        enabled = set(data.get("enabled", []))
        enabled.add(name)
        data["enabled"] = sorted(enabled)
        self._save_config(data)
        return "Plugin enabled: " + name

    def disable(self, name):
        data = self._config()
        enabled = set(data.get("enabled", []))
        enabled.discard(name)
        data["enabled"] = sorted(enabled)
        self._save_config(data)
        return "Plugin disabled: " + name

    def route(self, command):
        enabled = set(self._config().get("enabled", []))
        for plugin in self.available():
            if plugin["name"] not in enabled:
                continue
            if any(command.lower().startswith(c.lower()) for c in plugin.get("commands", [])):
                return self._run(plugin, command)
        return None

    def _run(self, plugin, command):
        path = Path(plugin["path"]) / "plugin.py"
        spec = importlib.util.spec_from_file_location("badshah_plugin_" + plugin["name"], path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return str(mod.handle(command))
