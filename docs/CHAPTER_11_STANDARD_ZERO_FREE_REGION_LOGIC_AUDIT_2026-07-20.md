# التدقيق المنطقي للمنطقة القياسية الخالية — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = ANT-LEM-11-01 / ANT-THM-11-01
AUDIT-STATE          = PASS
RESULT-REGISTRY      = REMAINS-DRAFT-UNTIL-POST-AUTHORING-AUDIT
```

## النتيجة المدققة

يوجد ثابت مطلق \(c_0>0\) بحيث لكل شخصية ديريشليه بدائية غير رئيسية
\(\chi\) بموصل \(q\ge3\)، تملك \(L(s,\chi)\) على الأكثر صفرًا واحدًا في
المنطقة

\[
\Re(s)>
1-\frac{c_0}{\log(q(|\Im(s)|+2))}.
\]

إذا وجد الصفر، فهو حقيقي وبسيط، وتكون الشخصية حقيقية تربيعية. هذه نتيجة
لدالة بدائية فردية، ولا تثبت وحدها فرادة الاستثناء عبر موصلات مختلفة.

## صيغة المشتقة اللوغاريتمية

من جداء هادامار للدالة المكتملة ومعادلتها الوظيفية نحصل على

\[
-\Re\frac{L'}{L}(s,\chi)=
\frac12\log\frac q\pi+
\frac12\Re\frac{\Gamma'}{\Gamma}
\left(\frac{s+a_\chi}{2}\right)-
\sum_\rho^*\Re\frac1{s-\rho}.
\]

مساهمة كل صفر في \(-\Re L'/L\) سالبة. وتضبط ستيرلينغ والموصل والعوامل
المحلية بقية الحدود بحد

\[
C\log(q(|t|+2)).
\]

## المتراجحة الموزونة

لكل \(\sigma>1\):

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{L'}{L}(\sigma+it,\chi)
-\Re\frac{L'}{L}(\sigma+2it,\chi^2)
\ge0.
\]

مصدرها الموجبية

\[
3+4\Re z+\Re(z^2)\ge0
\qquad(|z|\le1).
\]

## الحالات

### الشخصية غير الحقيقية

إذا كان \(\rho=\beta+i\gamma\) صفرًا، نأخذ \(t=\gamma\) ونحصل على

\[
0\le
\frac3\delta-
\frac4{\delta+\eta}+C\mathcal L,
\]

حيث \(\delta=\sigma-1\)، و\(\eta=1-\beta\)، و
\(\mathcal L=\log(q(|\gamma|+2))\). اختيار
\(\delta=A/\mathcal L\) بثابت صغير يستبعد
\(\eta\ll1/\mathcal L\).

### الشخصية الحقيقية والصفر غير الحقيقي

يجب الاحتفاظ بالصفر المرافق وبقطب \(\chi^2\) الرئيسي. بعد وضع

\[
r=\frac{\delta+\eta}{\delta},
\qquad
v=\frac{2|\gamma|}{\delta},
\]

يظهر التعبير

\[
G(r,v)=3+\frac1{1+v^2}-\frac4r-
\frac{4r}{r^2+v^2}.
\]

لدينا \(G(1,v)\le-1\) و\(|\partial G/\partial r|\le8\). لذلك يستحيل
وجود صفر غير حقيقي في منطقة أصغر بثابت مطلق.

### الصفر الحقيقي

عند \(t=0\)، يعطي القطبان \(4/\delta\). وإذا كان مجموع رتب الأصفار
الحقيقية في المنطقة لا يقل عن اثنين، تتغلب مساهمتها السالبة على القطب،
فنحصل على تناقض. إذن الصفر الحقيقي الممكن واحد وبسيط.

## عدم الدور

لم يستخدم البرهان Landau--Page أو Siegel أو Deuring--Heilbronn أو
Siegel--Walfisz أو Bombieri--Vinogradov أو Linnik أو GRH.

## الحكم

```text
ANT-LEM-11-01 LOGIC            = PASS
ANT-THM-11-01 LOGIC            = PASS
ZERO-SIGN                       = PASS
REAL-CHARACTER-PAIRING          = PASS
REAL-EXCEPTION-SIMPLICITY       = PASS
CIRCULARITY                     = PASS
BEST-EXPLICIT-CONSTANT          = OUT-OF-SCOPE
```

التفاصيل الجبرية محفوظة في
`docs/CHAPTER_11_QUANTITATIVE_INEQUALITY_AUDIT_2026-07-20.md`، وضبط
الباقي في `docs/CHAPTER_11_UNIFORM_REMAINDER_AUDIT_2026-07-20.md`.