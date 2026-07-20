# تدقيق هوية Vaughan للفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER             = 13
AUDIT               = VAUGHAN-IDENTITY
RESULT-CANDIDATE    = ANT-LEM-13-01
PROVENANCE          = PROVED-HERE
ALGEBRAIC-PROOF     = PASS
SIGN-AUDIT          = PASS
CUTOFF-AUDIT        = PASS
SUPPORT-AUDIT       = PASS
NON-CIRCULARITY     = PASS
TYPE-I-II-REDUCTION = PASS AT IDENTITY LEVEL
PRE-AUTHORING-GATE  = OPEN
AUTHORING           = BLOCKED
```

## 1. الصيغة المعتمدة

لتكن \(U,V\ge1\) عددين حقيقيين. نعرف

\[
\Lambda_U(n)=\Lambda(n)\mathbf 1_{n\le U},
\qquad
\mu_V(n)=\mu(n)\mathbf 1_{n\le V}.
\]

ولكل \(n\ge1\)، نضع

\[
\begin{aligned}
c_1(n)
&=\Lambda_U(n),\\
c_2(n)
&=-\sum_{\substack{rdk=n\\d\le U\\k\le V}}
  \Lambda(d)\mu(k),\\
c_3(n)
&=\sum_{\substack{mk=n\\k\le V}}
  \mu(k)\log m,\\
c_4(n)
&=\sum_{\substack{mk=n\\m>U\\k>V}}
  \left(\sum_{\substack{d\mid m\\d>U}}\Lambda(d)\right)\mu(k).
\end{aligned}
\]

هوية Vaughan التي يعتمدها الفصل هي

\[
\boxed{\Lambda(n)=c_1(n)+c_2(n)+c_3(n)+c_4(n).}
\]

هذه هي الصيغة (17.5) في Montgomery--Vaughan II، الصفحتان المطبوعتان
55--56، مع استعمال معلمات القطع نفسها \(U,V\).

## 2. البرهان الداخلي بالتفاف ديريشليه

نرمز إلى الدالة الثابتة \(1\) بـ\(\mathbf 1\)، وإلى عنصر الوحدة للالتفاف
بـ\(\varepsilon\). من الفصول السابقة لدينا

\[
\mathbf 1*\mu=\varepsilon
\]

وهوية فون مانغولت

\[
\log=\mathbf 1*\Lambda.
\]

تكتب الحدود الأربعة على مستوى الدوال الحسابية كما يأتي:

\[
\begin{aligned}
c_1&=\Lambda_U,\\
c_2&=-\mathbf 1*\Lambda_U*\mu_V,\\
c_3&=\log*\mu_V,\\
c_4&=(\log-\mathbf 1*\Lambda_U)*(\mu-\mu_V).
\end{aligned}
\]

إذن، باستعمال تجميعية وتبادلية الالتفاف:

\[
\begin{aligned}
c_1+c_2+c_3+c_4
&=\Lambda_U
 -\mathbf 1*\Lambda_U*\mu_V
 +\log*\mu_V\\
&\quad +(\log-\mathbf 1*\Lambda_U)*(\mu-\mu_V)\\
&=\Lambda_U
 -\mathbf 1*\Lambda_U*\mu_V
 +\log*\mu_V\\
&\quad +\log*\mu-\log*\mu_V
 -\mathbf 1*\Lambda_U*\mu
 +\mathbf 1*\Lambda_U*\mu_V\\
&=\Lambda_U+\log*\mu-\mathbf 1*\Lambda_U*\mu.
\end{aligned}
\]

وبما أن

\[
\log*\mu
=(\mathbf 1*\Lambda)*\mu
=\Lambda*(\mathbf 1*\mu)
=\Lambda*\varepsilon
=\Lambda,
\]

وكذلك

\[
\mathbf 1*\Lambda_U*\mu
=\Lambda_U*(\mathbf 1*\mu)
=\Lambda_U,
\]

نحصل على

\[
c_1+c_2+c_3+c_4=\Lambda_U+\Lambda-\Lambda_U=\Lambda.
\]

وهذا يثبت الهوية لكل \(n\ge1\) من دون استعمال تحليل عقدي أو تقارب سلاسل
ديريشليه.

## 3. مطابقة الحدود مع الصيغ المفصلة

### 3.1 الحد الثاني

معامل \(n\) في

\[
-\mathbf 1*\Lambda_U*\mu_V
\]

هو

\[
-\sum_{rdk=n}\mathbf 1(r)\Lambda_U(d)\mu_V(k)
=-\sum_{\substack{rdk=n\\d\le U\\k\le V}}
\Lambda(d)\mu(k),
\]

فتطابق الإشارة السالبة ومؤشرات القطع الصيغة المعتمدة.

### 3.2 الحد الثالث

معامل \(n\) في \(\log*\mu_V\) هو

\[
\sum_{mk=n}\log m\,\mu_V(k)
=
\sum_{\substack{mk=n\\k\le V}}\mu(k)\log m.
\]

### 3.3 الحد الرابع

نعرف

\[
B_U(m)
=\log m-\sum_{\substack{d\mid m\\d\le U}}\Lambda(d).
\]

وباستخدام

\[
\sum_{d\mid m}\Lambda(d)=\log m,
\]

نجد

\[
B_U(m)=\sum_{\substack{d\mid m\\d>U}}\Lambda(d).
\]

إذا كان \(m\le U\)، فلا يوجد قاسم \(d>U\) لـ\(m\)، ومن ثم \(B_U(m)=0\).
وبالمثل، معامل \(k\) في \(\mu-\mu_V\) يساوي صفرًا عندما \(k\le V\)،
ويساوي \(\mu(k)\) عندما \(k>V\). لذلك معامل \(n\) في

\[
(\log-\mathbf 1*\Lambda_U)*(\mu-\mu_V)
\]

هو بالضبط

\[
\sum_{\substack{mk=n\\m>U\\k>V}}
\left(\sum_{\substack{d\mid m\\d>U}}\Lambda(d)\right)\mu(k).
\]

إذن شرطان \(m>U\) و\(k>V\) ليسا فرضين إضافيين؛ بل ينتجان من دعم العاملين.

## 4. تدقيق الحالات الحدية

### 4.1 الحالة \(n=1\)

لدينا \(\Lambda(1)=0\). كما أن

- \(c_1(1)=0\)،
- لا يوجد \(d\) مع \(\Lambda(d)\ne0\) في حاصل \(rdk=1\)، لذا \(c_2(1)=0\)،
- \(c_3(1)=\mu(1)\log1=0\)،
- \(c_4(1)=0\) لأن \(m>U\ge1\) و\(k>V\ge1\) مستحيلان مع \(mk=1\).

فتصح الهوية عند \(n=1\).

### 4.2 القطع غير الصحيحة

لا يحتاج البرهان إلى أن يكون \(U,V\) عددين صحيحين؛ فالمؤشرات \(n\le U\)
و\(n\le V\) معرفة لأي \(U,V\ge1\)، وجميع المجاميع منتهية.

### 4.3 الإشارات

- الإشارة في \(c_2\) سالبة من الحد
  \(-\mathbf 1*\Lambda_U*\mu_V\).
- الإشارة في \(c_3\) موجبة لأن معاملات \(-\zeta'(s)\) هي \(\log m\)، أو
  مباشرة من \(\log*\mu_V\).
- الحد الرابع يحمل إشارة \(\mu(k)\) نفسها، ولا توجد إشارة سالبة إضافية.

الحكم: `SIGN-AUDIT = PASS`.

## 5. الانتقال إلى مجاميع Type I وType II

لتكن

\[
S(N;f)=\sum_{n\le N}\Lambda(n)f(n).
\]

من الهوية:

\[
S=S_1+S_2+S_3+S_4,
\qquad
S_i=\sum_{n\le N}c_i(n)f(n).
\]

### 5.1 الحد القصير

\[
S_1=\sum_{n\le\min(N,U)}\Lambda(n)f(n).
\]

يعالج عادةً تقديرًا تافهًا.

### 5.2 أول حد من Type I

ضع

\[
a(t)=-\sum_{\substack{dk=t\\d\le U\\k\le V}}
\Lambda(d)\mu(k).
\]

عندئذ

\[
c_2(n)=\sum_{t\mid n}a(t),
\]

ومن ثم

\[
S_2=\sum_{t\le UV}a(t)
\sum_{r\le N/t}f(tr).
\]

كما أن

\[
|a(t)|
\le\sum_{d\mid t}\Lambda(d)
=\log t
\le\log(UV)
\]

عندما \(t\le UV\).

### 5.3 الحد اللوغاريتمي من Type I

\[
S_3=\sum_{k\le V}\mu(k)
\sum_{m\le N/k}f(km)\log m.
\]

وبالجمع الجزئي، أو بالهوية

\[
\log m=\int_1^m\frac{dw}{w},
\]

يرد هذا إلى عائلة من مجاميع Type I منتظمة في نقطة البداية \(w\)، مع خسارة
عامل من رتبة \(\log N\). هذا يفسر سبب وجوب ظهور `sup` أو `max` على المجاميع
الجزئية في التدقيق اللاحق.

### 5.4 الحد من Type II

ضع

\[
b(m)=\sum_{\substack{d\mid m\\d>U}}\Lambda(d).
\]

إذن

\[
S_4=
\sum_{\substack{mk\le N\\m>U\\k>V}}
 b(m)\mu(k)f(mk),
\]

وهو شكل ثنائي حقيقي لأن كلا المتغيرين بعيد عن المجال الصغير. كذلك

\[
|b(m)|\le\sum_{d\mid m}\Lambda(d)=\log m.
\]

الحكم: `TYPE-I-II-REDUCTION = PASS AT IDENTITY LEVEL`.

هذا لا يغلق تقديري Type I وType II نفسيهما؛ بل يثبت فقط أن الهوية تنتج
الأشكال الصحيحة التي ستخضع للغربال الكبير.

## 6. تدقيق عدم الدور

البرهان يستعمل فقط:

1. جبر التفاف ديريشليه.
2. هوية \(\mathbf 1*\mu=\varepsilon\).
3. هوية فون مانغولت \(\log=\mathbf 1*\Lambda\).
4. قطعًا محدودًا للدالتين \(\Lambda\) و\(\mu\).

ولا يستعمل:

- Bombieri--Vinogradov؛
- الغربال الكبير؛
- Siegel--Walfisz؛
- PNT في المتتاليات الحسابية؛
- تقديرات Type I أو Type II.

إذن لا يوجد اعتماد دائري في هوية Vaughan نفسها.

```text
NON-CIRCULARITY = PASS
```

## 7. اختبار جبري محدود مقترح

يمكن إضافة اختبار حاسوبي لاحق، غير لازم للبرهان، يتحقق لكل
\(1\le n\le N_0\) ولعدة قيم صحيحة لـ\(U,V\) من أن

\[
\Lambda(n)-c_1(n)-c_2(n)-c_3(n)-c_4(n)=0.
\]

هذا اختبار انحدار للترميز، لا مصدر صحة رياضية.

## 8. الحكم النهائي

```text
ANT-LEM-13-01          = PROVED-HERE / PRE-AUTHORING-RESERVED
VAUGHAN-IDENTITY       = CLOSED / PASS
ALGEBRAIC-PROOF        = PASS
SIGNS                  = PASS
CUTOFFS                = PASS
SUPPORT                 = PASS
NON-CIRCULARITY        = PASS
TYPE-I-II-REDUCTION    = PASS AT IDENTITY LEVEL
TYPE-I-ESTIMATE        = OPEN
TYPE-II-ESTIMATE       = OPEN
PRE-AUTHORING-GATE     = OPEN
AUTHORING               = BLOCKED
```
