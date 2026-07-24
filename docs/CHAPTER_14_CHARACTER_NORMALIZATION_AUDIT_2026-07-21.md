# تدقيق التطبيع والتحويل إلى الشخصيات — الفصل الرابع عشر

التاريخ: 2026-07-21

```text
VERSION                 = 0.18.0-dev
CHAPTER                 = 14
OBJECT                  = BDH VARIANCE NORMALIZATION
STATUS                  = PROVED-HERE
REFERENCE-DEPENDENCE    = NONE FOR THE ALGEBRAIC IDENTITY
PRE-AUTHORING-GATE      = OPEN
PASS-FOR-AUTHORING      = NO
```

## 1. التعريفات

لـ `q >= 1` ولفئة مختزلة `a mod q` نضع

\[
\psi(x;q,a)=\sum_{\substack{n\le x\\ n\equiv a\pmod q}}\Lambda(n),
\qquad
E(x;q,a)=\psi(x;q,a)-\frac{x}{\varphi(q)}.
\]

ولكل شخصية ديريشليه `chi mod q` نضع

\[
\Psi(x,\chi)=\sum_{n\le x}\Lambda(n)\chi(n),
\]

ونعرّف النسخة المتمركزة

\[
\Psi^{\circ}(x,\chi)
=
\Psi(x,\chi)-\delta_{\chi=\chi_0}\,x,
\]

حيث `chi_0` هي الشخصية الرئيسية modulo `q`.

## 2. التحويل الدقيق إلى الشخصيات

إذا كان `(a,q)=1`، فإن تعامد الشخصيات يعطي

\[
\psi(x;q,a)
=
\frac{1}{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}\,\Psi(x,\chi).
\]

وبما أن `chi_0(a)=1` على الفئات المختزلة، نحصل على

\[
E(x;q,a)
=
\frac{1}{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}\,\Psi^{\circ}(x,\chi).
\]

هذه هوية منتهية دقيقة، ولا تستعمل مبرهنة الأعداد الأولية ولا الغربال الكبير ولا أي تقدير تحليلي.

## 3. هوية بارسيفال على الفئات المختزلة

بتربيع القيمة المطلقة والجمع على `a mod q` مع `(a,q)=1`، ثم استعمال تعامد الشخصيات مرة ثانية، نحصل على

\[
\boxed{
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
=
\frac{1}{\varphi(q)}
\sum_{\chi\bmod q}
\left|\Psi^{\circ}(x,\chi)\right|^2
}.
\]

وبفصل الشخصية الرئيسية:

\[
\sum_{\substack{a\bmod q\\(a,q)=1}}
|E(x;q,a)|^2
=
\frac{1}{\varphi(q)}
\left(
|\Psi(x,\chi_0)-x|^2
+
\sum_{\substack{\chi\bmod q\\\chi\ne\chi_0}}
|\Psi(x,\chi)|^2
\right).
\]

إذن كمية التباين الكلية

\[
V_\psi(x,Q)
=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
|E(x;q,a)|^2
\]

تساوي بالضبط

\[
\boxed{
V_\psi(x,Q)
=
\sum_{q\le Q}
\frac{1}{\varphi(q)}
\sum_{\chi\bmod q}
|\Psi^{\circ}(x,\chi)|^2
}.
\]

## 4. حد الشخصية الرئيسية

لدينا الهوية الدقيقة

\[
\Psi(x,\chi_0)
=
\sum_{\substack{n\le x\\(n,q)=1}}\Lambda(n)
=
\psi(x)-
\sum_{\substack{p^k\le x\\p\mid q}}\log p.
\]

ومن ثم

\[
\Psi(x,\chi_0)-x
=
\psi(x)-x
-
\sum_{\substack{p^k\le x\\p\mid q}}\log p.
\]

وبصورة أولية كافية للتدقيق البنيوي:

\[
\sum_{\substack{p^k\le x\\p\mid q}}\log p
\le \omega(q)\log x
\le \frac{\log q}{\log 2}\log x.
\]

هذا الحد ليس بعدُ التقدير النهائي المستعمل في مبرهنة BDH؛ وظيفته هنا فقط منع إسقاط حد الشخصية الرئيسية أو استبداله بالصفر بلا تبرير.

## 5. ما ثبت وما لم يثبت

### مثبت داخليًا

- تعامد الشخصيات على الفئات المختزلة.
- صيغة التحويل لـ `psi(x;q,a)`.
- هوية بارسيفال الدقيقة.
- فصل الشخصية الرئيسية.
- الصيغة الدقيقة لتصحيح الأوليات القاسمة لـ `q`.

### غير مثبت في هذا التدقيق

- أي حد من رتبة `x Q log x`.
- رد الشخصيات غير البدائية إلى موصلاتها.
- استعمال الغربال الكبير أو مبرهنة القيمة المتوسطة.
- الصيغة التقاربية لـ Montgomery--Hooley.
- مجال `Q` النهائي أو فعالية الثوابت.

## 6. قرار التطبيع

```text
REDUCED-RESIDUE-CLASSES      = FINAL
MAIN-TERM                    = x / phi(q)
CHARACTER-NORMALIZATION      = FINAL
PRINCIPAL-CHARACTER          = EXPLICITLY RETAINED
IMPRIMITIVE-REDUCTION        = NOT YET AUDITED
CLASSICAL-UPPER-BOUND        = NOT YET PROVED
PASS-FOR-NORMALIZATION       = YES
PASS-FOR-AUTHORING           = NO
```

الهوية الجبرية صالحة بوصفها مدخلًا مثبتًا داخليًا للفصل، لكن بوابة التأليف تبقى مفتوحة حتى إغلاق رد الموصلات والمدخل التحليلي ومجال `Q` والتحقق المرجعي.