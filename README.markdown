# Wrap Code Plugin for Sublime Text 2

This plugin makes a "Wrap Code" command available in Sublime Text 2 that wraps
selected text to a certain width.

Unlike the built-in "Wrap" command, Wrap Code is intelligent. If a
wrapped line was commented-out, new lines will begin with the same comment
character. They will also indent to the same level as the original line.

## Menu Item

You can use the Wrap Code command via the Sublime Text 2 menu by selecting the
text you want to wrap, then clicking Edit -> Wrap Code.

## Key Binding 

Wrap Code includes a Vintage mode key binding by default -- the same as the
"reformat" operation in Vim. In command mode, highlight the text you want to
wrap, then press the "gq" keys.

## Configuration

The width to which text is wrapped is configurable via the "wrapcode_column"
setting and defaults to 80 characters.

## Copyright

This plugin is copyright (c) 2012, Andrew Brookins <a@andrewbrookins.com>.

However, it relies heavily on the included `codewrap.py` module, which is
copyright (c) 2006, Nir Soffer <nirs@freeshell.org>.