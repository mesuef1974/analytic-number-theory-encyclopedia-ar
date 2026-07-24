# إغلاق المصادر والتطبيع ومدخل الأقواس الصغرى — الفصل السابع عشر

التاريخ: 2026-07-25

```text
CHAPTER                    = 17
VERSION                    = 0.21.0-dev
VINOGRADOV-ATTRIBUTION     = SOURCE-VERIFIED
WARING-TARGET              = FROZEN
MINOR-ARC-INPUTS           = SOURCE-VERIFIED / CITED
HELFGOTT-SCOPE             = DECIDED
NORMALIZATION              = FROZEN
AUTHORING                   = STILL BLOCKED PENDING INDEPENDENT GATE AUDIT
RELEASE-READY               = NO
```

## 1. مبرهنة فينوغرادوف

الصياغة المعتمدة في الفصل:

> كل عدد صحيح فردي كبير بما يكفي يمكن تمثيله على صورة مجموع ثلاثة أعداد أولية.

التصنيف:

```text
RESULT         = CITED
PROOF-IN-CH17  = NO
ATTRIBUTION    = I. M. Vinogradov, 1937
```

الإحالة المثبتة:

I. M. Vinogradov, *Representation of an odd number as the sum of three primes*,
*Doklady Akademii Nauk SSSR* 15 (1937), 129--132.

لا تُخلط هذه النتيجة مع مبرهنة هلفغوت الكاملة، التي تزيل قيد «كبير بما يكفي».

## 2. هدف وارينغ

الهدف المثبت ليس أفضل حد حديث لـ`G(k)` أو `\widetilde G(k)`، بل الصيغة البنيوية الكلاسيكية التالية:

لـ`k\ge2` و` s ` كبير بما يكفي بدلالة `k`، يكون عدد التمثيلات

\[
r_{s,k}(N)
=
\#\{(x_1,\ldots,x_s)\in\mathbb N^s:
N=x_1^k+\cdots+x_s^k\}
\]

ذا صيغة تقاربية من الشكل

\[
r_{s,k}(N)
=
\mathfrak S_{s,k}(N)\,\mathfrak J_{s,k}(N)
+o\!\left(N^{s/k-1}\right),
\]

بعد تثبيت التطبيع الدقيق في المتن.

التصنيف:

```text
ORTHOGONALITY IDENTITY      = PROVED-HERE
MAJOR-ARC DECOMPOSITION     = PROVED-HERE / SELECTED DETAILS
SINGULAR SERIES STRUCTURE   = PROVED-HERE OR CITED BY SUBCLAIM
MINOR-ARC POWER SAVING      = CITED
FULL ASYMPTOTIC THEOREM     = CITED / EXPLAINED
BEST MODERN VARIABLE BOUNDS = DEFERRED
```

المصادر الحاكمة:

1. G. H. Hardy and J. E. Littlewood, *Some problems of Partitio Numerorum IV: The singular series in Waring's Problem and the value of G(k)*, *Mathematische Zeitschrift* 12 (1922), 161--188, DOI `10.1007/BF01482074`.
2. R. C. Vaughan, *The Hardy--Littlewood Method*, 2nd ed., Cambridge Tracts in Mathematics 125, Cambridge University Press, 1997؛ ولا سيما فصول وارينغ والأقواس الكبرى وطرق فينوغرادوف.

## 3. مدخل الأقواس الصغرى

لن يثبت الفصل السابع عشر نظرية عامة جديدة للمجاميع الأسية. المدخل المسموح هو مبرهنة مقتبسة مضبوطة:

إذا كان

\[
f_k(\alpha;P)=\sum_{1\le x\le P}e(\alpha x^k),
\qquad e(t)=e^{2\pi i t},
\]

فإنه عند اختيار نظام أقواس كبرى قياسي ومع `s` كبير بما يكفي بدلالة `k`، تتوافر قيمة `\delta=\delta(k,s)>0` بحيث

\[
\int_{\mathfrak m}|f_k(\alpha;P)|^s\,d\alpha
\ll P^{s-k-\delta}.
\]

هذه الصياغة تستخدم فقط لإثبات أن مساهمة الأقواس الصغرى أصغر من الحد الرئيس. الثوابت المثلى وأفضل نطاق لـ`s` خارج نطاق الفصل.

```text
MINOR-ARC ESTIMATE = CITED / COMPOSITE INPUT
SOURCE ROUTE       = VAUGHAN + ORIGINAL HARDY-LITTLEWOOD CONTEXT
CHAPTER-18 ROLE    = LATER INTERNAL DEVELOPMENT OF EXPONENTIAL-SUM TOOLS
CIRCULARITY        = NONE
```

## 4. نطاق هلفغوت

تُذكر مبرهنة هلفغوت بوصفها الإكمال الحديث لغولدباخ الثلاثي:

> كل عدد فردي أكبر من 5 هو مجموع ثلاثة أعداد أولية.

التصنيف:

```text
ANALYTIC THEOREM       = CITED
FINITE VERIFICATION    = FINITE-VERIFIED
FULL PROOF IN CHAPTER  = NO
```

## 5. التطبيع المجمد

يعتمد الفصل:

\[
e(t)=e^{2\pi i t}.
\]

ولوارينغ:

\[
f_k(\alpha;P)=\sum_{1\le x\le P}e(\alpha x^k),
\qquad P=N^{1/k}.
\]

وهوية التمثيل:

\[
r_{s,k}(N)=\int_0^1 f_k(\alpha;P)^s e(-N\alpha)\,d\alpha.
\]

تُعرّف الأقواس الكبرى بواسطة الكسور المختزلة `a/q` مع

\[
1\le q\le Q,
\qquad
\left|\alpha-\frac aq\right|\le \frac{Q}{qN},
\]

حيث يثبت اختيار `Q` النهائي في خريطة البرهان قبل المتن. الأقواس الصغرى هي المتممة في `[0,1)`.

يستخدم الرمزان:

\[
\mathfrak S_{s,k}(N)
\quad\text{للسلسلة المفردة},
\qquad
\mathfrak J_{s,k}(N)
\quad\text{للتكامل المفرد}.
\]

## 6. الحكم

```text
REFERENCE-BLOCKERS = 0
SCOPE-BLOCKERS     = 0
TECHNICAL-BLOCKERS = 0 BEFORE INDEPENDENT GATE AUDIT
PASS-FOR-AUTHORING = NOT YET ISSUED
```

لم تُغلق بوابة التأليف بهذه الوثيقة وحدها؛ يلزم تدقيق مستقل للبوابة وإيصال إغلاق منفصل.