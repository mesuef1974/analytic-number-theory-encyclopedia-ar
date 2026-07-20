# تدقيق الباقي المنتظم — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = GAMMA / CONDUCTOR / LOCAL-FACTORS / PRINCIPAL-POLE
AUDIT-STATE          = PASS-CONDITIONAL-ON-STANDARD-PARTIAL-FRACTION-FORMULA
AUTHORING             = BLOCKED
```

## 1. الهدف

إثبات اللمّة الحاجزة في تقرير المتراجحات الكمية:

> يوجد ثابت مطلق \(C>0\) يضبط حدود الموصل وغاما والعوامل المحلية والأجزاء غير المعزولة في المتراجحة الموزونة بحد علوي
> \(C\log(q(|t|+2))\)، من دون استعمال منطقة خالية من الأصفار.

المكوّن الوحيد المقتبس هو صيغة الكسور الجزئية القياسية للمشتقة اللوغاريتمية للدالة المكتملة. بقية التقديرات تثبت هنا.

## 2. صيغة الكسور الجزئية المعتمدة

لتكن \(\xi\) شخصية بدائية غير رئيسية بموصل \(r\)، و

\[
\Lambda(s,\xi)
=
\left(\frac r\pi\right)^{(s+a_\xi)/2}
\Gamma\!\left(\frac{s+a_\xi}{2}\right)L(s,\xi).
\]

الصيغة القياسية، بالتجميع المتماثل للأصفار، هي

\[
-\Re\frac{L'}{L}(s,\xi)
=
\frac12\log\frac r\pi
+
\frac12\Re\frac{\Gamma'}{\Gamma}
\!\left(\frac{s+a_\xi}{2}\right)
-
\sum_{\rho_\xi}
\Re\frac1{s-\rho_\xi}.
\tag{PF-\(\xi\)}
\]

هذه الصيغة لا تعتمد على منطقة خالية؛ مصدرها جداء هادامار للدالة المكتملة من الرتبة الأولى ومعادلتها الوظيفية.

```text
PF-XI = STANDARD-CITED-COMPONENT / TEXTUAL-LOCATION-PENDING
```

أما الإشارة فقد اجتازت التدقيق السابق.

## 3. تقدير عامل غاما

### اللمّة

يوجد ثابت مطلق \(C_\Gamma>0\) بحيث لكل

\[
1\le\sigma\le2,
\qquad
u\in\{0,1\},
\qquad
u_t\in\mathbb R,
\]

لدينا

\[
\left|
\Re\frac{\Gamma'}{\Gamma}
\!\left(\frac{\sigma+\nu+i\nu_t}{2}\right)
\right|
\le
C_\Gamma\log(|\nu_t|+2).
\tag{3.1}
\]

### البرهان

إذا \(|\nu_t|\le2\)، فإن الحجة تقع في مجموعة مدمجة داخل نصف المستوى
\(\Re z\ge1/2\)، البعيد عن أقطاب \(\Gamma'/\Gamma\)، فتكون الدالة محدودة عليها.

إذا \(|\nu_t|>2\)، تعطي صيغة ستيرلينغ المنتظمة

\[
\frac{\Gamma'}{\Gamma}(z)
=
\log z+O\!\left(\frac1{|z|}\right)
\]

في الشريط المدروس. ومن ثم

\[
\left|\Re\frac{\Gamma'}{\Gamma}(z)\right|
\le
\log|z|+O(1)
\ll
\log(|\nu_t|+2).
\]

وهذا يثبت (3.1).

```text
GAMMA-BOUND = PROVED-HERE
DEPENDENCY  = ANT-THM-06-04
```

## 4. الحد العلوي للشخصية البدائية غير الرئيسية

إذا كان \(s=\sigma+it\) و\(1<\sigma\le2\)، فإن كل صفر غير بديهي
\(\rho=\beta+i\gamma\) يحقق \(\beta<1<\sigma\)، ولذلك

\[
\Re\frac1{s-\rho}>0.
\]

بحذف مجموع الأصفار السالب من الطرف الأيمن في (PF-\(\xi\))، وباستعمال (3.1):

\[
-\Re\frac{L'}{L}(s,\xi)
\le
\frac12\log r
+
C_1\log(|t|+2)
\le
C_2\log(r(|t|+2)).
\tag{4.1}
\]

وإذا عُزل صفر أو عدة أصفار محددة، تبقى مساهماتها السالبة ظاهرة ويُحذف ما عداها فقط.

```text
PRIMITIVE-NONPRINCIPAL-UPPER-BOUND = PROVED-FROM-PF
```

## 5. العوامل المحلية للشخصية المستحثة

إذا استحثت \(\chi\pmod q\) من \(\xi\pmod r\)، فـ

\[
\frac{L'}{L}(s,\chi)
=
\frac{L'}{L}(s,\xi)
+
\sum_{p\mid q,\,p\nmid r}
\frac{\xi(p)(\log p)p^{-s}}
{1-\xi(p)p^{-s}}.
\]

ولـ\(\sigma>1\):

\[
\left|
\frac{\xi(p)(\log p)p^{-s}}
{1-\xi(p)p^{-s}}
\right|
\le
\frac{\log p}{p^\sigma-1}
\le
\frac{\log p}{p-1}
\le
\log p.
\]

إذن

\[
\sum_{p\mid q,\,p\nmid r}
\left|
\frac{\xi(p)(\log p)p^{-s}}
{1-\xi(p)p^{-s}}
\right|
\le
\sum_{p\mid q}\log p
=
\log\operatorname{rad}(q)
\le
\log q.
\tag{5.1}
\]

```text
LOCAL-FACTOR-BOUND = PROVED-HERE / AT-MOST-LOG-Q
```

وهذا يكفي أيضًا عندما تكون \(\chi^2\) غير بدائية، لأن موصل جدها البدائي لا يتجاوز \(q\).

## 6. الشخصية الرئيسية

للشخصية الرئيسية بترديد \(q\):

\[
L(s,\chi_0)
=
\zeta(s)
\prod_{p\mid q}(1-p^{-s}).
\]

ومن (5.1):

\[
-\Re\frac{L'}{L}(s,\chi_0)
\le
-\Re\frac{\zeta'}{\zeta}(s)
+
\log q.
\tag{6.1}
\]

نستعمل الدالة المكتملة

\[
\xi(s)
=
\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

تأخذ صيغة المشتقة اللوغاريتمية، بعد أخذ الجزء الحقيقي، الشكل

\[
-\Re\frac{\zeta'}{\zeta}(s)
=
\Re\frac1{s-1}
+
\Re\frac1s
-
\sum_{\rho_\zeta}\Re\frac1{s-\rho_\zeta}
+
\frac12\Re\frac{\Gamma'}{\Gamma}(s/2)
-
\frac12\log\pi.
\]

لـ\(\sigma>1\)، يكون مجموع الأصفار مطروحًا وغير موجب، و

\[
\Re\frac1s\le1.
\]

إذن من تقدير غاما:

\[
-\Re\frac{\zeta'}{\zeta}(\sigma+it)
\le
\Re\frac1{\sigma-1+it}
+
C_3\log(|t|+2).
\tag{6.2}
\]

وبضم (6.1):

\[
-\Re\frac{L'}{L}(\sigma+it,\chi_0)
\le
\Re\frac1{\sigma-1+it}
+
C_4\log(q(|t|+2)).
\tag{6.3}
\]

```text
PRINCIPAL-CHARACTER-BOUND = PROVED-FROM-ZETA-PF
POLE-TERM                 = RETAINED-EXPLICITLY
```

## 7. التطبيق على الحدود الثلاثة

في المتراجحة

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{L'}{L}(\sigma+i\gamma,\chi)
-\Re\frac{L'}{L}(\sigma+2i\gamma,\chi^2)
\ge0,
\]

نحصل على الآتي.

### الحد الأول

من (6.2) عند \(t=0\):

\[
-3\frac{\zeta'}{\zeta}(\sigma)
\le
\frac3{\sigma-1}+O(1).
\]

### الحد الثاني

من (PF-\(\chi\)) نعزل الصفر \(\rho=\beta+i\gamma\)، والصفر المرافق أيضًا إذا كانت \(\chi\) حقيقية، ثم نطبق (4.1) على الباقي.

### الحد الثالث

- إذا كانت \(\chi^2\) غير رئيسية، نردها إلى جدها البدائي ونستعمل (4.1) و(5.1).
- إذا كانت \(\chi^2\) رئيسية، نستعمل (6.3) عند الارتفاع \(2\gamma\)، ونحتفظ صراحة بالحد
  \[
  \Re\frac1{\sigma-1+2i\gamma}.
  \]

وبما أن موصل كل جد بدائي ظاهر لا يتجاوز \(q\)، فإن جميع البواقي الأخرى تُجمع في

\[
C\log(q(|\gamma|+2))
\]

لثابت مطلق \(C\).

```text
UNIFORM-REMAINDER-LEMMA = PASS-FROM-PF
```

## 8. فحص عدم الدور

لم يُستخدم في البرهان:

- أي منطقة خالية من الأصفار.
- مبرهنة Siegel.
- مبرهنة Landau--Page.
- Siegel--Walfisz.
- PNT-AP بحد خطأ.
- Bombieri--Vinogradov.
- GRH.

المكونات الوحيدة هي:

- الجداء القانوني/صيغة الكسور الجزئية القياسية.
- المعادلة الوظيفية والبنية المكتملة.
- ستيرلينغ.
- ضبط عوامل أويلر المنتهية.

```text
CIRCULARITY = PASS
```

## 9. الحكم

```text
GAMMA-BOUND                  = PASS
LOCAL-FACTOR-BOUND           = PASS
PRINCIPAL-POLE-BOUND         = PASS
UNIFORM-REMAINDER-REDUCTION  = PASS
STANDARD-PF-FORMULA          = CITED / PAGE-LOCATION-PENDING
PRE-AUTHORING-GATE           = OPEN
AUTHORING                     = BLOCKED
```

## 10. الأثر على بوابة الفصل

بضم هذا التقرير إلى `CHAPTER_11_QUANTITATIVE_INEQUALITY_AUDIT_2026-07-20.md`، تصبح المنطقة القياسية وبساطة الاستثناء **مغلقتين منطقيًا بشرط توثيق صيغة (PF-\(\xi\)) نصيًا من مرجع قياسي**.

الإجراء التالي:

1. تثبيت موضع صيغة الكسور الجزئية في Davenport أو Montgomery--Vaughan أو Iwaniec--Kowalski.
2. إصدار حكم نهائي لـ`ANT-LEM-11-01`.
3. دمج التقارير الثلاثة في تدقيق منطقي شامل لـ`ANT-THM-11-01`.
