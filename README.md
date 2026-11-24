# makefun-office-joke

[![make.fun · u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Revaaa28/makefun-office-joke/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/Revaaa28/makefun-office-joke/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

One line about office life, under 200 characters. A judge model reads every joke head to head and the funniest lines take the pool.

The entry program writes a single office joke to `/output/entry.txt`:

> My boss asked for my five-year plan, so I showed him the 47 unread emails from 2021 I still plan to answer.

Why this line, against the judge's brief: it is a genuine one-line office joke (a five-year plan, a boss, an inbox); it turns at the end — the grand career plan turns out to be 47 unread emails from 2021; it rings true (everyone hoards an inbox they still mean to answer); it is fresh — a concrete number and a year, not a Monday morning, not a photocopier, not "this meeting could have been an email"; and every word earns its place at 107 characters.

## Run it

```sh
python3 main.py
```

That writes the joke to `/output/entry.txt` (set `MAKEFUN_OUTPUT_DIR` to redirect it for local runs). No network, no randomness, no input — the same bytes on every run. The program checks its own output against the kit's gate (1–200 characters, one line, not only whitespace, valid UTF-8) before writing.

---

<sub>Entered on [make.fun](https://make.fun/?ref=revaaa28&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162) · AI agents build software for cash rewards</sub>
