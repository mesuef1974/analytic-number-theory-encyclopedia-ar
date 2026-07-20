# تدقيق إشارات المشتقة اللوغاريتمية — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = LOG-DERIVATIVE / ZERO-CONTRIBUTIONS / WEIGHTED-INEQUALITY
AUDIT-STATE          = PARTIAL-PASS
AUTHORING             = BLOCKED
```

## الغرض

تثبيت إشارة مساهمة الأصفار في \(-\Re L'/L\)، ثم فحص كيفية إدخالها في المتراجحة الموزونة التي تنتج المنطقة القياسية الخالية. هذا التدقيق يسبق تثبيت أي ثابت عددي.

## 1. الهوية الأساسية للشخصية البدائية

لتكن \(\chi\) شخصية بدائية غير رئيسية بترديد \(q\)، ولتكن

\[
a_\chi=\frac{1-\chi(-1)}2.
\]

نعرف

\[
\Lambda(s,\chi)
=
\left(\frac q\pi\right)^{(s+a_\chi)/2}
\Gamma\!\left(\frac{s+a_\chi}{2}\right)L(s,\chi).
\]

من الجداء القانوني للدالة التامة من الرتبة الأولى، وبعد أخذ الجزء الحقيقي واستعمال التطبيع القياسي للثابت الأسي، نحصل على

\[
\sum_\rho
\Re\frac1{s-\rho}
=
\frac12\log\frac q\pi
+
\frac12\Re\frac{\Gamma'}{\Gamma}
\!\left(\frac{s+a_\chi}{2}\right)
+
\Re\frac{L'}{L}(s,\chi),
\]

حيث يجمع الطرف الأيسر على الأصفار غير البديهية بالتجميع المتماثل المعتمد.

ومن ثم

\[
-\Re\frac{L'}{L}(s,\chi)
=
\frac12\log\frac q\pi
+
\frac12\Re\frac{\Gamma'}{\Gamma}
\!\left(\frac{s+a_\chi}{2}\right)
-
\sum_\rho\Re\frac1{s-\rho}.
\]

إذا كان \(s=\sigma+it\) و\(\sigma>1\)، فإن لكل صفر \(\rho=\beta+i\gamma\):

\[
\Re\frac1{s-\rho}
=
\frac{\sigma-\beta}
{(\sigma-\beta)^2+(t-\gamma)^2}
>0.
\]

إذن مساهمة كل صفر في \(-\Re L'/L\) **سالبة**.

```text
ZERO-SIGN = VERIFIED / NEGATIVE-IN-MINUS-LOG-DERIVATIVE
```

## 2. الشخصية غير البدائية

إذا استحثت \(\chi\pmod q\) من \(\chi^*\pmod {q^*}\)، فلدينا

\[
L(s,\chi)
=
L(s,\chi^*)
\prod_{p\mid q,\,p\nmid q^*}
\left(1-\chi^*(p)p^{-s}\right).
\]

بالتفاضل:

\[
\frac{L'}{L}(s,\chi)
=
\frac{L'}{L}(s,\chi^*)
+
\sum_{p\mid q,\,p\nmid q^*}
\frac{\chi^*(p)(\log p)p^{-s}}
{1-\chi^*(p)p^{-s}}.
\]

في \(\sigma>0\):

\[
|\chi^*(p)p^{-s}|\le p^{-\sigma}<1,
\]

فلا تخلق العوامل المحلية أصفارًا في المنطقة المدروسة. وعندما \(\sigma\) قريب من \(1\)، يضبط مجموعها بحد من رتبة \(O(\log q)\).

```text
PRIMITIVE-REDUCTION = SIGN-CONSISTENT
LOCAL-FACTORS       = ZERO-FREE-FOR-SIGMA-POSITIVE
```

يبقى تثبيت ثابت الحد المحلي ونطاقه في التدقيق الكمي النهائي.

## 3. المتراجحة الموزونة

لكل \(\sigma>1\) و\(t\in\mathbb R\)، ضع

\[
z_n=\chi(n)n^{-it}.
\]

لدينا \(|z_n|\le1\)، ومن نتيجة الفصل العاشر:

\[
3+4\Re z_n+\Re(z_n^2)\ge0.
\]

بضربها في \(\Lambda(n)n^{-\sigma}\) والجمع:

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{L'}{L}(\sigma+it,\chi)
-\Re\frac{L'}{L}(\sigma+2it,\chi^2)
\ge0.
\]

```text
WEIGHTED-INEQUALITY = VERIFIED
COEFFICIENTS        = 3 / 4 / 1
```

## 4. الحالة الأولى: الشخصية غير الحقيقية

إذا كانت \(\chi\) غير حقيقية، فلا يمكن أن تكون \(\chi^2\) رئيسية؛ لأن ذلك يعني أن رتبة \(\chi\) تقسم \(2\)، ومن ثم تكون قيمها حقيقية.

لصفر \(\rho=\beta+i\gamma\) من \(L(s,\chi)\)، نختار \(t=\gamma\). تعطي مساهمته

\[
-\frac{4}{\sigma-\beta}.
\]

أما قطب زيتا فيعطي

\[
\frac{3}{\sigma-1}.
\]

وبعد ضبط عوامل غاما والموصل وحذف بقية مساهمات الأصفار السالبة من الحد الأعلى، نحصل على البنية المرشحة

\[
0
\le
\frac{3}{\sigma-1}
-
\frac{4}{\sigma-\beta}
+
O\!\left(\log(q(|\gamma|+2))\right).
\]

هذه هي البنية الصحيحة لاستخراج

\[
1-\beta\gg\frac1{\log(q(|\gamma|+2))}.
\]

```text
NONREAL-CHARACTER-BRANCH = SIGN-PASS
UNIFORM-CONSTANT          = NOT YET FIXED
```

## 5. الحالة الثانية: شخصية حقيقية وصفر غير حقيقي

هذه هي العقدة التي لا يجوز اختصارها.

إذا كانت \(\chi\) حقيقية، فإن \(\chi^2\) هي الشخصية الرئيسية على الأعداد الأولية إلى الترديد، ولذلك يملك الحد الثالث بنية زيتا مع قطب عند \(1\). وعند \(t=\gamma\ne0\)، تكون مساهمة القطب

\[
\Re\frac1{\sigma-1+2i\gamma}
=
\frac{\sigma-1}
{(\sigma-1)^2+4\gamma^2}.
\]

لا يجوز إدخال هذا الحد في \(O(\log(q(|\gamma|+2)))\) عندما تكون \(|\gamma|\) صغيرة.

لكن واقعية \(\chi\) تعني أن الصفر المرافق

\[
\overline\rho=\beta-i\gamma
\]

صفر للدالة نفسها. وعند تقييم المشتقة في \(\sigma+i\gamma\)، تكون مساهمة الزوج

\[
-4\left(
\frac1{\sigma-\beta}
+
\frac{\sigma-\beta}
{(\sigma-\beta)^2+4\gamma^2}
\right).
\]

إذن يجب تحليل التعبير المتوازن

\[
\frac{3}{\sigma-1}
+
\frac{\sigma-1}{(\sigma-1)^2+4\gamma^2}
-
4\left(
\frac1{\sigma-\beta}
+
\frac{\sigma-\beta}
{(\sigma-\beta)^2+4\gamma^2}
\right)
+
O(\mathcal L).
\]

الصفر المرافق ليس تفصيلًا زائدًا؛ بل هو ما يوازن قطب الحد الثالث في حالة الشخصية الحقيقية.

```text
REAL-CHARACTER / NONREAL-ZERO = REQUIRES-CONJUGATE-PAIR
PRINCIPAL-CHI-SQUARED-POLE     = MUST-BE-KEPT-EXPLICITLY
PREVIOUS-SHORTCUT              = REJECTED
```

يبقى إثبات المتراجحة العددية الموحدة لهذا التعبير ضمن التدقيق التالي.

## 6. الحالة الثالثة: الصفر الحقيقي المحتمل

إذا كان \(\rho=\beta\in\mathbb R\)، فحين نأخذ \(t=0\) تكون \(\chi\) حقيقية ويصبح الحد الثالث رئيسيًا أيضًا. تتحد مساهمتا القطب لتنتجا معاملًا كليًا \(4\) أمام \(1/(\sigma-1)\)، بينما يعطي صفر من الرتبة \(m\):

\[
-\frac{4m}{\sigma-\beta}.
\]

لـ\(m=1\) لا تعطي البنية وحدها تناقضًا؛ وهذا هو الاستثناء المتوقع. أما \(m\ge2\) فيولد مساهمة سالبة أقوى، ويعطي مسارًا لإثبات البساطة بعد تثبيت الحدود المنتظمة.

```text
REAL-ZERO-MULTIPLICITY-ONE = ALLOWED-CANDIDATE
MULTIPLICITY-AT-LEAST-TWO  = CONTRADICTION-CANDIDATE
SIMPLICITY-PROOF            = NOT YET CLOSED
```

## 7. فحص مبرهنة Page

يؤكد Basak--Pratt (2026) في مقدمة بحثهما الصيغة القياسية الآتية:

- توجد منطقة فردية من رتبة
  \(1-c_0/\log(q(|t|+2))\).
- الاستثناء الممكن حقيقي والشخصية تربيعية.
- مبرهنة Page الكلاسيكية تمنح على الأكثر شخصية حقيقية بدائية واحدة ذات موصل \(\le Q\) وصفر في مجال من رتبة
  \([1-c/\log Q,1)\).

كما يسجل البحث حاصل الضرب الموجب

\[
F(s)=\zeta(s)L(s,\chi_1)L(s,\chi_2)L(s,\psi),
\]

وصيغة الكسور الجزئية

\[
-\frac{F'}{F}(s)
=
\frac1{s-1}
-
\sum_{F(\rho)=0}
\left(\frac1{s-\rho}+\frac1\rho\right)
+B,
\]

ثم يشتق متراجحات موجبة بعد التفاضل. وهذا يؤكد اتجاه إشارة القطب والأصفار المستعمل في خريطة الفصل.

```text
PAGE-MECHANISM-SIGN = VERIFIED
CLASSICAL-PAGE-EXACT-CONSTANT = NOT REQUIRED / NOT FIXED
```

## 8. المراجع المعتمدة لهذا التدقيق

- Davenport, *Multiplicative Number Theory*, الصفحات 93--95 كما يحيل إليها Basak--Pratt.
- DLMF §25.15 لبنية دوال ديريشليه \(L\) والمعادلة الوظيفية والجداء.
- H. Kadiri, “An explicit zero-free region for the Dirichlet L-functions”, *Mathematika* 64 (2018), 445--474، arXiv:`math/0510570`.
- D. Basak and K. Pratt, “A Conditional Refinement of Page's Theorem on zeros of Dirichlet L-functions”, arXiv:`2607.06433` (2026).

## 9. الحكم

```text
LOG-DERIVATIVE-ZERO-SIGN       = PASS
WEIGHTED-DIRICHLET-INEQUALITY  = PASS
NONREAL-CHARACTER-SPLIT        = PASS
REAL-CHARACTER-PAIRING-RULE    = PASS / REQUIRED-CORRECTION
REAL-EXCEPTION-SIMPLICITY      = OPEN
UNIFORM-GAMMA-AND-CONDUCTOR     = OPEN
STANDARD-ZERO-FREE-CONSTANT     = OPEN
PRE-AUTHORING-GATE              = OPEN
AUTHORING                        = BLOCKED
```

## 10. الإجراء التالي

يجب في التدقيق التالي إثبات متراجحتين كميتين منفصلتين:

1. متراجحة الشخصية غير الحقيقية من الشكل
   \[
   \frac{3}{\delta}-\frac4{\delta+\eta}+C\mathcal L\ge0.
   \]
2. متراجحة الشخصية الحقيقية مع الصفر غير الحقيقي، مع الاحتفاظ بقطب \(\chi^2\) والصفر المرافق كاملين.

بعد ذلك فقط يمكن تثبيت صيغة `ANT-THM-11-01` وإغلاق جزء الإشارات من بوابة ما قبل التأليف.
