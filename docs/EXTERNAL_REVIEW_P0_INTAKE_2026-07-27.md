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
MERGE                 = NOT AUTHORIZED UNTIL ALL P0 GATES PASS
```

## قاعدة العمل

لا يُقبل أي ادعاء من التقرير الخارجي بوصفه خطأً مثبتًا قبل إعادة إنتاجه على الرأس الحالي للفرع. تسجل كل ملاحظة بإحدى الحالات:

- `EXTERNAL-CLAIM`
- `REPRODUCED`
- `NOT-REPRODUCED`
- `FIXED`
- `VERIFIED`
- `OPEN`

## حزم P0

### P0-01 — سلامة النص اللاتيني في PDF

- الادعاء: انقلاب موضعي في الأزواج `fi/fl/ffi` داخل السياق العربي.
- أمثلة الاختبار: `Walfisz`, `Zeitschrift`, `Scientifique`, `Ahlfors`, `Helfgott`, `Difference`, `Life`, `Asif`.
- إعادة الإنتاج: `PASS`؛ ظهرت الصيغ التالفة في PDF السابق.
- الإصلاح: خط لاتيني مستقل، وتعطيل `liga/clig/dlig` في السياقين العربي والإنجليزي، وفرض `\englishfont` على الببليوغرافيا.
- اختبار الرجوع: `scripts/check_latin_pdf_text.py` مدمج في بناء PDF.
- التحقق على الرأس `68da6e6b4437f54c34210c3b8a2e03cc73eefe49`:
  - `Quality checks` run 959 = `PASS`.
  - `Build encyclopedia PDF` run 766 = `PASS`.
  - `Verify Latin PDF text integrity` = `PASS`.
  - الصيغ التالفة = `0`.
  - الصيغ الصحيحة المتوقعة = `PRESENT`.
  - الفحص البصري للصفحات 152 و314 و316 و318 = `PASS`.
- السجل التفصيلي: `docs/P0_01_LATIN_SHAPING_REPRODUCTION_2026-07-27.md`.
- الحالة: `REPRODUCED / FIXED / VERIFIED / CLOSED`.

### P0-02 — فصل بناء المسودة عن بناء النشر

- الادعاء: ظهور وسوم الحوكمة ومسارات الملفات وبصمات Git وتعليمات البناء في PDF العام.
- الحالة: `EXTERNAL-CLAIM / OPEN`.
- المطلوب: بناءان واضحان، `draft` و`release`، مع إبقاء مواد الحوكمة في المسودة فقط.

### P0-03 — تنظيف تكرارات الببليوغرافيا

- الادعاء: تكرار كتاب Titchmarsh تحت المفاتيح `Tit86a`, `Tit86b`, `TH86`.
- الحالة: `EXTERNAL-CLAIM / OPEN`.
- المطلوب: جرد استعمال المفاتيح، اختيار مدخل قانوني واحد، تحديث الاستشهادات، وتشغيل فحص تكرار شامل.

### P0-04 — تعليق تدقيق Che73

- الادعاء: طباعة تعليق تدقيق داخلي داخل المرجع.
- الحالة: `EXTERNAL-CLAIM / OPEN`.
- المطلوب: نقله إلى سجل تدقيق غير مطبوع مع إبقاء بيانات المرجع الورقي.

### P0-05 — معرفات نتائج الفصل 18

- الادعاء: استعمال النمط `ANT-<TYPE>-<NN>-18` بدل `ANT-<TYPE>-18-<NN>`.
- الحالة: `EXTERNAL-CLAIM / OPEN`.
- المطلوب: جرد المصدر والسجل المركزي والإحالات، ثم إعادة تسمية ذرية مع فحص عدم وجود معرفات قديمة.

## بوابات الإغلاق

```text
P0-01 REPRODUCTION        = PASS
P0-01 FIX / REGRESSION    = PASS
P0-02 RELEASE BUILD       = PENDING
P0-03 BIB DEDUP           = PENDING
P0-04 PRINTED NOTE        = PENDING
P0-05 RESULT IDS          = PENDING
INDEX BUILD               = PASS FOR P0-01 HEAD
QUALITY CHECK             = PASS FOR P0-01 HEAD
LATIN TEXT INTEGRITY      = PASS
ARABIC SEARCHABILITY      = PENDING
INDEPENDENT FINAL REVIEW  = PENDING
PUBLICATION-READY         = NO
```

## خارج نطاق P0 الحالي

تُسجل ملاحظات P1/P2 في مرحلة لاحقة بعد إغلاق P0، ومنها: اشتقاق المنطقة الخالية لـζ من الحالة العامة، PNT الكمي، اتجاه فترة Baker–Harman–Pintz، تمييز رامانوجان للهولومورفي ومااس، وتحسين إتاحة النص العربي.
