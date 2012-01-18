import sublime_plugin
import codewrap


class WrapCodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        col = self.view.settings().get('wrapcode_column', 80)
        sel = self.view.sel()
        wrapper = codewrap.CodeWrapper(width=col)

        for region in sel:
            wrapped = wrapper.fillParagraphs(self.view.substr(region))
            self.view.replace(edit, region, wrapped)
            