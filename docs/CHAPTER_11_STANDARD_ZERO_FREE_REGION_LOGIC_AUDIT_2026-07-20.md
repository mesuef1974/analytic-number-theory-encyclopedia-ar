# التدقيق المنطقي للمنطقة القياسية الخالية — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = ANT-LEM-11-01 / ANT-THM-11-01
AUDIT-STATE          = PASS-FOR-INDIVIDUAL-PRIMITIVE-L-FUNCTION
RESULT-REGISTRY      = REMAINS-DRAFT-UNTIL-AUTHORING
CHAPTER-AUTHORING     = BLOCKED
```

## 1. النتيجة المدققة

توجد ثوابت مطلقة \(c_0>0\) و\(q_0\ge3\) بحيث لكل شخصية ديريشليه بدائية غير رئيسية \(\chi\) بموصل \(q\ge q_0\)، تملك الدالة \(L(s,\chi)\) على الأكثر صفرًا واحدًا في المنطقة

\[
\Re(s)>
1-
\frac{c_0}{\log(q(|\Im(s)|+2))}.
\tag{1.1}
\]

إذا وجد الصفر، فهو حقيقي وبسيط، و\(\chi\) شخصية حقيقية بدائية؛ ومن ثم هي تربيعية.

يمكن امتصاص الموصلات الصغيرة في تصغير \(c_0\) بعد فحص منتهٍ أو باستعمال عدم الانعدام على الخط واستمرارية الأصفار، لكن الفصل سيصوغ النتيجة أولًا لـ\(q\ge3\) مع ثابت مطلق مناسب.

**حد النتيجة:** هذه مبرهنة لدالة بدائية فردية. لا تثبت وحدها فرادة الاستثناء بين جميع الشخصيات بترديد ثابت أو بين جميع الموصلات حتى \(Q\).

## 2. المدخلات

### مدخلات مثبتة داخل الموسوعة

- `ANT-THM-07-04`: الجد البدائي والموصل.
- `ANT-PROP-07-03`: العوامل المحلية للشخصية المستحثة.
- `ANT-THM-07-08`: الدالة المكتملة والمعادلة الوظيفية.
- `ANT-PROP-07-04`: تناظرات الأصفار.
- `ANT-PROP-07-06`: المشتقة اللوغاريتمية في \(\Re(s)>1\).
- `ANT-LEM-07-01`: كثيرة الحدود المثلثية غير السالبة.
- `ANT-THM-10-01`: عدم الانعدام على الخط \(\Re(s)=1\).
- `ANT-THM-06-04`: ستيرلينغ المنتظمة في الشرائط.

### مدخلات مقتبسة

1. مبرهنة هادامار العامة لتفكيك دالة تامة من الرتبة على الأكثر واحدًا.
2. النمو القياسي من الرتبة واحد للدالة المكتملة \(\Lambda(s,\chi)\).

لا تستعمل النتيجة القياسية للمنطقة الخالية نفسها مدخلًا في البرهان.

## 3. اشتقاق صيغة الكسور الجزئية

بما أن \(\Lambda(s,\chi)\) تامة من الرتبة على الأكثر واحدًا، فإن هادامار تعطي

\[
\Lambda(s,\chi)
=
\exp(A_\chi+B_\chi s)
\prod_{\rho}
\left(1-\frac{s}{\rho}\right)e^{s/\rho}.
\]

بالتفاضل اللوغاريتمي:

\[
\frac{\Lambda'}{\Lambda}(s,\chi)
=
B_\chi
+
\sum_\rho
\left(
\frac1{s-\rho}+rac1\rho
\right).
\tag{3.1}
\]

وبالتجميع المتماثل نكتب

\[
\frac{\Lambda'}{\Lambda}(s,\chi)
=b_\chi+\sum_\rho^{*}\frac1{s-\rho}.
\tag{3.2}
\]

المعادلة الوظيفية

\[
\Lambda(s,\chi)
=
\varepsilon_\chi\Lambda(1-s,\overline\chi)
\]

وعلاقة المرافق تفرضان تناظر الأصفار

\[
\rho\longleftrightarrow1-\overline\rho.
\]

عند تجميع كل زوج حول \(1/2\)، تكون مساهمته في (3.2) عند نقطة التناظر ذات جزء حقيقي صفري. كما أن المشتقة اللوغاريتمية المنتظمة عند مركز المعادلة الوظيفية ذات جزء حقيقي صفري. وإذا وقع صفر عند المركز، نطرح حده القطبي أولًا ثم نأخذ الجزء المنتظم. لذلك

\[
\Re b_\chi=0.
\]

وبتفاضل تعريف \(\Lambda\) وأخذ الجزء الحقيقي نحصل على الهوية الدقيقة

\[
-\Re\frac{L'}{L}(s,\chi)
=
\frac12\log\frac q\pi
+
\frac12\Re\frac{\Gamma'}{\Gamma}
\!\left(\frac{s+a_\chi}{2}\right)
-
\sum_\rho^{*}\Re\frac1{s-\rho}.
\tag{3.3}
\]

```text
ANT-LEM-11-01 / PARTIAL-FRACTION-IDENTITY = LOGIC-PASS
GENERAL-HADAMARD-THEOREM                  = CITED
ORDER-ONE-GROWTH                          = CITED-STANDARD
```

## 4. الباقي المنتظم

أثبت التقرير

`docs/CHAPTER_11_UNIFORM_REMAINDER_AUDIT_2026-07-20.md`

ما يأتي من دون استعمال منطقة خالية:

- حد غاما \(O(\log(|t|+2))\).
- حد الموصل \(\frac12\log q\).
- حد العوامل المحلية \(O(\log q)\).
- حد الشخصية الرئيسية مع إبقاء
  \(\Re 1/(s-1)\) صراحة.

ومن ثم يوجد ثابت مطلق \(C>0\) يكفي لجميع فروع المتراجحة الموزونة.

```text
UNIFORM-REMAINDER = PASS
CIRCULARITY       = PASS
```

## 5. المتراجحة الموزونة

لكل \(\sigma>1\) و\(t\in\mathbb R\):

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{L'}{L}(\sigma+it,\chi)
-\Re\frac{L'}{L}(\sigma+2it,\chi^2)
\ge0.
\tag{5.1}
\]

وهي نتيجة مباشرة من

\[
3+4\Re z+\Re(z^2)\ge0,
\qquad |z|\le1.
\]

```text
WEIGHTED-INEQUALITY = PASS
```

## 6. استبعاد أصفار الشخصية غير الحقيقية

إذا كانت \(\chi\) غير حقيقية و\(\rho=\beta+i\gamma\) صفرًا، فإن \(\chi^2\) غير رئيسية. نأخذ \(t=\gamma\) في (5.1)، ونعزل الصفر في (3.3)، فنحصل على

\[
0
\le
\frac3\delta
-
\frac4{\delta+\eta}
+C\mathcal L,
\]

حيث

\[
\delta=\sigma-1,
\quad
\eta=1-\beta,
\quad
\mathcal L=\log(q(|\gamma|+2)).
\]

أثبت تقرير المتراجحات الكمية أن اختيار

\[
\delta=\frac A{\mathcal L}
\]

لـ\(A\) صغير مطلق يعطي تناقضًا إذا

\[
\eta\le\frac{c_1}{\mathcal L}
\]

لـ\(c_1>0\) صغير مناسب.

```text
NONREAL-CHARACTER = ZERO-FREE-IN-STANDARD-REGION
```

## 7. استبعاد الصفر غير الحقيقي للشخصية الحقيقية

إذا كانت \(\chi\) حقيقية و\(\rho=\beta+i\gamma\) مع \(\gamma\ne0\)، فإن:

- \(\overline\rho=\beta-i\gamma\) صفر للدالة نفسها.
- \(\chi^2\) رئيسية.

لذلك يجب إبقاء الصفرين وقطب الحد الثالث معًا. يصبح الحد الرئيسي

\[
\frac3\delta
+
\frac{\delta}{\delta^2+4\gamma^2}
-
\frac4{\delta+\eta}
-
\frac{4(\delta+\eta)}{(\delta+\eta)^2+4\gamma^2}.
\]

بوضع

\[
r=1+\frac\eta\delta,
\qquad
v=\frac{2|\gamma|}{\delta},
\]

وضرب التعبير في \(\delta\)، نحصل على

\[
G(r,v)
=
3+rac1{1+v^2}-\frac4r-\frac{4r}{r^2+v^2}.
\]

لدينا

\[
G(1,v)=-1-\frac3{1+v^2}\le-1
\]

و

\[
|\partial G/\partial r|\le8.
\]

إذن عندما \(\eta\le\delta/16\):

\[
G(r,v)\le-\frac12.
\]

بعد إضافة \(C\mathcal L\) واختيار \(\delta=A/\mathcal L\) مع \(1/(2A)>C\)، ينتج تناقض.

```text
REAL-CHARACTER / NONREAL-ZERO = EXCLUDED
CONJUGATE-PAIR                 = ESSENTIAL
PRINCIPAL-POLE                 = ESSENTIAL
```

## 8. بساطة الصفر الحقيقي وفرادته داخل الدالة

لتكن \(\chi\) حقيقية، ولنفترض وجود أصفار حقيقية

\[
\beta_j=1-\eta_j
\]

في المنطقة الصغيرة، محسوبة مع الرتب. عند \(t=0\)، تعطي قطبا الحدين الأول والثالث

\[
\frac4\delta,
\]

بينما تعطي الأصفار المعزولة

\[
-4\sum_j\frac1{\delta+\eta_j}.
\]

إذا كان مجموع الرتب على الأقل \(2\)، وإذا كانت كل
\(\eta_j\le\delta/2\)، فإن

\[
-4\sum_j\frac1{\delta+\eta_j}
\le
-\frac{16}{3\delta}.
\]

ومن ثم

\[
0
\le
-\frac4{3\delta}+C\log(2q),
\]

وهو تناقض عند \(\delta=A/\log(2q)\) و\(A\) صغير.

إذن داخل المنطقة:

- لا يمكن أن يوجد صفران حقيقيان متميزان.
- لا يمكن أن تكون رتبة الصفر الحقيقي \(\ge2\).

وبالتالي الصفر الممكن **وحيد داخل الدالة وبسيط**.

```text
REAL-ZERO-UNIQUENESS-IN-ONE-L = PASS
REAL-ZERO-SIMPLICITY          = PASS
```

## 9. البدائية والواقعية

النتيجة أُثبتت أولًا للشخصية البدائية. وإذا بدأت بشخصية غير بدائية، فإن العوامل المحلية لا تنعدم في \(\Re(s)>0\)، فتنتقل الأصفار القريبة من \(1\) إلى الجد البدائي.

أما إذا بقي صفر في المنطقة، فقد استبعدت الشخصيات غير الحقيقية، فتكون الشخصية البدائية حقيقية. وكل شخصية حقيقية بدائية غير رئيسية ذات رتبة اثنتين، أي تربيعية.

```text
EXCEPTIONAL-CHARACTER = PRIMITIVE / REAL / QUADRATIC / NONPRINCIPAL
```

## 10. عدم الدور

لا يعتمد البرهان على:

- مبرهنة المنطقة القياسية نفسها.
- Landau--Page.
- Siegel.
- Deuring--Heilbronn.
- Siegel--Walfisz.
- PNT-AP بحد خطأ.
- Bombieri--Vinogradov.
- Linnik.
- GRH.

```text
CIRCULARITY = PASS
```

## 11. مطابقة الأدبيات

تتفق الصيغة (1.1) مع العرض القياسي المسجل في:

- Davenport, *Multiplicative Number Theory*, p. 93، وفق إحالة Basak--Pratt (2026).
- Iwaniec--Kowalski, *Analytic Number Theory*, Theorem 5.10.
- Kadiri، المنطقة الصريحة المحسنة في نطاق الترديدات الذي عالجته.

لا تعتمد الموسوعة ثابت Kadiri العددي ولا أي أفضل ثابت صريح في النواة الأساسية.

## 12. الحكم النهائي للنطاق المدقق

```text
ANT-LEM-11-01 LOGIC             = PASS
ANT-THM-11-01 LOGIC             = PASS
STANDARD-INDIVIDUAL-L-REGION     = CLOSED
REAL-EXCEPTION-SIMPLE-AND-UNIQUE = CLOSED-WITHIN-ONE-L
FIXED-MODULUS-UNIQUENESS         = NOT PROVED HERE
LANDAU-PAGE-UNIQUENESS           = OPEN
SIEGEL                            = OPEN / EXPECTED-CITED
DEURING-HEILBRONN                 = OPEN / EXPECTED-CITED
PRE-AUTHORING-GATE                = OPEN
CHAPTER-AUTHORING                  = BLOCKED
```

تبقى حالتا `ANT-LEM-11-01` و`ANT-THM-11-01` في سجل النتائج `DRAFT` إلى أن تكتبا في متن الفصل وتجتازا تدقيق ما بعد التأليف.

## 13. الإجراء التالي

الانتقال إلى حاصل الضرب

\[
\zeta(s)L(s,\chi_1)L(s,\chi_2)L(s,\psi)
\]

لإثبات فرادة Landau--Page عبر الموصلات حتى \(Q\)، مع تدقيق:

1. موجبية المعاملات.
2. موصل \(\psi\) المستحثة من \(\chi_1\chi_2\).
3. حالة \(\chi_1\chi_2\) الرئيسية.
4. الثابت المطلق في \(1-c/\log Q\).
