# التدقيق المرجعي للفصل الرابع عشر — Barban--Davenport--Halberstam

التاريخ: 2026-07-24

```text
VERSION                    = 0.18.0-dev
CHAPTER                    = 14
AUDIT                      = REFERENCE-AUDIT
AUDITED-HEAD               = 5474d6a9a753642e653e4181654c08b0c29bd9f9
STATUS                     = PASS
REFERENCE-BLOCKERS         = 0
INHERITED-REVIEWED-INPUTS  = CHAPTER-12 / CHAPTER-13
BIBLIOGRAPHIC-DEBT         = 0 FOR PRE-AUTHORING
INDEPENDENT-REVIEW         = PENDING
PASS-FOR-AUTHORING         = NO
```

## 1. نطاق التدقيق

يدقق هذا الملف المداخل المرجعية المستعملة فعلًا في المسار النهائي:

```text
MV-01 weighted conductor reduction
 -> MV-02 weighted large sieve
 -> MV-04C conductor split
      small conductors: Siegel--Walfisz
      large conductors: primitive character large sieve
 -> MV-08 principal/local assembly
 -> MV-09 final range assembly
```

لا تدخل مواد Vaughan المؤجلة في سلسلة اعتماد الحد الكلاسيكي، ولذلك لا يلزمها تحقق مرجعي حاجز في هذه البوابة.

## 2. الغربال الكبير للشخصيات البدائية

الصيغة المستعملة هي

\[
\sum_{q\le Q}\frac q{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|\sum_{M<n\le M+N}c_n\chi(n)\right|^2
\le (N+Q^2)\sum|c_n|^2.
\]

وقد سبق التحقق منها في الفصل الثالث عشر بالمصدر:

```text
Hugh L. Montgomery; Robert C. Vaughan
Multiplicative Number Theory II: Primes and Sieves
Cambridge University Press, 2026
Theorem 19.16, printed page 174
Chapter 19: The Large Sieve, pp. 149--188
DOI: 10.1017/9781009445030
```

سجل الفصل الثالث عشر يثبت مطابقة رقم المبرهنة والصفحة والصيغة، وحالته النهائية `REVIEWED`. كما تؤكد صفحة Cambridge الرسمية عنوان الفصل ونطاق صفحاته وبيانات الكتاب.

```text
PRIMITIVE-LARGE-SIEVE-REFERENCE = PASS / INHERITED-REVIEWED-INPUT
```

## 3. المصدر التاريخي للغربال الكبير

المصدر التاريخي المسجل هو:

```text
Enrico Bombieri
On the Large Sieve
Mathematika 12(2) (1965), 201--225
DOI: 10.1112/S0025579300005313
```

تحققت بيانات المؤلف والعنوان والمجلد والعدد والصفحات وDOI من Cambridge Core. يستعمل هذا المرجع للسياق التاريخي، أما التطبيع الفني الدقيق المستعمل في البرهان فمن Montgomery--Vaughan، المبرهنة 19.16.

```text
LARGE-SIEVE-HISTORICAL-SOURCE = PASS
```

## 4. مدخل Siegel--Walfisz

المستعمل في الموصلات الصغيرة هو الحد الموحد، لكل ثابت `B>0`، عندما

\[
r\le(\log x)^B,
\]

من الشكل

\[
|\Psi^\circ(x,\chi^*)|
\ll_B x\exp(-c_B\sqrt{\log x}),
\]

مع ثابت غير فعال في المسار الحالي.

هذا المدخل مثبت ومراجع في الفصل الثاني عشر، وحالة الفصل `REVIEWED`. سجل تدقيق الفصل الثاني عشر يثبت صراحة:

```text
SIEGEL-WALFISZ-RANGE = q <= (log x)^A
REFERENCE-VERIFICATION = PASS-FOR-ADOPTED-ROUTE
FINAL-CONSTANT = INEFFECTIVE
```

كما يثبت أن رد الشخصية إلى الجد البدائي، وعزل الصفر الاستثنائي، وعدم الفعالية، وعدم الدور قد اجتازت التدقيق.

```text
SIEGEL-WALFISZ-REFERENCE = PASS / INHERITED-REVIEWED-INPUT
INEFFECTIVITY-LABEL       = PASS
```

## 5. حد دو لا فاليه بوسان للشخصية الرئيسية

حالة الموصل `1` تستعمل

\[
\psi(x)-x\ll x\exp(-c\sqrt{\log x}).
\]

الفصل الثاني عشر يسجل هذا المدخل بحالة `CITED`، ويفصل صراحة بينه وبين مبرهنة الأعداد الأولية النوعية في الفصل التاسع. وقد اجتاز التحقق المرجعي والمنطقي والمراجعة المستقلة ضمن الفصل الثاني عشر.

```text
PRINCIPAL-CHARACTER-INPUT = PASS / INHERITED-REVIEWED-INPUT
```

## 6. حد مربع فون مانغولت

المستعمل هو الحد القياسي

\[
\sum_{n\le x}\Lambda(n)^2\ll x\log x.
\]

وهو يتبع مباشرة من

\[
\Lambda(n)^2\le (\log x)\Lambda(n)
\qquad(n\le x)
\]

مع حد تشيبيشيف

\[
\psi(x)=\sum_{n\le x}\Lambda(n)\ll x.
\]

حد تشيبيشيف مثبت داخليًا في الفصل التاسع، والفصل التاسع `REVIEWED`. لذلك لا توجد هنا حاجة إلى مدخل خارجي جديد مستقل.

```text
LAMBDA-SQUARE-BOUND = PROVED-HERE-FROM-REVIEWED-RESULTS / PASS
```

## 7. تعامد الشخصيات والموصلات

الهويات الآتية ليست مقتبسة في الفصل الرابع عشر بوصفها صناديق سوداء:

- تعامد شخصيات ديريشليه على المجموعة المختزلة.
- هوية تحويل تباين الفئات إلى متوسط الشخصيات.
- فرادة الشخصية البدائية التي تستحث شخصية معطاة.
- صيغة حذف العوامل المحلية عند الانتقال إلى الجد البدائي.

هذه النتائج مثبتة داخليًا في الفصل السابع، والفصل السابع `REVIEWED`. أعاد الفصل الرابع عشر اشتقاق الهوية اللازمة للتوسيط وراجعها في `MV-10`.

```text
CHARACTER-ORTHOGONALITY = PROVED-HERE / REVIEWED-ANCESTOR / PASS
CONDUCTOR-REDUCTION      = PROVED-HERE / REVIEWED-ANCESTOR / PASS
```

## 8. عدم الخلط بين المراجع والمسارات

- لا ينسب الفصل الرابع عشر برهان الغربال الكبير إلى نفسه.
- لا يستعمل Bombieri--Vinogradov لإثبات BDH.
- لا يستعمل ورقة Vaughan 1975 في المسار النهائي بعد إصلاح المسار؛ تبقى مرجعًا لمسار Vaughan المؤجل فقط.
- لا تستعمل صيغة Montgomery--Hooley التقاربية في الحد العلوي الحالي.
- لا يدعى أن النتيجة الحالية هي مبرهنة باربان العامة.

```text
ORIGIN-LABELS      = PASS
ROUTE-SEPARATION   = PASS
NON-CIRCULARITY    = PASS
```

## 9. التحقق الببليوغرافي

تمت مطابقة البيانات التالية مع صفحات الناشرين الرسمية ومع سجلات الفصلين السابقين:

| المصدر | البيانات المتحققة | الحكم |
|---|---|---|
| Montgomery--Vaughan II (2026) | المؤلفان، العنوان، الناشر، السنة، DOI، ISBN، الفصل 19، الصفحات 149--188 | `PASS` |
| Bombieri (1965) | العنوان، Mathematika 12(2)، الصفحات 201--225، DOI | `PASS` |
| Vaughan (1975) | العنوان، JLMS s2-10(2)، الصفحات 153--162، DOI | `PASS / DEFERRED-ROUTE` |
| Chapter 12 Siegel--Walfisz package | النطاق، عدم الفعالية، التحقق المرجعي، حالة `REVIEWED` | `PASS` |
| Chapter 13 large-sieve package | المبرهنة 19.16، الصفحة 174، التطبيع، حالة `REVIEWED` | `PASS` |

لا يلزم إنشاء ملف BibTeX جديد قبل التأليف؛ المراجع الأساسية موجودة بالفعل في ملفات الفصلين 12 و13. عند التأليف يجب إما إعادة استعمال المفاتيح الحالية أو إنشاء ملف فصل 14 يضمها بلا تكرار.

## 10. ديون غير حاجزة

1. عند كتابة المتن، تثبيت إحالة مباشرة إلى المبرهنة 19.16 والصفحة 174.
2. تثبيت إحالة داخلية إلى نتيجة Siegel--Walfisz في الفصل الثاني عشر، مع تنبيه عدم الفعالية.
3. تثبيت اتفاقية الشخصية البدائية modulo `1` في الهامش أو التعريف.
4. عدم إدراج Vaughan 1975 في سلسلة اعتماد المبرهنة النهائية إلا إذا عرض المسار المؤجل تاريخيًا.

هذه نقاط تأليفية وليست عوائق مرجعية.

## 11. الحكم النهائي

```text
LARGE-SIEVE-TECHNICAL-REFERENCE = PASS
SIEGEL-WALFISZ-REFERENCE        = PASS
PRINCIPAL-CHARACTER-REFERENCE   = PASS
LAMBDA-SQUARE-BOUND             = PASS
CHARACTER-ANCESTOR-RESULTS      = PASS
BIBLIOGRAPHIC-METADATA          = PASS
ORIGIN-LABELS                   = PASS
REFERENCE-BLOCKERS              = 0
REFERENCE-AUDIT                 = PASS
INDEPENDENT-REVIEW              = PENDING
PASS-FOR-AUTHORING              = NO
NEXT                            = INDEPENDENT-REVIEW-PACKET
```
