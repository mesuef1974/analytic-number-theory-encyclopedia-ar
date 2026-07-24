# MV-08 — تجميع الشخصية الرئيسية والتصحيحات المحلية

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
UNIT                            = MV-08
TOPIC                           = PRINCIPAL-CHARACTER / LOCAL-PRIME-CORRECTIONS / CLASS-VARIANCE
STATUS                          = PROVED-HERE-DRAFT
CONDUCTOR-ONE                   = PROVED-HERE-DRAFT
IMPRIMITIVE-LOCAL-CORRECTIONS   = PROVED-HERE-DRAFT
CHARACTER-TO-CLASS-ASSEMBLY     = PROVED-HERE-DRAFT
FORMAL-LOGIC-AUDIT              = PENDING
REFERENCE-AUDIT                 = PENDING
INDEPENDENT-REVIEW              = PENDING
NEXT-UNIT                       = MV-09 / RANGE-AND-FINAL-ASSEMBLY
PASS-FOR-AUTHORING              = NO
```

## 1. التعريف المتمركز

لكل شخصية ديريشليه \(\chi\bmod q\) نعرّف

\[
\Psi^\circ(x,\chi)
=
\sum_{n\le x}\Lambda(n)\chi(n)
-x\,\mathbf 1_{\chi=\chi_0^{(q)}}.
\]

إذن الشخصية غير الرئيسية لا تتغير، بينما الشخصية الرئيسية تحقق

\[
\Psi^\circ(x,\chi_0^{(q)})
=
\sum_{\substack{n\le x\\(n,q)=1}}\Lambda(n)-x.
\]

هذا هو التوسيط الموافق تمامًا للحد \(x/\varphi(q)\) في الفئات المختزلة.

## 2. هوية التباين على الفئات

لكل فئة مختزلة \(a\bmod q\):

\[
\psi(x;q,a)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}
\sum_{n\le x}\Lambda(n)\chi(n).
\]

ولأن

\[
\frac{x}{\varphi(q)}
=
\frac1{\varphi(q)}
\overline{\chi_0^{(q)}(a)}\,x,
\]

نحصل على

\[
\psi(x;q,a)-\frac{x}{\varphi(q)}
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}\Psi^\circ(x,\chi).
\]

وبتعامد الشخصيات على المجموعة \((\mathbb Z/q\mathbb Z)^\times\):

\[
\boxed{
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2
}.
\]

لا يوجد عامل إضافي من \(\varphi(q)\)، ولا تُحذف الشخصية الرئيسية من الطرف الأيمن.

## 3. الموصل \(1\)

الشخصية البدائية الوحيدة modulo \(1\) هي الشخصية الثابتة، ونضع

\[
\Psi^\circ(x,\chi^{*}_{1})=\psi(x)-x.
\]

ومن حد دو لا فاليه بوسان المستعمل والمدقق في الفصل الثاني عشر:

\[
\psi(x)-x
\ll x e^{-c\sqrt{\log x}}.
\]

لذلك مساهمة الموصل \(1\) في المتوسط البدائي الموزون هي

\[
W_Q(1)|\psi(x)-x|^2
\ll
\log(2Q)x^2e^{-2c\sqrt{\log x}},
\]

وهي أصغر من \(xQ\log x\) في المجال المعتمد

\[
\frac{x}{(\log x)^A}\le Q\le x
\]

عندما يكون \(x\) كبيرًا.

إذن لا توجد فجوة عند الشخصية الرئيسية أو الموصل \(1\).

## 4. الشخصية الرئيسية عند ترديد عام

إذا كانت \(\chi_0^{(q)}\) الشخصية الرئيسية modulo \(q\)، فهي مستحثة من الموصل \(1\). ولدينا بالضبط

\[
\Psi^\circ(x,\chi_0^{(q)})
=
\psi(x)-x
-
\sum_{\substack{p^k\le x\\p\mid q}}\log p.
\]

فالفرق المحلي هو

\[
C_0(x;q)
=
\sum_{\substack{p^k\le x\\p\mid q}}\log p,
\]

ويحقق

\[
|C_0(x;q)|\le \omega(q)\log x.
\]

هذه هي حالة \(r=1\) من صيغة الاستحثاث العامة في `MV-01`، وليست تصحيحًا جديدًا منفصلًا.

## 5. التصحيحات المحلية لجميع الشخصيات المستحثة

إذا كانت \(\chi\bmod q\) مستحثة من شخصية بدائية \(\chi^*\bmod r\)، مع \(q=rm\)، فقد ثبت

\[
\Psi^\circ(x,\chi)
=
\Psi^\circ(x,\chi^*)-C(x;q,r,\chi^*),
\]

حيث

\[
|C(x;q,r,\chi^*)|\le \omega(m)\log x.
\]

وثبت في `MV-01` أن متوسط مربعات هذه التصحيحات يحقق

\[
\mathcal E(x,Q)
=
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}|C(x;q,r_\chi,\chi^*)|^2
\ll Q(\log x)^2.
\]

وباستخدام

\[
|A-B|^2\le2|A|^2+2|B|^2,
\]

نحصل على

\[
\mathcal S(x,Q)
\le
2\mathcal P(x,Q)+O\!\left(Q(\log x)^2\right),
\]

حيث

\[
\mathcal S(x,Q)
=
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2
\]

و

\[
\mathcal P(x,Q)
=
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}|\Psi^\circ(x,\chi^*)|^2.
\]

## 6. إدخال حد `MV-04C`

من `MV-04C`، في المجال

\[
\frac{x}{(\log x)^A}\le Q\le x,
\]

لدينا

\[
\mathcal P(x,Q)\ll_A xQ\log x.
\]

لذلك

\[
\mathcal S(x,Q)
\ll_A
xQ\log x+Q(\log x)^2.
\]

ولـ\(x\ge3\):

\[
Q(\log x)^2
\le xQ\log x
\]

بعد تعديل الثابت المطلق، ومن ثم

\[
\boxed{
\mathcal S(x,Q)\ll_A xQ\log x
}.
\]

## 7. العودة إلى تباين الفئات

بتطبيق هوية القسم 2 ثم الجمع على \(q\le Q\):

\[
\begin{aligned}
V_\psi(x,Q)
&=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2\\
&=
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}|\Psi^\circ(x,\chi)|^2\\
&=
\mathcal S(x,Q).
\end{aligned}
\]

إذن

\[
\boxed{
V_\psi(x,Q)\ll_A xQ\log x,
\qquad
\frac{x}{(\log x)^A}\le Q\le x
}.
\]

هذه صيغة الإغلاق الرياضي المرشحة، لكنها تبقى `PROVED-HERE-DRAFT` حتى تدقيق المجال والثوابت وعدم الفعالية في `MV-09` ثم التدقيق المنطقي والمرجعي والمستقل.

## 8. عدم الفعالية

الجزء الخاص بالموصلات الصغيرة يعتمد على Siegel--Walfisz، ولذلك ثابت المتراجحة النهائي في الصيغة الحالية قد يكون غير فعّال اعتمادًا على \(A\). يجب تسجيل ذلك صراحة:

```text
IMPLIED-CONSTANT = DEPENDS-ON-A / INEFFECTIVE-IN-CURRENT-ROUTE
```

الغربال الكبير والتصحيحات المحلية فعالة؛ مصدر عدم الفعالية الوحيد هو مدخل Siegel--Walfisz.

## 9. عدم الدور

هذه الوحدة تعتمد على:

1. تعامد شخصيات ديريشليه؛
2. رد الشخصيات إلى موصلاتها من `MV-01`؛
3. الحد البدائي الموزون من `MV-04C`؛
4. Siegel--Walfisz وحد دو لا فاليه بوسان من الفصل الثاني عشر.

ولا تعتمد على Barban أو BDH أو Bombieri--Vinogradov.

## 10. الحكم

```text
MV-08 CONDUCTOR-ONE                 = PROVED-HERE-DRAFT
MV-08 PRINCIPAL-CENTERING           = PROVED-HERE-DRAFT
MV-08 LOCAL-CORRECTIONS             = PROVED-HERE-DRAFT
MV-08 CHARACTER-TO-CLASS-IDENTITY   = PROVED-HERE-DRAFT
MV-08 CLASSICAL-BOUND-ASSEMBLY      = PROVED-HERE-DRAFT
MV-08 CONSTANT                      = INEFFECTIVE-IN-CURRENT-ROUTE
MV-08                               = COMPLETE-AS-DRAFT
NEXT                                = MV-09 / RANGE-AND-FINAL-ASSEMBLY
PASS-FOR-AUTHORING                  = NO
```