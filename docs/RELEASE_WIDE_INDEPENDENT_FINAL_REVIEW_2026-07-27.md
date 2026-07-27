# المراجعة المستقلة النهائية للإصدار 0.30.0-dev

التاريخ: 2026-07-27

الفرع المراجع: `review/release-wide-v0.30.0-dev`

الرأس المراجع: `05b61a1`

## نطاق المراجعة

- حوكمة النتائج والسجلات الفصلية.
- سجل التغييرات والمهام المفتوحة.
- مفاتيح BibTeX وروابط DOI.
- الفحص البصري للفهرس وبدايات الأجزاء والفصول 22--26 والمراجع.
- سجل البناء النهائي والـPDF الناتج.

## النتائج

```text
QUALITY-CHECK              = PASS
MANUSCRIPT-RESULTS         = 252
CENTRAL-REGISTRY-RESULTS   = 252
MISSING-RESULT-IDS         = 0
EXTRA-RESULT-IDS           = 0
DUPLICATE-RESULT-IDS       = 0
UNGOVERNED-ACTIVE-RESULTS = 0
CITATION-KEYS              = 90
BIBLIOGRAPHY-ENTRIES       = 106
MISSING-BIB-KEYS           = 0
DUPLICATE-BIB-KEYS         = 0
DOI-RESOLVER-PASS          = 55 / 56
LEGACY-DOI-EXCEPTIONS      = 1
VISUAL-BLOCKERS            = 0
PDF-PAGES                  = 321
PDF-SIZE-BYTES             = 1212922
PDF-SHA256                 = 1A694020B0F787285D1363F75B24E3A1B02D2693D281868B22C1696F116C0439
FATAL-BUILD-ERRORS         = 0
OVERFULL-HBOX-TOTAL        = 341
MAX-OVERFULL-PT            = 19.38495
OVERFULL-HBOX >= 20pt      = 0
```

## الاستثناءات والديون غير الحاجزة

- DOI مقال Chen لعام 1973 يعيد HTTP 404 من محللي DOI وCrossref، وقد احتُفظ به كمعرف قديم مع توثيق الحاجة إلى تحقق يدوي من سجل الناشر.
- بقيت 341 حالة `Overfull \hbox` أصغر من 20 نقطة، وأقصاها 19.38495 نقطة؛ صُنفت ديونًا طباعية غير حاجزة بعد الفحص البصري.
- تبقى قرارات المالك المتعلقة بالفهارس والتمارين والإحالات القديمة خارج حكم السلامة التقنية لهذا التقرير.

## الحكم

```text
FINAL-INDEPENDENT-REVIEW   = PASS
OPEN-MAJORS                = 0
TECHNICAL-BLOCKERS         = 0
RELEASE-READY              = NO
OWNER-DECISION-REQUIRED    = YES
MERGE                      = NOT AUTHORIZED
```

اجتازت النسخة بوابات الحوكمة والبناء والمراجع والفحص البصري المحددة في نطاق المراجعة.
لا يمنح هذا التقرير إذن الدمج، ولا يعلن الإصدار جاهزًا للنشر قبل قرارات المالك الصريحة.
