"""Sector list + random draw for the daily job search.

The daily routine does NOT get to pick which sectors it searches. It runs this
script, gets 3 sectors at random, and searches only those. That keeps the search
from collapsing back onto the same handful of industries every morning.

Insurance is deliberately absent from this list and is never to be added back:
no carriers, payers, reinsurers, insurtech, brokers, claims platforms, or
actuarial firms.

Usage:
    python sectors.py           # draw 3 sectors, one per line
    python sectors.py -n 5      # draw 5
    python sectors.py --all     # print the whole list
    python sectors.py --seed 7  # reproducible draw (testing only)
"""

import argparse
import random

SECTORS = [
    "SaaS / software vendors",
    "Cloud & infrastructure providers",
    "Fintech & payments",
    "Banking & lending",
    "E-commerce",
    "Cybersecurity",
    "Investment / hedge funds / trading",
    "AdTech / MarTech",
    "Social media / streaming platforms",
    "Consulting firms",
    "Hospitals & health systems",
    "Pharma & biotech",
    "Telecommunications",
    "Retail (brick-and-mortar)",
    "Consumer packaged goods (CPG)",
    "Logistics & freight",
    "Manufacturing",
    "Energy & utilities",
    "Government (federal, state, local)",
    "Gaming",
    "Marketing & advertising agencies",
    "Real estate / PropTech",
    "Accounting & audit",
    "Grocery & food service",
    "Medical devices",
    "Genomics & clinical research",
    "Automotive",
    "Warehousing & fulfillment",
    "Human resources / recruiting",
    "Aerospace & defense",
    "Agriculture / AgTech",
    "Airlines & aviation",
    "Rideshare / mobility",
    "Military / intelligence",
    "Public health agencies",
    "Education (K-12, higher ed, EdTech)",
    "Climate & sustainability",
    "Hospitality & hotels",
    "Travel & tourism",
    "Legal (eDiscovery, legal analytics)",
    "Sports",
    "Gambling / sportsbooks",
    "Academic & scientific research",
    "Mining & metals",
    "Construction",
    "Shipping & maritime",
    "Postal & courier",
    "Nonprofits & NGOs",
    "Think tanks & policy research",
    "News & journalism",
    "Film / TV / entertainment",
    "Publishing",
    "Music",
    "Dating apps",
    "Space (satellites, earth observation)",
    "Weather & climate forecasting",
    "Fashion / apparel",
    "Luxury goods",
    "Cannabis",
    "Museums & cultural institutions",
    "Libraries & archives",
]

# Substrings that must never appear in a sector name. Guards against insurance
# quietly reappearing in the list.
BANNED = ("insur", "reinsur", "actuar", "underwrit", "claims")


def draw(count=3, seed=None):
    """Return `count` distinct sectors drawn at random."""
    rng = random.Random(seed)
    return rng.sample(SECTORS, min(count, len(SECTORS)))


def _check():
    bad = [s for s in SECTORS if any(b in s.lower() for b in BANNED)]
    if bad:
        raise SystemExit("Insurance-related sector found in list: %s" % bad)
    if len(set(SECTORS)) != len(SECTORS):
        raise SystemExit("Duplicate sector in list")


def main():
    p = argparse.ArgumentParser(description="Draw random sectors for the job search.")
    p.add_argument("-n", "--count", type=int, default=3)
    p.add_argument("--all", action="store_true", help="print every sector instead of drawing")
    p.add_argument("--seed", type=int, default=None)
    args = p.parse_args()

    _check()
    for s in (SECTORS if args.all else draw(args.count, args.seed)):
        print(s)


if __name__ == "__main__":
    main()
