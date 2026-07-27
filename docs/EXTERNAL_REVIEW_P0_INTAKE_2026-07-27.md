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
- إعادة الإنتاج: `PASS`؛ ظهرت بيانات داخلية في نسخة PDF السابقة.
- الإصلاح:
  - بناء `draft` تدقيقي يحتفظ بمواد الحوكمة.
  - توليد مصدر `release` مستقل داخل `build/release-src` دون تعديل المصدر القانوني.
  - فحص آلي يمنع وسوم الحوكمة، المسارات، البصمات، مراجع PR/Issue، ومعرفات النتائج الداخلية في نسخة النشر.
- التحقق على الرأس `ac632552e439a4c084bfa424a8746b7dfed36813`:
  - `Quality checks` run 969 = `PASS`.
  - `Build encyclopedia PDF` run 776 = `PASS`.
  - بناء المسودة = `PASS`.
  - بناء النشر = `PASS`.
  - سلامة النص اللاتيني في الملفين = `PASS`.
  - فصل بيانات الحوكمة = `PASS`.
  - نسخة النشر: 299 صفحة، جميع مؤشرات التسرب الممنوعة = `0`.
  - المسودة: 319 صفحة، `REVIEWED = 21`، ومعرفات ANT الداخلية = `301`.
- أثر التحقق: `8665994526`، البصمة `sha256:1f3d79022274854241f2f2994167bb5c249a6847c994104dc60770f3aba02d7d`.
- السجل التفصيلي: `docs/P0_02_DRAFT_RELEASE_BUILD_SEPARATION_2026-07-27.md`.
- الحالة: `REPRODUCED / FIXED / VERIFIED / CLOSED`.

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
P0-02 RELEASE BUILD       = PASS / CLOSED
P0-03 BIB DEDUP           = PENDING
P0-04 PRINTED NOTE        = PENDING
P0-05 RESULT IDS          = PENDING
INDEX BUILD               = PASS FOR P0-02 HEAD
QUALITY CHECK             = PASS FOR P0-02 HEAD
LATIN TEXT INTEGRITY      = PASS FOR DRAFT AND RELEASE
ARABIC SEARCHABILITY      = PENDING
INDEPENDENT FINAL REVIEW  = PENDING
PUBLICATION-READY         = NO
```

## خارج نطاق P0 الحالي

تُسجل ملاحظات P1/P2 في مرحلة لاحقة بعد إغلاق P0، ومنها: اشتقاق المنطقة الخالية لـζ من الحالة العامة، PNT الكمي، اتجاه فترة Baker–Harman–Pintz، تمييز رامانوجان للهولومورفي ومااس، وتحسين إتاحة النص العربي.
