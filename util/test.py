from translation import *

if __name__ == '__main__':
    obj = translation(repo='exports', language='pt-BR')
    listed = ['issue.type', 'issue.type.issue', 'issue.type.other', 'issue.watchers']
    for key in listed:
        print(obj.tr9(key))
    obj.jsonFile.close()
