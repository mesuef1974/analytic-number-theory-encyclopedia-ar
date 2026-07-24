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
MAJOR-ARC-SCALE            = FROZEN
AUTHORING                   = STILL BLOCKED PENDING INDEPENDENT GATE AUDIT
RELEASE-READY               = NO
```

## 1. مبرهنة فينوغرادوف

الصياغة المعتمدة:

> كل عدد صحيح فردي كبير بما يكفي يمكن تمثيله على صورة مجموع ثلاثة أعداد أولية.

```text
RESULT         = CITED
PROOF-IN-CH17  = NO
ATTRIBUTION    = I. M. Vinogradov, 1937
```

الإحالة المثبتة:

I. M. Vinogradov, *Representation of an odd number as the sum of three primes*,
*Doklady Akademii Nauk SSSR* 15 (1937), 129--132.

لا تُخلط هذه النتيجة مع مبرهنة هلفغوت الكاملة التي تزيل قيد «كبير بما يكفي».

## 2. هدف وارينغ

الهدف ليس أفضل حد حديث لـ`G(k)` أو `\widetilde G(k)`، بل الصيغة البنيوية الكلاسيكية:

لـ`k\ge2` و`s` كبير بما يكفي بدلالة `k`، يكون عدد التمثيلات

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
+o\!\left(N^{s/k-1}\right).
\]

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
2. R. C. Vaughan, *The Hardy--Littlewood Method*, 2nd ed., Cambridge Tracts in Mathematics 125, Cambridge University Press, 1997.

## 3. مدخل الأقواس الصغرى

إذا

\[
f_k(\alpha;P)=\sum_{1\le x\le P}e(\alpha x^k),
\qquad e(t)=e^{2\pi i t},
\]

فإنه، عندما يكون `s` كبيرًا بما يكفي بدلالة `k`، توجد قيمة
`\delta=\delta(k,s)>0` بحيث

\[
\int_{\mathfrak m}|f_k(\alpha;P)|^s\,d\alpha
\ll P^{s-k-\delta}.
\]

تستعمل هذه الصياغة فقط لإثبات أن مساهمة الأقواس الصغرى أصغر من الحد الرئيس. الثوابت المثلى وأفضل نطاق لـ`s` خارج النطاق.

```text
MINOR-ARC ESTIMATE = CITED / COMPOSITE INPUT
SOURCE ROUTE       = VAUGHAN + ORIGINAL HARDY-LITTLEWOOD CONTEXT
CHAPTER-18 ROLE    = LATER INTERNAL DEVELOPMENT OF EXPONENTIAL-SUM TOOLS
CIRCULARITY        = NONE
```

## 4. نطاق هلفغوت

تذكر مبرهنة هلفغوت بوصفها الإكمال الحديث لغولدباخ الثلاثي:

> كل عدد فردي أكبر من 5 هو مجموع ثلاثة أعداد أولية.

```text
ANALYTIC THEOREM       = CITED
FINITE VERIFICATION    = FINITE-VERIFIED
FULL PROOF IN CHAPTER  = NO
```

## 5. التطبيع المجمد

يعتمد الفصل

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

## 6. مقياس الأقواس الكبرى المجمد

يثبت ثابت صغير

\[
0<\eta<\frac{1}{4k},
\qquad Q=P^\eta.
\]

ولكل كسر مختزل `a/q` مع `1\le q\le Q` نضع

\[
\mathfrak M(q,a)
=
\left\{\alpha\in[0,1):
\left|\alpha-\frac aq\right|
\le \frac{Q}{qN}
\right\}.
\]

ثم

\[
\mathfrak M
=
\bigcup_{q\le Q}
\bigcup_{(a,q)=1}
\mathfrak M(q,a),
\qquad
\mathfrak m=[0,1)\setminus\mathfrak M.
\]

هذا اختيار حاكم للعرض؛ لا يدعي أنه الاختيار الوحيد أو الأمثل. وأي تغيير لاحق فيه يستلزم إعادة فتح تدقيق التطبيع ومدخل الأقواس الصغرى.

تستخدم الرموز

\[
\mathfrak S_{s,k}(N)
\quad\text{للسلسلة المفردة},
\qquad
\mathfrak J_{s,k}(N)
\quad\text{للتكامل المفرد}.
\]

## 7. الحكم

```text
REFERENCE-BLOCKERS = 0
SCOPE-BLOCKERS     = 0
TECHNICAL-BLOCKERS = 0
PARAMETER-BLOCKERS = 0
NORMALIZATION      = FROZEN
PASS-FOR-AUTHORING = NOT YET ISSUED
```

هذه الوثيقة تغلق فجوة `Q` التي كشفها التدقيق، لكنها لا تغلق بوابة التأليف وحدها؛ يلزم إيصال تدقيق مستقل منفصل.
