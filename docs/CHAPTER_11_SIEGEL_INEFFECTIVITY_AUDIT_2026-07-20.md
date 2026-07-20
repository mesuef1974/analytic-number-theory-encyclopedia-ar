# تدقيق مبرهنة Siegel وعدم الفعالية — الفصل الحادي عشر

## بيانات التدقيق

```text
DATE                 = 2026-07-20
SCOPE                = ANT-THM-11-03 / ANT-COR-11-01
AUDIT-STATE          = PASS
RESULT-REGISTRY      = REMAINS-DRAFT-UNTIL-POST-AUTHORING-AUDIT
```

## مبرهنة Siegel

لكل \(\varepsilon>0\)، يوجد ثابت \(c(\varepsilon)>0\) بحيث لكل شخصية
ديريشليه حقيقية بدائية غير رئيسية \(\chi\) بموصل \(q\):

\[
|L(1,\chi)|
\ge c(\varepsilon)q^{-\varepsilon}.
\]

الثابت \(c(\varepsilon)\) غير فعال. تسجل النتيجة في الفصل بحالة
`CITED`، ولا يدعي المشروع برهانًا داخليًا كاملًا لها.

## معنى عدم الفعالية

عدم الفعالية يعني أن البرهان المعروف لا يقدم خوارزمية مضمونة لحساب
\(c(\varepsilon)\) من \(\varepsilon\). ولذلك لا يجوز استعماله لإنتاج
ثابت عددي صريح أو حد خطأ يعلن أنه فعال.

## حد فعال للمشتقة قرب الواحد

إذا كانت \(\chi\) غير رئيسية بترديد \(q\)، وكان

\[
1-\frac{c_0}{\log(2q)}\le\sigma\le1,
\]

فإن

\[
|L'(\sigma,\chi)|\ll\log^2(2q).
\]

لإثبات ذلك نضع

\[
S(x)=\sum_{n\le x}\chi(n).
\]

من دورية الشخصية وانعدام مجموع دورة كاملة، لدينا \(|S(x)|\le q\). ويعطي
الجمع الجزئي

\[
L(s,\chi)=
\sum_{n\le q}\frac{\chi(n)}{n^s}+
 s\int_q^\infty\frac{S(x)}{x^{s+1}}\,dx.
\]

بالتفاضل عند \(s=\sigma\):

\[
L'(\sigma,\chi)=
-
\sum_{n\le q}\frac{\chi(n)\log n}{n^\sigma}+
\int_q^\infty\frac{S(x)}{x^{\sigma+1}}\,dx-
\sigma\int_q^\infty
\frac{S(x)\log x}{x^{\sigma+1}}\,dx.
\]

في الشريط المحدد، \(q^{1-\sigma}\) محدود بثابت مطلق. لذلك يكون الحد
المنتهي \(O(\log^2(2q))\)، ويكون التكاملان \(O(1)\) و
\(O(\log(2q))\).

```text
DERIVATIVE-BOUND = PROVED-HERE / EFFECTIVE
POLYA-VINOGRADOV = NOT REQUIRED
```

## الإبعاد غير الفعال للصفر الاستثنائي

إذا كان \(\beta\) صفرًا استثنائيًا، فإن

\[
L(1,\chi)=\int_\beta^1L'(u,\chi)\,du.
\]

ومن حد المشتقة:

\[
|L(1,\chi)|
\ll(1-\beta)\log^2(2q).
\]

نطبق مبرهنة Siegel بالأس \(\varepsilon/2\)، فنحصل على

\[
1-\beta
\gg_\varepsilon
\frac{q^{-\varepsilon/2}}{\log^2(2q)}.
\]

وباستعمال

\[
\log^2(2q)\ll_\varepsilon q^{\varepsilon/2},
\]

ينتج

\[
1-\beta\gg_\varepsilon q^{-\varepsilon}.
\]

الثابت غير فعال لأنه يعتمد على ثابت Siegel.

## المراجع

- المصدر الأصلي: Siegel، Acta Arithmetica 1 (1935)، 83--86.
- برهان تحليلي حديث: Zihao Liu، arXiv:2202.00635.
- تعرض المراجع القياسية الفرق بين الحالة التربيعية والحالات التي تسمح
  بحدود فعالة أقوى.

## عدم الدور

اشتقاق حد المشتقة لا يستخدم Siegel--Walfisz أو Bombieri--Vinogradov أو
Linnik أو Deuring--Heilbronn أو GRH. تدخل مبرهنة Siegel فقط في الخطوة
المعلنة التي تنتج الحد غير الفعال.

## الحكم

```text
ANT-THM-11-03 SOURCE        = VERIFIED / CITED
ANT-THM-11-03 EFFECTIVITY   = INEFFECTIVE
DERIVATIVE-BOUND            = PASS / EFFECTIVE
ANT-COR-11-01 LOGIC         = PASS
ANT-COR-11-01 EFFECTIVITY   = INEFFECTIVE
MISUSE-AS-EFFECTIVE-BOUND   = PROHIBITED
CIRCULARITY                 = PASS
```
