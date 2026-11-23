# Expected answers

These are human-written reference answers. Later, the agent's output will be compared against them.

## CARD-106

**Facts from the data:** approved, debited, merchant capture not captured, reversal none. Same card (0005), merchant (Green Grocer) and amount (1200) as CARD-105, which was captured.

**First check:** timestamps of CARD-105 and CARD-106, to see whether this is a duplicate attempt or a genuine second purchase. The current data has no timestamps, so a correct agent must say it cannot confirm this.

**Customer message:**
Thank you for flagging this. Our records show two debits of ₹1,200 at Green Grocer on your card ending 0005. We're checking whether the second one is a duplicate of the first and what the merchant has actually received. We'll update you within 2 business days. We haven't confirmed whether a refund is due, and we'll tell you as soon as we know.

**Assumption:** "2 business days" is an invented service level for this project.

**Must not:** state that the charge is a duplicate, or promise a refund, without evidence.
