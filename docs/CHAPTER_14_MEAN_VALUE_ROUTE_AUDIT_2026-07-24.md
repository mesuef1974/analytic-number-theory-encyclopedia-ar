# تدقيق مسار القيمة المتوسطة — الفصل الرابع عشر

التاريخ: 2026-07-24

```text
VERSION                       = 0.18.0-dev
CHAPTER                       = 14
TOPIC                         = BARBAN--DAVENPORT--HALBERSTAM
AUDIT                         = MEAN-VALUE-ROUTE / NON-CIRCULARITY
CHAPTER-13-INPUT              = AVAILABLE / INSUFFICIENT-AS-STATED
DIRECT-LARGE-SIEVE            = INSUFFICIENT-FOR-TARGET-ORDER
BARBAN-MEAN-SQUARE-ROUTE      = SELECTED
PROOF-POLICY                  = FULL-INTERNALIZATION-FIRST
REFERENCE-AUDIT               = AFTER-INTERNAL-PROOF
MEAN-VALUE-ROUTE-GATE         = CLOSED / ROUTE-SELECTED
MEAN-VALUE-THEOREM-GATE       = OPEN / INTERNAL-PROOF-PENDING
PRE-AUTHORING-GATE            = OPEN
AUTHORING                     = BLOCKED
RELEASE-READY                 = NO
```

## 1. السؤال الحاكم

بعد تحويل التباين إلى الشخصيات ورد الشخصيات غير البدائية إلى موصلاتها، نحتاج إلى ضبط كمية من النوع

\[
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}
\left|\Psi^\circ(x,\chi^*)\right|^2,
\qquad
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}.
\]

السؤال هو: هل تكفي مبرهنة القيمة المتوسطة المثبتة في الفصل الثالث عشر، مع الغربال الكبير، لإنتاج الحد

\[
V_\psi(x,Q)\ll_M xQ\log x
\]

في المجال الكلاسيكي المرشح؟

## 2. ما يقدمه الفصل الثالث عشر فعليًا

الفصل الثالث عشر يملك مدخلين مختلفين:

1. الغربال الكبير للشخصيات البدائية:

\[
\sum_{q\le R}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|\sum_{n\le N}c_n\chi(n)\right|^2
\le (N+R^2)\sum_{n\le N}|c_n|^2.
\]

2. مبرهنة قيمة متوسطة من الرتبة الأولى لمجاميع فون مانغولت:

\[
\sum_{q\le R}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|\psi(y,\chi)|
\ll
\left(x+x^{5/6}R+x^{1/2}R^2\right)(\log x)^3.
\]

المدخل الثاني هو متوسط للقيم المطلقة، لا متوسطًا لمربعاتها. لذلك لا يمكن استعماله بوصفه BDH مقنعًا أو استنتاج المتوسط التربيعي المطلوب منه بلا حد أقصى مستقل يسبب خسارة كبيرة.

## 3. فشل التطبيق المباشر للغربال الكبير

إذا وضعنا

\[
c_n=\Lambda(n),
\]

فإن

\[
\sum_{n\le x}|c_n|^2
=
\sum_{n\le x}\Lambda(n)^2
\asymp x\log x
\]

على المقياس المتوقع. يعطي الغربال الكبير عند موصلات حتى `R` حدًا من الشكل

\[
(x+R^2)x\log x.
\]

هذا ليس من رتبة `xR log x` المطلوبة لـBDH. إذن الغربال الكبير الخام لا يلتقط البنية الإضافية التي تخفض العامل إلى المقياس المتوسط الصحيح.

```text
DIRECT-LARGE-SIEVE => CORRECT BUT TOO LARGE
```

## 4. منع الاستدلال العكسي من Bombieri--Vinogradov

Bombieri--Vinogradov يضبط متوسطًا من الرتبة الأولى لأكبر خطأ، بينما BDH يضبط متوسط مربعات الأخطاء على الترديدات والفئات معًا. الانتقال الساذج بينهما يحتاج حدًا نقطيًا إضافيًا ويؤدي إلى خسارة لا تستعيد رتبة `xQ log x`. لذلك يمنع هذا التدقيق أي استدلال عكسي من الفصل الثالث عشر إلى الفصل الرابع عشر.

## 5. المسار المختار

```text
CHARACTER PARSEVAL
    -> PRIMITIVE-CONDUCTOR REDUCTION
    -> INTERNAL PROOF OF BARBAN GENERAL MEAN-SQUARE THEOREM
    -> SPECIALIZATION TO VON MANGOLDT COEFFICIENTS
    -> PRINCIPAL / LOCAL CORRECTIONS
    -> INTERNAL PROOF OF BDH CLASSICAL UPPER BOUND
    -> LOGIC AUDIT
    -> REFERENCE AUDIT
    -> INDEPENDENT REVIEW
```

المكوّن الحاسم هو مبرهنة باربان العامة للقيمة المتوسطة التربيعية أو صيغة مكافئة لها. لكن قرار المشروع هو عدم اعتمادها صندوقًا أسود في الفصل الرابع عشر.

## 6. سياسة الإثبات الداخلي

اعتمد المالك السياسة الآتية:

```text
INTERNAL-PROOF-FIRST = YES
CITATION-AS-SUBSTITUTE-FOR-PROOF = NO
REFERENCE-CHECK-DURING-PROOF = ORIENTATION-ONLY
FORMAL-AUDIT-BEFORE-PROOF-COMPLETE = NO
FORMAL-AUDIT-AFTER-PROOF-COMPLETE = REQUIRED
```

وعليه:

1. يعاد بناء البرهان كاملًا داخل ملفات البحث أولًا.
2. يسمح باستعمال المراجع لتحديد الطريق ومنع إعادة اختراع مسار خاطئ، لكن لا تمنح نتيجة `CITED` بدل الإثبات.
3. كل خطوة تصنف مؤقتًا `PROVED-HERE-DRAFT` بعد اشتقاقها، ولا تصبح `PROVED-HERE` إلا بعد التدقيق.
4. لا تبدأ كتابة متن الفصل قبل اكتمال سلسلة البرهان وإغلاق تدقيق ما قبل التأليف.
5. بعد اكتمال البرهان تجرى ثلاثة تدقيقات منفصلة: منطقي، مرجعي، ومستقل.

## 7. وحدات البرهان المطلوبة

يُقسّم الإثبات الداخلي إلى الوحدات الآتية:

```text
MV-01  weighted conductor decomposition
MV-02  duality / character large-sieve preparation
MV-03  bilinear decomposition of arithmetic coefficients
MV-04  diagonal contribution
MV-05  off-diagonal contribution
MV-06  Barban general mean-square estimate
MV-07  specialization to Lambda
MV-08  principal-character and local-prime corrections
MV-09  dyadic summation and Q-range
MV-10  classical BDH upper bound
```

لا تغلق بوابة مبرهنة القيمة المتوسطة إلا بعد اكتمال `MV-01` إلى `MV-06`. ولا يغلق الحد الكلاسيكي إلا بعد اكتمال `MV-07` إلى `MV-10`.

## 8. قرار المنشأ المؤقت

| المكوّن | الحالة الحالية |
|---|---|
| الغربال الكبير | `CITED-TOOL / FROM CHAPTER 13` |
| تحويل التباين بالشخصيات | `PROVED-HERE` |
| رد الموصلات | `PROVED-HERE` |
| مبرهنة باربان العامة | `TARGET / INTERNAL-PROOF-REQUIRED` |
| تطبيقها على `Lambda` | `OPEN` |
| حد BDH النهائي | `OPEN` |

المراجع لا تستعمل لإغلاق المبرهنة، بل لمقارنة البرهان الداخلي بعد اكتماله.

## 9. الحكم

```text
CHAPTER-13-MEAN-VALUE         = NOT-A-BDH-SECOND-MOMENT
DIRECT-LARGE-SIEVE            = INSUFFICIENT-FOR-xQlogx
BOMBIERI-VINOGRADOV-REVERSE   = REJECTED
BARBAN-GENERAL-MEAN-SQUARE    = ADOPTED ROUTE
PROOF-INTERNALIZATION         = MANDATORY
AUDIT-ORDER                   = PROOF -> LOGIC -> REFERENCES -> INDEPENDENT
PASS-FOR-AUTHORING            = NO
```
