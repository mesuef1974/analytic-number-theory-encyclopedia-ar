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
- [المراجعة المستقلة بعد تأليف الفصل التاسع عشر](docs/CHAPTER_19_INDEPENDENT_POST_AUTHORING_REVIEW_2026-07-25.md)
- [إيصال البناء النهائي قبل اعتماد الفصل التاسع عشر](docs/CHAPTER_19_FINAL_PRE_OWNER_BUILD_RECEIPT_2026-07-25.md)
- [إيصال اعتماد المالك للفصل التاسع عشر](docs/CHAPTER_19_OWNER_ADOPTION_2026-07-25.md)
- [سجل نتائج الفصل التاسع عشر](docs/RESULTS_REGISTRY_CHAPTER_19.md)

## الحالة الحالية

```text
BASE-MAIN                  = 2ec3f8fcb5eb365ca582af32771a7790bcded4b5
VERSION                    = 0.23.0-dev
CHAPTERS-IN-MANUSCRIPT     = 1--19 ON MAIN
CHAPTER-18                 = REVIEWED / OWNER-ADOPTED / MERGED
PR-35                      = MERGED
ISSUE-34                   = CLOSED
CHAPTER-19                 = REVIEWED / OWNER-ADOPTED / CITABLE
BRANCH-19                  = MERGED INTO MAIN
ISSUE-36                   = CLOSED
PR-37                      = MERGED
PRE-AUTHORING-GATE-19      = CLOSED
PASS-FOR-AUTHORING-19      = YES
RESULTS-19                 = 8 ACTIVE / CITABLE
FINAL-PRE-OWNER-19         = QUALITY-643 / PDF-564 / 261 PAGES / VISUAL PASS
EVIDENCE-19                = FROZEN / FRONTIER UPDATED
CIRCULARITY-AUDIT-19       = PASS
INDEPENDENT-REVIEW-19      = APPROVED / TYPOGRAPHY-CLOSED
OWNER-ADOPTION-19          = APPROVED
LITERATURE-CUTOFF-19       = 2026-07-25
MERGE                      = COMPLETED
MERGE-COMMIT-19            = 8fa2aa7f5972776580983074309fa90e07b53364
RELEASE-READY              = NO
```

## آخر فصل معتمد

الفصل التاسع عشر عن الأوليات في الفترات القصيرة معتمد بحالة `REVIEWED / CITABLE` وموجود على `main` بعد دمج PR #37. آخر بناء معتمد نجح في 261 صفحة بلا مراجع أو إحالات غير معرّفة في المرور النهائي.

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

اكتمل التحقق من المصادر والاعتمادات والتحويلات وتدقيق عدم الدور، ثم اجتاز المتن التدقيق والمراجعة المستقلة. أُغلقت الملاحظتان الطباعيتان ونجح البناء النهائي قبل الاعتماد. اعتمد المالك الفصل وفعّل نتائجه الثماني بحالة `ACTIVE / CITABLE` وأذن بدمج PR #37.

## بناء PDF

آخر بناء كامل معتمد للفصل الثامن عشر:

```text
XeLaTeX -> Biber -> XeLaTeX -> XeLaTeX
PDF = 249 pages
UNDEFINED CITATIONS = 0
UNDEFINED REFERENCES = 0
```

أما الفصل التاسع عشر فاجتاز على رأس الإغلاق `Quality #643` وبناء PDF `#564` من 261 صفحة، وبصمة PDF هي `236A0CBE2D3CDC314CB244F4F77705AABB35FA6A766B27D4EC7CD5A04AC13E52`. لا يظهر تجاوز عمود داخل ملف الفصل في المرور النهائي، واجتازت افتتاحية الفصل وصفحتا التصحيح الفحص البصري. اعتمد المالك هذه الحزمة وأذن بدمجها.

اعتماد الفصل ودمجه لا يعني أن الموسوعة `RELEASE-READY`.
