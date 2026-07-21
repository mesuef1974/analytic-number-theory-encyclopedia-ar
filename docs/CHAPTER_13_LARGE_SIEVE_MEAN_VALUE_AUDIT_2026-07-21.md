# تدقيق الغربال الكبير ومسار القيمة المتوسطة للفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                   = 13
AUDIT                     = LARGE-SIEVE / MEAN-VALUE / LOG-LOSS
SOURCE                    = MONTGOMERY--VAUGHAN II (2026)
LARGE-SIEVE               = PASS / CITED-INPUT
MAX-Y                     = PASS / PRESENT-IN-SOURCE
LOG-LOSS                  = PASS / B(A)=A+3
EFFECTIVITY               = INEFFECTIVE-IN-ADOPTED-ROUTE
TYPE-I-II-INTERNALIZATION = OPEN
AUTHORING                 = BLOCKED
```

## 1. المصدر الحاكم

المصدر المعتمد لهذا التدقيق هو:

H. L. Montgomery and R. C. Vaughan,
*Multiplicative Number Theory II: Primes and Sieves*، 2026،
الفصل 19 للغربال الكبير والفصل 20 للأوليات في المتتاليات الحسابية.

جرى التحقق من النص في نسخة المؤلف المستضافة لدى R. C. Vaughan، لا من مقتطف
ثانوي.

## 2. الغربال الكبير للشخصيات البدائية

يعرف المصدر

\[
S(\chi)=\sum_{M<n\le M+N}c_n\chi(n).
\]

ثم يثبت في المبرهنة 19.16، الصفحة المطبوعة 175، أنه لكل \(Q\ge1\):

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|S(\chi)\right|^2
\le
(N+Q^2)
\sum_{M<n\le M+N}|c_n|^2.
\]

النجمة تعني الجمع على الشخصيات البدائية modulo \(q\). الصيغة تشمل فترة
منقولة عامة \(M<n\le M+N\)، وتحمل الوزن الدقيق \(q/\varphi(q)\)، ولا تحتاج
إضافة ثابت مجهول إلى \(N+Q^2\).

### حكم المنشأ

```text
ANT-THM-13-01 = CITED
```

لن تنسب الموسوعة هذه المتراجحة إلى برهان داخلي في الفصل الثالث عشر. يمكن
شرح اشتقاقها من الغربال الجمعي ومجاميع غاوس، لكن النتيجة الحاكمة ستبقى
مدخلًا مقتبسًا.

## 3. مبرهنة القيمة المتوسطة المطلوبة

المبرهنة 20.1، الصفحة المطبوعة 189، تثبت لكل \(Q\ge1\) و\(x\ge2\):

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|\psi(y,\chi)|
\ll
\left(x+x^{5/6}Q+x^{1/2}Q^2\right)(\log x)^3.
\]

إذن القيمة العظمى في \(y\) ليست انتقالًا غير مبرهن من تقدير عند \(x\)، بل
موجودة أصلًا في النتيجة المتوسطة التي يجب إعادة بنائها داخل الفصل.

### حكم المنشأ المرشح

```text
ANT-THM-13-02 = PROVED-HERE
```

لكن هذا الحكم لا يصبح نافذًا إلا بعد تدخيل:

1. هوية Vaughan.
2. تقدير Type I.
3. تقدير Type II.
4. معالجة المجاميع الجزئية التي تنتج `sup_{y\le x}`.

حتى ذلك الحين تبقى النتيجة `TARGET / NON-CITABLE`.

## 4. صيغة Bombieri--Vinogradov في المصدر

يعرف المصدر

\[
E(x;q,a)=\psi(x;q,a)-\frac{x}{\varphi(q)},
\]

و

\[
E^*(x,q)=
\sup_{y\le x}
\max_{(a,q)=1}
|E(y;q,a)|.
\]

المبرهنة 20.2، الصفحة المطبوعة 195، تعطي

\[
\sum_{q\le Q}E^*(x,q)
\ll
x^{1/2}Q(\log x)^3,
\]

في المجال

\[
x^{1/2}(\log x)^{-C}\le Q\le x^{1/2},
\]

حيث \(C>0\) ثابت، والثابت الضمني قد يعتمد عليه.

## 5. اشتقاق الخسارة اللوغاريتمية الصريحة

لإثبات الصيغة الموسوعية المرشحة عند أس ادخار \(A>0\)، نضع

\[
B=A+3,
\qquad
Q_0=x^{1/2}(\log x)^{-B}.
\]

بتطبيق المبرهنة 20.2 عند \(Q_0\) مع معامل المجال \(C=B\)، نحصل على

\[
\sum_{q\le Q_0}E^*(x,q)
\ll
x^{1/2}Q_0(\log x)^3
=
\frac{x}{(\log x)^A}.
\]

وبما أن الطرف الأيسر متزايد في \(Q\)، فإن النتيجة نفسها تصح لكل
\(Q\le Q_0\). لذلك يمكن اعتماد الشرط الصريح

\[
Q\le\frac{x^{1/2}}{(\log x)^{A+3}}.
\]

لا حاجة في هذا المسار إلى إبقاء \(B(A)\) مجهولًا، ما دام الفصل يتبنى قوة
اللوغاريتم \(3\) الواردة في المبرهنة 20.1.

### الحكم

```text
LOG-LOSS-AUDIT = PASS
B(A)           = A+3
```

إذا اختير لاحقًا مسار آخر أو تطبيع آخر، يجب إعادة فتح هذا الحكم.

## 6. الانتقال من الموصل إلى الترديد

برهان المبرهنة 20.2 في المصدر يقوم بالخطوات الآتية صراحة:

1. يكتب خطأ الفئة بمتوسط الشخصيات modulo \(q\).
2. يرد كل شخصية مستحثة إلى شخصية بدائية ذات موصل \(d\mid q\).
3. يضبط الفرق المحلي على القوى الأولية القاسمة لـ\(q\) بحد
   \(O((\log qy)^2)\).
4. يجمع تعدد الاستحثاثات بواسطة

\[
\sum_{\substack{q\le Q\\d\mid q}}
\frac1{\varphi(q)}
\ll
\frac1{\varphi(d)}\log\frac{2Q}{d}.
\]

5. يطبق المبرهنة 20.1 على كتل ديادية من الموصلات.

هذا يغلق صحة بنية الرد، لكنه لا يغني عن كتابة البرهان داخل الموسوعة بصورة
مستقلة ومتوافقة مع ترميز الفصول السابقة.

```text
CONDUCTOR-TO-MODULUS STRUCTURE = PASS / SOURCE-VERIFIED
INTERNAL PROOF                 = OPEN
```

## 7. الفعالية

في الترديدات الصغيرة

\[
q\le (\log x)^{C+1},
\]

يستعمل برهان المصدر مبرهنة Siegel--Walfisz مباشرة. النسخة المعتمدة في الفصل
الثاني عشر غير فعالة بسبب عقدة Siegel. لذلك يرث المسار الحالي عدم الفعالية.

```text
EFFECTIVITY = INEFFECTIVE-IN-ADOPTED-ROUTE
```

لا يجوز وصف ثابت Bombieri--Vinogradov في هذا الفصل بأنه فعال إلا بعد تقديم
مسار بديل فعال للترديدات الصغيرة أو صيغة تستبعد/تعزل الترديد الاستثنائي.
هذا التحسين غير مطلوب لحالة `REVIEWED`، لكنه يجب أن يظهر في حدود الادعاء.

## 8. العلاقة بـElliott--Halberstam

المصدر يضع بعد Bombieri--Vinogradov مباشرة فرضية Elliott--Halberstam، التي
تستبدل مستوى \(1/2\) بمجال \(Q\le x^{1-\varepsilon}\). هذا يثبت أن الفصل
المخطط يجب أن يفصل بوضوح بين:

- المستوى غير المشروط \(1/2\) حتى خسارة لوغاريتمية؛
- الفرضية المتوسطة الأقوى حتى \(1-\varepsilon\)؛
- نتائج موزونة أو مقيدة تتجاوز \(1/2\) ولا تثبت الفرضية العامة.

## 9. الحكم النهائي للتدقيق

```text
LARGE-SIEVE-NORMALIZATION = CLOSED / PASS
LARGE-SIEVE-PROVENANCE    = CITED
MAX-Y-MECHANISM           = CLOSED AT THEOREM LEVEL
LOG-LOSS                  = CLOSED / B=A+3
CONDUCTOR-STRUCTURE        = VERIFIED / INTERNALIZATION OPEN
EFFECTIVITY               = RESOLVED / INEFFECTIVE ROUTE
VAUGHAN-IDENTITY           = OPEN
TYPE-I                     = OPEN
TYPE-II                    = OPEN
NON-CIRCULARITY            = OPEN
PRE-AUTHORING-GATE         = OPEN
AUTHORING                  = BLOCKED
```
