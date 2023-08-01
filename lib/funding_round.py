class FundingRound:
    all_funding_rounds = []

    def __init__(self, startup, venture_capitalist, funding_type, investment):
        self.startup = startup
        self.venture_capitalist = venture_capitalist
        self.type = funding_type
        self.investment = float(investment)
        FundingRound.all_funding_rounds.append(self)

    @classmethod
    def all(cls):
        return cls.all_funding_rounds
