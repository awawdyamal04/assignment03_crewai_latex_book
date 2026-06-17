"""Generate ``latex/references.bib`` with real, course-relevant sources (F11).

Eight verifiable references covering the article's arc: backprop/RNNs, the
vanishing-gradient analysis, LSTM, GRU, additive attention, the Transformer,
BERT, and the CrewAI framework. These are genuine publications — no citation
is invented. Offline only; no LLM, no PDF build.
"""

from __future__ import annotations

from pathlib import Path

from src.config import LATEX_DIR, ensure_output_dirs, rel

REFERENCES_PATH: Path = LATEX_DIR / "references.bib"

# Real entries. Keys match the \cite{...} calls in latex_body.py.
BIB = r"""% references.bib — real, course-relevant sources (no invented citations).
@article{rumelhart1986,
  author  = {Rumelhart, David E. and Hinton, Geoffrey E. and Williams, Ronald J.},
  title   = {Learning representations by back-propagating errors},
  journal = {Nature},
  volume  = {323},
  number  = {6088},
  pages   = {533--536},
  year    = {1986},
  doi     = {10.1038/323533a0}
}

@article{bengio1994,
  author  = {Bengio, Yoshua and Simard, Patrice and Frasconi, Paolo},
  title   = {Learning long-term dependencies with gradient descent is difficult},
  journal = {IEEE Transactions on Neural Networks},
  volume  = {5},
  number  = {2},
  pages   = {157--166},
  year    = {1994},
  doi     = {10.1109/72.279181}
}

@article{hochreiter1997,
  author  = {Hochreiter, Sepp and Schmidhuber, J{\"u}rgen},
  title   = {Long Short-Term Memory},
  journal = {Neural Computation},
  volume  = {9},
  number  = {8},
  pages   = {1735--1780},
  year    = {1997},
  doi     = {10.1162/neco.1997.9.8.1735}
}

@inproceedings{cho2014,
  author    = {Cho, Kyunghyun and van Merri{\"e}nboer, Bart and Gulcehre, Caglar
               and Bahdanau, Dzmitry and Bougares, Fethi and Schwenk, Holger
               and Bengio, Yoshua},
  title     = {Learning Phrase Representations using RNN Encoder--Decoder for
               Statistical Machine Translation},
  booktitle = {Proceedings of EMNLP},
  pages     = {1724--1734},
  year      = {2014},
  doi       = {10.3115/v1/D14-1179}
}

@inproceedings{bahdanau2015,
  author    = {Bahdanau, Dzmitry and Cho, Kyunghyun and Bengio, Yoshua},
  title     = {Neural Machine Translation by Jointly Learning to Align and Translate},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2015},
  eprint    = {1409.0473},
  archivePrefix = {arXiv}
}

@inproceedings{vaswani2017,
  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit,
               Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, Lukasz
               and Polosukhin, Illia},
  title     = {Attention Is All You Need},
  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
  volume    = {30},
  year      = {2017},
  eprint    = {1706.03762},
  archivePrefix = {arXiv}
}

@inproceedings{devlin2019,
  author    = {Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  title     = {{BERT}: Pre-training of Deep Bidirectional Transformers for
               Language Understanding},
  booktitle = {Proceedings of NAACL-HLT},
  pages     = {4171--4186},
  year      = {2019},
  doi       = {10.18653/v1/N19-1423}
}

@online{crewai2024,
  author  = {{CrewAI, Inc.}},
  title   = {CrewAI: Framework for Orchestrating Role-Playing, Autonomous AI Agents},
  year    = {2024},
  url     = {https://docs.crewai.com},
  urldate = {2026-06-17}
}
"""


def build_references() -> Path:
    """Write ``latex/references.bib``; return its path."""
    ensure_output_dirs()
    REFERENCES_PATH.write_text(BIB, encoding="utf-8")
    return REFERENCES_PATH


if __name__ == "__main__":  # pragma: no cover - convenience entry point
    print(f"written: {rel(build_references())}")
