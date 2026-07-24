# MV-10 — التدقيق المنطقي للمسار النهائي

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
UNIT                            = MV-10
TOPIC                           = END-TO-END LOGIC AUDIT
AUDITED-HEAD                    = 0c0117c2ae52120d8c8643a04e58dd112cfca6f0
STATUS                          = PASS
BLOCKING-CORRECTIONS            = NONE
CLASSICAL-BDH-UPPER-BOUND       = LOGICALLY-CLOSED-AS-DRAFT
REFERENCE-AUDIT                 = PENDING
INDEPENDENT-REVIEW              = PENDING
PASS-FOR-AUTHORING              = NO
```

## 1. نطاق التدقيق

التدقيق الحالي يراجع المسار المعتمد فقط:

```text
CHARACTER ORTHOGONALITY
 -> MV-01 WEIGHTED CONDUCTOR REDUCTION
 -> MV-02 WEIGHTED LARGE SIEVE
 -> MV-04C CONDUCTOR SPLIT
      SMALL CONDUCTORS: SIEGEL--WALFISZ
      LARGE CONDUCTORS: DIRECT LARGE SIEVE ON LAMBDA
 -> MV-08 PRINCIPAL / LOCAL ASSEMBLY
 -> MV-09 RANGE / FINAL ASSEMBLY
```

أما `MV-03` و`MV-04` و`MV-04B` فتبقى مواد بحثية صحيحة في نطاقها، لكنها ليست اعتمادًا في البرهان النهائي المعتمد.

## 2. الهدف المدقق

لكل ثابت \(A>0\):

\[
V_\psi(x,Q)
=\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
\ll_A xQ\log x
\]

بانتظام في

\[
x\ge3,
\qquad
\frac{x}{(\log x)^A}\le Q\le x.
\]

الثابت يعتمد على \(A\) وغير فعال في المسار الحالي.

## 3. تدقيق تحويل الفئات إلى الشخصيات

التوسيط المعتمد هو

\[
\Psi^\circ(x,\chi)
=\sum_{n\le x}\Lambda(n)\chi(n)
-x\mathbf 1_{\chi=\chi_0^{(q)}}.
\]

بتعامد شخصيات المجموعة \((\mathbb Z/q\mathbb Z)^\times\):

\[
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2.
\]

### الحكم

- عامل \(1/\varphi(q)\) صحيح.
- لا يظهر عامل زائد من \(\varphi(q)\).
- الشخصية الرئيسية لا تحذف.
- التوسيط يطابق بالضبط \(x/\varphi(q)\).

```text
CHARACTER-TRANSFORM-AUDIT = PASS
```

## 4. تدقيق رد الشخصيات إلى موصلاتها

لكل شخصية \(\chi\bmod q\) موصل وحيد \(r\mid q\) وشخصية بدائية وحيدة \(\chi^*\bmod r\) تستحثها. بكتابة \(q=rm\):

\[
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}.
\]

إعادة الفهرسة

\[
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi^*)|^2
=
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}|\Psi^\circ(x,\chi^*)|^2
\]

هوية دقيقة وليست متراجحة.

كذلك

\[
\varphi(rm)\ge\varphi(r)\varphi(m)
\]

يعطي

\[
W_Q(r)\ll\frac{\log(2Q/r)}{\varphi(r)}.
\]

### الحكم

- اتجاه متراجحة أويلر صحيح.
- إعادة الفهرسة لا تضاعف الشخصيات ولا تسقطها.
- وزن الموصل موجب وفي الاتجاه المطلوب.

```text
CONDUCTOR-REINDEXING-AUDIT = PASS
WEIGHT-DIRECTION-AUDIT     = PASS
```

## 5. تدقيق تصحيحات الاستحثاث

إذا كانت \(\chi\bmod q\) مستحثة من \(\chi^*\bmod r\)، فإن

\[
\Psi^\circ(x,\chi)
=
\Psi^\circ(x,\chi^*)-C(x;q,r,\chi^*)
\]

مع

\[
|C(x;q,r,\chi^*)|\le\omega(q/r)\log x.
\]

والمتوسط المجمع يحقق

\[
\mathcal E(x,Q)\ll Q(\log x)^2.
\]

الخطوة الحاسمة

\[
\frac{\varphi^*(r)}{\varphi(rm)}
\le\frac1{\varphi(m)}
\]

تتبع من

\[
\varphi^*(r)\le\varphi(r),
\qquad
\varphi(rm)\ge\varphi(r)\varphi(m).
\]

### الحكم

```text
INDUCTION-CORRECTION-AUDIT = PASS
PRINCIPAL-r=1-COMPATIBILITY = PASS
```

## 6. تدقيق الغربال الكبير الموزون

على كتلة

\[
R<r\le2R
\]

لدينا

\[
W_Q(r)
\ll
\frac{\log(2Q/R)}{R}\frac r{\varphi(r)}.
\]

وبتطبيق الغربال الكبير للشخصيات البدائية حتى \(2R\):

\[
\sum_{R<r\le2R}W_Q(r)
\sum_{\chi\bmod r}^{*}
\left|\sum_n c_n\chi(n)\right|^2
\ll
\left(\frac NR+R\right)
\log\frac{2Q}{R}
\sum_n|c_n|^2.
\]

### الحكم

- الانتقال من \(1/\varphi(r)\) إلى \((1/R)r/\varphi(r)\) صحيح لأن \(r>R\).
- استعمال الحد الأعلى \(2R\) يولد \(N+4R^2\)، وهو من الرتبة المطلوبة.
- لا توجد خسارة مخفية تعتمد على عدد الشخصيات.

```text
WEIGHTED-LARGE-SIEVE-AUDIT = PASS
```

## 7. تدقيق حد الفصل

المعتمد:

\[
Y=\max\!\left(2,\frac{x}{Q}\log(2Q)\right).
\]

في المجال

\[
Q\ge x(\log x)^{-A}
\]

نحصل على

\[
Y\ll_A(\log x)^{A+1}.
\]

كما أن \(Y\le Q\) يكافئ، للجزء غير الثابت من \(Y\)،

\[
x\log(2Q)\le Q^2.
\]

وهذا يتبع لكبر \(x\) من

\[
Q^2\ge\frac{x^2}{(\log x)^{2A}},
\qquad
\log(2Q)\ll\log x.
\]

### الحكم

```text
THRESHOLD-Y-LOWER-AUDIT = PASS
THRESHOLD-Y-UPPER-AUDIT = PASS-FOR-x>=x0(A)
SMALL-x-ABSORPTION      = PASS
```

## 8. تدقيق الموصلات الصغيرة

لأن

\[
r\le Y\ll_A(\log x)^{A+1},
\]

يمكن تطبيق Siegel--Walfisz بقوة لوغاريتمية ثابتة أكبر، مثل \(A+2\):

\[
|\Psi^\circ(x,\chi^*)|
\ll_A xe^{-c_A\sqrt{\log x}}.
\]

ومن

\[
W_Q(r)\varphi^*(r)
\le W_Q(r)\varphi(r)
\ll\log(2Q/r)
\]

ينتج

\[
\mathcal P_{\le Y}
\ll_A
Y\log(2Q)x^2e^{-2c_A\sqrt{\log x}}.
\]

وبالمقارنة مع

\[
xQ\log x\ge x^2(\log x)^{1-A},
\]

يمتص الادخار الأسي جميع القوى اللوغاريتمية.

### الحكم

- الموصل \(1\) داخل المعالجة بعد استعمال حد دو لا فاليه بوسان.
- الشخصيات البدائية غير الرئيسية مغطاة بانتظام.
- الاعتماد على \(A\) مسجل.

```text
SMALL-CONDUCTOR-AUDIT = PASS
```

## 9. تدقيق الموصلات الكبيرة والجمع الديادي

مع \(c_n=\Lambda(n)\mathbf1_{n\le x}\):

\[
\sum_{n\le x}\Lambda(n)^2\ll x\log x.
\]

لكل كتلة كبيرة:

\[
\ll
x\log x
\left(\frac{x}{R}+R\right)
\log\frac{2Q}{R}.
\]

وللكتل الديادية \(R\ge Y/2\):

\[
\sum_R R\log\frac{2Q}{R}\ll Q,
\]

و

\[
\sum_R\frac{x}{R}\log\frac{2Q}{R}
\ll
\frac{x}{Y}\log\frac{2Q}{Y}
\le Q.
\]

المتراجحة الأخيرة تتبع من تعريف \(Y\):

\[
\frac{x}{Y}\log\frac{2Q}{Y}
\le
\frac{x}{Y}\log(2Q)
\le Q.
\]

### الحكم

```text
DYADIC-R-SUM-AUDIT   = PASS
DYADIC-x/R-SUM-AUDIT = PASS
LARGE-CONDUCTOR-AUDIT = PASS
```

## 10. تدقيق التجميع النهائي

من الأجزاء السابقة:

\[
\mathcal P(x,Q)\ll_A xQ\log x.
\]

ثم

\[
\mathcal S(x,Q)
\le2\mathcal P(x,Q)+O(Q(\log x)^2).
\]

ولأن \(\log x\le x\) لكل \(x\ge3\):

\[
Q(\log x)^2\le xQ\log x.
\]

وأخيرًا

\[
V_\psi(x,Q)=\mathcal S(x,Q).
\]

### الحكم

```text
FINAL-ASSEMBLY-AUDIT = PASS
```

## 11. تدقيق عدم الدور

المسار المعتمد لا يستعمل:

- Barban--Davenport--Halberstam نفسها؛
- Bombieri--Vinogradov؛
- Vaughan في المسار النهائي؛
- حدود القطر أو التصادمات في `MV-04` و`MV-04B`؛
- GRH.

المدخلات الخارجية الوحيدة في المسار النهائي هي:

1. الغربال الكبير للشخصيات البدائية؛
2. Siegel--Walfisz وحد دو لا فاليه بوسان؛
3. الحد القياسي \(\sum_{n\le x}\Lambda(n)^2\ll x\log x\).

```text
NON-CIRCULARITY-AUDIT = PASS
```

## 12. تتبع الفعالية

```text
LARGE-SIEVE-PART      = EFFECTIVE
LOCAL-CORRECTIONS     = EFFECTIVE
DYADIC-SUMMATION      = EFFECTIVE
SMALL-x-ABSORPTION    = EXISTENTIAL
SIEGEL-WALFISZ-PART   = INEFFECTIVE
FINAL-CONSTANT        = DEPENDS-ON-A / INEFFECTIVE
```

لا توجد دعوى فعالية زائفة.

## 13. ملاحظات غير حاجزة

1. يجب في المتن لاحقًا تثبيت اتفاقية الشخصية البدائية modulo \(1\) بوضوح.
2. يجب ألا يسمى المسار الحالي «مبرهنة باربان العامة»؛ إنه يثبت الحد الكلاسيكي لـBDH في المجال المحدد.
3. مواد Vaughan والتصادمات تحفظ في قسم منهجي أو ملحق فقط إذا خدمت السرد، ولا تدخل سلسلة اعتماد المبرهنة النهائية.
4. يجب أن يثبت التدقيق المرجعي مواضع الصيغ الدقيقة للغربال الكبير وSiegel--Walfisz وحد مربع فون مانغولت.

هذه الملاحظات لا تغير صحة البرهان الداخلي.

## 14. الحكم النهائي

```text
MV-10 CHARACTER-NORMALIZATION   = PASS
MV-10 CONDUCTOR-REDUCTION       = PASS
MV-10 LOCAL-CORRECTIONS         = PASS
MV-10 WEIGHTED-LARGE-SIEVE      = PASS
MV-10 CONDUCTOR-SPLIT           = PASS
MV-10 SMALL-CONDUCTORS          = PASS
MV-10 LARGE-CONDUCTORS          = PASS
MV-10 RANGE                     = PASS
MV-10 FINAL-ASSEMBLY            = PASS
MV-10 NON-CIRCULARITY           = PASS
MV-10 INEFFECTIVITY-TRACKING    = PASS
BLOCKING-CORRECTIONS            = NONE
LOGIC-AUDIT                     = PASS
CLASSICAL-UPPER-BOUND           = LOGICALLY-CLOSED-AS-DRAFT
REFERENCE-AUDIT                 = PENDING
INDEPENDENT-REVIEW              = PENDING
PASS-FOR-AUTHORING              = NO
NEXT                            = REFERENCE-AUDIT
```
