class HashProcessor():

    def __init__(self):
        self.HashCounts = HashCounts()

    def process(self, tweet):
        text = tweet['text']
        hashtags = self._return_hashtags_in_text(text)
        for tag in hashtags:
            self._hash_count_update(tag)

    def _return_hashtags_in_text(self, string):
        #: return set of hashtags
        return {tag.strip("#").lower() for tag in string.split() if tag.startswith("#")}

    def _hash_count_update(self, hashtag):
        self.HashCounts.update(hashtag)

    def get_hash_count(self):
        return self.HashCounts.hash_counts

    def get_topX_counts(self, X):
        return sorted(self.HashCounts.hash_counts.items(), key=lambda x:x[1], reverse=True)[:X]


class HashCounts():

    def __init__(self):
        self.hash_counts = dict()

    def update(self, hashtag):
        if hashtag in self.hash_counts.keys():
            self.hash_counts[hashtag] += 1
        else:
            self.hash_counts[hashtag] = 1
