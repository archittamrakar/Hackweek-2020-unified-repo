import json
import os


class translation(object):

    def __init__(self, language, repo):
        self.language = language
        self.repo = repo
        self.list = os.listdir('../translations/{}'.format(self.repo))
        self.file = '{}.json'.format(language)
        if self.file not in self.list:
            print('{} not found in translations, falling back to en-US'.format(language))
            self.language = 'en-US'
        self.path = '../translations/{}/{}.json'.format(self.repo, self.language)
        self.jsonFile = open(self.path, 'r')
        self.values = json.load(self.jsonFile)

    def tr9(self, _key):
        return self.values[_key]['message']


if __name__ == '__main__':
    obj = translation(repo='exports', language='pt-BR')
    listed = ['issue.type', 'issue.type.issue', 'issue.type.other', 'issue.watchers']
    for key in listed:
        print(obj.tr9(key))
    obj.jsonFile.close()
