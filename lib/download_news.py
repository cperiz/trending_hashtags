from googlesearch.googlesearch import GoogleSearch
import urllib
import json

class DownloadNews():

    def run(self, tag, num_results=1):
        urls = []
        response = GoogleSearch().search(tag, num_results=num_results)
        for result in response.results:
            urls.append(result.url)
        return urls

if __name__ == '__main__':
    d = DownloadNews()
    urls = d.run("bill clinton")
    print(urls)
