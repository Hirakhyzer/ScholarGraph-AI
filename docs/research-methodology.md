# Research Methodology

ScholarGraph AI is framed as a research software project for PhD-level literature intelligence. The methodology below explains how the platform should process scholarly literature while preserving academic integrity.

## 1. Literature ingestion

The system begins with a collection of papers selected by the researcher. Sources may include journal articles, conference papers, thesis chapters, technical reports, and systematic review corpora.

Minimum recommended metadata:

- Title
- Authors
- Year
- Venue
- DOI or URL
- Abstract
- Keywords
- Research domain

## 2. Paper-level extraction

Each paper should be converted into a structured representation.

| Field | Meaning |
|---|---|
| Problem statement | The research problem addressed by the paper |
| Theoretical framing | Concepts, theories, or assumptions used |
| Methodology | The method, model, framework, or study design |
| Dataset / evidence | Data source, participants, corpus, benchmark, or case material |
| Findings | The main result or contribution |
| Limitations | Weaknesses acknowledged by authors or inferred from design |
| Future work | Directions suggested by the paper |

## 3. Cross-paper synthesis

After paper-level extraction, the system groups papers by shared characteristics.

Possible grouping dimensions:

- Research problem
- Methodological approach
- Dataset or evidence type
- Evaluation metric
- Target population
- Theoretical lens
- Limitation type
- Future-work direction

## 4. Gap analysis

A research gap is not simply an empty topic. A defensible PhD-level gap should be supported by evidence from the literature.

ScholarGraph AI classifies gap signals into categories:

| Gap Type | Explanation |
|---|---|
| Empirical gap | Missing or weak evidence in a context, population, or dataset |
| Methodological gap | Existing methods have limitations or untested assumptions |
| Theoretical gap | Existing work lacks conceptual clarity or explanatory power |
| Evaluation gap | Metrics, baselines, or validation protocols are insufficient |
| Reproducibility gap | Results cannot be easily replicated or audited |
| Practical gap | Existing solutions are not evaluated in realistic settings |

## 5. Research question generation

Research questions should be generated only after evidence has been organized. A good research question should be:

- Specific enough to investigate.
- Grounded in literature evidence.
- Methodologically feasible.
- Academically meaningful.
- Ethically acceptable.
- Connected to a potential contribution.

## 6. Thesis roadmap construction

A thesis roadmap should translate the literature analysis into a multi-stage research plan.

Recommended roadmap structure:

1. Research area and motivation.
2. Literature clusters and key debates.
3. Evidence-based research gap.
4. Main research question.
5. Sub-questions.
6. Methodology and data strategy.
7. Evaluation and validation plan.
8. Expected contributions.
9. Publication plan.
10. Dissertation chapter plan.

## 7. Human verification requirement

ScholarGraph AI should never be treated as an authority by itself. Every generated theme, gap, and research question must be checked against original papers. The system should help organize scholarly reasoning, not replace it.
