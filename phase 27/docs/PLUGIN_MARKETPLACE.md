# Plugin Marketplace

## Commands

```text
plugin marketplace
plugin enable custom_notes
plugin disable custom_notes
custom note hello
```

## Plugin structure

```text
plugins/my_plugin/plugin.json
plugins/my_plugin/plugin.py
```

`plugin.json`:

```json
{
  "name": "my_plugin",
  "description": "My custom plugin",
  "commands": ["my command"]
}
```

`plugin.py` must expose:

```python
def handle(command: str) -> str:
    return "response"
```
