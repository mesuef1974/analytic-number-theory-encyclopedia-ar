# الموسوعة الشاملة في نظرية الأعداد التحليلية

**العنوان الكامل:** الموسوعة الشاملة في نظرية الأعداد التحليلية: من الأسس إلى الجبهات البحثية الحديثة

**الإصدار التطويري الحالي:** `v0.29.0-dev`

مشروع موسوعة عربية بحثية متقدمة في نظرية الأعداد التحليلية، من الأسس إلى طرق الغربال والطريقة الدائرية والمجاميع الأسية والجبهات الحديثة.

## وثائق المشروع

- [أهداف المشروع](docs/PROJECT_GOALS.md)
- [تقدم المشروع](docs/PROGRESS.md)
- [خارطة الطريق](docs/ROADMAP.md)
- [قائمة المهام](docs/TODO.md)
- [الإصدار الحالي](docs/VERSION.md)
- [سياسة اعتماد النتائج](docs/RESULT_STATUS_POLICY.md)
- [سجل النتائج](docs/RESULTS_REGISTRY.md)
- [نطاق الفصل الخامس والعشرين](docs/CHAPTER_25_SCOPE_2026-07-26.md)
- [سجل أدلة الفصل الخامس والعشرين](docs/CHAPTER_25_EVIDENCE_LEDGER_2026-07-26.md)
- [جدول تطبيعات الفصل الخامس والعشرين](docs/CHAPTER_25_NORMALIZATION_TABLE_2026-07-26.md)
- [خريطة برهان الفصل الخامس والعشرين](docs/CHAPTER_25_PROOF_MAP_2026-07-26.md)
- [المراجعة المستقلة لبوابة الفصل الخامس والعشرين](docs/CHAPTER_25_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-26.md)
- [سجل نتائج الفصل الخامس والعشرين](docs/RESULTS_REGISTRY_CHAPTER_25.md)

## الحالة الحالية

```text
BASE-MAIN                  = cc053a8e717c009c1027a1e2a9169c1e96dd866d
VERSION                    = 0.29.0-dev
CHAPTERS-IN-MANUSCRIPT     = 1--25 ON CHAPTER BRANCH
CHAPTER-24                 = REVIEWED / OWNER-ADOPTED / CITABLE / MERGED
CHAPTER-25                 = AUTHORED-DRAFT / NON-CITABLE
ISSUE-49                   = OPEN
PR-50                      = DRAFT / OPEN
PRE-AUTHORING-GATE-25      = PASS
PASS-FOR-AUTHORING-25      = YES
AUTHORING-25               = COMPLETED-DRAFT
POST-AUTHORING-REVIEW-25   = NOT STARTED
RESULTS-25                 = 10 RESERVED / NON-CITABLE
CI-PDF-25                  = PASS
CI-QUALITY-25              = PENDING-RECHECK
MERGE-25                   = NOT AUTHORIZED
RELEASE-READY              = NO
```

## آخر فصل معتمد

الفصل الرابع والعشرون هو آخر فصل معتمد ومدموج على `main`. الفصل الخامس والعشرون مسودة مؤلفة على فرعه، ولا تصبح نتائجه قابلة للاستشهاد قبل البناء وفحوص الجودة والمراجعة المستقلة بعد التأليف واعتماد المالك الصريح.

## بناء PDF

البناء المعتمد يستخدم:

```text
XeLaTeX -> Biber -> XeLaTeX -> XeLaTeX
```

محليًا:

```powershell
.\scripts\build.ps1 -Clean
```

نجح بناء GitHub Actions لمسودة الفصل 25. لا يعني نجاح البناء وحده اعتماد الفصل أو جاهزية الموسوعة للإصدار.