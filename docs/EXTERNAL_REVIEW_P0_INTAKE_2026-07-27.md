# استقبال التقييم الخارجي وخطة معالجة P0

## الحالة

```text
ISSUE                 = #59
BRANCH                = agent/release-p0-external-review-remediation-v0.30.1
BASE                  = main
BUILD-READY           = YES
PUBLICATION-READY     = NO
STABLE-RELEASE        = BLOCKED
AUTHORING             = NOT IN SCOPE
MERGE                 = NOT AUTHORIZED
```

## قاعدة العمل

لا يُقبل أي ادعاء من التقرير الخارجي بوصفه خطأً مثبتًا قبل إعادة إنتاجه على الرأس الحالي للفرع. تسجل كل ملاحظة بإحدى الحالات: `EXTERNAL-CLAIM`, `REPRODUCED`, `NOT-REPRODUCED`, `FIXED`, `VERIFIED`, `OPEN`, `CLOSED`.

## حزم P0

### P0-01 — سلامة النص اللاتيني في PDF

- الادعاء: انقلاب موضعي في الأزواج `fi/fl/ffi` داخل السياق العربي.
- إعادة الإنتاج: `PASS`.
- الإصلاح: خط لاتيني مستقل وتعطيل الربط الطباعي المسبب للخلل وفرض الخط اللاتيني على الببليوغرافيا.
- فحص الرجوع: `scripts/check_latin_pdf_text.py`.
- التحقق: Quality #959 وBuild #766 = `PASS`، والصيغ التالفة = `0`.
- السجل: `docs/P0_01_LATIN_SHAPING_REPRODUCTION_2026-07-27.md`.
- الحالة: `REPRODUCED / FIXED / VERIFIED / CLOSED`.

### P0-02 — فصل بناء المسودة عن بناء النشر

- الادعاء: ظهور وسوم الحوكمة ومسارات الملفات وبصمات Git وتعليمات البناء في PDF العام.
- إعادة الإنتاج: `PASS`.
- الإصلاح: بناء `draft` تدقيقي وبناء `release` من مصدر مولد منزوع البيانات الداخلية.
- الفحوص: `scripts/prepare_release_source.py` و`scripts/check_release_pdf_text.py`.
- التحقق: Quality #969 وBuild #776 = `PASS`؛ نسخة النشر 299 صفحة ومؤشرات التسرب الممنوعة = `0`.
- السجل: `docs/P0_02_DRAFT_RELEASE_BUILD_SEPARATION_2026-07-27.md`.
- الحالة: `REPRODUCED / FIXED / VERIFIED / CLOSED`.

### P0-03 — تنظيف تكرارات الببليوغرافيا

- الادعاء: تكرار كتاب Titchmarsh تحت مفاتيح متعددة.
- إعادة الإنتاج: `PASS`؛ وجدت ثلاثة مداخل فعلية.
- الإصلاح: اعتماد `Titchmarsh1986` مدخلًا قانونيًا وحيدًا، وحفظ المفتاحين القديمين في `ids`، وحذف النسختين المكررتين.
- التحقق: Quality #974 وBuild #781 = `PASS`.
- السجل: `docs/P0_03_TITCHMARSH_BIBLIOGRAPHY_DEDUP_2026-07-27.md`.
- الحالة: `REPRODUCED / FIXED / VERIFIED / CLOSED`.

### P0-04 — تعليق تدقيق Chen 1973

- الادعاء: طباعة تعليق تدقيق داخلي داخل المرجع.
- إعادة الإنتاج: `PASS`؛ كان التعليق في حقل `note` المطبوع.
- الإصلاح: حذف الحقل المطبوع ونقل الملاحظة إلى سجل تدقيق غير مطبوع مع إبقاء بيانات المقالة والـDOI.
- التحقق: Quality #979 وBuild #786 = `PASS`.
- السجل: `docs/P0_04_CHEN_1973_AUDIT_NOTE_RELOCATION_2026-07-27.md`.
- الحالة: `REPRODUCED / FIXED / VERIFIED / CLOSED`.

### P0-05 — معرفات نتائج الفصل 18

- الادعاء: استعمال النمط `ANT-<TYPE>-<NN>-18` بدل `ANT-<TYPE>-18-<NN>`.
- إعادة الإنتاج: `NOT-REPRODUCED`؛ المتن والسجل المركزي وسجل الفصل تستخدم النمط الصحيح لجميع المعرفات الثمانية.
- الإجراء الوقائي: إضافة حارس رجوع في `scripts/quality_check.py` يمنع النمط القديم مستقبلًا.
- التحقق: Quality #980 وBuild #787 = `PASS`، ثم Quality #981 وBuild #788 = `PASS` بعد توثيق الإغلاق.
- السجل: `docs/P0_05_CHAPTER_18_RESULT_ID_AUDIT_2026-07-27.md`.
- الحالة: `NOT-REPRODUCED / REGRESSION-GUARDED / VERIFIED / CLOSED`.

## بوابات الإغلاق

```text
P0-01 LATIN TEXT           = PASS / CLOSED
P0-02 RELEASE BUILD        = PASS / CLOSED
P0-03 BIB DEDUP            = PASS / CLOSED
P0-04 PRINTED NOTE         = PASS / CLOSED
P0-05 RESULT IDS           = PASS / CLOSED
P0 OPEN BLOCKERS           = 0
QUALITY CHECK              = #981 PASS
DRAFT/RELEASE BUILD        = #788 PASS
LATIN TEXT INTEGRITY       = PASS FOR DRAFT AND RELEASE
ARABIC SEARCHABILITY       = FAIL / OPEN
INDEPENDENT FINAL REVIEW   = CHANGES-REQUIRED
PUBLICATION-READY          = NO
STABLE-RELEASE             = BLOCKED
```

## ملاحظة المراجعة المستقلة

أثر Build #788 يولد نصًا عربيًا دون رموز استبدال، لكن `pdftotext -layout` يستخرج الحروف العربية في صور عرض منفصلة ومجزأة؛ لم يمكن العثور على عبارات عربية معيارية كاملة مثل عنوان الموسوعة أو «المجاميع الأسية» أو «مبرهنة الأعداد الأولية». لذلك لا تعد قابلية البحث العربية ناجحة، ولا يجوز تحويل PR #60 إلى Ready أو دمجه قبل معالجة هذه البوابة أو اعتماد قرار حوكمي صريح يغير متطلبها.

## خارج نطاق P0 الحالي

تسجل ملاحظات P1/P2 في مرحلة لاحقة، ومنها اشتقاق المنطقة الخالية لـζ من الحالة العامة، PNT الكمي، اتجاه فترة Baker–Harman–Pintz، تمييز رامانوجان للهولومورفي ومااس، وتحسينات الإتاحة العامة.