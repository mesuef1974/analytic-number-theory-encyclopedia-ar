# MV-04B — تدقيق طاقة التصادمات الضربية

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
UNIT                            = MV-04B
TOPIC                           = MULTIPLICATIVE-COLLISION-ENERGY
STATUS                          = OBSTRUCTION-PROVED / ROUTE-CORRECTION-REQUIRED
GENERIC-DIVISOR-BOUND           = PROVED-HERE-DRAFT
POLYLOG-LOSS                    = NOT-PROVED
TARGET-ORDER-COMPATIBILITY      = FAIL-FOR-CURRENT-ROUTE
MV-04-FULL-DIAGONAL             = OPEN
NEXT-UNIT                       = MV-04C / ROUTE-REPAIR
PASS-FOR-AUTHORING              = NO
```

## 1. السؤال

لمستطيل Type II نكتب

\[
c_n=\sum_{mk=n}\alpha_m\beta_k,
\]

حيث \(M<m\le2M\)، و\(K<k\le2K\)، و\(MK\ll x\). القطر العددي الكامل هو

\[
\sum_n |c_n|^2.
\]

المطلوب معرفة هل يمكن ضبطه، لمعاملات عامة ذات حدود \(\ell^2\)، بحد من الرتبة

\[
(\log x)^A\|\alpha\|_2^2\|\beta\|_2^2
\]

ببرهان شكلي فقط.

## 2. عدد التمثيلات

عرّف

\[
d_{M,K}(n)
=
\#\{(m,k):mk=n,\ M<m\le2M,\ K<k\le2K\}.
\]

بمتراجحة كوشي:

\[
|c_n|^2
\le
 d_{M,K}(n)
\sum_{mk=n}|\alpha_m|^2|\beta_k|^2.
\]

ومن ثم

\[
\sum_n|c_n|^2
\le
\Bigl(\max_{n\le 4MK}d_{M,K}(n)\Bigr)
\sum_{m,k}|\alpha_m|^2|\beta_k|^2.
\]

أي

\[
\boxed{
\sum_n|c_n|^2
\le
D_{M,K}\,\|\alpha\|_2^2\|\beta\|_2^2
},
\qquad
D_{M,K}=\max_{n\le4MK}d_{M,K}(n).
\]

وهذا حد صحيح عام.

## 3. الحد المتاح من دالة القواسم

لدينا دائمًا

\[
d_{M,K}(n)\le \tau(n).
\]

إذن

\[
D_{M,K}
\le
\max_{n\le4MK}\tau(n).
\]

ومن الحد القياسي الأعظمي لدالة القواسم:

\[
\max_{n\le X}\tau(n)
=
\exp\!\left(O\!\left(\frac{\log X}{\log\log X}\right)\right)
=X^{o(1)}.
\]

وعليه

\[
\boxed{
\sum_n|c_n|^2
\ll
x^{o(1)}\|\alpha\|_2^2\|\beta\|_2^2
}.
\]

هذا يثبت حدًا دون قوة ثابتة من \(x\)، لكنه لا يثبت خسارة لوغاريتمية ثابتة.

## 4. لماذا لا يكفي هذا للهدف

إدخال هذا الحد في الغربال الكبير الموزون من `MV-02` يعطي على كتلة موصلات \(R<r\le2R\):

\[
\mathfrak M_R(\mathcal B)
\ll
\left(\frac{x}{R}+R\right)
\log\frac{2Q}{R}
\,x^{o(1)}
\|\alpha\|_2^2\|\beta\|_2^2.
\]

عامل \(x^{o(1)}\) ليس مقبولًا إذا كان الهدف الداخلي هو استرجاع الرتبة الكلاسيكية الدقيقة

\[
xQ\log x
\]

حتى قوة لوغاريتمية مضبوطة. لذلك لا يغلق هذا المسار `MV-04` ولا `MV-06`.

## 5. عدم كفاية خاصية \(\beta_k=\mu(k)\) وحدها

في تطبيق Vaughan يكون \(\beta_k=\mu(k)\). هذا يحصر \(k\) في الأعداد الخالية من المربعات، لكنه لا يعطي وحده حدًا منتظمًا من نوع \((\log x)^A\) لعدد القواسم الخالية من المربعات في نافذة ديادية. لذلك لا يجوز تسجيل تحسين لوغاريتمي بلا حجة إضافية تستعمل بنية \(\alpha_m=b_U(m)\) أو إعادة تنظيم البرهان كله.

## 6. الحكم على المسار الحالي

المسار

```text
VAUGHAN RECTANGLES
 -> FORM c_n BY MULTIPLICATIVE CONVOLUTION
 -> APPLY WEIGHTED LARGE SIEVE DIRECTLY TO c_n
```

يصطدم بطاقة التصادمات الضربية. الحد العام المتاح شكليًا هو \(x^{o(1)}\)، لا حدًا لوغاريتميًا ثابتًا.

إذن:

```text
CURRENT-RECTANGLE-ROUTE = INSUFFICIENT-FOR-TARGET-LOG-PRECISION
```

هذا ليس فشلًا لمبرهنة Vaughan، بل فشل لطريقة تجميع القطع الثنائية في معامل واحد قبل استغلال البنية الإضافية في برهان باربان.

## 7. مسارات الإصلاح المقبولة

يلزم أحد الآتي:

1. إثبات لمّة خاصة لمعاملات Vaughan \(b_U*\mu\) تضبط طاقة التصادمات بخسارة لوغاريتمية ثابتة؛
2. عدم تجميع المستطيل في \(c_n\)، واستعمال تقدير ثنائي/تشتتي يحافظ على المتغيرين منفصلين؛
3. إعادة بناء مبرهنة باربان العامة مباشرة بصيغتها التي تتجنب هذه البوابة أو تمتصها داخل حد خارج القطر؛
4. استعمال تنعيم أو متوسط إضافي يتيح تقدير طاقة الالتفاف في المتوسط بدل الحد الأعظمي.

المسار الثالث هو الأكثر اتساقًا مع قرار المشروع الأصلي: تدخيل برهان باربان العام كاملًا، لا اختزاله إلى تطبيق مباشر للغربال الكبير على معاملات Vaughan المجمعة.

## 8. عدم الدور

هذا التدقيق يستعمل فقط:

- متراجحة كوشي؛
- عدد تمثيلات حاصل الضرب؛
- الحد الأعظمي القياسي لدالة القواسم؛
- الغربال الكبير الموزون المثبت في `MV-02` لتشخيص الرتبة.

لا يستعمل Barban أو BDH في إثبات العائق.

## 9. الحكم النهائي

```text
MV-04B GENERIC-COLLISION-BOUND   = PROVED-HERE-DRAFT
MV-04B BOUND-SIZE                = x^{o(1)} TIMES L2 PRODUCT
MV-04B POLYLOG-BOUND             = OPEN
MV-04B CURRENT-ROUTE             = FAIL-FOR-TARGET-LOG-PRECISION
MV-04 FULL-DIAGONAL              = OPEN
ROUTE-REPAIR                     = REQUIRED
NEXT                             = MV-04C / BARBAN-PROOF-ARCHITECTURE
PASS-FOR-AUTHORING               = NO
```
