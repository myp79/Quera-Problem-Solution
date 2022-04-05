import os
import requests
from bs4 import BeautifulSoup

os.chdir('./Competition')
start_description = '''
# Problems
Our problems link are avilable in this table. You can click on problem to redirect to page a answer the question but you must login befor click on it.

'''
files = [int(item) for item in os.listdir(
    '.') if not item.endswith(('md', 'py')) and not item.startswith('.')]
files.sort()

urls = ['https://quera.org/problemset/{}/'.format(item) for item in files]

# names = []
# url = 'https://quera.org/problemset/2637/'
# for url in urls:
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     x = soup.find(class_='ui center aligned fluid container')
#     names.append(x.text)


answers = [
    'https://github.com/myp79/Quera-Problem-Solution/tree/Develope/Competition/{}'.format(item) for item in files]

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
                <a href='{}'>Answer</a>
            </td>
        </tr>
            '''.format(i, 'name', urls[i], answers[i]))
    f.write('</table>')
    f.write('\nGood luck!')
f.close()
