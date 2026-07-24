# بوابة ما قبل التأليف — الفصل السابع عشر

التاريخ: 2026-07-25

```text
CHAPTER                    = 17
VERSION                    = 0.21.0-dev
TOPIC                      = CIRCLE METHOD / GOLDBACH / WARING
ISSUE                      = #32 / OPEN
BRANCH                     = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
EVIDENCE-LEDGER            = INITIALIZED
PROOF-MAP                  = INITIALIZED
PRIMARY-SOURCE-AUDIT       = PASS-FOR-RESEARCH-INTAKE
NONCIRCULARITY-AUDIT       = PASS
RESULT-IDS                 = 7 / PROVISIONALLY RESERVED
REFERENCE-BLOCKERS         = 3
SCOPE-BLOCKERS             = 2
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

النطاق الدقيق المقترح للبوابة:

1. التعامد الفورييري وصيغة تكامل عدد التمثيلات.
2. الأقواس الكبرى والصغرى.
3. التقريب المحلي، السلسلة المفردة، والتكامل المفرد.
4. نموذج وارينغ كلاسيكي واحد مضبوط النطاق.
5. مبرهنة الثلاثة أوليات بوصفها `CITED` مع خريطة برهان.
6. صيغة غولدباخ الثنائية بوصفها `HYPOTHESIS / OPEN`.
7. إحالة الأدوات العامة للمجاميع الأسية وفان دير كوربوت إلى الفصل الثامن عشر.

## 2. ما أُغلق

- [x] التحقق من رأس الأساس المعتمد.
- [x] قراءة خريطة الطريق وتثبيت عنوان الفصل.
- [x] قراءة موضع الفصل في المخطوط ونهاية الفصل السادس عشر.
- [x] إنشاء Issue مستقلة.
- [x] إنشاء فرع مستقل من الرأس المعتمد.
- [x] بدء سجل الأدلة.
- [x] بدء خريطة البرهان.
- [x] تحديد المصادر الأولية المؤسسة.
- [x] تدقيق عدم الدور مع الفصول السابقة والفصل 18.
- [x] حجز معرفات النتائج مبدئيًا.
- [x] تثبيت أن غولدباخ الثنائية `OPEN`.

## 3. العوائق الحاجبة

### عوائق مرجعية

1. تثبيت النص الأولي/الترجمة الموثوقة لمصدر فينوغرادوف وصياغته الدقيقة.
2. تثبيت المصدر والنسخة الدقيقة لمبرهنة وارينغ المستهدفة.
3. حسم إدراج مبرهنة هلفغوت الكاملة لغولدباخ الضعيف من عدمه.

### عوائق نطاقية

4. اختيار نتيجة وارينغ واحدة قابلة للعرض دون استباق الفصل 18.
5. تحديد تقديرات الأقواس الصغرى التي ستقتبس حرفيًا وحدودها ومعلماتها.

## 4. اختبارات الإغلاق

لا يصدر `PASS-FOR-AUTHORING` إلا بعد تحقق جميع البنود:

- [ ] `WARING-TARGET = FROZEN`.
- [ ] `MINOR-ARC-INPUTS = SOURCE-VERIFIED`.
- [ ] `VINOGRADOV-ATTRIBUTION = SOURCE-VERIFIED`.
- [ ] `HELFGOTT-SCOPE = DECIDED`.
- [ ] `NORMALIZATION = FROZEN` لـ`e(α)` والأقواس و`𝔖, 𝔍`.
- [ ] كل نتيجة مرتبطة بتصنيف واحد واضح من التصنيفات الحاكمة.
- [ ] لا اعتماد على فصل لاحق بوصفه نتيجة داخلية.
- [ ] لا عائق مرجعي أو منطقي مفتوح.
- [ ] صدور تدقيق مستقل للبوابة بحكم `PASS`.

## 5. قرار المرحلة الحالية

```text
RESEARCH-INTAKE       = AUTHORIZED
SOURCE-MINING         = AUTHORIZED
PROOF-DESIGN          = AUTHORIZED
RESULT-RESERVATION    = AUTHORIZED / NON-CITABLE
AUTHORING             = BLOCKED
CHAPTER-TEX           = DO NOT CREATE
MANUSCRIPT-MAIN       = DO NOT EDIT
```

هذه الوثيقة لا تغلق البوابة؛ بل تثبت ما أنجز وما بقي، وتحظر التأليف إلى أن تصدر وثيقة إغلاق مستقلة.