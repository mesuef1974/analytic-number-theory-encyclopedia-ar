# بوابة ما قبل التأليف للفصل الثامن عشر

التاريخ: 2026-07-25

## الحالة

```text
CHAPTER             = 18
VERSION             = 0.22.0-dev
BASE-MAIN           = 95209028f7e9f10dd8b47baef4bd4194df40a5a0
ISSUE               = #34 / OPEN
BRANCH              = agent/chapter-18-exponential-sums-van-der-corput-v0.22.0
EVIDENCE-LEDGER     = CREATED
PROOF-MAP           = CREATED
CONSENSUS-AUDIT     = PASS-AS-SCOPING-INPUT
NORMALIZATION       = FROZEN
NONCIRCULARITY      = PASS
INDEPENDENT-REVIEW  = APPROVED
RESULTS             = 8 / RESERVED-DRAFT
PRE-AUTHORING-GATE  = CLOSED
PASS-FOR-AUTHORING  = YES
AUTHORING           = AUTHORIZED ON WORK BRANCH
MERGE               = NOT AUTHORIZED
RELEASE-READY       = NO
```

## النطاق المجمد

1. المجاميع الأسية والحد التافه ومعنى الادخار.
2. الجمع الجزئي ونقل الأوزان.
3. متباينة فرق فان دير كوربوت بصيغتها القياسية الدقيقة.
4. اختبار المشتقة الأولى بشرط البعد عن الأعداد الصحيحة.
5. اختبار المشتقة الثانية بصيغة كلاسيكية `CITED / EXPLAINED`.
6. عملية `A` في نسخة محدودة داخلية، وعملية `B` مقتبسة ومشروحة.
7. إطار محدود للأزواج الأسية دون تحسين شامل.
8. أمثلة خطية وتربيعية وتطبيق نموذجي على مجموع فايل.
9. صلة أحادية الاتجاه بالفصل 17 دون إعادة تصنيف تقدير الأقواس الصغرى.

## التصنيفات المجمدة

```text
ANT-ID-18-01    = IDENTITY / PROVED-HERE
ANT-LEM-18-01   = PROVED-HERE
ANT-LEM-18-02   = PROVED-HERE TARGET / INDEPENDENTLY APPROVED
ANT-THM-18-01   = PROVED-HERE TARGET / INDEPENDENTLY APPROVED
ANT-THM-18-02   = CITED / EXPLAINED
ANT-DEF-18-01   = DEFINITION / CITED-FRAMEWORK
ANT-PROP-18-01  = PROVED-HERE-LIMITED / CITED-GENERAL
ANT-PROP-18-02  = CITED / EXPLAINED
```

## نتائج المراجعة المستقلة

- صيغة فرق فان دير كوربوت صحيحة، بما فيها العامل `(N+H-1)/H` والأوزان الطرفية.
- شرط اختبار المشتقة الأولى هو `||f'(x)|| >= lambda` مع الرتابة المناسبة، لا مجرد `|f'(x)| >= lambda`.
- اختبارات الأطوار الثابتة والخطية متوافقة مع الصياغات المجمدة.
- الحالة التربيعية لا تكشف تعارضًا، وتبقى المقارنة الكمية التفصيلية بندًا أثناء التأليف.
- تدقيق عدم الدور مع الفصل 17 ناجح.

## حدود الادعاء

- لا تُنسب نظرية الأزواج الأسية الكاملة إلى الفصل.
- لا يدعى الوصول إلى أفضل النتائج الحديثة.
- اختبارات المشتقة الثالثة وما فوق `DEFERRED`.
- عملية `B` لا تعرض بوصفها نتيجة من متباينة الفرق وحدها.
- تقدير الأقواس الصغرى في الفصل 17 يبقى `CITED / COMPOSITE INPUT`.

## الملفات المرتبطة

- `research/literature-reviews/chapter-18-exponential-sums-van-der-corput-evidence.md`
- `research/literature-reviews/chapter-18-exponential-sums-van-der-corput-proof-map.md`
- `docs/CHAPTER_18_CONSENSUS_LITERATURE_AUDIT_2026-07-25.md`
- `docs/CHAPTER_18_SOURCE_NORMALIZATION_AND_THEOREM_FREEZE_2026-07-25.md`
- `docs/CHAPTER_18_NONCIRCULARITY_AUDIT_2026-07-25.md`
- `docs/CHAPTER_18_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-25.md`
- `docs/RESULTS_REGISTRY_CHAPTER_18.md`

## القرار

```text
PRE-AUTHORING-GATE = CLOSED
PASS-FOR-AUTHORING = YES
AUTHORING = AUTHORIZED ON WORK BRANCH
MERGE = NOT AUTHORIZED
RELEASE-READY = NO
```
