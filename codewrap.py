"""
codewrap - code wrapping and filling

@copyright: (c) 2006 by Nir Soffer <nirs@freeshell.org>
@license: GNU GPL, see COPYING for details.
@url: http://nirs.freeshell.org/code/codewrap/
"""

from textwrap import TextWrapper
import re


class CodeWrapper(TextWrapper):
    """ Code aware text wrapper
    
    Wrap comments like emacs fill-paragraph command - long comment turn
    into multiple comments, not one comment with following code, like
    most dumb editors do.
    """

    paragraph_separator = re.compile(r'\n\s*\n', 
                                     re.MULTILINE | re.UNICODE)

    def __init__(self,
                 width=72,
                 indent_re=r'^\s*(#+|//+|;+)?\s*',
                 fix_sentence_endings=False,
                 break_long_words=True):
        """ Init instance, use only subset of text wrapper options 

        Disabled TextWrapper options:
         - Indents -- should not be used, because this wrapper set them
                      automatically from the text.
         - expand_tabs -- Should not be used in code context.
         - replace_whitespace -- same, don't do things behind the back
        """
        TextWrapper.__init__(self,
                             width=width,
                             expand_tabs=False,
                             replace_whitespace=False,
                             fix_sentence_endings=fix_sentence_endings,
                             break_long_words=break_long_words)
        
        self.indent_re = re.compile(indent_re, re.UNICODE)

    # ------------------------------------------------------------------
    # High level methods - should be enough for most cases, handle
    # multiple paragraphs.
        
    def fillParagraphs(self, text):
        """ Fill multiple paragraphs 
        
        Assume that paragraphs are separated by empty lines. Preserve
        the ammount of white space between paragraphs.
        
        @param text: text to fill, may contain multiple paragraphs
        @rtype: unicode or str
        @return: filled text
        """
        result = [] 
        location = 0
        for match in self.paragraph_separator.finditer(text):
            # Fill paragraph before match and copy the match
            paragraph = text[location:match.start()]
            result.append(self.fill(paragraph))
            result.append(match.group())
            location = match.end()

        # Add last paragraph
        if location < len(text):
            result.append(self.fill(text[location:]))

        return ''.join(result)

    def dewrapParagraphs(self, text):
        """ Dewrap multiple paragraphs

        @param text: text to dewrap, may contain multiple paragraphs
        @rtype: unicode or str
        @return: dewrapped text
        """
        result = [] 
        location = 0
        for match in self.paragraph_separator.finditer(text):
            # dewrap paragraph before match and copy the match
            paragraph = text[location:match.start()]
            result.append(self.dewrap(paragraph))
            result.append(match.group())
            location = match.end()

        # Add last paragraph
        if location < len(text):
            result.append(self.dewrap(text[location:]))
            
        return ''.join(result)

    # ------------------------------------------------------------------
    # Lower level methods - works with single paragraph

    def fill(self, text):
        """ Fill paragraph by joining wrapped lines 
        
        @param text: unicode or str
        @rtype: unicode or str
        @return: text filled with current width
        """
        result = '\n'.join(self.wrap(text))

        # Keep trailing text newline, not done by TextWrapper
        if text.endswith('\n'):
            result += '\n'
            
        return result    
    
    def wrap(self, text):
        """ Wrap code, and comments in a smart way

        Reformat the single paragraph in 'text' so it fits in lines of
        no more than 'self.width' columns, and return a list of wrapped
        lines.

        This is a modified version from Python 2.5a. wrap is broken
        in Python 2.3 for short strings that fit in the width as is.
        
        @param text: unicode or str
        @rtype: list of unicode or str
        @return: lines filled with current width
        """        
        # First de-wrap text, removing indent and comments marks from lines
        text = self.dewrap(text)
        
        # Get indent value from the first line
        indent, text = self.splitIndent(text)
        self.initial_indent = self.subsequent_indent = indent

        # --------------------------------------------------------------
        # Copy from Python 2.5a following
        
        chunks = self._split(text)
        if self.fix_sentence_endings:
            self._fix_sentence_endings(chunks)
        return self._wrap_chunks(chunks)
                    
    def dewrap(self, text):
        """ Convert hard wrapped paragraph to one line.

        The indentation and comments of the first line are preserved,
        subsequent lines indent and comments characters are striped.

        @param text: one paragraph of text, possibly hard-wrapped
        @rtype: unicode or str
        @return: one line of text
        """
        if not text:
            return text
            
        lines = text.splitlines()

        # Add first line as is, keeping indent
        result = [lines[0]]

        # Add rest of lines removing indent
        for line in lines[1:]:
            indent, line = self.splitIndent(line)
            result.append(line)

        result = ' '.join(result) 
    
        # Keep trailing newline (removed by splitlines)
        if text.endswith('\n'):
            result += '\n'
            
        return result
    
    def splitIndent(self, text):
        """ Split text on indent, including comments characters
        
        Eaxmple (parsed from left margin):
            ## Comment -> '            ## ', 'Comment'
        
        @param text: unicode or str
        @rtype: tuple
        @return: indent (including commnents chars), rest
        """
        match = self.indent_re.match(text)
        if match:
            indent = match.group()
            return indent, text[len(indent):]
        return '', text
        

# ----------------------------------------------------------------------
# Convenience interface

# For description of these fuctions, see the corrosponding methods of
# CodeWrapper.

def fillParagraphs(text, **kw):
    return CodeWrapper(**kw).fillParagraphs(text)

def dewrapParagraphs(text, **kw):
    return CodeWrapper(**kw).dewrapParagraphs(text)