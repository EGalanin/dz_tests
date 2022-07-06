import requests

with open('token.txt', 'r') as f:
    token_YD = f.read().strip()

class YaDisk:

    def __init__(self, token, folder_name):
        self.token = token
        self.folder_name = folder_name
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.params = {"path": self.folder_name, "overwrite": "true"}


    def get_folder(self):
        res = requests.put(self.url, headers=self.headers, params=self.params)
        # print(res.status_code)
        return res.status_code

    def del_folder(self):
        res = requests.delete(self.url, headers=self.headers, params=self.params)
        # print(res.status_code)
        return res.status_code

    def info_to_folder(self):
        res = requests.get(self.url, headers=self.headers, params=self.params)
        # print(res.status_code)
        # print(res.text)
        return res.status_code







if __name__ == '__main__':
    uploader = YaDisk(token_YD, "TEST")
    result = uploader.get_folder()
    del_ = uploader.del_folder()
    info = uploader.info_to_folder()
