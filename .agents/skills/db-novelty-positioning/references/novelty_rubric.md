# Novelty Rubric

- contribution must be specific and testable
- nearest prior must be explicit
- mechanism-level delta must be explicit
- new system capability or formal guarantee must be explicit
- differentiation must be measurable or provable
- title, Abstract, Introduction, contributions, and experiments must share one paper-level subject

Identity risks:
- fatal: the paper claims a complete system, but the narrative repeatedly reduces it to a generic internal component
- fatal: the claimed novelty is an established pattern with only a learned predictor added and no new contract, capability, or evidence
- major: the paper reads as an extension of the nearest system because inherited structure appears before its own design
- major: contributions are abstract while experiments only show implementation gains
- major: companion workloads appear stitched together because their role in one system thesis is unexplained

Safer positioning:
- name the artifact first, then explain its components
- describe what the artifact newly supports under the target constraints
- state which prior design is nearest, what is retained as a design principle, and what mechanism or contract is new
- assign specialized baselines roles such as latency, update, or full-system reference
- map each contribution to one method section and one evidence object

Risk levels:
- fatal: no clear delta vs nearest prior
- major: delta exists but missing key evidence
- moderate: mostly clear, some support gaps
- minor: clear and well-supported
