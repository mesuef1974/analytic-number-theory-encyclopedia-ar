# تدقيق الباقي المنتظم — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = GAMMA / CONDUCTOR / LOCAL-FACTORS / PRINCIPAL-POLE
AUDIT-STATE          = PASS
AUTHORING             = AUTHORIZED-BY-LATER-COMPREHENSIVE-AUDIT
```

## الهدف

نثبت وجود ثابت مطلق \(C>0\) يضبط حدود الموصل وغاما والعوامل المحلية في
المتراجحة الموزونة بحد

\[
C\log(q(|t|+2)),
\]

من دون استعمال منطقة خالية من الأصفار.

## صيغة المشتقة اللوغاريتمية

إذا كانت \(\xi\) شخصية بدائية غير رئيسية بموصل \(r\)، فإن الصيغة
القياسية هي

\[
-\Re\frac{L'}{L}(s,\xi)=
\frac12\log\frac r\pi+
\frac12\Re\frac{\Gamma'}{\Gamma}
\left(\frac{s+a_\xi}{2}\right)-
\sum_{\rho_\xi}^{*}\Re\frac1{s-\rho_\xi}.
\tag{1}
\]

مصدرها جداء هادامار للدالة المكتملة ومعادلتها الوظيفية. ولا تعتمد على أي
منطقة خالية يراد إثباتها.

## تقدير عامل غاما

يوجد ثابت مطلق \(C_\Gamma>0\) بحيث لكل
\(1\le\sigma\le2\)، و\(a\in\{0,1\}\)، و\(t\in\mathbb R\):

\[
\left|
\Re\frac{\Gamma'}{\Gamma}
\left(\frac{\sigma+a+it}{2}\right)
\right|
\le C_\Gamma\log(|t|+2).
\tag{2}
\]

عند الارتفاعات المحدودة تأتي النتيجة من الاستمرارية على مجموعة مدمجة
بعيدة عن أقطاب غاما، وعند الارتفاعات الكبيرة من صيغة ستيرلينغ المنتظمة.

بحذف مجموع الأصفار المطروح في (1)، نحصل على

\[
-\Re\frac{L'}{L}(\sigma+it,\xi)
\le C_1\log(r(|t|+2)).
\tag{3}
\]

وإذا عزلنا صفرًا محددًا، نبقي مساهمته السالبة صراحة ونحذف بقية مساهمات
الأصفار فقط.

## العوامل المحلية

إذا كانت \(\chi\pmod q\) مستحثة من \(\xi\pmod r\)، فإن

\[
\frac{L'}{L}(s,\chi)=
\frac{L'}{L}(s,\xi)+
\sum_{\substack{p\mid q\\p\nmid r}}
\frac{\xi(p)(\log p)p^{-s}}
     {1-\xi(p)p^{-s}}.
\]

ولـ\(\sigma>1\):

\[
\left|
\frac{\xi(p)(\log p)p^{-s}}
     {1-\xi(p)p^{-s}}
\right|
\le\frac{\log p}{p^\sigma-1}\le\log p.
\]

إذن مجموع العوامل المحلية لا يتجاوز

\[
\sum_{p\mid q}\log p
=\log\operatorname{rad}(q)
\le\log q.
\tag{4}
\]

## الشخصية الرئيسية

للشخصية الرئيسية \(\chi_0\pmod q\):

\[
L(s,\chi_0)=
\zeta(s)\prod_{p\mid q}(1-p^{-s}).
\]

ومن صيغة الكسور الجزئية لزيتا وتقدير غاما:

\[
-\Re\frac{\zeta'}{\zeta}(\sigma+it)
\le
\Re\frac1{\sigma-1+it}+C_2\log(|t|+2).
\]

بضم العوامل المحلية:

\[
-\Re\frac{L'}{L}(\sigma+it,\chi_0)
\le
\Re\frac1{\sigma-1+it}
+C_3\log(q(|t|+2)).
\tag{5}
\]

يجب إبقاء حد القطب في (5) صراحة عندما تكون الشخصية الرئيسية هي
\(\chi^2\) في المتراجحة الموزونة.

## التطبيق

في المتراجحة

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{L'}{L}(\sigma+i\gamma,\chi)
-\Re\frac{L'}{L}(\sigma+2i\gamma,\chi^2)
\ge0,
\]

نعزل الصفر المطلوب في الحد الثاني، ونستعمل (3)--(5) للبقية. وبما أن
موصل كل جد بدائي ظاهر لا يتجاوز \(q\)، تجمع الحدود غير المعزولة في

\[
C\log(q(|\gamma|+2)).
\]

## عدم الدور

لم يستخدم البرهان:

- المنطقة القياسية الخالية.
- مبرهنة Landau--Page.
- مبرهنة Siegel.
- Deuring--Heilbronn.
- Siegel--Walfisz أو Bombieri--Vinogradov.
- Linnik أو GRH.

## الحكم

```text
PARTIAL-FRACTION-IDENTITY = PASS
GAMMA-BOUND               = PASS
LOCAL-FACTOR-BOUND        = PASS
PRINCIPAL-POLE-BOUND      = PASS
UNIFORM-REMAINDER         = PASS
CIRCULARITY               = PASS
```

التدقيق الشامل للمنطقة القياسية مسجل في
`docs/CHAPTER_11_STANDARD_ZERO_FREE_REGION_LOGIC_AUDIT_2026-07-20.md`.