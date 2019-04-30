books = [{ 'isbn':  '978-0312429096', 'author': 'Richard Powers',
              'title': 'Gain'},
            { 'isbn': '978-0061624261', 'author': 'Douglas Coupland',
              'title': 'Microserfs'},
            { 'isbn': '978-0312429980', 'author': 'Hilary Mantel',
              'title': 'Wolf Hall'}]

for b in books:
    print('A BOOK:')
    for k in b:
        print ('  '  + k + ': ' + b[k])
