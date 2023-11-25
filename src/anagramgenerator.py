class AnagramGenerator:
    def __init__(self, strategy):
        self.strategy = strategy

    def generate(self, corpus):
        return self.strategy.generate(corpus)