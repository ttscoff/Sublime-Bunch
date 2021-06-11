A Sublime Text package for Bunch.app on macOS.

[Bunch](https://bunchapp.co) is a Mac automation app that runs on plain text files with the extension `.bunch`. It has its own "language", and this package provides syntax highlighting for Bunch files, as well as light/dark schemes, snippets for common commands, and completion for app names.

- Syntax highlighting for Bunch files and Snippets
- Light and Dark schemes
- Completions for Bunch commands
- Completions for any app name on your system
- Completions for frontmatter keys
- Navigate snippet fragments with ⌘R

![](https://cdn.bunchapp.co/images/bunch-sublime@2x.jpg)

### Built-in Color Schemes

This package comes with a light and dark scheme for Bunch files built in. If you want to enable one, go to __Preferences->Package Settings->Bunch->Settings__ and add:

```
{
    "color_scheme": "Packages/Bunch/Bunch-Dark.sublime-color-scheme"
}
```

(Or `Bunch-Light.sublime-color-scheme` for the light version.)

### Completing App Names

To ensure you get the spelling and capitalization right when adding an app to a Bunch, just start typing the app name on a new line and then trigger autocomplete (varies based on your settings). Matching apps on your system will be listed.

### Autocomplete Keybindings

You can have all available commands pop up as autocomplete options whenever you type a left paren, or fragment IDs within the document when you type `#` in a snippet line. Use the following keybindings (the `chained_actions` command is included in the package).

```
[
    {
        "keys": ["("],
        "command": "chained_actions",
        "args": {
            "actions":["insert_snippet","auto_complete"],
            "args":[{"contents": "(${0:$SELECTION})"},{}]
        },
        "context": [
            {"key": "selector", "operator": "equal", "operand": "text.bunch"},
            {"key": "preceding_text", "operator": "regex_contains", "operand": "^\\s*$", "match_all": true }
        ]
    },
    {
        "keys": ["#"],
        "command": "chained_actions",
        "args": {
            "actions":["insert_snippet","auto_complete"],
            "args":[{"contents": "#${0:$SELECTION}"},{}]
        },
        "context": [
            {"key": "selector", "operator": "equal", "operand": "entity.name.file.bunch"},
            {"key": "preceding_text", "operator": "regex_contains", "operand": "<\\S+", "match_all": true }
        ]
    }
]
```
