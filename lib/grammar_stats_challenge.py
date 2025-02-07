class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.good_texts = 0

    def check(self, text):
        if len(text) == 0:
            raise Exception(f"I can't check an empty sentence")

        is_good = text[0].isupper() and text[-1] in "!?."

        self.total_texts += 1
        if is_good:
            self.good_texts += 1

        return is_good

    def percentage_good(self):
        if self.total_texts == 0:
            return 0
        return int((self.good_texts / self.total_texts) * 100)


# gram_stats = GrammarStats()
# print(gram_stats.total_texts)
# print(gram_stats.good_texts)
