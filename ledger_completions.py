import sublime_plugin
# import sublime
# import re
import datetime
from Ledger3.ledger_support import selectors, list_accounts, list_payees, guess_date_format, \
    strings_for_regions, selector_search


# TODO: add "reconcile" command, which markes selected entries with ! and opens a pane with ledger reconcile output
# TODO: add ability to run common reports, and to define new reports in comments in the file

class LedgerCompletions(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if not view.match_selector(locations[0] - 1, 'source.ledger'):
            return
        # Complete according to the scope of the character
        # before the cursor
        # print('START')
        if view.match_selector(locations[0] - 1, selectors['account']):
            return self.complete_account(view)
        elif view.match_selector(locations[0] - 1, selectors['payee']):
            return self.complete_payee(view)
        else:
            return self.complete_misc(view)

    def complete_account(self, view):
        accounts = list_accounts(view)
        # print(accounts)
        return [(x, x) for x in accounts]

    def complete_payee(self, view):
        payees = list_payees(view)
        # print(payees)
        return [(x, x) for x in payees]

    def complete_misc(self, view):
        return self.complete_date(view)

    def complete_date(self, view):
        last_date = strings_for_regions(view, selector_search(view, selectors['date'], 'before'))[-1]
        date_format = guess_date_format(last_date)
        today = datetime.date.today().strftime(date_format)
        yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime(date_format)
        dates = [('today\t' + today, today),
                 ('yesterday\t' + yesterday, yesterday)]
        # print(dates)
        return [x for x in dates]
