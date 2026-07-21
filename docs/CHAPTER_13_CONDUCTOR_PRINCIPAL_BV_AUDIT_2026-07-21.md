# تدقيق الموصل والشخصية الرئيسية ومبرهنة Bombieri--Vinogradov

التاريخ: 2026-07-21

```text
CHAPTER                = 13
AUDIT                  = PRINCIPAL / CONDUCTOR / MODULUS / BV
PRINCIPAL-CHARACTER    = PASS
LOCAL-FACTOR-ERROR     = PASS
CONDUCTOR-TO-MODULUS   = PASS
SMALL-CONDUCTORS       = PASS VIA SIEGEL--WALFISZ
LARGE-CONDUCTORS       = PASS VIA ANT-THM-13-02
BOMBIERI--VINOGRADOV   = PROVED-HERE / INEFFECTIVE-CONSTANT
THETA-COROLLARY        = PASS
PI-COROLLARY           = PASS
ALMOST-ALL-COROLLARY   = PASS
NON-CIRCULARITY        = PASS
PRE-AUTHORING-GATE     = OPEN PENDING FINAL GOVERNANCE AUDITS
AUTHORING              = BLOCKED
```

## 1. تعريف الخطأ والنسخة المنزوعة من الحد الرئيسي

للفئة المختزلة \((a,q)=1\)، نضع

\[
E(y;q,a)=\psi(y;q,a)-\frac{y}{\varphi(q)},
\]

و

\[
E^*(x,q)=
\max_{(a,q)=1}\sup_{2\le y\le x}|E(y;q,a)|.
\]

ولكل شخصية \(\chi\pmod q\)، نعرف

\[
\psi'(y,\chi)
=
\psi(y,\chi)-\mathbf 1_{\chi=\chi_0}\,y,
\]

حيث \(\chi_0\) الشخصية الرئيسية modulo \(q\).

من تعامد الشخصيات:

\[
E(y;q,a)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\overline{\chi(a)}\,\psi'(y,\chi).
\]

إذن

\[
\boxed{
E^*(x,q)
\le
\frac1{\varphi(q)}
\sum_{\chi\bmod q}
\sup_{y\le x}|\psi'(y,\chi)|.}
\]

هذا الفصل الدقيق يمنع عد الحد الرئيسي مرتين، ويعالج الشخصية الرئيسية داخل
الصيغة نفسها.

## 2. الرد إلى الشخصية البدائية

لتكن \(\chi\pmod q\) مستحثة من شخصية بدائية \(\chi^*\pmod d\)، حيث
\(d\mid q\). سواء كانت الشخصية رئيسية أم غير رئيسية، يكون الفرق مدعومًا على
القوى الأولية ذات \(p\mid q\) التي حذفتها العوامل المحلية. لذلك

\[
|\psi'(y,\chi)-\psi'(y,\chi^*)|
\le
\sum_{p\mid q}
\sum_{p^k\le y}\log p.
\]

ولكل \(p\mid q\):

\[
\sum_{p^k\le y}\log p
\le\log y.
\]

ومن ثم

\[
|\psi'(y,\chi)-\psi'(y,\chi^*)|
\le\omega(q)\log y
\ll(\log(2qy))^2.
\]

الحكم:

```text
LOCAL-FACTOR-ERROR = PASS
```

## 3. جمع تعدد الاستحثاثات

كل شخصية modulo \(q\) لها جد بدائي وحيد ذو موصل \(d\mid q\). لذلك، بعد
الجمع على \(q\le Q\):

\[
\begin{aligned}
\sum_{q\le Q}E^*(x,q)
&\ll Q(\log(2Qx))^2\\
&\quad+
\sum_{d\le Q}
\left(
\sum_{\chi\bmod d}^{*}
\sup_{y\le x}|\psi'(y,\chi)|
\right)
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}.
\end{aligned}
\]

### لمّة مجموع مقلوبات \(\varphi\)

لدينا

\[
\sum_{m\le X}\frac1{\varphi(m)}\ll\log(2X).
\]

فالهوية الضربية

\[
\frac n{\varphi(n)}
=
\sum_{r\mid n}\frac{\mu^2(r)}{\varphi(r)}
\]

تعطي

\[
\begin{aligned}
\sum_{m\le X}\frac1{\varphi(m)}
&=
\sum_{r\le X}
\frac{\mu^2(r)}{r\varphi(r)}
\sum_{k\le X/r}\frac1k\\
&\ll
\log(2X)
\sum_{r\ge1}\frac{\mu^2(r)}{r\varphi(r)}.
\end{aligned}
\]

والمتسلسلة الأخيرة تتقارب لأن حاصل ضربها الأويلري هو

\[
\prod_p\left(1+\frac1{p(p-1)}\right)<\infty.
\]

كما أن \(\varphi(dm)\ge\varphi(d)\varphi(m)\)، ومن ثم

\[
\boxed{
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll
\frac1{\varphi(d)}\log\frac{2Q}{d}.}
\]

إذن

\[
\boxed{
\sum_{q\le Q}E^*(x,q)
\ll
Q(\log(2Qx))^2
+
\sum_{d\le Q}
\frac{\log(2Q/d)}{\varphi(d)}
\sum_{\chi\bmod d}^{*}
\sup_{y\le x}|\psi'(y,\chi)|.}
\]

الحكم:

```text
CONDUCTOR-TO-MODULUS = PASS
```

## 4. الترديدات الصغيرة

ثبت \(A>0\)، وضع

\[
L=\log x,
\qquad
D=L^{A+4}.
\]

نثبت أولًا أنه لكل شخصية بدائية ذات موصل \(d\le D\):

\[
\sup_{y\le x}|\psi'(y,\chi)|
\ll_A x e^{-c_A\sqrt L}.
\]

إذا \(d=1\)، فهذه نتيجة PNT الفعال. وإذا \(d>1\)، فالشخصية البدائية غير
رئيسية، ومن صيغة Siegel--Walfisz للفئات مع أس
\(2(A+4)\)، ثم جمع الفئات مع استعمال

\[
\sum_{a\bmod d}\chi(a)=0,
\]

نحصل على التقدير نفسه، مع عامل متعدد اللوغاريتمات يمتص في الحد الأسي.

لتوحيد `sup` في \(y\):

- إذا \(y\ge e^{\sqrt L}\)، فإن
  \(d\le L^{A+4}\le(\log y)^{2(A+4)}\)، فتطبق Siegel--Walfisz عند \(y\).
- إذا \(y<e^{\sqrt L}\)، فالتقدير التافه
  \(\psi(y)+y\ll e^{\sqrt L}\) أصغر من
  \(x e^{-c'_A\sqrt L}\) عندما يكبر \(x\).

لذلك مساهمة \(d\le D\) لا تتجاوز

\[
D\log(2Q)\,x e^{-c_A\sqrt L}
\ll_A \frac{x}{L^A}.
\]

هذا هو الموضع الوحيد الذي تدخل فيه Siegel--Walfisz، ولذلك تكون الثوابت
العامة غير فعالة.

```text
SMALL-CONDUCTORS = PASS
EFFECTIVITY       = INEFFECTIVE
```

## 5. الترديدات الكبيرة

نقسم المجال \(D<d\le Q\) إلى كتل ديادية

\[
U<d\le2U.
\]

بما أن \(d>D>1\)، فكل شخصية بدائية هنا غير رئيسية، ومن ثم
\(\psi'=\psi\). كذلك

\[
\frac1{\varphi(d)}
\le\frac1U\frac d{\varphi(d)}.
\]

بتطبيق مبرهنة القيمة المتوسطة `ANT-THM-13-02` عند \(2U\):

\[
\begin{aligned}
&\sum_{U<d\le2U}
\frac{\log(2Q/d)}{\varphi(d)}
\sum_{\chi\bmod d}^{*}
\sup_{y\le x}|\psi(y,\chi)|\\
&\quad\ll
\frac{\log(4Q/U)}U
\left(x+x^{5/6}U+x^{1/2}U^2\right)L^3\\
&\quad=
\left(
\frac xU+x^{5/6}+x^{1/2}U
\right)L^3\log(4Q/U).
\end{aligned}
\]

عند الجمع على الكتل:

\[
\sum_{D<U\le Q}\frac xU\log(4Q/U)
\ll\frac xD L,
\]

\[
\sum_{D<U\le Q}x^{5/6}\log(4Q/U)
\ll x^{5/6}L^2,
\]

و

\[
\sum_{D<U\le Q}x^{1/2}U\log(4Q/U)
\ll x^{1/2}Q.
\]

إذن مساهمة الترديدات الكبيرة

\[
\ll
xD^{-1}L^4+x^{5/6}L^5+x^{1/2}QL^3.
\]

## 6. اختيار مستوى التوزيع

نضع

\[
Q_0=\frac{x^{1/2}}{L^{A+3}}.
\]

عند \(Q=Q_0\):

\[
xD^{-1}L^4=\frac{x}{L^A},
\]

\[
x^{1/2}Q_0L^3=\frac{x}{L^A},
\]

و

\[
x^{5/6}L^5\ll_A\frac{x}{L^A}.
\]

كذلك

\[
Q_0(\log(2Q_0x))^2\ll_A\frac{x}{L^A}.
\]

بضم الترديدات الصغيرة والكبيرة والخطأ المحلي نحصل على

\[
\sum_{q\le Q_0}E^*(x,q)
\ll_A\frac{x}{L^A}.
\]

ولأن الطرف الأيسر متزايد في \(Q\)، تصح النتيجة لكل \(Q\le Q_0\). أما قيم
\(x\) المحدودة فتمتص في الثابت الضمني.

## 7. مبرهنة Bombieri--Vinogradov

لكل \(A>0\)، وبانتظام عندما

\[
Q\le\frac{x^{1/2}}{(\log x)^{A+3}},
\]

لدينا

\[
\boxed{
\sum_{q\le Q}
\max_{(a,q)=1}
\sup_{2\le y\le x}
\left|
\psi(y;q,a)-\frac y{\varphi(q)}
\right|
\ll_A
\frac{x}{(\log x)^A}.}
\]

```text
ANT-THM-13-03 = PROVED-HERE / INEFFECTIVE-CONSTANT / RESERVED
```

عدم الفعالية يأتي فقط من استعمال Siegel--Walfisz في قسم الموصلات الصغيرة.

## 8. النسخة الموافقة لـ\(\vartheta\)

من حد القوى الأولية العليا في الفصل التاسع:

\[
|\psi(y;q,a)-\vartheta(y;q,a)|
\le\psi(y)-\vartheta(y)
\ll y^{1/2}\log(2y).
\]

إذن

\[
E^*_{\vartheta}(x,q)
\ll E^*(x,q)+x^{1/2}\log(2x).
\]

وبجمع \(q\le Q\)، يكون الحد الإضافي

\[
Qx^{1/2}\log(2x)
\le\frac{x}{(\log x)^{A+2}}
\]

في المجال المركزي. لذلك

\[
\boxed{
\sum_{q\le Q}
\max_{(a,q)=1}\sup_{y\le x}
\left|
\vartheta(y;q,a)-\frac y{\varphi(q)}
\right|
\ll_A\frac{x}{(\log x)^A}.}
\]

```text
ANT-COR-13-01 = PROVED-HERE / INEFFECTIVE-CONSTANT / RESERVED
```

## 9. النسخة الموافقة لـ\(\pi\)

بالتجميع الجزئي:

\[
\pi(y;q,a)
=
\frac{\vartheta(y;q,a)}{\log y}
+
\int_2^y\frac{\vartheta(t;q,a)}{t(\log t)^2}\,dt.
\]

وبطرح الحد الرئيسي الموافق لـ\(\operatorname{Li}(y)/\varphi(q)\)، نحصل على

\[
\left|
\pi(y;q,a)-\frac{\operatorname{Li}(y)}{\varphi(q)}
\right|
\ll
E^*_{\vartheta}(x,q)+1.
\]

نطبق نتيجة \(\vartheta\) بأس الادخار \(A+1\). عند

\[
Q\le\frac{x^{1/2}}{(\log x)^{A+4}},
\]

نجد

\[
\boxed{
\sum_{q\le Q}
\max_{(a,q)=1}\sup_{y\le x}
\left|
\pi(y;q,a)-\frac{\operatorname{Li}(y)}{\varphi(q)}
\right|
\ll_A\frac{x}{(\log x)^A}.}
\]

```text
ANT-COR-13-02 = PROVED-HERE / INEFFECTIVE-CONSTANT / RESERVED
```

## 10. تقريبًا كل الترديدات

لتكن \(B,C>0\). نطبق المبرهنة المركزية بالأس \(A=B+C\)، ونفترض

\[
Q\le\frac{x^{1/2}}{(\log x)^{B+C+3}}.
\]

سم الترديد \(q\le Q\) سيئًا إذا

\[
E^*(x,q)>\frac{x}{Q(\log x)^B}.
\]

إذا كان عدد الترديدات السيئة \(R\)، فإن

\[
R\frac{x}{Q(\log x)^B}
\le
\sum_{q\le Q}E^*(x,q)
\ll
\frac{x}{(\log x)^{B+C}}.
\]

ومن ثم

\[
\boxed{R\ll\frac{Q}{(\log x)^C}.}
\]

أي أن جميع الترديدات عدا نسبة لوغاريتمية متلاشية تحقق خطأً أصغر من
\(x/(Q(\log x)^B)\).

```text
ANT-COR-13-03 = PROVED-HERE / INEFFECTIVE-CONSTANT / RESERVED
```

## 11. تدقيق عدم الدور

- مبرهنة القيمة المتوسطة ثبتت قبل Bombieri--Vinogradov ومن دون استعمالها.
- الغربال الكبير مستقل عن توزيع الأوليات في المتتاليات الحسابية.
- Siegel--Walfisz نتيجة سابقة من الفصل الثاني عشر ولا تعتمد على الفصل الثالث
  عشر.
- الرد إلى الشخصيات البدائية جبر محلي في عوامل أويلر.
- لم تستعمل نتيجة «تقريبًا كل الترديدات» إلا بعد إثبات المبرهنة المركزية.
- لم تستعمل Elliott--Halberstam أو أي نتيجة تتجاوز حاجز \(1/2\).

```text
NON-CIRCULARITY = PASS
```

## 12. الحكم النهائي

```text
PRINCIPAL-CHARACTER    = CLOSED / PASS
LOCAL-FACTOR-ERROR     = CLOSED / PASS
CONDUCTOR-TO-MODULUS   = CLOSED / PASS
SMALL-CONDUCTORS       = CLOSED / PASS / INEFFECTIVE
LARGE-CONDUCTORS       = CLOSED / PASS
ANT-THM-13-03          = PROVED-HERE / RESERVED / NON-CITABLE
ANT-COR-13-01          = PROVED-HERE / RESERVED / NON-CITABLE
ANT-COR-13-02          = PROVED-HERE / RESERVED / NON-CITABLE
ANT-COR-13-03          = PROVED-HERE / RESERVED / NON-CITABLE
NON-CIRCULARITY        = CLOSED / PASS
PRE-AUTHORING-GATE     = READY-FOR-FINAL-LOGIC-AND-REFERENCE-AUDITS
AUTHORING              = BLOCKED
```
