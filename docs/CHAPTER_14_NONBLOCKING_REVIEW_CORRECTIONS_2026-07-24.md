# إغلاق التصحيحات غير الحاجزة للمراجعة المستقلة — الفصل الرابع عشر

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
SOURCE-VERDICT                  = APPROVED-WITH-NONBLOCKING-CORRECTIONS
REVIEWED-HEAD                   = 49a76dcdb18318aaa548a34d2918b9c7d846a141
NONBLOCKING-CORRECTIONS         = 5
CORRECTIONS-CLOSED              = 5 / 5
MATHEMATICAL-CLAIM-CHANGED      = NO
RANGE-CHANGED                   = NO
CONSTANT-CLAIM-CHANGED          = NO
PASS-FOR-AUTHORING              = NO / OWNER-DECISION-PENDING
```

## 1. توضيح رمز إعادة الفهرسة في `MV-01 §5`

الصيغة الوسيطة

\[
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}
|\Psi^\circ(x,\chi^*)|^2
\]

لا تعني أن \(\chi\) و\(\chi^*\) الشخصية نفسها modulo \(q\). المقصود هو المؤثر الوسيط الآتي:

- لكل \(\chi\bmod q\)، نعيّن موصلها \(r_\chi\mid q\) وجدها البدائي الفريد \(\chi^*\bmod r_\chi\).
- نستبدل مؤقتًا قيمة \(\Psi^\circ(x,\chi)\) بالقيمة البدائية \(\Psi^\circ(x,\chi^*)\).
- بعد ذلك يعاد إدخال الفرق المحلي
  \[
  C(x;q,r_\chi,\chi^*)
  \]
  في قسم تصحيحات الاستحثاث.

إذن الهوية الدقيقة هي

\[
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}
F(\chi^*)
=
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}F(\chi^*)
\]

لأي دالة \(F\) على الشخصيات البدائية. نأخذ لاحقًا

\[
F(\chi^*)=|\Psi^\circ(x,\chi^*)|^2.
\]

```text
CORRECTION-01 = CLOSED / NOTATIONAL-CLARIFICATION
```

## 2. تقسيم ديادي غير متراكب للمجال \((Y,Q]\)

لتجنب أي لبس عند أول كتلة، نختار

\[
R_j=2^jY
\]

ونعرّف الكتل نصف المفتوحة

\[
I_j=(R_j,\min(2R_j,Q)]
\]

لجميع \(j\ge0\) التي تحقق \(R_j<Q\). هذه الكتل:

1. متباينة زوجيًا؛
2. تغطي \((Y,Q]\) تمامًا؛
3. تحقق على كل كتلة \(R_j<r\le2R_j\)، مع قطع الكتلة الأخيرة عند \(Q\).

وعليه تطبق لمّة `MV-02` على كل كتلة بلا تداخل. وتظل المجاميع

\[
\sum_j R_j\log\frac{2Q}{R_j}\ll Q,
\]

و

\[
\sum_j\frac{x}{R_j}\log\frac{2Q}{R_j}
\ll
\frac{x}{Y}\log\frac{2Q}{Y}
\le Q.
\]

الصياغة السابقة `R>=Y/2` كانت وسيلة لاحتواء أول كتلة ضمن لمّة ديادية، وليست تعريفًا لتقسيم متراكب. تعتمد صياغة \(I_j\) أعلاه في المتن النهائي.

```text
CORRECTION-02 = CLOSED / EXACT-DYADIC-PARTITION
```

## 3. تحديث الدلالة الحوكمية لتدقيق الوحدات

الترويسات القديمة في `MV-01` و`MV-02` التي تقول:

```text
FORMAL-LOGIC-AUDIT = PENDING
REFERENCE-AUDIT    = PENDING
INDEPENDENT-REVIEW = PENDING
```

تعكس حالة الوحدة وقت إنشائها، ولا تعكس الحالة النهائية للبرنامج. الحالة الحاكمة الحالية التي تعلو عليها هي:

```text
END-TO-END-LOGIC-AUDIT = MV-10 / PASS
REFERENCE-AUDIT        = PASS
INDEPENDENT-REVIEW     = APPROVED-WITH-NONBLOCKING-CORRECTIONS
```

تبقى الترويسات التاريخية داخل الملفات الأصلية بوصفها أثرًا زمنيًا، ويجب ألا تُقرأ بوصفها الحالة الحالية. المرجع الحاكم هو خريطة البرهان وPR #26 وسجلا `MV-10` والحكم المستقل.

```text
CORRECTION-03 = CLOSED / GOVERNANCE-SUPERSESSION
```

## 4. برهان صريح لتقارب متسلسلة \(\omega(m)^2\)

ضع

\[
g(n)=\frac1{n\varphi(n)}.
\]

وهي دالة تضاعفية غير سالبة. لكل أولي \(p\):

\[
G_p:=\sum_{k\ge1}g(p^k)
=
\frac{p}{(p-1)(p^2-1)}
\ll p^{-2}.
\]

كما أن

\[
\omega(n)^2
=
\sum_{p\mid n}1
+2\sum_{p<\ell\atop p\ell\mid n}1.
\]

بتونيللي، لأن جميع الحدود غير سالبة:

\[
\sum_{n\ge1}\omega(n)^2g(n)
=
\sum_p\sum_{p\mid n}g(n)
+2\sum_{p<\ell}\sum_{p\ell\mid n}g(n).
\]

من التضاعف:

\[
\sum_{p\mid n}g(n)
=
G_p\prod_{q\ne p}(1+G_q),
\]

و

\[
\sum_{p\ell\mid n}g(n)
=
G_pG_\ell\prod_{q\ne p,\ell}(1+G_q).
\]

ولأن

\[
\prod_q(1+G_q)<\infty
\]

بسبب \(\sum_qG_q<\infty\)، ينتج

\[
\sum_{n\ge1}\omega(n)^2g(n)
\le
C\left(
\sum_pG_p
+2\sum_{p<\ell}G_pG_\ell
\right)<\infty.
\]

أي

\[
\boxed{
\sum_{n\ge1}\frac{\omega(n)^2}{n\varphi(n)}<\infty
}.
\]

هذا برهان صريح بتونيللي والتضاعف ولا يعتمد على اختصار غير مفسر.

```text
CORRECTION-04 = CLOSED / EXPLICIT-TONELLI-EULER-PROOF
```

## 5. غياب الشخصية الرئيسية عن الموصلات الكبيرة

في المتوسط البدائي، الشخصية الرئيسية البدائية توجد فقط عند الموصل \(r=1\). بالفعل:

- الشخصية الرئيسية modulo \(q>1\) مستحثة من الشخصية البدائية modulo \(1\)؛
- لذلك ليست بدائية modulo \(q>1\).

أما طبقة الموصلات الكبيرة فتعرف بواسطة

\[
r>Y,
\qquad Y\ge2.
\]

ومن ثم \(r\ge3\) للأعداد الصحيحة الواقعة في هذه الطبقة، ولا توجد فيها شخصية رئيسية بدائية. لذلك لكل شخصية بدائية في الجزء الكبير:

\[
\mathbf1_{\chi^*=\chi_0}=0
\]

و

\[
\Psi^\circ(x,\chi^*)
=
\sum_{n\le x}\Lambda(n)\chi^*(n).
\]

إذن تطبيق الغربال الكبير مباشرة على المتتالية \(c_n=\Lambda(n)\mathbf1_{n\le x}\) مشروع دون حد توسيط مفقود.

```text
CORRECTION-05 = CLOSED / PRINCIPAL-CHARACTER-EXCLUSION
```

## 6. أثر التصحيحات

```text
NORMALIZATION-CHANGED       = NO
CONDUCTOR-WEIGHT-CHANGED    = NO
LARGE-SIEVE-BOUND-CHANGED   = NO
THRESHOLD-Y-CHANGED         = NO
FINAL-RANGE-CHANGED         = NO
FINAL-ORDER-CHANGED         = NO
INEFFECTIVITY-CHANGED       = NO
```

التصحيحات الخمسة توضيحية وتوثيقية، وتغلق الملاحظات المستقلة دون إعادة فتح المسار الرياضي.

## 7. الحكم بعد الإغلاق

```text
NONBLOCKING-CORRECTIONS     = 5 / 5 CLOSED
BLOCKING-CORRECTIONS        = 0
INDEPENDENT-REVIEW          = CLOSED
INDEPENDENT-VERDICT         = APPROVED-WITH-NONBLOCKING-CORRECTIONS
MATHEMATICAL-ROUTE          = APPROVED
AUTHORING-RECOMMENDATION    = YES
OWNER-AUTHORING-DECISION    = PENDING
PASS-FOR-AUTHORING          = NO
NEXT                        = OWNER DECISION
```
