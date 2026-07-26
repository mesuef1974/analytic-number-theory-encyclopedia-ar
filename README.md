# الموسوعة الشاملة في نظرية الأعداد التحليلية

**العنوان الكامل:** الموسوعة الشاملة في نظرية الأعداد التحليلية: من الأسس إلى الجبهات البحثية الحديثة

**الإصدار التطويري الحالي:** `v0.30.0-dev`

مشروع موسوعة عربية بحثية متقدمة في نظرية الأعداد التحليلية، من الأسس إلى طرق الغربال والطريقة الدائرية والمجاميع الأسية والجبهات الحديثة.

## وثائق المشروع

- [أهداف المشروع](docs/PROJECT_GOALS.md)
- [تقدم المشروع](docs/PROGRESS.md)
- [خارطة الطريق](docs/ROADMAP.md)
- [قائمة المهام](docs/TODO.md)
- [الإصدار الحالي](docs/VERSION.md)
- [سياسة اعتماد النتائج](docs/RESULT_STATUS_POLICY.md)
- [سجل النتائج](docs/RESULTS_REGISTRY.md)
- [نطاق الفصل السادس والعشرين](docs/CHAPTER_26_SCOPE_2026-07-26.md)
- [سجل أدلة الفصل السادس والعشرين](docs/CHAPTER_26_EVIDENCE_LEDGER_2026-07-26.md)
- [خريطة بناء الفصل السادس والعشرين](docs/CHAPTER_26_STRUCTURE_MAP_2026-07-26.md)
- [المراجعة المستقلة النهائية للفصل السادس والعشرين](docs/CHAPTER_26_INDEPENDENT_POST_AUTHORING_NARROW_REVIEW_2026-07-26.md)
- [اعتماد مالك الفصل السادس والعشرين](docs/CHAPTER_26_OWNER_ADOPTION_2026-07-26.md)
- [سجل نتائج الفصل السادس والعشرين](docs/RESULTS_REGISTRY_CHAPTER_26.md)

## الحالة الحالية

```text
VERSION                    = 0.30.0-dev
CHAPTERS-IN-MANUSCRIPT     = 1--26 / MERGED
CHAPTER-26                 = REVIEWED / OWNER-ADOPTED / ACTIVE-CITABLE / MERGED
ISSUE-51                   = CLOSED
PR-52                      = MERGED
PRE-AUTHORING-GATE-26      = PASS
POST-AUTHORING-REVIEW-26   = PASS
RESULTS-26                 = 10 ACTIVE / CITABLE
LOCAL-PDF                  = PASS / 321 PAGES
MERGE-26                   = COMPLETED
RELEASE-READY              = NO
```

## آخر فصل معتمد

الفصل السادس والعشرون هو آخر فصل في المخطوط، وقد اجتاز المراجعة المستقلة واعتمده المالك وفُعّلت معرفاته العشرة ثم دُمج PR #52. اكتملت بنية الموسوعة ذات الفصول الستة والعشرين، لكن ذلك لا يعني أن الإصدار جاهز للنشر النهائي.

## بناء PDF

البناء المعتمد يستخدم:

```text
XeLaTeX -> Biber -> XeLaTeX -> XeLaTeX
```

محليًا:

```powershell
.\scripts\build.ps1 -Clean
```

يلزم بعد أي تحديث مركزي إعادة فحص الجودة والبناء الكامل وتسجيل عدد الصفحات وبصمة SHA-256. نجاح البناء وحده لا يمنح حالة `RELEASE-READY`.
