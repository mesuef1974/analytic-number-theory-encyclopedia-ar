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
- [نطاق الفصل الحادي والعشرين](docs/CHAPTER_21_SCOPE_2026-07-25.md)
- [سجل أدلة الفصل الحادي والعشرين](docs/CHAPTER_21_EVIDENCE_LEDGER_2026-07-25.md)
- [جدول تطبيعات الفصل الحادي والعشرين](docs/CHAPTER_21_NORMALIZATION_TABLE_2026-07-25.md)
- [خريطة برهان الفصل الحادي والعشرين](docs/CHAPTER_21_PROOF_MAP_2026-07-25.md)
- [المراجعة المستقلة لبوابة الفصل الحادي والعشرين](docs/CHAPTER_21_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-25.md)
- [المراجعة المستقلة للمتن](docs/CHAPTER_21_MANUSCRIPT_INDEPENDENT_REVIEW_2026-07-25.md)
- [إيصال اعتماد المالك وإغلاق الفصل](docs/CHAPTER_21_OWNER_ADOPTION_2026-07-25.md)
- [سجل نتائج الفصل الحادي والعشرين](docs/RESULTS_REGISTRY_CHAPTER_21.md)

## الحالة الحالية

```text
MAIN-HEAD                  = 470abde4ebb8d30a6accbb664a68d344f503b91e
VERSION                    = 0.25.0-dev
CHAPTERS-IN-MANUSCRIPT     = 1--21 ON MAIN
CHAPTER-21                 = REVIEWED / OWNER-ADOPTED / CITABLE / MERGED
ISSUE-40                   = CLOSED
PR-41                      = MERGED
PRE-AUTHORING-GATE-21      = PASSED
PASS-FOR-AUTHORING-21      = YES
AUTHORING-21               = COMPLETED
INDEPENDENT-REVIEW-21      = PASS / 0 BLOCKERS
RESULTS-21                 = 10 ACTIVE / CITABLE
CI-QUALITY-21              = PASS
CI-PDF-21                  = PASS / 286 PAGES
LOCAL-BUILD-21             = PASS / 286 PAGES
LOCAL-PDF-SHA256           = C2E77CE7640EB5AA3F8D39D55E6EB3D6D8F9BB3482E3801C44ACEB06ED5244D0
RELEASE-READY              = NO
```

## آخر فصل معتمد

الفصل الحادي والعشرون عن دوال \(L\) الآلية وحدود التحدب ودون التحدب والمدخل المنضبط إلى لانجلاندز معتمد بحالة `REVIEWED / OWNER-ADOPTED / CITABLE / MERGED`. نتائجه العشر فعالة وفق تصنيفات منشئها، ودُمج PR #41 في `main` عند الالتزام `470abde4ebb8d30a6accbb664a68d344f503b91e`.

## بناء PDF

البناء المعتمد يستخدم:

```text
XeLaTeX -> Biber -> XeLaTeX -> XeLaTeX
```

محليًا:

```powershell
.\scripts\build.ps1 -Clean
```

آخر بناء محلي للفصل 21 أنتج `releases/preview.pdf` من 286 صفحة وبصمة SHA-256 المسجلة أعلاه.

اعتماد الفصل ودمجه لا يعني أن الموسوعة `RELEASE-READY`.
