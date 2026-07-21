# oddsinfer

Overround correction and probability inference for betting markets — implements the Additive, Multiplicative, Power, and Shin methods for converting bookmaker odds into valid probabilities, plus Brier and Log-Loss scoring to evaluate them.

Full write-up of the underlying maths (derivations, proofs, and empirical results) is available in [report.pdf](./report.pdf).

## Install

```bash
pip install git+https://github.com/JamesRestell8/oddsinfer.git
```

## Usage

```python
from oddsinfer.overround import additive, multiplicative, power, shin
from oddsinfer.scoring import brier, log_loss

odds = [4, 5, 6, 3.8, 4]
probs = shin(odds)

brier(probs, outcome_index=0)
log_loss(probs, outcome_index=0)
```

## License

MIT