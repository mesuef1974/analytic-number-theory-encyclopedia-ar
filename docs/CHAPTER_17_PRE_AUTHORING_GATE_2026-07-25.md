# بوابة ما قبل التأليف — الفصل السابع عشر

التاريخ: 2026-07-25

```text
CHAPTER                    = 17
VERSION                    = 0.21.0-dev
TOPIC                      = CIRCLE METHOD / GOLDBACH / WARING
ISSUE                      = #32 / OPEN
BRANCH                     = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
EVIDENCE-LEDGER            = UPDATED
PROOF-MAP                  = INITIALIZED
PRIMARY-SOURCE-AUDIT       = PASS-FOR-RESEARCH-INTAKE
NONCIRCULARITY-AUDIT       = PASS
RESULT-IDS                 = 7 / PROVISIONALLY RESERVED
REFERENCE-BLOCKERS         = 2
SCOPE-BLOCKERS             = 1
PRE-AUTHORING-GATE         = OPEN
PASS-FOR-AUTHORING         = NO
AUTHORING                  = BLOCKED
MANUSCRIPT-LINK            = PROHIBITED
MERGE                      = NOT AUTHORIZED
RELEASE-READY              = NO
```

## 1. النطاق الصحيح

العنوان المثبت من خريطة الطريق:

> **الطريقة الدائرية ومدخل إلى غولدباخ ووارينغ**.

النطاق المعتمد للبوابة:

1. التعامد الفورييري وصيغة تكامل عدد التمثيلات.
2. الأقواس الكبرى والصغرى.
3. التقريب المحلي، السلسلة المفردة، والتكامل المفرد.
4. الصيغة التقاربية الكلاسيكية في وارينغ بحالة `CITED / EXPLAINED`، مع إثبات البنية الأساسية داخليًا.
5. مبرهنة فينوغرادوف للأعداد الفردية الكبيرة بحالة `CITED`.
6. مبرهنة هلفغوت لكل عدد فردي أكبر من 5 بحالة `CITED / MODERN COMPLETION`.
7. غولدباخ الثنائية بحالة `HYPOTHESIS / OPEN`.
8. إحالة الأدوات العامة للمجاميع الأسية وفان دير كوربوت إلى الفصل الثامن عشر.

## 2. ما أُغلق

- [x] التحقق من رأس الأساس المعتمد.
- [x] قراءة خريطة الطريق وتثبيت عنوان الفصل.
- [x] قراءة موضع الفصل في المخطوط ونهاية الفصل السادس عشر.
- [x] إنشاء Issue مستقلة وفرع مستقل وDraft PR.
- [x] بدء سجل الأدلة وخريطة البرهان.
- [x] تحديد المصادر المؤسسة.
- [x] تدقيق عدم الدور مع الفصول السابقة والفصل 18.
- [x] حجز معرفات النتائج مبدئيًا.
- [x] تثبيت أن غولدباخ الثنائية `OPEN`.
- [x] `WARING-TARGET = FROZEN`.
- [x] `HELFGOTT-SCOPE = DECIDED`.
- [x] تثبيت الصياغة النوعية لمبرهنة فينوغرادوف.

## 3. القرارات المجمدة

### 3.1 هدف وارينغ

```text
WARING-TARGET = CLASSICAL ASYMPTOTIC FORMULA
CLASSIFICATION = CITED / EXPLAINED
INTERNAL-PROOF = ORTHOGONALITY + MAJOR-TERM STRUCTURE
DEEP-MINOR-ARC-ESTIMATE = CITED
BEST-MODERN-THRESHOLD = OUT OF SCOPE
```

### 3.2 نطاق هلفغوت

```text
HELFGOTT-SCOPE = INCLUDE
THEOREM = EVERY ODD INTEGER > 5 IS A SUM OF THREE PRIMES
CLASSIFICATION = CITED
FULL-PROOF = OUT OF SCOPE
FINITE-COMPUTATION = FINITE-VERIFIED COMPONENT
```

### 3.3 فينوغرادوف

```text
THEOREM-STATEMENT = VERIFIED
STATEMENT = EVERY SUFFICIENTLY LARGE ODD INTEGER IS A SUM OF THREE PRIMES
CLASSIFICATION = CITED
EXACT-1937-BIBLIOGRAPHY = OPEN / INDEX CONFLICT
```

## 4. العوائق الحاجبة المتبقية

### عوائق مرجعية

1. حسم بيانات الورقة القصيرة الأصلية لفينوغرادوف؛ الفهارس تعرض سجلات متعارضة للمجلد والصفحات.
2. تثبيت مصدر وصياغة كمية محددة لتقدير الأقواس الصغرى المستخدم في مسار وارينغ.

### عائق نطاقي/ترميزي

3. تجميد التطبيع النهائي لـ`e(α)`، ومقاييس الأقواس، وتعريفَي `𝔖` و`𝔍`.

## 5. اختبارات الإغلاق

لا يصدر `PASS-FOR-AUTHORING` إلا بعد تحقق جميع البنود:

- [x] `WARING-TARGET = FROZEN`.
- [ ] `MINOR-ARC-INPUTS = SOURCE-VERIFIED`.
- [ ] `VINOGRADOV-ATTRIBUTION = SOURCE-VERIFIED` على المستوى الببليوغرافي الدقيق.
- [x] `HELFGOTT-SCOPE = DECIDED`.
- [ ] `NORMALIZATION = FROZEN` لـ`e(α)` والأقواس و`𝔖, 𝔍`.
- [x] كل نتيجة مرتبطة مبدئيًا بتصنيف حاكم واضح.
- [x] لا اعتماد على فصل لاحق بوصفه نتيجة داخلية.
- [ ] لا عائق مرجعي أو منطقي مفتوح.
- [ ] صدور تدقيق مستقل للبوابة بحكم `PASS`.

## 6. قرار المرحلة الحالية

```text
RESEARCH-INTAKE       = AUTHORIZED
SOURCE-MINING         = AUTHORIZED
PROOF-DESIGN          = AUTHORIZED
RESULT-RESERVATION    = AUTHORIZED / NON-CITABLE
AUTHORING             = BLOCKED
CHAPTER-TEX           = DO NOT CREATE
MANUSCRIPT-MAIN       = DO NOT EDIT
```

هذه الوثيقة لا تغلق البوابة. انخفضت العوائق من خمسة إلى ثلاثة، لكن التأليف ما يزال محظورًا حتى إغلاقها وتدقيق البوابة مستقلًا.
