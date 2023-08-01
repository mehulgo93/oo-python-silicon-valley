

class Startup:
   all = []
   def __init__(self, name, founderName, domainName):
      self._name = name
      self._founderName =founderName
      self._domaninName = domainName
      Startup.all.append(self)

      @property
      def name(self):
         return self._name
      
      @property
      def founderName(self):
         return self._founderName
      
      @property
      def domainName(self):
         return self._domaninName
      
      def pivot(self, newdomain, new_name):
         self._newdomain = newdomain
         self._newname = new_name
      
      @classmethod
      def all(cls):
         return cls.all_startups

      @classmethod
      def find_by_founder(cls, founder_name):
         for startup in cls.all_startups:
            if startup.founder == founder_name:
               return startup
         return None

      @classmethod
      def domains(cls):
         return list(set([startup.domain for startup in cls.all_startups]))
      
      def sign_contract(self, venture_capitalist, funding_type, investment):
         funding_round = FundingRound(self, venture_capitalist, funding_type, investment)
         self.funding_rounds.append(funding_round)

      def num_funding_rounds(self):
         return len(self.funding_rounds)

      def total_funds(self):
         return sum(fr.investment for fr in self.funding_rounds)

      def investors(self):
         return list(set(fr.venture_capitalist for fr in self.funding_rounds))


      