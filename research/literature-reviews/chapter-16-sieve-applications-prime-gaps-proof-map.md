# خريطة برهان الفصل السادس عشر

آخر تحديث: 2026-07-24

```text
CHAPTER               = 16
VERSION               = 0.20.0-dev
BASE-MAIN             = 5ebe7fd5ade9e1c1c7c3edabf646bad90a9cff6a
BRANCH                = agent/chapter-16-sieve-applications-prime-gaps-v0.20.0
ISSUE                 = #29 / OPEN
PRE-AUTHORING-GATE    = OPEN
AUTHORING             = BLOCKED
PASS-FOR-AUTHORING    = NO
```

## البنية المرشحة

### الوحدة 16.1 — من غربال سيلبرغ إلى التطبيقات

- استدعاء مضبوط للحد العلوي المنتهي من الفصل 15.
- إعادة تعريف الأنماط المقبولة محليًا فقط عند الحاجة.
- فصل البعد الغربالي عن مستوى التوزيع.
- لا إعادة إثبات للمادة المغلقة في الفصل 15.

### الوحدة 16.2 — برون والأنماط الثنائية

هدف مرشح:

- اشتقاق حد علوي من الرتبة الصحيحة لعدد الأزواج المرشحة أوليًا.
- شرح كيف يقود حد علوي مناسب إلى تقارب مجموع مقلوبات الأوليات التوأم.

تصنيف أولي:

```text
UPPER-BOUND-PAIR-COUNT = PROVED-HERE أو CITED-AUGMENTED
BRUN-SUM-CONVERGENCE   = PROVED-HERE محتمل بعد تثبيت المدخل الكمي
TWIN-PRIME-EXISTENCE   = NOT CLAIMED
```

### الوحدة 16.3 — الأعداد شبه الأولية ومبرهنة تشن

- تعريف \(P_r\) بدقة.
- توضيح لماذا تجاوز عائق التكافؤ يتطلب معلومات إضافية.
- عرض مبرهنة تشن بصيغة مقتبسة فقط ما لم تُبنَ سلسلة اعتماد كاملة.

```text
CHEN-THEOREM = CITED
FULL-PROOF   = DEFERRED
```

### الوحدة 16.4 — طريقة GPY

اعتمادات مرشحة:

1. أوزان سيلبرغ معدلة على كثيرات حدود قابلة للقسمة.
2. متوسطات دالة فون مانغولد في المتتاليات الحسابية.
3. Bombieri--Vinogradov من الفصل 13.
4. نسبة بين متوسط موزون لعدد الأوليات ومتوسط الوزن.

حدود الوحدة:

- شرح الآلية البرهانية المركزية.
- عدم ادعاء الفجوات المحدودة من Bombieri--Vinogradov الكلاسيكية وحدها.

### الوحدة 16.5 — Zhang

سلسلة الاعتماد المرشحة:

```text
DISTRIBUTION-BEYOND-1/2 FOR SMOOTH MODULI
        +
GPY-TYPE WEIGHT
        ->
BOUNDED PRIME GAPS
```

التصنيف:

```text
ZHANG-DISTRIBUTION-INPUT = CITED
ZHANG-BOUNDED-GAPS       = CITED
FULL TECHNICAL PROOF     = DEFERRED
```

### الوحدة 16.6 — Maynard--Tao

سلسلة الاعتماد المرشحة:

```text
MULTIDIMENSIONAL SELBERG WEIGHT
        +
BOMBIERI--VINOGRADOV LEVEL 1/2
        +
VARIATIONAL INTEGRALS
        ->
MANY PRIMES IN BOUNDED ADMISSIBLE TUPLES
```

المطلوب قبل التأليف:

- تثبيت تعريف الدوال التكاملية المستخدمة.
- تحديد النتيجة التي يمكن شرح برهانها ضمن حجم الفصل.
- الفصل بين المبرهنة النوعية والثوابت العددية المتغيرة تاريخيًا.

## خريطة عدم الدور

| المدخل | موضعه السابق | استعماله في الفصل 16 |
|---|---|---|
| Bombieri--Vinogradov | الفصل 13 | مدخل موزون في GPY وMaynard |
| Barban--Davenport--Halberstam | الفصل 14 | سياق متوسط تربيعي؛ ليس بديلًا تلقائيًا عن كل مدخل توزيع |
| حد سيلبرغ العلوي | الفصل 15 | أساس التطبيقات البسيطة فقط |
| عائق التكافؤ | الفصل 15 | تفسير الحاجة إلى شبه الأوليات أو معلومات إضافية |

## بوابات القرار

### Gate A — اختيار النتيجة المركزية

يجب اختيار واحدة فقط بوصفها النتيجة التعليمية المركزية المثبتة أو المشروحة بعمق:

1. مبرهنة برون وتقارب مجموع برون؛ أو
2. نواة GPY النوعية؛ أو
3. مبرهنة Maynard تعليمية مبسطة.

لا تُجمع ثلاثة براهين عميقة كاملة في فصل واحد بلا تقدير للحجم والاعتمادات.

### Gate B — المراجع الأصلية

- [ ] Brun.
- [ ] Chen.
- [ ] Goldston--Pintz--Yıldırım.
- [ ] Zhang.
- [ ] Maynard.
- [ ] Tao أو المرجع الموازي المناسب.

### Gate C — التصنيف

لكل نتيجة يجب تسجيل:

```text
OBJECT
HYPOTHESES
INPUTS
PROOF-LOCATION
CONSTANT-STATUS
EFFECTIVITY
CLASSIFICATION
NON-CLAIMS
```

### Gate D — الإذن

```text
PASS-FOR-AUTHORING = NO
```

يبقى كذلك حتى إغلاق الأدلة، واختيار النتيجة المركزية، وتدقيق عدم الدور، واعتماد نطاق الفصل.
