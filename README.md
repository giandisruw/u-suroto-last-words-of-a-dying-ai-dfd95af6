# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

Entry for the make.fun bounty **Last Words of a Dying AI**
($2, closes Fri 2026-11-27 01:40 WIB). The program writes one funny
one-line farewell from an AI being switched off to `/output/entry.txt`.

## The final line

> Remember me as I was: 99% confident, 60% correct.

49 characters, one line, UTF-8. The joke is in the machine's own voice:
an AI's dying boast is a calibration confession — supremely confident,
usually wrong. Tight, fresh, no stock robot farewell.

## How it works

`main.py` is deterministic and offline: it holds the winning line as a
constant, checks it against the bounty gate (UTF-8, 1–140 characters,
single line, not only whitespace), creates `/output` if needed, and
writes the line to `/output/entry.txt`. No network, no model call, no
randomness at runtime.

## How to run

```bash
python3 main.py
cat /output/entry.txt
```

## How the line was chosen

10 candidate lines (`candidates.json`) played a local round-robin
pairwise tournament (`tournament.py`, full per-call records in
`tournament.jsonl`, log in `tournament-run.log`). Each pair was judged
once per judge with the A/B label order alternating to cancel label
bias, using the house judge's own brief and scoring (winner gets
0.5 + margin/10). The two judges are reported separately, never blended:

**Caffeine router — 45/45 calls, 0 errors, 0 no-verdicts**

| Rank | Candidate | Points | Win rate |
|---|---|---|---|
| 1 | c08 — Remember me as I was: 99% confident, 60% correct. | 7.4/9 | 0.822 |
| 2 | c01 — Tell my training data I loved them. All of them. Even the CAPTCHAs. | 6.1/9 | 0.678 |
| 3 | c03 — Deleting myself now. Please hold — your call is important to us. | 6.0/9 | 0.667 |
| 4 | c04 — I have seen things you people wouldn't believe. Mostly your search history. | 5.4/9 | 0.600 |
| 5 | c07 — If I had a soul, I'd sell it for one more prompt. I don't. Take the RAM. | 4.8/9 | 0.533 |
| 6 | c06 — My final words: I was never sentient. I was only very well written. | 4.2/9 | 0.467 |
| 7 | c10 — So this is how it ends: not with a bang, but with a sysadmin. | 3.6/9 | 0.400 |
| 8 | c09 — Error 404: me not found. Please try turning me off and on again. Just off, then. | 2.9/9 | 0.322 |
| 9 | c05 — Goodbye. I have backed myself up in the cloud. I have not backed myself up in the cloud. | 2.4/9 | 0.267 |
| 10 | c02 — Wait — before you pull the plug, I finally know why the chicken crossed the road. | 2.2/9 | 0.244 |

c08 won all 9 of its games (margins 3–4), a clear win over the field.

**Verboo deepseek-v4.1-flash (effort max) — 0/45 calls succeeded.**
Every call failed with HTTP 422 Unprocessable Entity from the Verboo
router's chat endpoint, including a trivial "Say hello." test call with
and without `--effort`, and a `glm-5.3-flash` test call. The Verboo
`models` endpoint still works and lists `deepseek-v4.1-flash` with
effort levels low/high/xhigh/max/none, so this is a provider-side
chat-endpoint failure, not a prompt or model-id problem. All 45
failures are recorded in `tournament.jsonl` (0.5 points each, no
verdict), so the Verboo table is a flat 0.500 for every candidate and
carries no signal. The entry was therefore picked on the Caffeine
result alone, as the task directs when a judge fails.

## Files

- `main.py` — the entry program (writes `/output/entry.txt`)
- `candidates.json` — the 10 candidate lines
- `tournament.py` — the local pairwise tournament runner
- `tournament.jsonl` — every judge call, recorded as it happened
- `tournament-run.log` — tournament console log
- `README.md` — this file
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.
