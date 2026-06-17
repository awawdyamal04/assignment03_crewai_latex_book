"""Generate ``latex/references.bib`` with real, credible sources (F11).

Eight verifiable references covering the article's arc: cyberbullying research,
online harassment and the law, digital safety / platform responsibility, and
the CrewAI framework. These are genuine publications - no citation is invented,
and no unsupported legal claim is attached to any source. Offline only; no LLM,
no PDF build.
"""

from __future__ import annotations

from pathlib import Path

from src.config import LATEX_DIR, ensure_output_dirs, rel

REFERENCES_PATH: Path = LATEX_DIR / "references.bib"

# Real entries. Keys match the \cite{...} calls in the chapter modules.
BIB = r"""% references.bib - real, credible sources (no invented citations).
@article{patchin2006,
  author  = {Patchin, Justin W. and Hinduja, Sameer},
  title   = {Bullies Move Beyond the Schoolyard: A Preliminary Look at
             Cyberbullying},
  journal = {Youth Violence and Juvenile Justice},
  volume  = {4},
  number  = {2},
  pages   = {148--169},
  year    = {2006},
  doi     = {10.1177/1541204006286288}
}

@article{smith2008,
  author  = {Smith, Peter K. and Mahdavi, Jess and Carvalho, Manuel and
             Fisher, Sonja and Russell, Shanette and Tippett, Neil},
  title   = {Cyberbullying: Its Nature and Impact in Secondary School Pupils},
  journal = {Journal of Child Psychology and Psychiatry},
  volume  = {49},
  number  = {4},
  pages   = {376--385},
  year    = {2008},
  doi     = {10.1111/j.1469-7610.2007.01846.x}
}

@article{tokunaga2010,
  author  = {Tokunaga, Robert S.},
  title   = {Following You Home from School: A Critical Review and Synthesis of
             Research on Cyberbullying Victimization},
  journal = {Computers in Human Behavior},
  volume  = {26},
  number  = {3},
  pages   = {277--287},
  year    = {2010},
  doi     = {10.1016/j.chb.2009.11.014}
}

@article{kowalski2014,
  author  = {Kowalski, Robin M. and Giumetti, Gary W. and Schroeder,
             Amber N. and Lattanner, Micah R.},
  title   = {Bullying in the Digital Age: A Critical Review and Meta-Analysis
             of Cyberbullying Research Among Youth},
  journal = {Psychological Bulletin},
  volume  = {140},
  number  = {4},
  pages   = {1073--1137},
  year    = {2014},
  doi     = {10.1037/a0035618}
}

@book{hinduja2015,
  author    = {Hinduja, Sameer and Patchin, Justin W.},
  title     = {Bullying Beyond the Schoolyard: Preventing and Responding to
               Cyberbullying},
  edition   = {2},
  publisher = {Corwin Press},
  address   = {Thousand Oaks, CA},
  year      = {2015}
}

@book{citron2014,
  author    = {Citron, Danielle Keats},
  title     = {Hate Crimes in Cyberspace},
  publisher = {Harvard University Press},
  address   = {Cambridge, MA},
  year      = {2014}
}

@online{unicef2019,
  author  = {{UNICEF}},
  title   = {Cyberbullying: What Is It and How to Stop It},
  year    = {2019},
  url     = {https://www.unicef.org/end-violence/how-to-stop-cyberbullying},
  urldate = {2026-06-17}
}

@online{crewai2024,
  author  = {{CrewAI, Inc.}},
  title   = {CrewAI: Framework for Orchestrating Role-Playing, Autonomous AI
             Agents},
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
