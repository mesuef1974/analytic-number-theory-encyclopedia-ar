# سجل أدلة الفصل السابع عشر — الطريقة الدائرية وغولدباخ ووارينغ

آخر تحديث: 2026-07-25

```text
CHAPTER             = 17
VERSION             = 0.21.0-dev
BASE-MAIN           = 0bd442bc48490115bed48b18ed32783ad5bd1c9c
BRANCH              = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
ISSUE               = #32 / OPEN
METHOD              = EVIDENCE-FIRST
AUTHORING           = BLOCKED PENDING INDEPENDENT GATE AUDIT
PRE-AUTHORING-GATE  = OPEN / FINAL AUDIT PENDING
RELEASE-READY       = NO
```

## 1. الموضوع والنطاق

العنوان الحاكم:

> **الطريقة الدائرية ومدخل إلى غولدباخ ووارينغ**.

النطاق المجمد:

1. دالة التوليد الأسية وهوية التعامد.
2. الأقواس الكبرى والصغرى.
3. التقريب المحلي والسلسلة والتكامل المفردان.
4. صيغة وارينغ التقاربية الكلاسيكية بحالة `CITED / EXPLAINED`.
5. مبرهنة فينوغرادوف بحالة `CITED`.
6. مبرهنة هلفغوت بحالة `CITED`، والمكوّن الحاسوبي `FINITE-VERIFIED`.
7. غولدباخ الثنائية `HYPOTHESIS / OPEN`.
8. الأدوات العامة للمجاميع الأسية مؤجلة إلى الفصل الثامن عشر.

## 2. التطبيع

\[
e(t)=e^{2\pi i t}.
\]

\[
f_k(\alpha;P)=\sum_{1\le x\le P}e(\alpha x^k),
\qquad P=N^{1/k}.
\]

\[
r_{s,k}(N)=\int_0^1f_k(\alpha;P)^s e(-N\alpha)\,d\alpha.
\]

الأقواس الكبرى حول الكسور المختزلة `a/q` وفق

\[
1\le q\le Q,
\qquad
\left|\alpha-\frac aq\right|\le\frac{Q}{qN},
\]

والأقواس الصغرى هي المتممة في `[0,1)`.

## 3. المصادر الأولية والمراجع التقنية

### غولدباخ والطريقة الدائرية

- G. H. Hardy and J. E. Littlewood, *Some problems of Partitio Numerorum III: On the expression of a number as a sum of primes*, *Acta Mathematica* 44 (1923), 1--70, DOI `10.1007/BF02403921`.
- G. H. Hardy and J. E. Littlewood, *Some Problems of Partitio Numerorum V: A Further Contribution to the Study of Goldbach's Problem*, *Proceedings of the London Mathematical Society* s2-22, 46--56, DOI `10.1112/plms/s2-22.1.46`.
- I. M. Vinogradov, *Representation of an odd number as the sum of three primes*, *Doklady Akademii Nauk SSSR* 15 (1937), 129--132.
- H. A. Helfgott, *The ternary Goldbach conjecture is true*, modern completion; cited result only.

### وارينغ

- G. H. Hardy and J. E. Littlewood, *Some problems of Partitio Numerorum IV: The singular series in Waring's Problem and the value of G(k)*, *Mathematische Zeitschrift* 12 (1922), 161--188, DOI `10.1007/BF01482074`.
- R. C. Vaughan, *The Hardy--Littlewood Method*, 2nd ed., Cambridge University Press, 1997.

## 4. هدف وارينغ المجمد

لـ`k\ge2` و`s` كبير بما يكفي بدلالة `k`، تُعرض الصيغة البنيوية

\[
r_{s,k}(N)
=
\mathfrak S_{s,k}(N)\mathfrak J_{s,k}(N)
+o\!\left(N^{s/k-1}\right).
\]

التصنيف:

| المكوّن | التصنيف |
|---|---|
| هوية التعامد | `IDENTITY / PROVED-HERE` |
| تفكيك الأقواس | `DEFINITION / PROVED-HERE` |
| بنية الحد الرئيس | `PROVED-HERE / SELECTED DETAILS` |
| تقدير الأقواس الصغرى | `CITED / COMPOSITE INPUT` |
| الصيغة التقاربية الكاملة | `CITED / EXPLAINED` |
| أفضل حدود المتغيرات الحديثة | `DEFERRED` |

## 5. مدخل الأقواس الصغرى

يستخدم الفصل فقط وجود `\delta=\delta(k,s)>0`، في النطاق الكلاسيكي الملائم، بحيث

\[
\int_{\mathfrak m}|f_k(\alpha;P)|^s\,d\alpha
\ll P^{s-k-\delta}.
\]

لا يثبت الفصل هذه الحزمة العامة، ولا يدعي أمثلية نطاق `s`.

## 6. النتائج الثلاثية

### فينوغرادوف

> كل عدد فردي كبير بما يكفي هو مجموع ثلاثة أعداد أولية.

`CITED`.

### هلفغوت

> كل عدد فردي أكبر من 5 هو مجموع ثلاثة أعداد أولية.

الجزء التحليلي `CITED`، والتحقق العددي المنفصل `FINITE-VERIFIED`.

### غولدباخ الثنائية

تبقى `HYPOTHESIS / OPEN`، ولا تتحول صيغة هاردي--ليتلوود المتوقعة إلى مبرهنة.

## 7. عدم الدور

```text
CHAPTER-17 MINOR-ARC TOOLS = CITED INPUT
CHAPTER-18 EXPONENTIAL-SUM THEORY = FUTURE INTERNAL DEVELOPMENT
CIRCULARITY = NONE
```

## 8. الحكم

```text
PRIMARY-SOURCES        = VERIFIED FOR FROZEN SCOPE
PROOF-SCOPE            = FROZEN
NORMALIZATION          = FROZEN
REFERENCE-BLOCKERS     = 0
SCOPE-BLOCKERS         = 0
TECHNICAL-BLOCKERS     = 0
INDEPENDENT-GATE-AUDIT = PENDING
PASS-FOR-AUTHORING     = NO
```