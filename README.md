# Wrap Code Plugin for Sublime Text 2 and 3

This plugin makes a "Wrap Code" command available in Sublime Text that wraps
selected text to a certain width.

Unlike the built-in "Wrap" command, Wrap Code is intelligent. If a wrapped line
was commented-out, new lines will begin with the same comment character. They
will also indent to the same level as the original line.

## Installing

Clone the repo and place the included files in a `WrapCode` directory in the
Packages directory for your Sublime Text install. On OS X, this is
`~/Library/Application Support/Sublime Text 2/Packages/` or
`~/Library/Application Support/Sublime Text 3/Packages/`.

## Menu Item

You can use the Wrap Code command via the Sublime Text 2 menu by selecting the
text you want to wrap, then clicking Edit -> Wrap Code.

You also call it by bringing up the Command Palette and selecting "Wrap
Code".

## Key Binding

Wrap Code includes a Vintage mode key binding by default -- the same as the
"reformat" operation in Vim. In command mode, highlight the text you want to
wrap, then press the "gq" keys one after another.

## Configuration

The width to which text is wrapped is configurable via the "wrapcode_column"
setting and defaults to 80 characters.

## Copyright

Copyright (c) 2012 by Andrew Brookins <a@andrewbrookins.com>.

The included `codewrap.py` module is copyright (c) by 2006 Nir Soffer
<nirs@freeshell.org>
