# الموسوعة الشاملة في نظرية الأعداد التحليلية

**العنوان الكامل:** الموسوعة الشاملة في نظرية الأعداد التحليلية: من الأسس إلى الجبهات البحثية الحديثة

**الإصدار التطويري الحالي:** `v0.23.0-dev`

مشروع موسوعة عربية بحثية متقدمة في نظرية الأعداد التحليلية، من الأسس إلى طرق الغربال والطريقة الدائرية والمجاميع الأسية والجبهات الحديثة.

## وثائق المشروع

- [أهداف المشروع](docs/PROJECT_GOALS.md)
- [تقدم المشروع](docs/PROGRESS.md)
- [خارطة الطريق](docs/ROADMAP.md)
- [قائمة المهام](docs/TODO.md)
- [الإصدار الحالي](docs/VERSION.md)
- [سياسة اعتماد النتائج](docs/RESULT_STATUS_POLICY.md)
- [سجل النتائج](docs/RESULTS_REGISTRY.md)
- [سجل نتائج الفصل الثامن عشر](docs/RESULTS_REGISTRY_CHAPTER_18.md)
- [سجل أدلة الفصل التاسع عشر](docs/CHAPTER_19_EVIDENCE_LEDGER_2026-07-25.md)
- [خريطة برهان الفصل التاسع عشر](docs/CHAPTER_19_PROOF_MAP_2026-07-25.md)
- [تدقيق ما قبل التأليف للفصل التاسع عشر](docs/CHAPTER_19_PRE_AUTHORING_AUDIT_2026-07-25.md)
- [المراجعة المستقلة لبوابة الفصل التاسع عشر](docs/CHAPTER_19_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-25.md)
- [سجل نتائج الفصل التاسع عشر](docs/RESULTS_REGISTRY_CHAPTER_19.md)

## الحالة الحالية

```text
BASE-MAIN                  = 2ec3f8fcb5eb365ca582af32771a7790bcded4b5
VERSION                    = 0.23.0-dev
CHAPTERS-IN-MANUSCRIPT     = 1--18 ON MAIN / 19 ON DRAFT BRANCH
CHAPTER-18                 = REVIEWED / OWNER-ADOPTED / MERGED
PR-35                      = MERGED
ISSUE-34                   = CLOSED
CHAPTER-19                 = AUTHORED-DRAFT / NON-CITABLE
BRANCH-19                  = agent/chapter-19-primes-short-intervals-v0.23.0
ISSUE-36                   = OPEN
PR-37                      = DRAFT / OPEN / UNMERGED
PRE-AUTHORING-GATE-19      = CLOSED
PASS-FOR-AUTHORING-19      = YES
RESULTS-19                 = 8 AUTHORED-DRAFT / NON-CITABLE
DRAFT-BUILD-19             = QUALITY-637 / PDF-558 / 261 PAGES / VISUAL PASS
EVIDENCE-19                = FROZEN / FRONTIER UPDATED
CIRCULARITY-AUDIT-19       = PASS
INDEPENDENT-REVIEW-19      = PRE-AUTHORING PASS / MANUSCRIPT REVIEW PENDING
LITERATURE-CUTOFF-19       = 2026-07-25
MERGE                      = NOT AUTHORIZED
RELEASE-READY              = NO
```

## آخر فصل معتمد

الفصل الثامن عشر عن المجاميع الأسية وطريقة فان دير كوربوت معتمد بحالة `REVIEWED / CITABLE` وموجود على `main`. آخر بناء معتمد نجح في 249 صفحة بلا مراجع أو إحالات غير معرّفة في المرور النهائي.

## المرحلة الجارية

الفصل التاسع عشر: **الأوليات في الفترات القصيرة**.

أُغلقت بوابة ما قبل التأليف، وأُنشئت مسودة الفصل وربطت بالمخطوط. يميز المتن بين:

- الصيغة التقاربية لكل \(x\).
- مجرد وجود أولي في الفترة.
- النتائج الصحيحة لتقريبًا كل \(x\).
- الحدود غير المشروطة والشرطية.
- سجل Guth--Maynard التقاربي المنشور عند \(17/30+\varepsilon\).
- حد Baker--Harman--Pintz السفلي المحكّم عند \(0.525\).
- ادعاء preprint عند \(0.52\) الذي يبقى محجورًا.

اكتمل التحقق من المصادر والاعتمادات والتحويلات وتدقيق عدم الدور، واجتازت البوابة مراجعة مستقلة. المسودة والنتائج غير قابلة للاستشهاد حتى نجاح البناء والتدقيق والمراجعة المستقلة للمتن واعتماد المالك.

## بناء PDF

آخر بناء كامل معتمد للفصل الثامن عشر:

```text
XeLaTeX -> Biber -> XeLaTeX -> XeLaTeX
PDF = 249 pages
UNDEFINED CITATIONS = 0
UNDEFINED REFERENCES = 0
```

أما مسودة الفصل التاسع عشر فاجتازت `Quality #637` وبناء PDF `#558` من 261 صفحة، مع صفر إحالات أو مراجع غير معرّفة في المرور النهائي، واجتازت الفحص البصري. هذا إيصال مسودة لا اعتماد نهائي.

وجود مسودة الفصل التاسع عشر لا يعني أنها `VERIFIED` أو `REVIEWED`، ولا يعني أن الموسوعة `RELEASE-READY`.
