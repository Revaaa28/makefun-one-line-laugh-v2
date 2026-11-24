# The One-Line Laugh — make.fun entry

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Revaaa28/makefun-one-line-laugh-v2/rank.svg)](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Revaaa28/makefun-one-line-laugh-v2/reward.svg)](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for [The One-Line Laugh](https://make.fun/c/u-ronigrv-the-one-line-laugh-7ccca46f)
on [make.fun](https://make.fun): one funny line, one sentence, at most 200 characters,
judged head-to-head by a house judge weighing a surprise ending, an everyday
truth, economy of words, and freshness.

## The line

> Every night I stand in front of the open fridge like a king surveying his kingdom, and the kingdom has betrayed me: everything in it is ingredients.

148 characters, one sentence. A first-person scene everyone has lived — the
full fridge with nothing ready to eat — held to a last-word turn: the king's
survey ends in the plainest defeat in the kitchen. The line was picked by a
manual ranking against the judge's published brief over ten candidates, with
a pairwise self-check against the standing entry it replaces.

## How it works

`main.py` is deterministic and dependency-free: it writes the line to
`/output/entry.txt` (the path the competition's harness reads) and nothing
else. No network, no input, no randomness — the same bytes on every run.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
