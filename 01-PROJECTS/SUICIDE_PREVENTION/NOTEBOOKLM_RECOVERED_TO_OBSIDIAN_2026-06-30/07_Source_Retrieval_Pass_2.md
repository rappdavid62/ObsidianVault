# Source Retrieval Pass 2 — Live Fetch Results

Prepared: 2026-07-01  
Method: Direct URL fetch of indexed sources from the handoff packet + PubMed abstract retrieval + web search for corrected citations.

## Access Honesty

This pass used Antigravity's `read_url_content` and `search_web` tools to fetch live data from indexed URLs. CDC and NIMH pages returned mostly navigation HTML (JavaScript-rendered content) rather than article text. PubMed abstracts were successfully retrieved for key papers. Two PMIDs in the original handoff were incorrect and have been corrected below.

---

## PMID Corrections

The original handoff packet contained incorrect PMIDs for two key sources:

### Motto & Bostrom — Caring Letters RCT
- **Wrong PMID in handoff**: 11775719 (actually: "Evaluations of the quality of coping reported by prisoners who have self-harmed")
- **Correct PMID**: **11376235**
- **Correct citation**: Motto JA, Bostrom AG. A randomized controlled trial of postcrisis suicide prevention. *Psychiatric Services*. 2001;52(6):828-833. doi:10.1176/appi.ps.52.6.828
- **Key finding**: "A systematic program of contact with persons who are at risk of suicide and who refuse to remain in the health care system appears to exert a significant preventive influence for at least two years."
- **URL**: https://pubmed.ncbi.nlm.nih.gov/11376235/

### Luxton et al. — Caring Letters in Military/VA
- **Wrong PMID in handoff**: 24582736 (actually: a flatfish phylogenetics paper)
- **Correct reference**: Luxton DD et al. Caring emails for military and veteran suicide prevention: A randomized controlled trial. *Suicide and Life-Threatening Behavior*. 2020.
- **Updated finding from 2024 JAMA Network Open large-scale RCT (102,000+ VCL callers)**: Caring Letters did not significantly reduce suicide attempts, BUT were associated with higher probability of veterans using VA mental healthcare resources.
- **Nuance for State Not Fate**: Caring contacts are best framed as connection-maintenance and help-seeking facilitation rather than a standalone suicide-prevention intervention.

---

## Successfully Retrieved Source Abstracts & Search Results

### Stanley et al. — Safety Planning Intervention + Follow-up (PMID 29998307)
- **Citation**: Stanley B et al. Comparison of the Safety Planning Intervention With Follow-up vs Usual Care of Suicidal Patients Treated in the Emergency Department. *JAMA Psychiatry*. 2018;75(9):894-900.
- **Key finding**: "SPI+ was associated with a reduction in suicidal behavior and increased treatment engagement among suicidal patients following ED discharge and may be a valuable clinical tool in health care settings."
- **Strength**: Large-scale cohort comparison
- **Relevance to SNF**: Strongest evidence that safety planning + structured follow-up reduces suicidal behavior. This is the backbone for SNF's safety planning integration.

### Favril et al. — Individual-Level Risk Factors Umbrella Review
- **Citation**: Favril L et al. Individual-level risk factors for suicide mortality in the general population: an umbrella review. *The Lancet Public Health*. 2024;11(1):e68-e82. doi:10.1016/S2468-2667(23)00207-4
- **Key finding**: Umbrella review of risk factor evidence across general population
- **Relevance to SNF**: Use to validate the risk-stack model; avoid presenting risk factors as deterministic prediction tools

### Gallagher et al. — Social Determinants Umbrella Review
- **Citation**: Gallagher et al. Social determinants of suicide: an umbrella review. *Epidemiologic Reviews*. 2024. doi:10.1093/epirev/mxaf004
- **Key finding**: Upstream social determinants framing for suicide prevention
- **Relevance to SNF**: Supports the systems-failure framing — suicide emerges from conditions, not just individual psychology

### Trevor Project — 2025 U.S. National Survey (May 2026 Release)
- **Sample**: 16,000+ LGBTQ+ youth ages 13-24
- **Key Statistics**:
  - **36%** of LGBTQ+ young people seriously considered suicide in the past year (**40%** among transgender and nonbinary youth).
  - **1 in 10** attempted suicide in the past year.
  - **47%** experienced depression symptoms (**51%** for trans/nonbinary, **39%** for cisgender).
  - **44%** who sought care were unable to access it (improved from 50% in 2024).
  - **21%** reported threats or physical harm (**23%** for trans/nonbinary).
- **Protective Factors**: 
  - LGBTQ+ youth living in very accepting communities attempted suicide at **less than one-third** of the rate of those who did not.
  - Pronoun respect, access to gender-neutral bathrooms, and gender-aligned clothing were associated with significantly lower suicidality.
- **Relevance to SNF**: Emphasize that community acceptance, basic respect, and safety are highly predictive protective factors.

### SAVE — Media Recommendations for Responsible Coverage
- **Source**: consensus-based guidelines from ReportingonSuicide.org
- **Language Rules**:
  - *Avoid*: "committed suicide", "successful attempt", "failed attempt", "completed suicide".
  - *Use*: "died by suicide", "killed him/herself", "attempted to take his/her life".
- **Coverage Rules**:
  - Report as a public health issue focusing on hope, recovery, and prevention.
  - Minimize specific details about the method or location.
  - Avoid quoting or summarizing suicide notes.
  - Focus on hope and stories of individuals who overcame crises.
- **Relevance to SNF**: Apply strictly to all user-facing copy, articles, and app logs.

### Action Alliance — Grief, Trauma, and Distress After a Suicide (U.S. National Guidelines)
- **Purpose**: A national blueprint for **postvention** (organized response to a suicide death).
- **Application**: Workplaces, places of worship, schools, military, and general organizations.
- **Goals**:
  1. *Facilitate healing*: Compassionate outreach and support to survivors.
  2. *Reduce risk*: Supporting high-risk individuals exposed to the loss to mitigate contagion.
  3. *Community stability*: Trauma-informed organizational stabilization.
- **Relevance to SNF**: Design a postvention support guide for friends, families, and workplace leaders.

### WHO — LIVE LIFE Initiative for Suicide Prevention
- **Core Elements**:
  - **4 Key Interventions**:
    1. Limiting access to means of suicide.
    2. Responsible media reporting.
    3. Fostering socio-emotional life skills in adolescents.
    4. Early identification, assessment, management, and follow-up.
  - **6 Foundational Pillars**: Situation analysis, multisectoral collaboration, awareness/advocacy, capacity building, financing, surveillance/monitoring.
- **Relevance to SNF**: Positions SNF as a contributor to adolescent and adult socio-emotional life skills, early identification, and follow-up support.

---

## Gap Analysis After This Pass

### Gaps Successfully Narrowed
- ✅ PMID corrections for Motto and Luxton — now have correct citations
- ✅ Stanley safety planning abstract verified with key finding
- ✅ Caring contacts evidence updated with 2024 large-scale RCT results
- ✅ Official source freshness verified (CDC updated May 2026, NIMH has restructuring caveat)
- ✅ Trevor Project 2025 survey, SAVE safe messaging, Action Alliance postvention, and WHO LIVE LIFE frameworks fetched and summarized

### Gaps Still Open
1. **Perinatal/postpartum suicide**: ACOG sources (indexed as #17, #18) not fetched — these require clinical guideline access.
2. **VA/DoD 2024 Clinical Practice Guideline**: PDF URL indexed (#14) — not fetched (508-page PDF).
3. **IHS tribal prevention**: URL indexed (#31) — partially fetched, need to extract details if needed.

### Gaps That Require David's Files
4. **NotebookLM direct export** — still the biggest single gap.
5. **Drive corpus listing** — `CHATGPT_MASTER_context`, `AI_Life_Coach_Friend`.
6. **Local .docx files**: `five_year_depression_implementation_manual_2026.*`, `Copy of suicide prevention packet.docx`.
