# Ledger 3 Plugin for Sublime Text 3

This plugin provides syntax highlighting, completion, and general support functions for [Ledger](http://ledger-cli.org/3.0/doc/ledger3.html) journal files.

The syntax highlighting uses Sublime's new .sublime-syntax format, and is deliberately over-engineered. This is so that by simply querying the scopes, the plugin can easily find the names of your accounts, payees, and so on.

In keeping with Ledger's principle of letting you do things your way, this plugin tries hard not to be opinionated. For example, when it auto-inserts dates, it looks at the format of dates you've entered and matches them automatically.

## Features:
  - Syntax coloring.
  - Autocompletion of account names, aliases, and payees. When "strict" mode is specified, only pre-defined entities are auto-completed.
  - Typing "today" or "yesterday" when a date is expected fills in the appropriate date, intelligently recognizing your most recently used date format.
  - Smart, automatic indentation of account names, and automatic un-indentation on typing a date.
  - The ability to run common reports from the Command Palette (currently just a Ledger Balance report with no arguments, but it's easy to add more yourself!)

## Things I want to implement next:
- Add automated transactions and periodic transactions into the syntax definition
- What I currently call "strict" mode is really ledger's "explicit" mode, which requires pre-declarations. Ledger's "strict" mode actually allows entities to be defined in cleared transactions. This shouldn't be hard to implement.
- Add reconciliation assistance, which will work as follows:
    - The user is asked what account they want to reconcile.
    - All selected, uncleared transactions involving that account are marked as pending.
    - A pane opens showing the current value of all cleared transactions, and the value of all cleared+pending transactions, updated in real-time. 
    - If the "cleared+pending" value matches the statement, the user can run a "clear all" command to finish reconciliation immediately.
    - Otherwise, the user should then compare their pending transactions to their bank statement, clearing, adjusting, and adding as appropriate. When all are cleared, the balance in the pane should match the balance on the statement.
- The autocomplete menu's descriptions should show notes when autocompleting declared entities with notes.
- Add more commands to run common reports.
- Add the ability to define favorite reports in comments in the journal file which can be run by Sublime commands.
- Autocompletion of tag names and values
- Basic highlighting of expressions, such as in assertions.
- When a journal entry is started with an integer instead of date, Sublime will calculate a date offset from the previous or next entry. Example: Typing "3" means to insert a date 3 days after the previous entry, while typing "-2" means to insert a date 2 days before the next entry. Typing "0" or "-0" means to repeat the date of the previous or next entry.
- Color reports in output pane. Ledger can already output ANSI color sequences, and there is already a plugin that can use that to colorize the report.
- Run reports to a terminal or a new document, instead of an output pane.
- Integrate with tools that can output HTML reports and display them in a web browser.
- Ensure that the syntax coloring also properly colors "hledger" files, and possibly other ledger-likes.
- Keyboard shortcuts for common operations like marking a transaction as pending or cleared.

If there's a feature listed under "Todo" that you would like to see implemented next, file an issue and I'll make it a priority, or another feature you think would be useful, file a feature request as an issue on GitHub and let's talk about it!

Also, I have very little (i.e. zero) experience writing Sublime plug-ins, so feel free to give me feedback on better ways to do things!
