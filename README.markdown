# About

This plugin makes a "Wrap Code" command available in Sublime Text 2 that wraps
selected text to a certain width.

Unlike the built-in "Wrap" command, "Wrap Code" is intelligent. If a
wrapped line was commented-out, new lines will begin with the same comment
character. They will also indent to the same level as the original line.

# Configuration

The width is configurable via the "wrapcode_column" setting and defaults to 80
characters. Unlike the built-in "Wrap" command, "Wrap Code" is intelligent. If a

# Key bindings

Wrap Code includes a Vintage mode key binding by default -- the same as the
"reformat" operation in Vim. In command mode, highlight the text you want to
wrap, then press the "gq" keys.

# Copyright

This plugin is copyright (c) 2012, Andrew Brookins <a@andrewbrookins.com>.

However, it relies heavily on the included `codewrap.py` module, which is
copyright (c) 2006, Nir Soffer <nirs@freeshell.org>.