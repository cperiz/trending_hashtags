class HashProcessor():

    def __init__(self):
        self.HashCounts = HashCounts()
        self.STOPHASHES = ["#job", "#hiring", "#job?"]

    def process(self, tweet):
        text = tweet['text']
        hashtags = self._return_hashtags_in_text(text)
        for tag in hashtags:
            if tag not in self.STOPHASHES: #: remove unwanted hashes
                self._hash_count_update(tag)

    def _return_hashtags_in_text(self, string):
        #: return set of hashtags
        return {tag.lower() for tag in string.split() if tag.startswith("#")}

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


class ReplyProcessor():

    def __init__(self):
        self.ReplyCounts = ReplyCounts()
        self.STOPREPLIES = ["@"]

    def process(self, tweet):
        text = tweet['text']
        replies = self._return_replies_in_text(text)
        for reply in replies:
            if reply not in self.STOPREPLIES: #: remove unwanted replies
                self._reply_count_update(reply)

    def _return_replies_in_text(self, string):
        #: return set of replies
        return {reply.lower() for reply in string.split() if reply.startswith("@")}

    def _reply_count_update(self, reply):
        self.ReplyCounts.update(reply)

    def get_reply_count(self):
        return self.ReplyCounts.reply_counts

    def get_topX_counts(self, X):
        return sorted(self.ReplyCounts.reply_counts.items(), key=lambda x:x[1], reverse=True)[:X]


class ReplyCounts():

    def __init__(self):
        self.reply_counts = dict()

    def update(self, reply):
        if reply in self.reply_counts.keys():
            self.reply_counts[reply] += 1
        else:
            self.reply_counts[reply] = 1
