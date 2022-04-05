import os

os.chdir('./Competition')
start_description = '''
# Problems
Our problems link are avilable in this table. You can click on problem to redirect to page a answer the question but you must login befor click on it.

'''
files = [int(item) for item in os.listdir(
    '.') if not item.endswith(('md', 'py')) and not item.startswith('.')]
files.sort()

urls = ['https://quera.org/problemset/{}/'.format(item) for item in files]


with open('README.md', 'w') as f:
    f.write(start_description)
    f.write('''<table border="0" cellspacing="0" cellpadding="0" align="center">
                <tr>
                    <td align="center">
                        NO
                    </td>
                    <td align="center">
                        Question name
                    </td>
                    <td align="center">
                        URL
                    </td>
                    <td align="center">
                        Answer
                    </td>
                </tr>
        ''')
    for i in range(len(urls)):
        f.write(
            '''<tr>
            <td align="center">
                {}
            </td>
            <td align="center">
                {}
            </td>
            <td align="center">
                {}
            </td>
            <td align="center">
                {}
            </td>
        </tr>
            '''.format(i, 'name', urls[i], 'address'))
    f.write('</table>')
    f.write('\nGood luck!')
f.close()
