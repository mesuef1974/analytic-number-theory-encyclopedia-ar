# الموسوعة الشاملة في نظرية الأعداد التحليلية

**العنوان الكامل:** الموسوعة الشاملة في نظرية الأعداد التحليلية: من الأسس إلى الجبهات البحثية الحديثة

**الإصدار التطويري الحالي:** `v0.25.0-dev`

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
- [حكم المراجعة المستقلة لبوابة الفصل العشرين](docs/CHAPTER_20_INDEPENDENT_REVIEW_VERDICT_2026-07-25.md)
- [تدقيق تأليف الفصل العشرين](docs/CHAPTER_20_AUTHORING_AUDIT_2026-07-25.md)
- [سجل نتائج الفصل العشرين](docs/RESULTS_REGISTRY_CHAPTER_20.md)
- [نطاق الفصل الحادي والعشرين](docs/CHAPTER_21_SCOPE_2026-07-25.md)
- [سجل أدلة الفصل الحادي والعشرين](docs/CHAPTER_21_EVIDENCE_LEDGER_2026-07-25.md)
- [جدول تطبيعات الفصل الحادي والعشرين](docs/CHAPTER_21_NORMALIZATION_TABLE_2026-07-25.md)
- [خريطة برهان الفصل الحادي والعشرين](docs/CHAPTER_21_PROOF_MAP_2026-07-25.md)
- [تدقيق ما قبل تأليف الفصل الحادي والعشرين](docs/CHAPTER_21_PRE_AUTHORING_AUDIT_2026-07-25.md)
- [المراجعة المستقلة لبوابة الفصل الحادي والعشرين](docs/CHAPTER_21_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-25.md)
- [تدقيق تأليف الفصل الحادي والعشرين](docs/CHAPTER_21_AUTHORING_AUDIT_2026-07-25.md)
- [المراجعة المستقلة بعد تأليف الفصل الحادي والعشرين](docs/CHAPTER_21_INDEPENDENT_POST_AUTHORING_REVIEW_2026-07-25.md)
- [سجل نتائج الفصل الحادي والعشرين](docs/RESULTS_REGISTRY_CHAPTER_21.md)

## الحالة الحالية

```text
BASE-MAIN                  = dd92caa3dba416ffc0f718d6bc037d67ec50466f
VERSION                    = 0.25.0-dev
CHAPTERS-IN-MANUSCRIPT     = 1--20 ON MAIN
CHAPTER-20                 = REVIEWED / OWNER-ADOPTED / CITABLE / MERGED
CHAPTER-21                 = REVIEWED-CANDIDATE / NON-CITABLE
BRANCH-21                  = agent/chapter-21-automorphic-l-subconvexity-langlands-v0.25.0
ISSUE-40                   = OPEN
PR-41                      = DRAFT / OPEN
PRE-AUTHORING-GATE-21      = PASSED
PASS-FOR-AUTHORING-21      = YES
AUTHORING-21               = COMPLETED
RESULTS-21                 = 10 AUTHORED-DRAFT / NON-CITABLE
POST-AUTHORING-21          = APPROVED / READY-FOR-OWNER
QUALITY-21                 = #742 / PASS
PDF-21                     = #648 / PASS / 286 PAGES / VISUAL PASS
LITERATURE-CUTOFF-21       = 2026-07-25
RELEASE-READY              = NO
```

## آخر فصل معتمد

الفصل العشرون عن الأشكال المعيارية وأشكال مااس وصيغ التتبع معتمد بحالة `REVIEWED / OWNER-ADOPTED / CITABLE`، ونتائجه الخمس عشرة فعالة، وهو موجود على `main` بعد دمج PR #39.

## المرحلة الجارية

الفصل الحادي والعشرون: **دوال (L) الآلية، حدود التحدب ودون التحدب، ومدخل منضبط إلى لانجلاندز**.

فُتحت المرحلة `0.25.0-dev` من الرأس `dd92caa3dba416ffc0f718d6bc037d67ec50466f`، وأُنشئت حزمة ما قبل التأليف وسجلت عشرة معرفات `RESERVED / NON-CITABLE`. استُعمل Consensus للاكتشاف فقط، ثم تحققت بيانات Michel--Venkatesh من صفحة الناشر وDOI. جُمّدت التطبيعات والمصادر واجتازت الحزمة المراجعة المستقلة، ثم أُنشئ متن الفصل وملف مراجع وربطا بالمخطوط. اجتاز المتن `Quality #742` وبناء `PDF #648` من 286 صفحة والفحص البصري والمراجعة المستقلة اللاحقة بحكم `APPROVED`. وهو الآن `REVIEWED-CANDIDATE / NON-CITABLE` بانتظار اعتماد المالك الصريح؛ PR #41 ما يزال مسودة والدمج غير مأذون.

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
