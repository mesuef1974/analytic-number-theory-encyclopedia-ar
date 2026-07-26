# سجل نتائج الفصل الرابع والعشرين

```text
CHAPTER                = 24
VERSION                = 0.28.0-dev
REGISTRY               = RESERVED / BLOCKER-CORRECTED-PENDING-NARROW-REVIEW
RESULTS                = 10 RESERVED / NON-CITABLE
PRIMARY-REVIEW         = CHANGES-REQUIRED / 1 BLOCKER
BLOCKER-CORRECTION     = APPLIED
NARROW-RE-REVIEW       = REQUESTED
PASS-FOR-AUTHORING     = NO
AUTHORING              = BLOCKED
LOCAL-BUILD            = NOT STARTED
POST-AUTHORING-REVIEW  = NOT STARTED
OWNER-ADOPTION         = NOT REQUESTED
MERGE                  = NOT AUTHORIZED
```

| المعرّف | الوصف | التصنيف المجمد | الحالة |
|---|---|---|---|
| ANT-DEF-24-01 | الدوال الضربية المقيدة والمتوسط المطبع | DEFINITION | RESERVED / NON-CITABLE |
| ANT-DEF-24-02 | المسافة الادعائية | DEFINITION / CITED-ORIGIN | RESERVED / NON-CITABLE |
| ANT-PROP-24-01 | خصائص المسافة الادعائية الأساسية | PROVED-HERE | RESERVED / NON-CITABLE |
| ANT-DEF-24-03 | المقياس \(\mathcal M(f;x,T)=\min_{|t|\le2T}\mathbb D(f,n^{it};x)^2\) | DEFINITION | RESERVED / NON-CITABLE |
| ANT-THM-24-01 | مبرهنة هالاش الكمية مع \(+T^{-1/2}\) | CITED-CORE | RESERVED / NON-CITABLE |
| ANT-COR-24-01 | معيار الإلغاء بعد ضبط الحدين | DERIVED-FROM-CITED | RESERVED / NON-CITABLE |
| ANT-EX-24-01 | أمثلة موبيوس وليوفيل والشخصيات | EXAMPLES / INTERPRETATION-GUARDED | RESERVED / NON-CITABLE |
| ANT-PRIN-24-01 | تفسير العائق الادعائي للمتوسط الكبير | CITED-INTERPRETATION | RESERVED / NON-CITABLE |
| ANT-PRIN-24-02 | فصل المتوسطات الطويلة عن الفترات القصيرة | METHODOLOGICAL-PRINCIPLE / INFERENCE-GUARDED | RESERVED / NON-CITABLE |
| ANT-OPEN-24-01 | الفترات القصيرة والارتباطات وتشاو | OPEN / DEFERRED-FRONTIER | RESERVED / NON-CITABLE |

## سجل المراجعة

```text
REVIEW-COMMIT           = 1fb25deeac05beada7abe0e8f68a77f8d5fd2f70
VERDICT                 = CHANGES-REQUIRED
BLOCKERS                = 1
BLOCKER                 = HALASZ QUANTITATIVE NORMALIZATION
CORRECTED-T-RANGE       = |t| <= 2T
CORRECTED-REMAINDER     = + T^(-1/2)
PASS-FOR-AUTHORING      = NO UNTIL INDEPENDENT NARROW PASS
```

## الحراس

- لا يصبح أي معرّف قابلًا للاستشهاد قبل التأليف والبناء والمراجعة المستقلة واعتماد المالك.
- `ANT-THM-24-01` منقول من المصدر، وليس `PROVED-HERE`.
- لا يجوز حذف \(T^{-1/2}\) أو تغيير مجال التصغير \(|t|\le2T\).
- `ANT-COR-24-01` يضبط تباعد \(\mathcal M\) واختيار \(T(x)\to\infty\) معًا.
- `ANT-PRIN-24-02` مبدأ منهجي لا يحمل ادعاء برهانيًا مستقلًا.
- `ANT-OPEN-24-01` لا يدخل في نواة الفصل المثبتة.
- لا دمج ولا تغيير على `main` قبل اعتماد المالك الصريح.