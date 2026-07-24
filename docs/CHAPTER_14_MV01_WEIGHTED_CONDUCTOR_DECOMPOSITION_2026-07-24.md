# MV-01 — تفكيك الموصلات الموزون

التاريخ: 2026-07-24

```text
VERSION                         = 0.18.0-dev
CHAPTER                         = 14
UNIT                            = MV-01
TOPIC                           = WEIGHTED-CONDUCTOR-DECOMPOSITION
STATUS                          = PROVED-HERE-DRAFT
EXACT-CONDUCTOR-REINDEXING      = PROVED-HERE-DRAFT
WEIGHT-BOUND                    = PROVED-HERE-DRAFT
INDUCTION-CORRECTION-AGGREGATE  = PROVED-HERE-DRAFT
FORMAL-LOGIC-AUDIT              = PENDING
REFERENCE-AUDIT                 = PENDING
INDEPENDENT-REVIEW              = PENDING
NEXT-UNIT                       = MV-02
PASS-FOR-AUTHORING              = NO
```

## 1. الهدف

نبدأ من المتوسط التربيعي على الشخصيات

\[
\mathcal S(x,Q)=
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\left|\Psi^\circ(x,\chi)\right|^2.
\]

المطلوب هو رده إلى الشخصيات البدائية مع وزن موصل صريح، وضبط الفرق الناتج من استحثاث الشخصية البدائية إلى ترديد أكبر.

لكل شخصية \(\chi\bmod q\) يوجد موصل وحيد \(r\mid q\) وشخصية بدائية وحيدة \(\chi^*\bmod r\) تستحث \(\chi\). نكتب

\[
q=rm.
\]

ونعرّف

\[
W_Q(r)=\sum_{m\le Q/r}\frac1{\varphi(rm)}.
\]

## 2. لمّة الضرب لدالة أويلر

لكل عددين موجبين \(a,b\):

\[
\varphi(ab)\ge \varphi(a)\varphi(b).
\]

### البرهان

يكفي الفحص على القوى الأولية. إذا لم يشترك \(a,b\) في أولي فلدينا المساواة بالتضاعف. وإذا ظهر الأولي \(p\) في كليهما بأسين موجبين \(\alpha,\beta\)، فإن

\[
\frac{\varphi(p^{\alpha+\beta})}
{\varphi(p^\alpha)\varphi(p^\beta)}
=
\frac{p}{p-1}\ge1.
\]

وبضرب العوامل الأولية نحصل على المطلوب. \(\square\)

ومن ثم

\[
\frac1{\varphi(rm)}
\le
\frac1{\varphi(r)\varphi(m)}.
\]

## 3. لمّة مجموع مقلوبات \(\varphi\)

لكل \(M\ge1\):

\[
\sum_{m\le M}\frac1{\varphi(m)}
\ll \log(2M).
\]

### البرهان

نستعمل الهوية

\[
\frac{n}{\varphi(n)}
=
\sum_{d\mid n}\frac{\mu^2(d)}{\varphi(d)}.
\]

إذن

\[
\begin{aligned}
\sum_{n\le M}\frac1{\varphi(n)}
&=
\sum_{n\le M}\frac1n
\sum_{d\mid n}\frac{\mu^2(d)}{\varphi(d)}\\
&=
\sum_{d\le M}\frac{\mu^2(d)}{d\varphi(d)}
\sum_{k\le M/d}\frac1k.
\end{aligned}
\]

وبما أن

\[
\sum_{k\le y}\frac1k\le \log(2y),
\]

ولدينا تقارب حاصل أويلر

\[
\sum_{d\ge1}\frac{\mu^2(d)}{d\varphi(d)}
=
\prod_p\left(1+\frac1{p(p-1)}\right)<\infty,
\]

ينتج الحد المطلوب. \(\square\)

## 4. تقدير وزن الموصل

من الحد السابق:

\[
W_Q(r)
\le
\frac1{\varphi(r)}
\sum_{m\le Q/r}\frac1{\varphi(m)}
\ll
\frac{\log(2Q/r)}{\varphi(r)}.
\]

ومن حد \(m=1\) نحصل أيضًا على

\[
W_Q(r)\ge \frac1{\varphi(r)}.
\]

إذن، بانتظام لكل \(1\le r\le Q\):

\[
\boxed{
\frac1{\varphi(r)}
\le W_Q(r)
\ll
\frac{\log(2Q/r)}{\varphi(r)}
}.
\]

هذا هو الوزن الدقيق الذي سيظهر في الوحدات اللاحقة، ولا يجوز استبداله اعتباطيًا بوزن ثابت.

## 5. هوية إعادة الفهرسة الدقيقة

عرّف المتوسط البدائي الموزون

\[
\mathcal P(x,Q)=
\sum_{r\le Q}W_Q(r)
\sum_{\chi^*\bmod r}^{*}
\left|\Psi^\circ(x,\chi^*)\right|^2.
\]

بما أن شخصيات modulo \(q\) تتجزأ تجزئة وحيدة حسب موصلاتها، فإن

\[
\begin{aligned}
&\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\left|\Psi^\circ(x,\chi^*)\right|^2\\
&\qquad=
\sum_{r\le Q}
\sum_{\chi^*\bmod r}^{*}
\sum_{m\le Q/r}\frac1{\varphi(rm)}
\left|\Psi^\circ(x,\chi^*)\right|^2\\
&\qquad=
\mathcal P(x,Q).
\end{aligned}
\]

هذه هوية فهرسة، لا متراجحة.

## 6. تصحيح الاستحثاث

إذا كانت \(\chi\bmod q\) مستحثة من \(\chi^*\bmod r\)، حيث \(q=rm\)، فقد ثبت سابقًا أن

\[
\Psi^\circ(x,\chi)
=
\Psi^\circ(x,\chi^*)
-C(x;q,r,\chi^*),
\]

حيث

\[
C(x;q,r,\chi^*)=
\sum_{\substack{p^k\le x\\p\mid q,\ p\nmid r}}
\chi^*(p^k)\log p
\]

و

\[
|C(x;q,r,\chi^*)|
\le \omega(m)\log x.
\]

يشمل هذا أيضًا الشخصية الرئيسية: الشخصية الرئيسية modulo \(q\) مستحثة من الشخصية البدائية modulo \(1\)، والتوسيط بطرح \(x\) متوافق مع الصيغة نفسها.

## 7. تقارب المتسلسلة الحاكمة للتصحيح

سنحتاج إلى

\[
\sum_{m\ge1}
\frac{\omega(m)^2}{m\varphi(m)}<\infty.
\]

### البرهان

الدالة

\[
g(m)=\frac1{m\varphi(m)}
\]

تضاعفية، وللأولي \(p\):

\[
\sum_{k\ge1}g(p^k)
=
\sum_{k\ge1}
\frac1{p^k\,p^{k-1}(p-1)}
=
\frac{p}{(p-1)(p^2-1)}
\ll \frac1{p^2}.
\]

كذلك

\[
\omega(m)^2
=
\sum_{p\mid m}1
+2\sum_{\substack{p<\ell\\p\ell\mid m}}1.
\]

وبتوسيع المجموع وفق هذا التفكيك، تكون مساهمة الحد الأول محكومة بمجموع من رتبة \(\sum_p p^{-2}\)، ومساهمة الحد الثاني بمربع هذا المجموع، بينما حاصل أويلر لبقية العوامل

\[
\prod_p\left(1+\sum_{k\ge1}g(p^k)\right)
\]

متقارب لأن العوامل المحلية هي \(1+O(p^{-2})\). إذن المتسلسلة متقاربة. \(\square\)

## 8. ضبط كلفة التصحيحات المجمعة

عرّف

\[
\mathcal E(x,Q)=
\sum_{q\le Q}\frac1{\varphi(q)}
\sum_{\chi\bmod q}
|C(x;q,r_\chi,\chi^*)|^2.
\]

بإعادة الفهرسة \(q=rm\)، واستعمال عدد الشخصيات البدائية \(\varphi^*(r)\le\varphi(r)\)، نحصل على

\[
\begin{aligned}
\mathcal E(x,Q)
&\le
(\log x)^2
\sum_{m\le Q}\omega(m)^2
\sum_{r\le Q/m}
\frac{\varphi^*(r)}{\varphi(rm)}\\
&\le
(\log x)^2
\sum_{m\le Q}\omega(m)^2
\sum_{r\le Q/m}
\frac1{\varphi(m)}\\
&\le
Q(\log x)^2
\sum_{m\le Q}
\frac{\omega(m)^2}{m\varphi(m)}.
\end{aligned}
\]

وبتقارب المتسلسلة السابقة:

\[
\boxed{
\mathcal E(x,Q)\ll Q(\log x)^2
}.
\]

هذا يحسن الحد الخام المسجل سابقًا، ويثبت أن كلفة الاستحثاث محلية وصغيرة أمام المقياس المستهدف \(xQ\log x\) عندما \(x\) كبير.

## 9. المتراجحة النهائية للوحدة

من

\[
|A-B|^2\le2|A|^2+2|B|^2
\]

نحصل على

\[
\boxed{
\mathcal S(x,Q)
\le
2\mathcal P(x,Q)
+O\!\left(Q(\log x)^2\right)
}.
\]

وباستعمال تقدير الوزن:

\[
\boxed{
\mathcal S(x,Q)
\ll
\sum_{r\le Q}
\frac{\log(2Q/r)}{\varphi(r)}
\sum_{\chi^*\bmod r}^{*}
|\Psi^\circ(x,\chi^*)|^2
+
Q(\log x)^2
}.
\]

هذه هي نقطة الانطلاق الدقيقة لـ`MV-02`.

## 10. حدود الادعاء

1. لم تثبت بعد مبرهنة باربان العامة.
2. لم يضبط بعد المتوسط البدائي في الطرف الأيمن.
3. لم يطبق بعد التفكيك على معاملات فون مانغولت داخل برهان كامل.
4. الحالة `PROVED-HERE-DRAFT` مؤقتة حتى التدقيق المنطقي والمرجعي والمستقل.
5. لا يوجد إذن لكتابة متن الفصل.

## 11. الحكم

```text
MV-01 EXACT-REINDEXING       = PROVED-HERE-DRAFT
MV-01 WEIGHT-BOUND           = PROVED-HERE-DRAFT
MV-01 CORRECTION-AGGREGATE   = PROVED-HERE-DRAFT
MV-01 FINAL-REDUCTION        = PROVED-HERE-DRAFT
MV-01 LOGIC-AUDIT            = PENDING
MV-01 REFERENCE-AUDIT        = PENDING
MV-01 INDEPENDENT-REVIEW     = PENDING
MV-01                        = COMPLETE-AS-DRAFT
NEXT                         = MV-02
PASS-FOR-AUTHORING           = NO
```