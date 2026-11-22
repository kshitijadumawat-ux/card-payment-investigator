# Card Payment Investigator

AI agent that investigates failed debit-card payments, using synthetic data only.

## The problem
A customer pays ₹1,500 by debit card. The merchant says the payment failed, but the customer sees the money debited or blocked, and complains. A card-operations analyst then has to check several separate systems (authorization, ledger posting, merchant capture, reversal status) and piece together what happened. The work is slow, repetitive, and easy to get wrong, and the customer waits in the meantime.

## How we'd measure it
- Time to investigate one case: about 20 minutes (estimate)
- Systems checked per case: 3 to 4 (estimate)
- Cases where the first answer to the customer was incomplete or wrong: about 1 in 10 (estimate)

These are assumptions to be replaced with real observations or clearly labeled test results.

## What better looks like
Investigation time drops from about 20 minutes to under 5 minutes per case, with the evidence for each answer shown, and an analyst reviews the result before anything is sent to the customer.

## What it must never do
- Never move money, change a balance, or start a refund.
- Never tell a customer a refund is complete unless the evidence shows it.
- Never invent a transaction detail. If evidence is missing, say so.
- Any financial adjustment needs a human to approve it.

## Note
This project uses synthetic (invented) data only. It does not use any real customer or employer information.
