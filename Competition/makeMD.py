import os

os.chdir('./Competition')
start_description = '''
# Problems
Our problems link are avilable in this table. You can click on problem to redirect to page a answer the question but you must login befor click on it.

'''
files = [item for item in os.listdir(
    '.') if not item.endswith(('md', 'py')) and not item.startswith('.')]

urls = ['https://quera.org/problemset/{}/'.format(item) for item in files]
print(urls)

with open('README.md', 'w') as f:
    f.write(start_description)
    for url in urls:
        f.write(url)
        f.write('\n')
    f.write('\nGood luck!')
f.close()
