import sublime_plugin
try:
    import WrapCode.codewrap as codewrap
except ImportError:
    import codewrap

class WrapCodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        col = self.view.settings().get('wrapcode_column', 80)
        sel = self.view.sel()
        wrapper = codewrap.CodeWrapper(
            width=col, indent_re=r'^\s*(#+|\*|//+|;+)?\s*')

        for region in sel:
            if region.empty():
                region = self.view.line(region)
            wrapped = wrapper.fillParagraphs(self.view.substr(region))
            self.view.replace(edit, region, wrapped)
            
