import sublime_plugin

class LedgerRunCommand(sublime_plugin.TextCommand):
    def run(self, edit, cmd, arg=None):
        command = ['/usr/local/bin/ledger', '-f', self.view.file_name()] + [cmd]
        if arg:
            command += [arg]
        print(command)
        self.view.window().run_command('exec', {'cmd': command})
