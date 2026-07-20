# تدقيق المتراجحات الكمية — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = STANDARD-ZERO-FREE-REGION / ALGEBRAIC-REDUCTION
AUDIT-STATE          = CONDITIONAL-PASS
AUTHORING             = BLOCKED
```

## 1. فرضية الحد المنتظم المطلوب إثباتها

ضع

\[
\mathcal L=\log(q(|\gamma|+2)).
\]

تختزل البنية البرهانية إلى إثبات وجود ثابت مطلق \(C>0\) بحيث، عندما
\(1<\sigma\le2\)، يمكن جمع حدود الموصل وغاما والعوامل المحلية والأقطاب غير المعزولة في باقي علوي لا يتجاوز

\[
C\mathcal L.
\]

نسمي هذا مؤقتًا:

```text
UNIFORM-REMAINDER-LEMMA(C)
```

لا يُعد هذا الفرض نتيجة معتمدة بعد. الغرض من التدقيق هو إثبات أن هذه اللمّة، متى أغلقت، تكفي جبريًا لاستخراج المنطقة القياسية.

نكتب

\[
\delta=\sigma-1>0,
\qquad
\eta=1-\beta\ge0.
\]

## 2. الشخصية غير الحقيقية

من المتراجحة الموزونة وتدقيق الإشارات، إذا كان
\(\rho=\beta+i\gamma\) صفرًا لـ\(L(s,\chi)\) وشخصية \(\chi\) غير حقيقية، نحصل على

\[
0
\le
\frac3\delta
-
\frac4{\delta+\eta}
+
C\mathcal L.
\tag{2.1}
\]

اختر ثابتًا \(A>0\) يحقق

\[
\frac1A>2C,
\]

وضع

\[
\delta=\frac A{\mathcal L}.
\]

إذا افترضنا

\[
\eta\le\frac c{\mathcal L},
\]

فإن الطرف الأيمن من (2.1)، بعد القسمة على \(\mathcal L\)، لا يزيد على

\[
\frac3A-rac4{A+c}+C.
\]

عند \(c=0\) تساوي هذه الكمية

\[
-\frac1A+C<-C<0.
\]

وبالاستمرار توجد قيمة مطلقة صغيرة \(c_1=c_1(C,A)>0\) تجعلها سالبة لكل
\(0\le c\le c_1\)، وهذا يناقض (2.1).

إذن

\[
1-\beta>\frac{c_1}{\mathcal L}.
\]

```text
NONREAL-CHARACTER-ZERO-FREE-REGION = ALGEBRAIC-PASS
DEPENDENCY = UNIFORM-REMAINDER-LEMMA
```

## 3. شخصية حقيقية وصفر غير حقيقي

لنفترض أن \(\chi\) حقيقية وأن

\[
\rho=\beta+i\gamma,
\qquad \gamma\ne0,
\]

صفر لها. الصفر المرافق \(\overline\rho\) صفر أيضًا، و\(\chi^2\) رئيسية. بعد عزل الزوج والقطب نحصل على

\[
0\le
\frac3\delta
+
\frac{\delta}{\delta^2+4\gamma^2}
-
\frac4{\delta+\eta}
-
\frac{4(\delta+\eta)}{(\delta+\eta)^2+4\gamma^2}
+
C\mathcal L.
\tag{3.1}
\]

ضع

\[
r=\frac{\delta+\eta}{\delta}\ge1,
\qquad
v=\frac{2|\gamma|}{\delta}.
\]

يضرب الجزء الكسري من (3.1) في \(\delta\) ليصبح

\[
G(r,v)
=
3+
\frac1{1+v^2}
-
\frac4r
-
\frac{4r}{r^2+v^2}.
\]

عند \(r=1\):

\[
G(1,v)
=
-1-rac3{1+v^2}
\le-1.
\]

كما أن

\[
\left|\frac{\partial G}{\partial r}(r,v)\right|
\le8
\qquad (r\ge1,\ v\ge0).
\]

فإذا

\[
1\le r\le1+\frac1{16},
\]

فإن مبرهنة القيمة المتوسطة تعطي

\[
G(r,v)\le-\frac12
\]

بصورة منتظمة في \(v\). الشرط على \(r\) يكافئ

\[
\eta\le\frac\delta{16}.
\]

إذن (3.1) تعطي

\[
0
\le
-\frac1{2\delta}
+C\mathcal L.
\]

اختر

\[
\delta=\frac A{\mathcal L}
\]

مع

\[
\frac1{2A}>C.
\]

عندئذ يكون الطرف الأيمن سالبًا. لذلك يستحيل وجود صفر غير حقيقي يحقق

\[
\eta\le\frac A{16\mathcal L}.
\]

ومن ثم

\[
1-\beta>rac{c_2}{\mathcal L},
\qquad
c_2=\frac A{16}.
\]

```text
REAL-CHARACTER-NONREAL-ZERO = ALGEBRAIC-PASS
CONJUGATE-PAIR               = ESSENTIAL
CHI-SQUARED-POLE             = RETAINED
DEPENDENCY                   = UNIFORM-REMAINDER-LEMMA
```

## 4. الصفر الحقيقي وبساطته

افترض أن \(\chi\) حقيقية وأن \(\beta\in\mathbb R\) صفر من الرتبة \(m\ge1\). عند \(t=0\)، تجمع قطبا الحد الأول والحد الثالث إلى

\[
\frac4\delta,
\]

بينما يعطي الصفر

\[
-\frac{4m}{\delta+\eta}.
\]

إذن

\[
0
\le
\frac4\delta
-
\frac{4m}{\delta+\eta}
+
C\log(2q).
\tag{4.1}
\]

إذا كان \(m\ge2\) و\(\eta\le\delta/2\)، فإن

\[
\frac4\delta-rac{4m}{\delta+\eta}
\le
\frac4\delta-rac8{3\delta/2}
=
-\frac4{3\delta}.
\]

اختر

\[
\delta=\frac A{\log(2q)}
\]

مع

\[
\frac4{3A}>C.
\]

ينتج تناقض. لذلك كل صفر حقيقي يقع داخل المنطقة الصغيرة الموافقة يجب أن يكون بسيطًا.

أما \(m=1\)، فلا تنتج (4.1) تناقضًا عامًا؛ وهذا هو الصفر الاستثنائي الممكن.

```text
EXCEPTIONAL-ZERO-SIMPLICITY = ALGEBRAIC-PASS
REAL-SIMPLE-ZERO            = ONLY-REMAINING-CANDIDATE
DEPENDENCY                  = UNIFORM-REMAINDER-LEMMA
```

## 5. جمع الثوابت

بعد إثبات لمّة الباقي المنتظم بثابت مطلق \(C\)، نختار \(A>0\) صغيرًا بحيث يحقق في آن واحد

\[
\frac1A>2C,
\qquad
\frac1{2A}>C,
\qquad
\frac4{3A}>C.
\]

ثم نأخذ

\[
c
=
\min\left\{
 c_1,
 \frac A{16},
 \frac A2
\right\}.
\]

ينتج:

- لا صفر في المنطقة للشخصيات غير الحقيقية.
- لا صفر غير حقيقي في المنطقة للشخصيات الحقيقية.
- الصفر الحقيقي الممكن في المنطقة بسيط.

ومع الرد إلى الجد البدائي، يكون الاستثناء من شخصية حقيقية بدائية غير رئيسية.

## 6. ما أُغلق وما بقي

```text
ALGEBRA-NONREAL-CHARACTER       = PASS
ALGEBRA-REAL-NONREAL-ZERO       = PASS
ALGEBRA-SIMPLICITY              = PASS
CONSTANT-OPTIMIZATION           = NOT NEEDED
UNIFORM-REMAINDER-LEMMA         = OPEN / BLOCKING
PRIMITIVE-REDUCTION-CONSTANT    = OPEN
PRE-AUTHORING-GATE              = OPEN
AUTHORING                        = BLOCKED
```

## 7. اللمّة الحاجزة التالية

المطلوب الآن إثبات صيغة موحدة من النوع الآتي:

> يوجد ثابت مطلق \(C>0\) بحيث، لكل شخصية بدائية مناسبة ولكل
> \(1<\sigma\le2\)، تضبط مجموعات الموصل وغاما والثوابت والعوامل المحلية غير المعزولة في تطبيق المتراجحة الموزونة بحد علوي
> \(C\log(q(|t|+2))\).

يجب أن يشمل البرهان:

1. صيغة المشتقة اللوغاريتمية بالتجميع المتماثل للأصفار.
2. تقدير \(\Re\Gamma'/\Gamma\) عند جميع الارتفاعات.
3. الشخصية الرئيسية والعوامل المحذوفة.
4. توحيد موصلات \(\chi\)، و\(\chi^2\)، وجدهما البدائي.
5. عدم الاعتماد على أي منطقة خالية يراد إثباتها.
