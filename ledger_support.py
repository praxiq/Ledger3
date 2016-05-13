import re

# I haven't yet finalized scope names. As such, I use this array so that scope name literals
# aren't scattered throughout the code

selectors = {'account': 'other.account.ledger',
             'payee': 'string.unquoted.payee.ledger',
             'strict_account': 'meta.account string.unquoted.account.ledger',
             'strict_payee': 'meta.payee string.unquoted.account.ledger',
             'date': 'constant.numeric.date.ledger',
             'alias': 'string.unquoted.alias.ledger',
             }

def strings_for_regions(view, regions):
    return [view.substr(s).strip() for s in regions]

def selector_search(view, selector, which='all', regions=None):
    # TODO support multiple regions for 'inside' and 'around'
    if regions is None:
        regions = view.selection
    locations = view.find_by_selector(selector)
    if which == 'all':
        return locations
    elif which == 'before':
        return [x for x in locations if x.b < regions[0].a]
    elif which == 'after':
        return [x for x in locations if x.a > regions[-1].b]
    elif which == 'inside':
        return [x for x in locations for r in regions if r.contains(x)]
    elif which == 'around':
        return [x for x in locations for r in regions if r.intersects(x)]

def list_accounts(view, strict=False):
    if strict:
        account_selector = selectors['strict_account']
    else:
        account_selector = selectors['account']
    alias_selector = selectors['alias']
    account_strings = strings_for_regions(view, selector_search(view, account_selector))
    alias_strings = strings_for_regions(view, selector_search(view, alias_selector))
    return list(set(account_strings + alias_strings))

def list_payees(view, strict=False):
    if strict:
        selector = selectors['strict_payee']
    else:
        selector = selectors['payee']
    payee_strings = strings_for_regions(view, selector_search(view, selector))
    return list(set(payee_strings))

def guess_date_format(date):
    first, separator, third = re.match(r'(\d+)([/.-])\d+([/.-]\d+)?', date).groups()
    if third:
        if len(first) == 2:
            year_format = '%y' + separator
        else:
            year_format = '%Y' + separator
    else:
        year_format = ''
    return year_format + '%m' + separator + '%d'
