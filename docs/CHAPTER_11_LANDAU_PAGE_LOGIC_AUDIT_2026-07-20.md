# التدقيق المنطقي لمبرهنة Landau--Page — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = ANT-THM-11-02
AUDIT-STATE          = PASS
RESULT-REGISTRY      = REMAINS-DRAFT-UNTIL-POST-AUTHORING-AUDIT
```

## الصيغة المدققة

يوجد ثابت مطلق \(c_P>0\) بحيث لكل \(Q\ge3\)، توجد على الأكثر شخصية
ديريشليه حقيقية بدائية واحدة \(\chi\) موصلها \(q\le Q\) وتملك صفرًا
حقيقيًا \(\beta\) في المجال

\[
1-\frac{c_P}{\log Q}<\beta<1.
\]

المبرهنة تثبت الفرادة ولا تثبت وجود الصفر.

## افتراض التناقض

نفترض وجود شخصيتين حقيقيتين بدائيتين متميزتين
\(\chi_i\pmod{q_i}\)، حيث \(q_i\le Q\)، ولكل منهما صفر

\[
\beta_i=1-\eta_i,
\qquad
0<\eta_i\le\frac c{\log Q}.
\]

على الترديد \(m=\operatorname{lcm}(q_1,q_2)\)، نعرف

\[
\chi(n)=\chi_1(n)\chi_2(n).
\]

هذه الشخصية غير رئيسية؛ وإلا اتفق جدا الشخصيتين البدائيان. وقد تكون غير
بدائية، وهذا مقصود في خطوة الموجبية. موصل جدها البدائي لا يتجاوز

\[
q_1q_2\le Q^2.
\]

## حاصل الضرب الموجب

ضع

\[
F(s)=
\zeta(s)L(s,\chi_1)L(s,\chi_2)L(s,\chi).
\]

في \(\sigma>1\):

\[
-\frac{F'}{F}(\sigma)=
\sum_{n\ge1}\frac{\Lambda(n)}{n^\sigma}
(1+\chi_1(n))(1+\chi_2(n))\ge0.
\]

نحتفظ بشخصية حاصل الضرب كما هي في تعريف \(F\) حتى لا تضيع الموجبية، ثم
نردها إلى جدها البدائي عند تقدير المشتقة فقط.

## المتراجحة الأساسية

بوضع \(\delta=\sigma-1\)، وعزل الصفرين، وضبط غاما والموصل والعوامل
المحلية، نحصل على

\[
0\le
\frac1\delta-
\frac1{\delta+\eta_1}-
\frac1{\delta+\eta_2}+C\log Q.
\]

نختار

\[
\delta=\frac A{\log Q}.
\]

إذا \(\eta_i\le c/\log Q\)، صار الطرف الأيمن بعد القسمة على \(\log Q\)
لا يزيد على

\[
\frac1A-
\frac2{A+c}+C.
\]

عند \(c=0\) تكون القيمة \(-1/A+C\). نختار \(A\) بحيث \(1/A>2C\)، ثم
نختار \(c_P\) صغيرًا بما يكفي، فنحصل على تناقض.

## طبقات الفرادة

- المنطقة القياسية الفردية تصف الاستثناء داخل دالة واحدة.
- Landau--Page تمنع استثناءين من شخصيتين بدائيتين مختلفتين عبر الموصلات
  حتى \(Q\).
- النتيجة الصريحة عند ترديد ثابت تخص حاصل ضرب جميع دوال الشخصيات، ولا
  تستبدل مبرهنة Page.

## عدم الدور

لم يستخدم البرهان مبرهنة Siegel أو Deuring--Heilbronn أو
Siegel--Walfisz أو Bombieri--Vinogradov أو Linnik أو GRH.

## الحكم

```text
ANT-THM-11-02 LOGIC         = PASS
PRODUCT-CHARACTER           = HANDLED
POSITIVITY                  = PASS
CONDUCTOR-CONTROL           = PASS
THREE-UNIQUENESS-LEVELS     = SEPARATED
CIRCULARITY                 = PASS
CONSTANT                    = ABSOLUTE / NOT OPTIMIZED
```

يتفق المسار مع العرض الكلاسيكي في Davenport والمناقشة الحديثة في
Basak--Pratt.