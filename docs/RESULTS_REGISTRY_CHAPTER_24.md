# سجل نتائج الفصل الرابع والعشرين

```text
CHAPTER                    = 24
VERSION                    = 0.28.0-dev
REGISTRY                   = READY-FOR-OWNER-ADOPTION / NON-CITABLE
RESULTS                    = 10 AUTHORED-DRAFT / NON-CITABLE
PRIMARY-REVIEW             = CHANGES-REQUIRED / 1 BLOCKER
BLOCKER-CORRECTION         = APPLIED
NARROW-RE-REVIEW           = PASS / 0 BLOCKERS
PASS-FOR-AUTHORING         = YES
AUTHORING                  = COMPLETED
LOCAL-BUILD                = PASS
POST-AUTHORING-REVIEW      = CHANGES-REQUIRED / 0 BLOCKERS / 1 MAJOR / 1 MINOR
POST-AUTHORING-FIXES       = APPLIED
POST-AUTHORING-NARROW      = PASS / 0 BLOCKERS / 0 MAJORS / 0 MINORS
PASS-FOR-OWNER-ADOPTION    = YES
OWNER-ADOPTION             = AWAITING EXPLICIT OWNER DECISION
MERGE                      = NOT AUTHORIZED
```

| المعرّف | الوصف | التصنيف المجمد | الحالة |
|---|---|---|---|
| ANT-DEF-24-01 | الدوال الضربية المقيدة والمتوسط المطبع | DEFINITION | AUTHORED-DRAFT / NON-CITABLE |
| ANT-DEF-24-02 | المسافة الادعائية | DEFINITION / CITED-ORIGIN | AUTHORED-DRAFT / NON-CITABLE |
| ANT-PROP-24-01 | خصائص المسافة الادعائية الأساسية | PROVED-HERE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-DEF-24-03 | المقياس \(\mathcal M(f;x,T)=\min_{|t|\le2T}\mathbb D(f,n^{it};x)^2\) | DEFINITION | AUTHORED-DRAFT / NON-CITABLE |
| ANT-THM-24-01 | مبرهنة هالاش الكمية مع \(+T^{-1/2}\) | CITED-CORE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-COR-24-01 | معيار الإلغاء بعد ضبط الحدين | DERIVED-FROM-CITED | AUTHORED-DRAFT / NON-CITABLE |
| ANT-EX-24-01 | أمثلة موبيوس وليوفيل والشخصيات | EXAMPLES / INTERPRETATION-GUARDED | AUTHORED-DRAFT / NON-CITABLE |
| ANT-PRIN-24-01 | تفسير العائق الادعائي للمتوسط الكبير | CITED-INTERPRETATION | AUTHORED-DRAFT / NON-CITABLE |
| ANT-PRIN-24-02 | فصل المتوسطات الطويلة عن الفترات القصيرة | METHODOLOGICAL-PRINCIPLE / INFERENCE-GUARDED | AUTHORED-DRAFT / NON-CITABLE |
| ANT-OPEN-24-01 | الفترات القصيرة والارتباطات وتشاو | OPEN / DEFERRED-FRONTIER | AUTHORED-DRAFT / NON-CITABLE |

## سجل المراجعة

```text
PRIMARY-REVIEW-COMMIT      = 1fb25deeac05beada7abe0e8f68a77f8d5fd2f70
PRIMARY-VERDICT            = CHANGES-REQUIRED
PRIMARY-BLOCKERS           = 1
BLOCKER                    = HALASZ QUANTITATIVE NORMALIZATION
CORRECTED-T-RANGE          = |t| <= 2T
CORRECTED-REMAINDER        = + T^(-1/2)
NARROW-REVIEW-COMMIT       = 7fed8eb9dd3f69f4d43c2d5a720489b9f5a79830
NARROW-VERDICT             = PASS
NARROW-BLOCKERS            = 0
PASS-FOR-AUTHORING         = YES
POST-REVIEW-COMMIT         = 3eacb0091b005e4e02e821765c69e0b933492da6
POST-VERDICT               = CHANGES-REQUIRED
POST-BLOCKERS              = 0
POST-MAJORS                = 1
POST-MINORS                = 1
MAJOR                      = ANT-PROP-24-01 GENERAL UNIT-DISK TRIANGLE PROOF GAP
MINOR                      = ELLIOTT SOURCES UNUSED IN CHAPTER TEXT
CORRECTION-COMMIT          = cb05df974df9485c367f30a275c0be2e5c3c9872
CORRECTION                 = PROBABILISTIC UNIT-CIRCLE LIFT + ELLIOTT CITATIONS
POST-NARROW-REVIEW-COMMIT  = a24a30c0f4fdcaf5b4e61a70bb7462e22f42ae53
POST-NARROW-VERDICT        = PASS
POST-NARROW-BLOCKERS       = 0
POST-NARROW-MAJORS         = 0
POST-NARROW-MINORS         = 0
PASS-FOR-OWNER-ADOPTION    = YES
```

## ملفات التأليف والبناء

```text
AUTHORING-AUTHORIZATION = docs/CHAPTER_24_AUTHORING_AUTHORIZATION_2026-07-26.md
CHAPTER-TEXT            = volumes/volume-15-modern-frontiers/chapters/chapter-24-pretentious-multiplicative-functions.tex
BIBLIOGRAPHY            = manuscript/chapter-24-bibliography.bib
MANUSCRIPT-LINK         = manuscript/main.tex
BUILD-RECEIPT           = docs/CHAPTER_24_LOCAL_BUILD_RECEIPT_2026-07-26.md
BUILT-HEAD              = ccd9c4b55c17b2117cc27bec95a0d615f5353ffb
PDF-PAGES               = 308 INITIAL / 309 AFTER POST-REVIEW FIXES
PDF-SHA256              = NON-DETERMINISTIC ACROSS INDEPENDENT BUILDS
```

## الحراس

- لا يصبح أي معرّف قابلًا للاستشهاد إلا بعد اعتماد المالك الصريح وتفعيل السجل.
- حكم المراجعة الضيقة بعد التأليف يفتح طلب اعتماد المالك، لكنه لا يقوم مقام قرار المالك.
- `ANT-PROP-24-01` صادقت عليه المراجعة المستقلة بعد التحقق من برهان الرفع الاحتمالي للحالة العامة \(|f(p)|\le1\).
- `ANT-THM-24-01` منقول من المصدر، وليس `PROVED-HERE`.
- لا يجوز حذف \(T^{-1/2}\) أو تغيير مجال التصغير \(|t|\le2T\).
- `ANT-COR-24-01` يضبط تباعد \(\mathcal M\) واختيار \(T(x)\to\infty\) معًا.
- `ANT-PRIN-24-02` مبدأ منهجي لا يحمل ادعاء برهانيًا مستقلًا.
- `ANT-OPEN-24-01` لا يدخل في نواة الفصل المثبتة.
- الفصل 24 يسبق خريطة الجبهات، وتبقى الخريطة الفصل الأخير.
- لا تفعيل للنتائج ولا دمج ولا تغيير على `main` قبل اعتماد المالك الصريح.
