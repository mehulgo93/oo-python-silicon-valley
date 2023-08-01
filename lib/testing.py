from .funding_round import FundingRound
from .startup import Startup
from .venture_capitalist import VentureCapitalist




# Assuming you have already implemented the classes Startup, VentureCapitalist, and FundingRound

# Create some venture capitalists
vc1 = VentureCapitalist("John Smith", 2000000000)
vc2 = VentureCapitalist("Jane Doe", 800000000)
vc3 = VentureCapitalist("Mike Johnson", 1500000000)

# Create some startups
startup1 = Startup("Example Inc.", "John Doe", "example.com")
startup2 = Startup("Sample Co.", "Jane Smith", "sampleco.com")

# Venture capitalists offer contracts to startups
vc1.offer_contract(startup1, "Series A", 5000000.0)
vc1.offer_contract(startup2, "Seed", 1000000.0)
vc2.offer_contract(startup1, "Angel", 2000000.0)
vc3.offer_contract(startup1, "Series A", 3000000.0)

# Get all startups and venture capitalists
all_startups = Startup.all()
all_vcs = VentureCapitalist.all()

# Check number of startups and venture capitalists
assert len(all_startups) == 2
assert len(all_vcs) == 3

# Test FundingRound methods
funding_round1 = startup1.funding_rounds[0]
funding_round2 = startup1.funding_rounds[1]
assert funding_round1.startup == startup1
assert funding_round1.venture_capitalist == vc1
assert funding_round1.type == "Series A"
assert funding_round1.investment == 5000000.0

# Test Startup methods
assert startup1.num_funding_rounds() == 3
assert startup1.total_funds() == 11000000.0
assert set(startup1.investors()) == {vc1, vc2, vc3}
assert set(startup1.big_investors()) == {vc1, vc3}

# Test VentureCapitalist methods
assert set(vc1.funding_rounds()) == {funding_round1, funding_round2}
assert set(vc1.portfolio()) == {startup1, startup2}
assert vc1.biggest_investment() == funding_round1
assert vc1.invested("example.com") == 8000000.0
assert vc1.invested("sampleco.com") == 1000000.0

print("All tests passed!")



