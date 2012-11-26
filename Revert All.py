import sublime, sublime_plugin

class RevertAllCommand(sublime_plugin.WindowCommand):
	def run(self):
		confirmMessage = 'Pressing OK will revert all unsaved files in this window back to the last saved state. This may be difficult to recover from!'
		confirmRevertAll = sublime.ok_cancel_dialog(confirmMessage)
		active_window = sublime.Window.views(sublime.active_window())
		if confirmRevertAll:
			for view in active_window:
				view.run_command('revert')