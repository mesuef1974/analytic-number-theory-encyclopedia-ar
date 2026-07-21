# تدقيق Type I وType II ومبرهنة القيمة المتوسطة للفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                  = 13
AUDIT                    = POLYA--VINOGRADOV / TYPE-I / TYPE-II / MEAN-VALUE
LARGE-SIEVE-PACKAGE      = CITED / COMPOSITE-INPUT
POLYA--VINOGRADOV        = PROVED-HERE
TYPE-I                   = PASS
TYPE-II                  = PASS
MAX-Y-INTERNALIZATION    = PASS VIA MAXIMAL-BILINEAR-INPUT
PARAMETER-OPTIMIZATION   = PASS
MEAN-VALUE-THEOREM       = PROVED-HERE FROM CITED PACKAGE
NON-CIRCULARITY          = PASS
PRE-AUTHORING-GATE       = OPEN
AUTHORING                = BLOCKED
```

## 1. الحزمة المقتبسة من الغربال الكبير

يعتمد التدقيق مدخلين من Montgomery--Vaughan II.

### 1.1 الغربال الكبير التربيعي

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|\sum_{M<n\le M+N}a_n\chi(n)\right|^2
\le
(N+Q^2)\sum_{M<n\le M+N}|a_n|^2.
\]

### 1.2 النسخة الثنائية العظمى

\[
\begin{aligned}
&\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_y
\left|
\sum_{\substack{1\le m\le M\\1\le n\le N\\mn\le y}}
 a_m b_n\chi(mn)
\right|\\
&\qquad\ll
(M+Q^2)^{1/2}(N+Q^2)^{1/2}
\left(\sum_{m\le M}|a_m|^2\right)^{1/2}
\left(\sum_{n\le N}|b_n|^2\right)^{1/2}
\log(2MN).
\end{aligned}
\]

هذه هي المبرهنة 19.19، الصيغة (19.34)، الصفحة المطبوعة 181. يشتقها
المصدر من الغربال الكبير بكوشي وأداة قطع عظمى من الملحق E.4.1.

```text
ANT-THM-13-01 = CITED / COMPOSITE-INPUT
```

الحزمة المقتبسة تشمل النسختين؛ أما تطبيقها على حدود Vaughan والحساب اللاحق
فمثبتان هنا.

## 2. متراجحة Pólya--Vinogradov للشخصيات البدائية

إذا كانت \(\chi\) شخصية بدائية غير رئيسية modulo \(q>1\)، فإن لكل فترة
صحيحة \(M<n\le M+N\):

\[
\left|\sum_{M<n\le M+N}\chi(n)\right|
\ll \sqrt q\log(2q).
\]

من تحويل فورييه المنتهي للشخصية البدائية وقيمة مجموع غاوس المطلقة
\(\sqrt q\)، المثبتين في الفصل السابع، نحصل -- وفق اصطلاح المرافق -- على
صيغة عكسية من الشكل

\[
\chi(n)
=\frac1{\tau(\overline\chi)}
\sum_{a=1}^{q}\overline\chi(a)e(an/q),
\qquad
|\tau(\overline\chi)|=\sqrt q.
\]

ومن ثم

\[
\left|\sum_{n\le N}\chi(n)\right|
\le
\frac1{\sqrt q}
\sum_{a=1}^{q-1}
\left|\sum_{n\le N}e(an/q)\right|.
\]

وباستخدام

\[
\left|\sum_{n\le N}e(an/q)\right|
\ll \min\left(N,\frac1{\|a/q\|}\right)
\]

وتناظر \(a\) و\(q-a\):

\[
\sum_{a=1}^{q-1}
\min\left(N,\frac1{\|a/q\|}\right)
\ll q\sum_{1\le a\le q/2}\frac1a
\ll q\log(2q).
\]

فيكون مجموع البداية \(\ll\sqrt q\log(2q)\)، ويعطي طرح مجموعي بدايتين
التقدير نفسه لأي فترة.

```text
ANT-LEM-13-04      = PROVED-HERE / RESERVED
POLYA--VINOGRADOV  = PASS
NON-CIRCULARITY    = PASS
```

## 3. تفكيك Vaughan

لكل شخصية بدائية \(\chi\) ولكل \(y\le x\):

\[
\psi(y,\chi)=S_1+S_2+S_3+S_4,
\]

حيث

\[
S_1(y,\chi)=\sum_{n\le\min(y,U)}\Lambda(n)\chi(n),
\]

\[
S_2(y,\chi)
=\sum_{t\le UV}a(t)\chi(t)
  \sum_{r\le y/t}\chi(r),
\qquad |a(t)|\le\log t,
\]

\[
|S_3(y,\chi)|
\le
(\log x)\sum_{k\le V}
\sup_w\left|\sum_{w\le m\le y/k}\chi(km)\right|,
\]

و

\[
S_4(y,\chi)
=
\sum_{\substack{mk\le y\\m>U\\k>V}}
 b(m)\mu(k)\chi(mk),
\qquad |b(m)|\le\log m.
\]

نضع

\[
\mathcal M(T)
=
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|T(y,\chi)|.
\]

نفترض أولًا \(Q\le x^{1/2}\).

## 4. Type II: الحد \(S_4\)

نقسم \(m\) إلى كتل ديادية

\[
M<m\le2M,
\qquad U/2\le M\le x/V.
\]

في كتلة ثابتة نأخذ

\[
\alpha_m=b(m)\mathbf 1_{M<m\le2M},
\qquad
\beta_k=\mu(k)\mathbf 1_{V<k\le x/M}.
\]

لدينا

\[
\sum_m|\alpha_m|^2\ll M(\log 2x)^2,
\qquad
\sum_k|\beta_k|^2\le x/M.
\]

فتعطي النسخة الثنائية العظمى

\[
\mathcal M(S_{4,M})
\ll
(M+Q^2)^{1/2}(x/M+Q^2)^{1/2}
 x^{1/2}(\log 2x)^2.
\]

وبتوسيع حاصل الضرب تحت الجذر واستعمال
\(\sqrt{A+B+C+D}\le\sqrt A+\sqrt B+\sqrt C+\sqrt D\):

\[
\mathcal M(S_{4,M})
\ll
\left(
 x+QxM^{-1/2}+Qx^{1/2}M^{1/2}+Q^2x^{1/2}
\right)(\log 2x)^2.
\]

بعد الجمع الديادي، يهيمن الطرف الأدنى \(U\) على حدود \(M^{-1/2}\)، ويهيمن
الطرف الأعلى \(x/V\) على حدود \(M^{1/2}\)، وتُمتص أعداد الكتل في قوة
لوغاريتم إضافية. لذلك

\[
\boxed{
\mathcal M(S_4)
\ll
\left(
 x+QxU^{-1/2}+QxV^{-1/2}+Q^2x^{1/2}
\right)(\log 2x)^3.}
\]

```text
ANT-LEM-13-03 = PROVED-HERE / RESERVED
TYPE-II        = PASS
```

## 5. الجزء الكبير من \(S_2\)

نكتب

\[
S_2=S_2'+S_2'',
\]

بحسب \(t\le U\) أو \(U<t\le UV\). بالنسبة إلى \(S_2''\)، نطبق الحساب
السابق مع

\[
\alpha_t=a(t),
\qquad
\beta_r=1.
\]

على كتل \(M<t\le2M\)، حيث \(U/2\le M\le UV\). ومن

\[
\sum_t|a(t)|^2\ll M(\log 2x)^2,
\qquad
\sum_{r\le x/M}1\le x/M,
\]

نحصل على

\[
\boxed{
\mathcal M(S_2'')
\ll
\left(
 x+QxU^{-1/2}+Qx^{1/2}(UV)^{1/2}+Q^2x^{1/2}
\right)(\log 2x)^3.}
\]

## 6. Type I: الجزء الصغير من \(S_2\)

عند \(q=1\) يعطينا التقدير التافه مساهمة
\(\ll x(\log 2x)^2\).

أما إذا \(q>1\)، فبضربية الشخصية ومتراجحة Pólya--Vinogradov:

\[
\left|\sum_{r\le y/t}\chi(rt)\right|
\le |\chi(t)|
\sup_z\left|\sum_{r\le z}\chi(r)\right|
\ll\sqrt q\log(2q).
\]

إذن

\[
\sup_{y\le x}|S_2'(y,\chi)|
\ll U\sqrt q\,(\log(2qU))^2.
\]

ولأن عدد الشخصيات البدائية modulo \(q\) لا يتجاوز \(\varphi(q)\):

\[
\begin{aligned}
\mathcal M(S_2')
&\ll x(\log 2x)^2
 +U(\log(2Qx))^2\sum_{2\le q\le Q}q^{3/2}\\
&\ll
\left(x+Q^{5/2}U\right)(\log(2Qx))^2.
\end{aligned}
\]

## 7. Type I: الحد \(S_3\)

لـ\(q>1\):

\[
\sup_w\left|\sum_{w\le m\le y/k}\chi(km)\right|
\ll\sqrt q\log(2q).
\]

ومن ثم

\[
\sup_{y\le x}|S_3(y,\chi)|
\ll V\sqrt q\,(\log(2qx))^2.
\]

ومع معالجة \(q=1\) تافهًا:

\[
\boxed{
\mathcal M(S_3)
\ll
\left(x+Q^{5/2}V\right)(\log(2Qx))^2.}
\]

```text
ANT-LEM-13-02 = PROVED-HERE / RESERVED
TYPE-I         = PASS
```

## 8. الحد القصير \(S_1\)

من حد تشيبيشيف \(\psi(U)\ll U\):

\[
\sup_{y\le x}|S_1(y,\chi)|\ll U.
\]

إذن

\[
\mathcal M(S_1)\ll Q^2U,
\]

ويمتص هذا في \(Q^{5/2}U\) لأن \(Q\ge1\).

## 9. التقدير العام قبل اختيار المعلمات

بجمع الحدود:

\[
\begin{aligned}
&\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|\psi(y,\chi)|\\
&\quad\ll
\Bigl(
 x+QxU^{-1/2}+QxV^{-1/2}+Q^2x^{1/2}
 +Qx^{1/2}(UV)^{1/2}\\
&\hspace{37mm}+Q^{5/2}U+Q^{5/2}V
\Bigr)(\log(2xUV))^3.
\end{aligned}
\]

## 10. اختيار \(U,V\)

### 10.1 إذا \(1\le Q\le x^{1/3}\)

نأخذ

\[
U=V=x^{1/3}.
\]

عندئذ

\[
QxU^{-1/2}=Qx^{5/6},
\qquad
Qx^{1/2}(UV)^{1/2}=Qx^{5/6},
\]

و

\[
Q^{5/2}U=Q^{5/2}x^{1/3}\le Qx^{5/6}
\]

لأن \(Q^{3/2}\le x^{1/2}\). وهكذا

\[
\mathcal M(\psi)
\ll
\left(x+x^{5/6}Q+x^{1/2}Q^2\right)(\log 2x)^3.
\]

### 10.2 إذا \(x^{1/3}\le Q\le x^{1/2}\)

نأخذ

\[
U=V=\frac{x^{2/3}}Q.
\]

فيكون

\[
QxU^{-1/2}=Q^{3/2}x^{2/3}\le x^{1/2}Q^2
\]

لأن \(Q\ge x^{1/3}\)، و

\[
Qx^{1/2}(UV)^{1/2}=x^{7/6}\le x^{5/6}Q.
\]

وكذلك

\[
Q^{5/2}U=Q^{3/2}x^{2/3}\le x^{1/2}Q^2.
\]

فتعود الصيغة نفسها.

### 10.3 إذا \(Q>x^{1/2}\)

نطبق النسخة الثنائية العظمى مباشرة مع

\[
M=1,
\qquad
a_1=1,
\qquad
b_n=\Lambda(n)\mathbf 1_{n\le x}.
\]

عندئذ

\[
\sum_{n\le x}|b_n|^2
=\sum_{n\le x}\Lambda(n)^2
\le (\log x)\psi(x)
\ll x\log(2x).
\]

فتعطي الحزمة المقتبسة

\[
\mathcal M(\psi)
\ll
(1+Q^2)^{1/2}(x+Q^2)^{1/2}
 x^{1/2}(\log 2x)^{3/2}.
\]

ولأن \(Q^2>x\)، فهذا

\[
\ll Q^2x^{1/2}(\log 2x)^3,
\]

وهو داخل الشكل المعلن. هذه المعالجة هي المطابقة لتطبيق المصدر عند
\(Q^2>x\).

## 11. مبرهنة القيمة المتوسطة

لكل \(Q\ge1\) و\(x\ge2\):

\[
\boxed{
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|\psi(y,\chi)|
\ll
\left(x+x^{5/6}Q+x^{1/2}Q^2\right)(\log 2x)^3.}
\]

```text
ANT-THM-13-02 = PROVED-HERE / RESERVED / NON-CITABLE
```

النتيجة مثبتة اعتمادًا على حزمة الغربال الكبير المقتبسة، وهوية Vaughan
المثبتة داخليًا، وPólya--Vinogradov المثبتة داخليًا، وحد تشيبيشيف السابق.

## 12. تدقيق عدم الدور

لا يستعمل البرهان Bombieri--Vinogradov، أو Siegel--Walfisz، أو توزيعًا
متوسطيًا سابقًا للأوليات، أو Elliott--Halberstam. مدخلاته الوحيدة السابقة
هي حزمة الغربال الكبير العامة، وهوية Vaughan، والتحليل المنتهي لمجاميع
الشخصيات، وحدود الفصول السابقة.

```text
NON-CIRCULARITY = PASS
```

## 13. الحكم النهائي

```text
LARGE-SIEVE-PACKAGE    = CITED / COMPOSITE-INPUT
POLYA--VINOGRADOV      = PROVED-HERE
TYPE-I                 = CLOSED / PASS
TYPE-II                = CLOSED / PASS
MAX-Y                  = CLOSED / PASS
PARAMETER-OPTIMIZATION = CLOSED / PASS
ANT-THM-13-02          = PROVED-HERE / RESERVED / NON-CITABLE
PRINCIPAL-CHARACTER    = OPEN FOR THEOREM 13-03
CONDUCTOR-TO-MODULUS   = OPEN FOR THEOREM 13-03
PRE-AUTHORING-GATE     = OPEN
AUTHORING               = BLOCKED
```
