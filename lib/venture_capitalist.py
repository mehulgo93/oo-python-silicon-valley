

class VentureCapitalist:
    all_vcs = []

    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all_vcs.append(self)

    @classmethod
    def all(cls):
        return cls.all_vcs

    @classmethod
    def tres_commas_club(cls):
        return [vc for vc in cls.all_vcs if vc.total_worth > 1000000000]


    def offer_contract(self, startup, funding_type, investment):
        from .funding_round import FundingRound
        funding_round = FundingRound(startup, self, funding_type, investment)
        self.funding_rounds.append(funding_round)

    def funding_rounds(self):
        return self.funding_rounds

    def portfolio(self):
        return list(set(fr.startup for fr in self.funding_rounds))

    def biggest_investment(self):
        if not self.funding_rounds:
            return None
        return max(self.funding_rounds, key=lambda fr: fr.investment)

    def invested(self, domain):
        total_invested = sum(fr.investment for fr in self.funding_rounds if fr.startup.domain == domain)
        return total_invested
