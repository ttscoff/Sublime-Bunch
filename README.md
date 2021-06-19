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

This package comes with a light and dark scheme for Bunch files built in. Syntax highlighting will work with any theme, but the built-in themes highlight some Bunch-specific syntax nicely. If you want to enable one, go to __Preferences->Package Settings->Bunch->Settings__ and add:

```
{
    "color_scheme": "Packages/Bunch/Bunch-Dark.sublime-color-scheme"
}
```

(Or `Bunch-Light.sublime-color-scheme` for the light version.)

### Completing App Names

To ensure you get the spelling and capitalization right when adding an app to a Bunch, just start typing the app name on a new line and then trigger autocomplete (varies based on your settings). Matching apps on your system will be listed.

Because searching your system for matching apps can take a second, autocomplete is disabled while typing, except when inside of parentheses (i.e. a command). You must manually trigger it to complete app names.

### Key Bindings

Choose Sublime Text->Preferences->Package Settings->Bunch->Key Bindings to open the example bindings along with your user key bindings file. Copy any bindings you want into your user file, uncomment them, and enjoy them when editing Bunches.

#### File Items

Example Key Bindings are included which allow Bunch to automatically insert a `- filename` line when you hit return at the end of an app line, and continue inserting file lines until you enter a blank line (the same way Markdown editors continue unordered lists). Just hit return twice to start typing another app name instead.

Here's what's in the commented-out example file:

```json
// Start file lists
{ "keys": ["enter"], "command": "insert_snippet", "args": {"contents": "\n- "}, "context":
    [
        { "key": "selector", "operator": "equal", "operand": "entity.name.function.app.bunch", "match_all": true },
        { "key": "preceding_text", "operator": "regex_contains", "operand": "^(\\s*(!!)?[@%]?)\\S.*", "match_all": true },
        { "key": "auto_complete_visible", "operator": "equal", "operand": false }
    ]
},
// Extend file lists
{ "keys": ["enter"], "command": "insert_snippet", "args": {"contents": "\n- "}, "context":
    [
        { "key": "selector", "operator": "equal", "operand": "source.bunch", "match_all": true },
        { "key": "preceding_text", "operator": "regex_contains", "operand": "^(\\s*(-)\\s+)\\S.*", "match_all": true },
        { "key": "auto_complete_visible", "operator": "equal", "operand": false }
    ]
},
// Remove empty file item
{ "keys": ["enter"], "command": "run_macro_file", "args": {"file": "Packages/Bunch/macros/Remove Empty File Item.sublime-macro"}, "context":
    [
        { "key": "selector", "operator": "equal", "operand": "source.bunch", "match_all": true },
        { "key": "preceding_text", "operator": "regex_contains", "operand": "^\\s*-\\s*$", "match_all": true },
        { "key": "following_text", "operator": "regex_contains", "operand": "^\\s*$", "match_all": true },
        { "key": "auto_complete_visible", "operator": "equal", "operand": false }
    ]
},
```


#### Autocomplete

You can have all available commands pop up as autocomplete options whenever you type a left paren, or fragment IDs within the document when you type `#` in a snippet line. Use the following keybindings (the `chained_actions` command is included in the package).

```json
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

