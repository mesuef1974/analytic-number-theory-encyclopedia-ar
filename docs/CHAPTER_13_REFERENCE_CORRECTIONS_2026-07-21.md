# تصحيحات الإحالات التقنية للفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                 = 13
AUDIT                   = EXACT-TEXT / PRINTED-PAGE RECHECK
SOURCE                  = MONTGOMERY--VAUGHAN II (2026) / FULL PDF
MATHEMATICAL-CHANGES    = 0
PROVENANCE-CHANGES      = 0
REFERENCE-CORRECTIONS   = 3
REFERENCE-BLOCKERS      = 0 AFTER CORRECTION
RELEASE-READY           = NO
```

## 1. سبب إعادة الفتح

أعيد فحص الإحالات التقنية مباشرة في النسخة الكاملة من:

H. L. Montgomery and R. C. Vaughan,
*Multiplicative Number Theory II: Primes and Sieves*،
Cambridge Studies in Advanced Mathematics 218، 2026.

كانت الصيغ الرياضية وحالات المنشأ صحيحة، لكن ثلاث إحالات إلى الصفحة أو رقم
الصيغة احتاجت إلى تصحيح دقيق.

## 2. الإحالات المصححة

### 2.1 الغربال الكبير للشخصيات

الصحيح:

```text
THEOREM = 19.16
PRINTED-PAGE = 174
```

تبدأ المبرهنة 19.16 في أسفل الصفحة المطبوعة 174. الصفحة 175 تبدأ بتمارين
القسم 19.3، ولذلك فالإحالة السابقة إلى الصفحة 175 غير دقيقة.

### 2.2 المدخل الثنائي الأعظمي

الصحيح:

```text
THEOREM = 19.19
FORMULA = (19.35)
PRINTED-PAGE = 181
```

الصيغة الرئيسة في المبرهنة 19.19 هي (19.35). أما الصيغة (19.34) فتظهر في
الصفحة المطبوعة 180 داخل البرهان السابق لأداة عظمى أحادية، وتستعمل لاحقًا
في الوصول إلى المبرهنة 19.19، لكنها ليست رقم صيغة المبرهنة الثنائية نفسها.

### 2.3 مبرهنة Bombieri--Vinogradov ورد الموصلات

الصحيح:

```text
THEOREM = 20.2
THEOREM-START-PAGE = 194
PROOF-AND-CONDUCTOR-REDUCTION = 195--197
```

تبدأ صياغة المبرهنة 20.2 في الصفحة المطبوعة 194. يبدأ البرهان ورد الشخصيات
المستحثة إلى البدائية في الصفحة 195، وتستمر عملية جمع الموصلات وفصل المجال
واستعمال Siegel--Walfisz حتى اكتمال البرهان في الصفحة 197.

## 3. الإحالات التي بقيت صحيحة

```text
VAUGHAN-IDENTITY = (17.5) / PRINTED PAGES 55--56
MEAN-VALUE       = THEOREM 20.1 / PRINTED PAGE 189
```

## 4. الملفات التي supersede هذه الوثيقة إحالاتها القديمة

هذا السجل يصحح أي ظهور سابق للصيغ الآتية في ملفات التدقيق التاريخية:

```text
Theorem 19.16 / p. 175
Theorem 19.19 / equation (19.34) / p. 181
Theorem 20.2 / p. 195
conductor reduction / pp. 196--197
```

وتصبح الإحالات الحاكمة هي:

```text
Theorem 19.16 / p. 174
Theorem 19.19 / equation (19.35) / p. 181
Theorem 20.2 / p. 194
proof and conductor reduction / pp. 195--197
```

تشمل الملفات التاريخية التي قد تحمل الصياغة القديمة:

- `docs/CHAPTER_13_LARGE_SIEVE_MEAN_VALUE_AUDIT_2026-07-21.md`
- `docs/CHAPTER_13_TYPE_I_TYPE_II_MEAN_VALUE_AUDIT_2026-07-21.md`
- `research/literature-reviews/chapter-13-bombieri-vinogradov-evidence.md`

يُقرأ هذا السجل معها بوصفه تصحيحًا لاحقًا صريحًا، لا تغييرًا في البرهان.

## 5. الحكم

```text
MATHEMATICAL-BLOCKERS = 0
REFERENCE-BLOCKERS    = 0 AFTER RECORDED CORRECTION
TYPOGRAPHIC-BLOCKERS  = 0 IN THIS CORRECTION
PROOF-STATUS          = UNCHANGED
CHAPTER-STATE         = VERIFIED
PROMOTION             = NOT PERFORMED HERE
MERGE                 = NOT AUTHORIZED
RELEASE-READY         = NO
```
