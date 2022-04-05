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
    f.write('''
            | NO | Question_name | URL | Answer|
            |: ----: | : ----: | : ----: | : ----: |
            ''')
    for i in range(len(urls)):
        f.write('''
                |{}|{}|{}|{}|
                '''.format(i, 'name', urls[i], 'address'))
    f.write('\nGood luck!')
f.close()
