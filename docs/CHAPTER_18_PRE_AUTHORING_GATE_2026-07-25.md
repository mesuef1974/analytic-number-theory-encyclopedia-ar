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
RESULTS             = 8 / RESERVED-DRAFT
PRE-AUTHORING-GATE  = OPEN
PASS-FOR-AUTHORING  = NO
AUTHORING           = BLOCKED
MERGE               = NOT AUTHORIZED
RELEASE-READY       = NO
```

## السؤال المركزي

ما الحزمة الدنيا الصارمة من نظرية المجاميع الأسية التي ينبغي إثباتها أو اقتباسها كي يصبح القارئ قادرًا على فهم أدوات الإلغاء المستخدمة في الأقواس الصغرى، دون إعادة إثبات نظرية أوسع من نطاق الموسوعة ودون اعتماد دائري على الفصل السابع عشر؟

## النطاق المجمد

1. المجاميع الأسية من الشكل
   \[
   S=\sum_{a<n\le b} e(f(n)),
   \qquad e(t)=e^{2\pi i t}.
   \]
2. الحد التافه ومعنى الادخار.
3. الجمع الجزئي ونقل الأوزان.
4. متباينة فرق فان دير كوربوت.
5. اختبار المشتقة الأولى بصياغة البعد عن الأعداد الصحيحة.
6. اختبار المشتقة الثانية بصيغة كلاسيكية مقتبسة ومشروحة.
7. عملية `A` في نسخة محدودة، وعملية `B` بوصفها `CITED / EXPLAINED`.
8. إطار محدود للأزواج الأسية دون تحسين شامل.
9. أمثلة خطية وتربيعية وتطبيق نموذجي على مجموع فايل.
10. صلة أحادية الاتجاه بالفصل 17، لا إعادة إثبات الحزمة الكاملة للأقواس الصغرى.

## المصادر المثبتة

- Montgomery–Vaughan, *Multiplicative Number Theory II*, Chapter 16.
- Graham–Kolesnik, *Van der Corput's Method of Exponential Sums*.
- O. Robert, *On van der Corput’s k-th derivative test for exponential sums*.
- Hong-quan Liu, *On a fundamental result in van der Corput's method of estimating exponential sums*.
- Hong-quan Liu, *On van der Corput's method for exponential sums*.
- Arias de Reyna, *Explicit van der Corput's d-th derivative estimate*.
- Heath-Brown, *A New k-th Derivative Estimate for Exponential Sums via Vinogradov's Mean Value*.

الحالة:

```text
SOURCE-LIST       = PASS FOR SCOPING
PRIMARY-EXTRACTION = PARTIAL / SUFFICIENT FOR CANDIDATE FREEZE
```

## البنود المغلقة

- [x] إنشاء سجل الأدلة.
- [x] إنشاء خريطة البرهان والاعتمادات.
- [x] استخدام Consensus لمسح الأدبيات المتخصصة والحديثة.
- [x] تجميد التطبيع `e(t)=exp(2 pi i t)` وتعريف `||x||`.
- [x] اختيار صيغة تأليف مرشحة لمتباينة فرق فان دير كوربوت.
- [x] تجميد اختبار المشتقة الأولى بالبعد عن الأعداد الصحيحة.
- [x] تجميد اختبار المشتقة الثانية بصيغة كلاسيكية `CITED / EXPLAINED`.
- [x] إبقاء عملية `B` مقتبسة ومشروحة.
- [x] تحديد عملية `A` إلى نسخة داخلية محدودة وإطار عام مقتبس.
- [x] تحديد إطار الأزواج الأسية بوصفه `CITED-FRAMEWORK`.
- [x] إجراء تدقيق عدم الدور مع الفصل 17 والحكم `PASS`.
- [x] حجز ثمانية معرفات نتائج بحالة `DRAFT / NON-CITABLE`.
- [x] تحديد حدود الادعاء: لا أفضل اختبارات حديثة ولا تحسين شامل للأزواج الأسية.

## البنود المتبقية

- [ ] تدقيق مستقل جبري لصيغة فرق فان دير كوربوت، خصوصًا العامل الخارجي والأوزان الطرفية.
- [ ] تدقيق مستقل كامل لبرهان اختبار المشتقة الأولى.
- [ ] تنفيذ اختبارات sanity على:
  - `z_n=1` لمتباينة الفرق؛
  - `f(n)=alpha n` للاختبار الأول؛
  - `f(n)=alpha n^2` للاختبار الثاني؛
  - طور فرق شبه ثابت لعملية `A`.
- [ ] إصدار مراجعة مستقلة لقرار `PASS-FOR-AUTHORING`.

## التصنيفات المجمدة

```text
ANT-ID-18-01    = IDENTITY / PROVED-HERE
ANT-LEM-18-01   = PROVED-HERE
ANT-LEM-18-02   = PROVED-HERE CANDIDATE / INDEPENDENT CHECK REQUIRED
ANT-THM-18-01   = PROVED-HERE CANDIDATE / INDEPENDENT CHECK REQUIRED
ANT-THM-18-02   = CITED / EXPLAINED
ANT-DEF-18-01   = DEFINITION / CITED-FRAMEWORK
ANT-PROP-18-01  = PROVED-HERE-LIMITED / CITED-GENERAL
ANT-PROP-18-02  = CITED / EXPLAINED
```

## حدود الادعاء

- لا تُنسب نظرية الأزواج الأسية الكاملة إلى الفصل.
- لا تستخدم نتيجة الأقواس الصغرى من الفصل 17 لإثبات الأدوات العامة هنا.
- لا يدعى الوصول إلى أفضل النتائج الحديثة.
- اختبارات المشتقة الثالثة وما فوق `DEFERRED`.
- عملية `B` لا تعرض بوصفها نتيجة من متباينة الفرق وحدها.
- تصنيف تقدير الأقواس الصغرى في الفصل 17 يبقى `CITED / COMPOSITE INPUT`.

## الملفات المرتبطة

- `research/literature-reviews/chapter-18-exponential-sums-van-der-corput-evidence.md`
- `research/literature-reviews/chapter-18-exponential-sums-van-der-corput-proof-map.md`
- `docs/CHAPTER_18_CONSENSUS_LITERATURE_AUDIT_2026-07-25.md`
- `docs/CHAPTER_18_SOURCE_NORMALIZATION_AND_THEOREM_FREEZE_2026-07-25.md`
- `docs/CHAPTER_18_NONCIRCULARITY_AUDIT_2026-07-25.md`
- `docs/RESULTS_REGISTRY_CHAPTER_18.md`

## القرار الحالي

```text
EVIDENCE-LEDGER       = CREATED
PROOF-MAP             = CREATED
CONSENSUS-AUDIT       = PASS-AS-SCOPING-INPUT
NORMALIZATION         = FROZEN
DERIVATIVE-TESTS      = FROZEN-AS-CANDIDATES
EXPONENT-PAIR-FRAME   = FROZEN-LIMITED
NONCIRCULARITY-AUDIT  = PASS
INDEPENDENT-REVIEW    = PENDING
PRE-AUTHORING-GATE    = OPEN
PASS-FOR-AUTHORING    = NO
AUTHORING             = BLOCKED
```
