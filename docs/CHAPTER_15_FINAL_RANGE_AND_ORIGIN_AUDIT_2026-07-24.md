# الفصل الخامس عشر — تدقيق المجال النهائي ومنشأ النتائج

التاريخ: 2026-07-24

```text
CHAPTER                = 15
VERSION                = 0.19.0-dev
AUDIT                   = FINAL-RANGE-AND-ORIGIN
STATUS                  = PASS
AUTHORING               = BLOCKED-PENDING-RESERVATION
PASS-FOR-AUTHORING      = NO
```

## 1. تقدير مقام سيلبرغ

في البعد الغربالي \(\kappa\)، يثبت التقدير القياسي لمجموع سيلبرغ

\[
G(z,z)
=
\frac{e^{\gamma\kappa}}{\Gamma(\kappa+1)}
V(z)^{-1}
\left(1+O\left(\frac1{\log z}\right)\right),
\]

تحت فرض البعد المنتظم المناسب. هذا التقدير مسجل في معالجة Halberstam--Richert ويعرض في مراجع المحاضرات القياسية على أنه مدخل مستقل عن المتراجحة التربيعية المنتهية.

للتطبيق \(n(n+h)\) مع \(h\ne0\) زوجي، سبق إثبات

\[
\kappa=2,
\qquad
V_h(z)\asymp_h(\log z)^{-2}.
\]

ومن ثم

\[
G_h(z,z)\asymp_h(\log z)^2.
\]

التصنيف:

```text
G-ASYMPTOTIC = CITED / COMPOSITE-INPUT
```

ولا يدعي الفصل إثبات هذه الصيغة التقاربية العامة من الصفر.

## 2. حد البواقي

من التدقيق المحلي:

\[
|r_{h,d}|\le\rho_h(d)\le2^{\omega(d)}.
\]

ومن حد سيلبرغ المنتهي عند \(R=z\):

\[
\mathcal R_h(z)
\le
\sum_{d<z^2}\mu^2(d)6^{\omega(d)}.
\]

باستعمال التقدير القياسي

\[
\sum_{d<Y}\mu^2(d)k^{\omega(d)}
\ll_k Y(\log Y)^{k-1},
\]

نحصل عند \(k=6\) على

\[
\mathcal R_h(z)
\ll z^2(\log z)^5.
\]

يمكن تقديم هذا التقدير داخل الموسوعة بواسطة سلسلة ديريشليه أو الالتفاف، أو اقتباسه كلّمة قياسية. المنشأ النهائي يثبت أثناء التأليف، لكنه ليس عائقًا رياضيًا.

## 3. اختيار المجال

نختار المجال التعليمي الآمن

\[
3\le z\le x^{1/4}.
\]

عندئذ

\[
z^2(\log z)^5
\le
x^{1/2}(\log x)^5
\ll
\frac{x}{(\log z)^2}
\]

لـ\(x\) كبير بما يكفي. أما القيم المحدودة من \(x\) فتمتص في الثابت الضمني المعتمد على \(h\).

إذن:

\[
S_h(x,z)
\ll_h
\frac{x}{(\log z)^2}
\qquad
(3\le z\le x^{1/4},\ h\ne0\text{ زوجي}).
\]

## 4. الحالة الفردية

إذا كان \(h\) فرديًا و\(z>2\)، فإن

\[
S_h(x,z)=0
\]

لأن أحد \(n,n+h\) زوجي دائمًا. لذلك تصاغ المبرهنة المركزية للحالة الزوجية، وتذكر الحالة الفردية كملاحظة انعدام تامة.

## 5. منشأ مكونات النتيجة

| المكوّن | الحالة |
|---|---|
| تعريف \(S(\mathcal A,\mathcal P,z)\) وبيانات الغربال | `DEFINITION` |
| متراجحة المربع | `PROVED-HERE` |
| تحويل صورة سيلبرغ والتصغير المنتهي | `PROVED-HERE` |
| الحد العلوي \(X/G+\sum3^{\omega(d)}|r_d|\) | `PROVED-HERE` |
| تعريف البعد الغربالي | `DEFINITION` |
| تقدير \(G(z,z)\) العام | `CITED / COMPOSITE-INPUT` |
| اللمّة الأساسية العامة | `CITED / COMPOSITE-INPUT` |
| حساب \(\rho_h(p)\) والعامل المحلي | `PROVED-HERE` |
| المجال \(z\le x^{1/4}\) والنتيجة التطبيقية | `PROVED-HERE` |
| عائق التكافؤ | `DIAGNOSTIC / CITED` |

## 6. عدم الدور

- لا يستخدم البرهان Bombieri--Vinogradov.
- لا يستخدم Barban--Davenport--Halberstam.
- لا يستخدم مبرهنة الفجوات المحدودة.
- لا يستنتج وجود أزواج أولية.
- اللمّة الأساسية تعرض كأداة عامة مستقلة، وليست لازمة لإثبات التطبيق المركزي في المجال المختار.

## 7. الحكم

```text
SELBERG-MINIMIZATION     = PASS
LOCAL-FACTOR             = PASS
FINAL-RANGE              = 3 <= z <= x^(1/4)
NO-CIRCULARITY           = PASS
MATHEMATICAL-BLOCKERS    = 0
RESULT-RESERVATION       = NEXT
PASS-FOR-AUTHORING       = NO
```
