# Candidates — One-Line Office Joke: 24-Hour Sprint

Competition: `u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162` ($2, top 8 paid).
Judge brief criteria, in the kit's stated order:
1. A genuine one-line joke about office life (not a caption, quip, or stray observation).
2. Funny: the punchline surprises and pays off the setup in a way anyone who has sat in an office recognises.
3. One line: a single sentence, or a setup and punchline on one line, no rambling.
4. Fresh: a specific detail of office life, not a generic complaint, not a joke everyone has already heard.
5. Clear on first read: no explanation needed, tight wording.

Target shape (from prior finals pattern): 100–160 chars, at least two beats
(setup → turn/reframe), one concrete detail, punch in the last 3–5 words.
Top one-liners in cousin finals run 93–154 chars with a direct second-person
hook or a concrete number.

## The candidates

| # | Chars | Line |
|---|-------|------|
| C1 | 107 | My boss asked for my five-year plan, so I showed him the 47 unread emails from 2021 I still plan to answer. |
| C2 | 127 | The meeting could have been an email, the email could have been a Slack message, and the Slack message could have been silence. |
| C3 | 109 | Our printer has been out of toner since March, yet somehow it still prints the 'low toner' warning perfectly. |
| C4 | 114 | HR said bring my whole self to work, so I brought my blanket, my pillow, and my resignation letter — just in case. |
| C5 | 110 | We spent forty-five minutes in a meeting about meetings, then booked a follow-up to decide when to meet again. |
| C6 | 105 | My out-of-office says I'm on holiday, my laptop says I'm in a meeting, and my boss says I am the meeting. |
| C7 | 118 | I asked IT for a second monitor and got a ticket number, a lecture on minimalism, and a chair that squeaks in D minor. |
| C8 | 108 | Our standup lasts thirty minutes because everyone stands up, sits down, and then explains why they sat down. |
| C9 | 111 | I told my boss I was working from home today; technically, the office Wi-Fi reaches the café across the street. |
| C10 | 111 | The office coffee tastes like it was brewed during last quarter's budget review — and nobody dares to complain. |
| C11 | 107 | My calendar finally had a free hour, so I booked a meeting called 'Do Not Disturb' and invited only myself. |
| C12 | 93 | I set my Slack status to 'in a meeting' at 9 a.m. and my calendar has believed me ever since. |

(Char counts verified with Python `len()` on the exact strings; C4/C9/C10 are
116/112/113 bytes because of the em dash / apostrophe.)

## Manual ranking (no judge API, no Gemini, no NVIDIA — manual only, per Rev's rule)

Criterion 1 — all twelve are genuine one-line office jokes; nobody fails the gate.
Criterion 3 — all twelve are single sentences; tie across the board.
So the ranking is decided by criteria 2, 4, and 5.

**Criterion 2 (funny — surprise payoff, recognisable):**
Strongest payoffs: C1 (a five-year plan that is just a stale inbox), C2
(triple escalation landing on "silence"), C4 (resignation letter smuggled
into the bring-your-whole-self list), C7 (the chair squeaking in D minor),
C3 (the printer that can only print its own low-toner warning). Mid: C5,
C11, C9, C6, C8. Weakest: C10 (bad-coffee complaint, no real turn) and C12
(a single observation with a thin punch).

**Criterion 4 (fresh — specific detail, not heard before):**
Freshest: C1 (concrete number 47 + year 2021 — a detail nobody else's joke
carries), C7 (D minor chair), C3 ("since March" + the self-printing warning),
C11 (a "Do Not Disturb" meeting with one invitee: yourself).
Stale: C2's opening IS the single most-told office joke in existence ("this
meeting could have been an email") — the brief explicitly penalises "a joke
everyone has already heard". The escalation is the fresh part, but the first
half is the cliché verbatim. C5 (meeting about meetings) and C10 (bad office
coffee) are equally well-worn tropes; C12 (Slack status) is a common shape;
C6 (out-of-office) is a common family and overlaps the theme of our own
sibling entry in the other office-jokes competition, so it is out on
freshness grounds too.

**Criterion 5 (clear, tight):** C1, C2, C3, C11 are the tightest. C7's setup
runs slightly long but earns it with the punch. Nothing is unclear anywhere.

## Ranking

1. **C1** — 2. C2 — 3. C7 — 4. C3 — 5. C4 — 6. C11 — 7. C5 — 8. C9 — 9. C8 — 10. C6 — 11. C10 — 12. C12

## Pairwise checks (first differing brief criterion decides)

- **C1 vs C2:** both pass 1–3. Criterion 4 decides: C2 opens with the
  cliché itself; C1's 47-unread-emails-from-2021 detail is fresh. **C1 wins.**
- **C1 vs C7:** both fresh. Criterion 2 decides: C1's payoff is universally
  recognisable (everyone hoards unread emails); C7's D-minor punch is absurd
  but narrower. **C1 wins.**
- **C1 vs C3:** criterion 2 — C1 has two beats (plan → emails) against C3's
  single irony. **C1 wins.**
- **C1 vs C4:** criterion 4 — C4's "bring your whole self" HR phrase is a
  known trope; C1's number + year is fresher. **C1 wins.**
- **C1 vs C11:** criterion 2 — C11's "invited only myself" is good, but C1's
  misdirection (a five-year plan that is just a stale inbox) is the bigger
  surprise. **C1 wins.**

## Chosen entry

> My boss asked for my five-year plan, so I showed him the 47 unread emails from 2021 I still plan to answer.

107 characters / 107 bytes. Two beats (five-year plan → the inbox as the
plan), concrete detail (47 unread emails from 2021), punch in the last five
words ("I still plan to answer"). One sentence, one line, no explanation
needed.
