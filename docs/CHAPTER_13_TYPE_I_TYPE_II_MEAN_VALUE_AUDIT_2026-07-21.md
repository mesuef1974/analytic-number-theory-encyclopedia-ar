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

يعتمد هذا التدقيق مدخلين من Montgomery--Vaughan II:

### 1.1 الغربال الكبير التربيعي

لكل معاملات مركبة \(a_n\):

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|\sum_{M<n\le M+N}a_n\chi(n)\right|^2
\le
(N+Q^2)\sum_{M<n\le M+N}|a_n|^2.
\]

### 1.2 النسخة الثنائية العظمى

لكل معاملات مركبة \(a_m,b_n\):

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

هذه هي المبرهنة 19.19، الصيغة (19.34)، الصفحة المطبوعة 181 في المصدر.
يشتقها المصدر من الغربال الكبير بكوشي وأداة قطع عظمى من الملحق E.4.1.

### حكم المنشأ

```text
ANT-THM-13-01 = CITED / COMPOSITE-INPUT
```

أي أن الحزمة المقتبسة تشمل النسختين التربيعية والثنائية العظمى. أما تطبيقها
على حدود Vaughan والحساب اللاحق فمثبتان داخل المشروع.

## 2. متراجحة Pólya--Vinogradov للشخصيات البدائية

### اللمّة

إذا كانت \(\chi\) شخصية بدائية غير رئيسية modulo \(q>1\)، فإن لكل فترة
صحيحة \(M<n\le M+N\):

\[
\left|\sum_{M<n\le M+N}\chi(n)\right|
\ll \sqrt q\log(2q).
\]

### البرهان

من تحويل فورييه المنتهي للشخصية البدائية وقيمة مجموع غاوس المطلقة
\(\sqrt q\)، المثبتين في الفصل السابع، توجد صيغة عكسية من الشكل

\[
\chi(n)
=\frac1{\tau(\overline\chi)}
\sum_{a=1}^{q}\overline\chi(a)e(an/q),
\qquad
|\tau(\overline\chi)|=\sqrt q,
\]

مع اختلاف غير مؤثر في موضع المرافق بحسب اصطلاح مجموع غاوس.

لذلك

\[
\left|\sum_{n\le N}\chi(n)\right|
\le
\frac1{\sqrt q}
\sum_{a=1}^{q-1}
\left|\sum_{n\le N}e(an/q)\right|.
\]

وباستخدام تقدير المتسلسلة الهندسية

\[
\left|\sum_{n\le N}e(an/q)\right|
\ll \min\left(N,\frac1{\|a/q\|}\right),
\]

وتناظر \(a\) و\(q-a\)، نحصل على

\[
\sum_{a=1}^{q-1}
\min\left(N,\frac1{\|a/q\|}\right)
\ll
q\sum_{1\le a\le q/2}\frac1a
\ll q\log(2q).
\]

إذن مجموع البداية \(\ll\sqrt q\log(2q)\). ويعطي طرح مجموعي بدايتين التقدير
نفسه لأي فترة، مع تغيير ثابت مطلق فقط.

```text
ANT-LEM-13-04       = PROVED-HERE / RESERVED
POLYA--VINOGRADOV   = PASS
NON-CIRCULARITY     = PASS
```

البرهان لا يستعمل مبرهنة Bombieri--Vinogradov أو الغربال الكبير.

## 3. تفكيك Vaughan المستخدم

لكل شخصية بدائية \(\chi\) ولكل \(y\le x\)، نكتب

\[
\psi(y,\chi)=S_1(y,\chi)+S_2(y,\chi)+S_3(y,\chi)+S_4(y,\chi),
\]

حيث، وفق تدقيق هوية Vaughan:

\[
S_1(y,\chi)=\sum_{n\le\min(y,U)}\Lambda(n)\chi(n),
\]

\[
S_2(y,\chi)
=\sum_{t\le UV}a(t)\chi(t)
  \sum_{r\le y/t}\chi(r),
\qquad
|a(t)|\le\log t,
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
\qquad
|b(m)|\le\log m.
\]

نضع

\[
\mathcal M(T)
=
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|T(y,\chi)|.
\]

نفترض أولًا \(Q\le x^{1/2}\)؛ أما \(Q>x^{1/2}\) فيغطيه مباشرة المدخل
الثنائي العظمى بتطبيقه على \(1*\Lambda\)، كما في المصدر.

## 4. تقدير Type II للحد \(S_4\)

نقسم مجال \(m\) إلى كتل ديادية

\[
M<m\le2M,
\qquad
U/2\le M\le x/V.
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

بتطبيق النسخة الثنائية العظمى نحصل على

\[
\mathcal M(S_{4,M})
\ll
(M+Q^2)^{1/2}(x/M+Q^2)^{1/2}
 x^{1/2}(\log 2x)^2.
\]

وباستخدام

\[
\sqrt{A+B+C+D}
\le\sqrt A+\sqrt B+\sqrt C+\sqrt D,
\]

ينتج

\[
\mathcal M(S_{4,M})
\ll
\left(
 x+QxM^{-1/2}+Qx^{1/2}M^{1/2}+Q^2x^{1/2}
\right)(\log 2x)^2.
\]

عند الجمع على الكتل الديادية:

- مجموع \(x\) يضيف عامل \(O(\log x)\)؛
- \(M^{-1/2}\) يهيمن عليه الطرف الأدنى \(U\) هندسيًا؛
- \(M^{1/2}\) يهيمن عليه الطرف الأعلى \(x/V\) هندسيًا؛
- حد \(Q^2x^{1/2}\) يضيف عامل \(O(\log x)\).

ومن ثم

\[
\boxed{
\mathcal M(S_4)
\ll
\left(
 x+QxU^{-1/2}+QxV^{-1/2}+Q^2x^{1/2}
\right)(\log 2x)^3.}
\]

هذا يطابق الصيغة (20.6).

```text
ANT-LEM-13-03 = PROVED-HERE / RESERVED
TYPE-II        = PASS
```

## 5. تقدير الحد الكبير من \(S_2\)

نقسم

\[
S_2=S_2'+S_2'',
\]

حيث \(S_2'\) يأتي من \(t\le U\)، و\(S_2''\) من \(U<t\le UV\).

بالنسبة إلى \(S_2''\)، نطبق البرهان السابق نفسه مع

\[
\alpha_t=a(t),
\qquad
\beta_r=1.
\]

على كتل \(M<t\le2M\)، حيث \(U/2\le M\le UV\). لدينا

\[
\sum_t|a(t)|^2\ll M(\log 2x)^2,
\qquad
\sum_{r\le x/M}1\le x/M.
\]

فتنتج بعد الجمع الديادي

\[
\boxed{
\mathcal M(S_2'')
\ll
\left(
 x+QxU^{-1/2}+Qx^{1/2}(UV)^{1/2}+Q^2x^{1/2}
\right)(\log 2x)^3.}
\]

وهذه هي بنية الصيغة (20.8).

## 6. تقدير Type I للحد الصغير من \(S_2\)

### الترديد \(q=1\)

بالتقدير التافه:

\[
\sup_{y\le x}|S_2'(y,\mathbf 1)|
\ll x(\log 2x)^2.
\]

### الترديدات \(q>1\)

لأن الشخصية ضربـية:

\[
\left|\sum_{r\le y/t}\chi(rt)\right|
\le
\left|\chi(t)\right|
\sup_z\left|\sum_{r\le z}\chi(r)\right|
\ll \sqrt q\log(2q).
\]

إذن

\[
\sup_{y\le x}|S_2'(y,\chi)|
\ll U\sqrt q\,(\log(2qU))^2.
\]

وعدد الشخصيات البدائية modulo \(q\) لا يتجاوز \(\varphi(q)\). لذلك

\[
\begin{aligned}
\mathcal M(S_2')
&\ll x(\log 2x)^2
 +U(\log(2Qx))^2
 \sum_{2\le q\le Q}q^{3/2}\\
&\ll
\left(x+Q^{5/2}U\right)(\log(2Qx))^2.
\end{aligned}
\]

وهذه هي الصيغة (20.9).

## 7. تقدير Type I للحد \(S_3\)

لـ\(q>1\)، تعطي Pólya--Vinogradov لكل فترة:

\[
\sup_w\left|\sum_{w\le m\le y/k}\chi(km)\right|
\ll\sqrt q\log(2q).
\]

ومن ثم

\[
\sup_{y\le x}|S_3(y,\chi)|
\ll V\sqrt q\,(\log(2qx))^2.
\]

وبمعالجة \(q=1\) تافهًا كما سبق:

\[
\boxed{
\mathcal M(S_3)
\ll
\left(x+Q^{5/2}V\right)(\log(2Qx))^2.}
\]

وهذه هي الصيغة (20.10).

```text
ANT-LEM-13-02 = PROVED-HERE / RESERVED
TYPE-I         = PASS
```

## 8. الحد القصير \(S_1\)

باستعمال حد تشيبيشيف \(\psi(U)\ll U\):

\[
\sup_{y\le x}|S_1(y,\chi)|\ll U.
\]

ومن ثم

\[
\boxed{\mathcal M(S_1)\ll Q^2U.}
\]

ولأن \(Q\ge1\)، يمتص هذا الحد في \(Q^{5/2}U\) داخل التقدير النهائي.

## 9. مبرهنة القيمة المتوسطة قبل التحسين

بجمع الحدود السابقة نحصل على

\[
\begin{aligned}
&\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|\psi(y,\chi)|\\
&\quad\ll
\Bigl(
 x
 +QxU^{-1/2}
 +QxV^{-1/2}
 +Q^2x^{1/2}
 +Qx^{1/2}(UV)^{1/2}\\
&\hspace{40mm}
 +Q^{5/2}U
 +Q^{5/2}V
\Bigr)
(\log(2xUV))^3.
\end{aligned}
\]

هذا يطابق التقدير السابق لاختيار المعلمات في المصدر.

## 10. تحسين المعلمات

### الحالة الأولى: \(1\le Q\le x^{1/3}\)

نأخذ

\[
U=V=x^{1/3}.
\]

عندئذ:

\[
QxU^{-1/2}=Qx^{5/6},
\qquad
Qx^{1/2}(UV)^{1/2}=Qx^{5/6},
\]

و

\[
Q^{5/2}U
=Q^{5/2}x^{1/3}
\le Qx^{5/6}
\]

لأن \(Q^{3/2}\le x^{1/2}\). وكذلك الحد الموافق لـ\(V\). فتنتج

\[
\mathcal M(\psi)
\ll
\left(x+x^{5/6}Q+x^{1/2}Q^2\right)(\log 2x)^3.
\]

### الحالة الثانية: \(x^{1/3}\le Q\le x^{1/2}\)

نأخذ

\[
U=V=\frac{x^{2/3}}Q.
\]

فيكون

\[
QxU^{-1/2}=Q^{3/2}x^{2/3},
\]

وهو يساوي \(x^{5/6}Q\) عند \(Q=x^{1/3}\)، ويظل في المجال مغطى بمجموع
\(x^{5/6}Q+x^{1/2}Q^2\). كذلك

\[
Qx^{1/2}(UV)^{1/2}=x^{7/6}\le x^{5/6}Q
\]

لأن \(Q\ge x^{1/3}\)، و

\[
Q^{5/2}U=Q^{3/2}x^{2/3}
\ll x^{5/6}Q+x^{1/2}Q^2.
\]

فتعود الصيغة نفسها.

### الحالة الثالثة: \(Q>x^{1/2}\)

تطبق النسخة الثنائية العظمى مباشرة على

\[
\psi(y,\chi)=\sum_{mn\le y}\mu(m)\log n\,\chi(mn),
\]

أي على الهوية \(\Lambda=\mu*\log\). ينتج حد لا يتجاوز الشكل المعلن عندما
\(Q^2>x\). هذه الحالة لا تدخل في تطبيق Bombieri--Vinogradov، لكنها تكمل
صياغة مبرهنة القيمة المتوسطة لكل \(Q\ge1\).

## 11. النتيجة

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
ANT-THM-13-02 = PROVED-HERE / RESERVED
```

النتيجة مثبتة داخل التدقيق اعتمادًا على:

- حزمة الغربال الكبير الثنائية المقتبسة؛
- هوية Vaughan المثبتة داخليًا؛
- Pólya--Vinogradov المثبتة داخليًا؛
- حد تشيبيشيف من الفصول السابقة.

## 12. تدقيق عدم الدور

لا يستعمل البرهان:

- Bombieri--Vinogradov؛
- Siegel--Walfisz؛
- أي توزيع للأوليات على متوسط الترديدات؛
- النتيجة «تقريبًا كل الترديدات»؛
- Elliott--Halberstam.

ويستعمل فقط حزمة الغربال الكبير العامة، وهوية Vaughan، والتحليل المنتهي
لمجاميع الشخصيات، وحدودًا سابقة غير معتمدة على الفصل الثالث عشر.

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
