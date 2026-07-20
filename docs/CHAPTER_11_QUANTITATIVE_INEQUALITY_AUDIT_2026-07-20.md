# تدقيق المتراجحات الكمية — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = STANDARD-ZERO-FREE-REGION / ALGEBRAIC-REDUCTION
AUDIT-STATE          = PASS
AUTHORING             = AUTHORIZED-BY-LATER-COMPREHENSIVE-AUDIT
```

## الهدف

نثبت أن حدًا منتظمًا من الشكل

\[
C\mathcal L,
\qquad
\mathcal L=\log(q(|\gamma|+2)),
\]

يكفي جبريًا لاستخراج المنطقة القياسية، واستبعاد الأصفار غير الحقيقية،
وإثبات بساطة الصفر الحقيقي الممكن.

نكتب

\[
\delta=\sigma-1>0,
\qquad
\eta=1-\beta\ge0.
\]

## الشخصية غير الحقيقية

إذا كانت \(\chi\) غير حقيقية، وكان
\(\rho=\beta+i\gamma\) صفرًا، تعطي المتراجحة الموزونة

\[
0\le
\frac3\delta-
\frac4{\delta+\eta}+C\mathcal L.
\tag{1}
\]

نختار

\[
\delta=\frac A{\mathcal L},
\]

حيث \(A>0\) صغير بحيث \(1/A>2C\). وإذا
\(\eta\le c/\mathcal L\)، يصبح الطرف الأيمن في (1)، بعد القسمة على
\(\mathcal L\)، مساويًا على الأكثر

\[
\frac3A-
\frac4{A+c}+C.
\]

عند \(c=0\) تكون القيمة \(-1/A+C<0\)، وبالاستمرار تبقى سالبة لقيمة
مطلقة صغيرة من \(c\). إذن

\[
1-\beta\gg\frac1{\mathcal L}.
\]

## الشخصية الحقيقية والصفر غير الحقيقي

إذا كانت \(\chi\) حقيقية و\(\gamma\ne0\)، فإن
\(\overline\rho=\beta-i\gamma\) صفر أيضًا، و\(\chi^2\) رئيسية. لذلك يجب
الاحتفاظ بالصفرين وبقطب الحد الثالث. نحصل على

\[
0\le
\frac3\delta+
\frac{\delta}{\delta^2+4\gamma^2}-
\frac4{\delta+\eta}-
\frac{4(\delta+\eta)}{(\delta+\eta)^2+4\gamma^2}
+C\mathcal L.
\tag{2}
\]

ضع

\[
r=\frac{\delta+\eta}{\delta},
\qquad
v=\frac{2|\gamma|}{\delta},
\]

وعرف

\[
G(r,v)=
3+\frac1{1+v^2}-\frac4r-
\frac{4r}{r^2+v^2}.
\]

لدينا

\[
G(1,v)=-1-\frac3{1+v^2}\le-1,
\qquad
\left|\frac{\partial G}{\partial r}(r,v)\right|\le8.
\]

إذا \(\eta\le\delta/16\)، فإن \(r\le1+1/16\)، ومن مبرهنة القيمة
المتوسطة

\[
G(r,v)\le-\frac12.
\]

فتعطي (2)

\[
0\le-\frac1{2\delta}+C\mathcal L,
\]

وهو تناقض عند اختيار \(A\) بحيث \(1/(2A)>C\).

## الصفر الحقيقي وبساطته

إذا كان \(\beta\) صفرًا حقيقيًا من الرتبة \(m\)، فإن أخذ \(t=0\)
يعطي

\[
0\le
\frac4\delta-
\frac{4m}{\delta+\eta}+C\log(2q).
\tag{3}
\]

إذا \(m\ge2\) و\(\eta\le\delta/2\)، فإن الجزء الكسري في (3) لا يزيد على

\[
-\frac4{3\delta}.
\]

وباختيار \(\delta=A/\log(2q)\) و\(A\) صغير نحصل على تناقض. وبالحجة
نفسها يستحيل وجود صفرين حقيقيين متميزين في المنطقة. إذن الصفر الحقيقي
الممكن واحد وبسيط.

## الحكم

```text
NONREAL-CHARACTER-CASE      = PASS
REAL-NONREAL-ZERO-CASE      = PASS
CONJUGATE-PAIR-HANDLING     = PASS
PRINCIPAL-POLE-HANDLING     = PASS
REAL-ZERO-SIMPLICITY        = PASS
CONSTANT-OPTIMIZATION       = NOT REQUIRED
DEPENDENCY                  = UNIFORM-REMAINDER-AUDIT
```

التفاصيل النهائية وترتيب الاعتماد مسجلان أيضًا في
`docs/CHAPTER_11_STANDARD_ZERO_FREE_REGION_LOGIC_AUDIT_2026-07-20.md`.