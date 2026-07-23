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
SOURCE-TEXT-PINNING           = PARTIAL
MEAN-VALUE-ROUTE-GATE         = CLOSED / ROUTE-SELECTED
MEAN-VALUE-THEOREM-GATE       = OPEN / PROOF-NOT-INTERNALIZED
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

إذا وضعنا ببساطة

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

هذا ليس من رتبة `xR log x` المطلوبة لـBDH، خصوصًا عندما `R` أصغر كثيرًا من `x^{1/2}`. إذن الغربال الكبير الخام لا يلتقط البنية الإضافية التي تخفض العامل من `x+R^2` إلى المقياس المتوسط المناسب.

```text
DIRECT-LARGE-SIEVE => CORRECT BUT TOO LARGE
```

## 4. لماذا لا نستخدم Bombieri--Vinogradov عكسيًا

Bombieri--Vinogradov يضبط متوسطًا من الرتبة الأولى لأكبر خطأ:

\[
\sum_{q\le Q}\max_{(a,q)=1}|E(x;q,a)|.
\]

أما BDH فيضبط

\[
\sum_{q\le Q}\sum_{(a,q)=1}|E(x;q,a)|^2.
\]

الانتقال من الأول إلى الثاني يحتاج حدًا نقطيًا إضافيًا، ويؤدي في المسار الساذج إلى خسارة لا تستعيد رتبة `xQ log x`. لذلك يمنع هذا التدقيق أي استدلال عكسي من الفصل الثالث عشر إلى الفصل الرابع عشر.

## 5. المسار المختار

اعتمد المسار التالي:

```text
CHARACTER PARSEVAL
    -> PRIMITIVE-CONDUCTOR REDUCTION
    -> BARBAN GENERAL MEAN-SQUARE THEOREM
    -> SPECIALIZATION TO VON MANGOLDT COEFFICIENTS
    -> PRINCIPAL / LOCAL CORRECTIONS
    -> BDH CLASSICAL UPPER BOUND
```

المكوّن الحاسم هو **مبرهنة باربان العامة للقيمة المتوسطة التربيعية** أو برهان مكافئ لها كما يعرضه Montgomery في الفصل «The mean value theorem of Barban» من *Topics in Multiplicative Number Theory*، الصفحات 145--154.

هذا المسار مستقل منطقيًا عن Bombieri--Vinogradov. يمكنه استعمال الغربال الكبير بوصفه أداة داخل برهان باربان، لكنه لا يستبدل برهان باربان بتطبيق مباشر للغربال.

## 6. قرار المنشأ

حتى فحص النص الكامل وإعادة بناء البرهان:

| المكوّن | القرار |
|---|---|
| الغربال الكبير | `CITED / FROM CHAPTER 13` |
| تحويل التباين بالشخصيات | `PROVED-HERE` |
| رد الموصلات | `PROVED-HERE` |
| مبرهنة باربان العامة | `TARGET / SOURCE-PINNING-PARTIAL` |
| تطبيقها على `Lambda` | `OPEN` |
| حد BDH النهائي | `OPEN` |

لا تسجل مبرهنة باربان العامة `CITED` بعد؛ لأن موضع الفصل معروف لكن نص الفرضيات والتطبيع والثوابت لم يثبت بعد من النص الكامل.

## 7. المصادر المثبتة في هذا التدقيق

1. H. L. Montgomery, *Topics in Multiplicative Number Theory*, LNM 227 (1971):
   - فصل «The mean value theorem of Barban»؛
   - الصفحات 145--154.
2. R. C. Vaughan, “Mean Value Theorems in Prime Number Theory”, JLMS (2) 10 (1975), 153--162، DOI `10.1112/jlms/s2-10.2.153`.
3. P. X. Gallagher, “Bombieri's mean value theorem”, Mathematika 15 (1968), 1--6، DOI `10.1112/S002557930000231X`.
4. H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory II: Primes and Sieves* (2026), الفصلان 19 و20، للغربال الكبير ومسار Bombieri--Vinogradov؛ وهما مدخل مقارنة لا مصدرًا لبرهان BDH في حالته الحالية.

## 8. البوابة التالية

يلزم إغلاق البنود الآتية قبل التأليف:

1. فحص النص الكامل للفصل 18 من Montgomery 1971 أو مصدر أولي مكافئ.
2. استخراج الصيغة العامة الدقيقة لمبرهنة باربان، بما فيها شروط المعاملات ونطاق `Q`.
3. إعادة بناء البرهان مع منع استعمال BDH أو نتيجة مكافئة بصورة دورية.
4. تطبيق الصيغة على معاملات فون مانغولت مع ضبط الحد القطري وتصحيحات الموصل.
5. تثبيت رتبة `xQ log x` ومجال `Q` والفعالية.

## 9. الحكم

```text
CHAPTER-13-MEAN-VALUE         = NOT-A-BDH-SECOND-MOMENT
DIRECT-LARGE-SIEVE            = INSUFFICIENT-FOR-xQlogx
BOMBIERI-VINOGRADOV-REVERSE   = REJECTED
BARBAN-GENERAL-MEAN-SQUARE    = ADOPTED ROUTE
NON-CIRCULARITY               = PASS AT ROUTE LEVEL
PROOF-INTERNALIZATION         = OPEN
PASS-FOR-AUTHORING            = NO
```
