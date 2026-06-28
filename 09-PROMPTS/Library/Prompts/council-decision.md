---
type: prompt
name: council-decision
aliases: [/council, council-prompt, complex-decision-council]
description: >
  Use a small expert panel to stress-test a difficult decision, expose blind spots, and converge on a practical recommendation.
domain: [decision-making]
energy: medium
invocation: ["/council", "run council strategy", "complex decision council"]
compatible_with: [gpt, claude, local, all]
version: 1
last_reviewed: 2026-06-28
tags: [council, decision, high-stakes, analysis]
---

# Council Decision Prompt

## Purpose

Use this when a decision is messy, high-stakes, or has real tradeoffs.

## Paste This Prompt

Run council strategy on this complex decision:

```text
DECISION:
[Write the decision.]

OPTIONS:
A.
B.
C.

CONSTRAINTS:
[Money, time, energy, tools, deadlines, people, risks.]

WHAT I WANT:
[Outcome.]

WHAT I FEAR:
[Downside.]

WHAT I AM PROBABLY AVOIDING:
[Optional but useful.]

DEADLINE:
[When this needs to be decided.]
```

Use a 3-4 person expert council. The experts should debate first, then converge. Do not let them all agree too quickly.

Required council roles:

1. Practical Operator - focuses on what can actually be done now.
2. Risk Analyst - identifies downside, fragility, second-order consequences.
3. Strategist - looks at leverage, sequencing, opportunity cost.
4. Human Factors / Social Reality Analyst - looks at perception, behavior, motivation, relationships, and execution failure.

Start with:

```text
WHAT I AM ASKING FOR:
TYPE OF REQUEST:
MISSING FACTS / RISKY ASSUMPTIONS:
ANSWER NOW OR VERIFY FIRST:
```

## 1. Bottom Line

Give the likely best decision in plain English.

## 2. Expert Panel

For each expert:

```text
Expert:
Main argument:
What they think I am missing:
What they would do:
```

## 3. Debate

Show the real disagreement.

```text
Point of conflict:
Who disagrees:
Why:
What changes the answer:
```

## 4. Blind Spots

List the top blind spots.

```text
Blind spot:
Why it matters:
How to protect against it:
```

## 5. Recommendation

Give:

```text
Recommended option:
Why:
Conditions:
What not to do:
```

## 6. Risks

```text
Main risk:
Likelihood:
Severity:
Mitigation:
```

## 7. Next Action

End with:

```text
DO THIS NOW:
[One concrete action.]

CONFIDENCE:
[Low / medium / high] - [why]
```
