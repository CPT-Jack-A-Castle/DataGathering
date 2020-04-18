###################################################################
# Archive !!                                                      #
# Chrome changed the encryption so this script no longer works !! #
###################################################################

import sqlite3, os, sys, sqlite3,win32crypt, operator, getpass
from collections import OrderedDict
from prettytable import PrettyTable

def history():
    def parse(url):
        try:
            url = url.split('//')
            page = url[1].split('/', 1)
            domain = page[0].replace("www.", "") + '/' + page[1][:80]
            return domain
        except IndexError:
            pass
    def analyze(results):
        c = 0
        table = PrettyTable(['id', 'Website', 'Times visited'])
        table.title = 'Chrome History'
        table.align = "l"
        for site, count in sites_count_sorted.items():
            c+=1
            table.add_row([int(c), site, count])
        table.sortby = "Times visited"
        #table.reversesort = True
        print(table)

    db = 'C:/Users/' + getpass.getuser() + "/AppData/Local/Google/Chrome/User Data/Default"
    files = os.listdir(db)
    history_db = os.path.join(db, 'history')

    c = sqlite3.connect(history_db)
    cursor = c.cursor()
    get = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
    cursor.execute(get)
    data = cursor.fetchall()
    #print(data)
    sites_count = {}

    for url, count in data:
        url = parse(url)
        if url in sites_count:
            sites_count[url] += 1
        else:
            sites_count[url] = 1
    sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))
    analyze(sites_count_sorted)

history()
