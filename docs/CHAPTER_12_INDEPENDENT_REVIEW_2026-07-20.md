# تقرير مراجعة مستقلة — الفصل الثاني عشر: مبرهنة Siegel--Walfisz

## بيانات المراجعة

```text
DATE                     = 2026-07-20
CHAPTER                  = 12 — مبرهنة Siegel--Walfisz
BRANCH                   = agent/chapter-12-siegel-walfisz-v0.16.0
REVIEWED-CONTENT-HEAD    = 05dca3f1175d0be5d61f7c5dcc7bbce5361a7b36
LOCAL-BUILD-SOURCE-HEAD  = 62fac059604136fd18ece01213a71fc90a5bded4
LOCAL-BUILD-RECEIPT      = c79c6f3cc314004911a3fc80633a1476e62f98b5
PR                       = #20
CURRENT-CHAPTER-STATUS   = VERIFIED
```

## الحكم العام

لم يجد المراجع المستقل خطأً برهانيًا أو مرجعيًا حاجزًا. البراهين السبعة المنجزة داخليًا صحيحة، ومحاسبة الفعالية دقيقة، والاستشهادات الحديثة الثلاثة متحققة ومنسوبة بدقة.

```text
VERDICT                  = APPROVED
MATHEMATICAL-BLOCKERS    = 0
REFERENCE-BLOCKERS       = 0
TYPOGRAPHIC-BLOCKERS     = 0
RECOMMENDATION           = PROMOTE-TO-REVIEWED
MERGE                    = NOT AUTHORIZED
RELEASE-READY            = NO
```

## 1. منهج المراجعة

شملت المراجعة:

1. إعادة اشتقاق حدود الخطأ والمتراجحات في البراهين السبعة.
2. تتبع مصدر عدم الفعالية عبر البرهان كله.
3. مطابقة فرضي النتيجتين المقتبستين مع استعمالهما داخل الفصل.
4. التحقق من المعرفات المحال إليها والاعتماديات بين الفصول 9--11 و12.
5. التحقق المرجعي للمراجع الحديثة عبر arXiv وصفحات الناشرين.
6. فحص البناء المحلي المتزامن ونتيجته النهائية.

## 2. التحقق الرياضي

### الهوية (12.1) ومرشح الشخصيات

تعامد الشخصيات مستعمل بصورة صحيحة، وعامل

\[
\frac{1}{\varphi(q)}
\]

يمتص كثرة الشخصيات من دون خسارة إضافية في \(q\).

```text
VERDICT = PASS
```

### `ANT-LEM-12-01` — الرد إلى الشخصية البدائية

الفرق هو

\[
-\sum_{\substack{p^k\le x\\p\mid q,\ p\nmid r}}
\chi^*(p)^k\log p,
\]

ومن ثم

\[
\left|\psi(x,\chi)-\psi(x,\chi^*)\right|
\le \omega(q)\log x
\ll \log(2q)\log(2x).
\]

```text
VERDICT = PASS
```

### `ANT-THM-12-01` و`ANT-THM-12-02`

النتيجتان مقتبستان بأمانة، وليستا موسومتين `PROVED-HERE`:

- حد دو لا فاليه بوسان الفعال.
- المدخل الكمي المركب للصيغة الصريحة المقطوعة مع عزل الصفر الاستثنائي.

الفصل يعلن صراحة أن المدخل الثاني يعتمد على صيغة Perron المقطوعة وتحويل المسار وعد الأصفار والمنطقة الخالية، ولا يدعي إغلاق هذه الديون داخليًا.

```text
ANT-THM-12-01 = PASS-AS-CITED
ANT-THM-12-02 = PASS-AS-COMPOSITE-CITED-INPUT
```

### `ANT-LEM-12-02` — اختيار الارتفاع

مع

\[
T=e^{\kappa\sqrt L},\qquad U\in[T,2T],\qquad L=\log x,
\]

نحصل على

\[
\log(r(U+2))\ll\sqrt L,
\]

ومن ثم

\[
\exp\!\left(-\frac{cL}{\log(r(U+2))}\right)
\le e^{-c'\sqrt L}.
\]

كما أن كلفة القطع تحقق

\[
\frac{x\log^2(rxU)}{U}
\ll xL^2e^{-\kappa\sqrt L},
\]

وتمتص الخسائر متعددة اللوغاريتمات باستعمال

\[
L^D e^{-c\sqrt L}\le e^{-c'\sqrt L}.
\]

```text
VERDICT    = PASS
EFFECTIVITY = EFFECTIVE
```

### `ANT-LEM-12-03` — امتصاص الصفر الاستثنائي

باختيار

\[
\varepsilon=\frac{1}{2A}
\]

في `ANT-COR-11-01`:

\[
1-\beta
\ge c_\varepsilon r^{-\varepsilon}
\ge c_\varepsilon(\log x)^{-1/2}.
\]

إذن

\[
(1-\beta)\log x
\ge c_\varepsilon\sqrt{\log x},
\]

ومن ثم

\[
\frac{x^\beta}{\beta}
\ll xe^{-c_\varepsilon\sqrt{\log x}}.
\]

الصفر الاستثنائي بقي ظاهرًا حتى هذه الخطوة، وعدم الفعالية معزول في ثابت مبرهنة Siegel وحده.

```text
VERDICT     = PASS
EFFECTIVITY = INEFFECTIVE
```

### `ANT-THM-12-03` — مبرهنة Siegel--Walfisz

تركيب مساهمة الشخصية الرئيسية وغير الرئيسية في مرشح الشخصيات صحيح، وينتج

\[
\psi(x;q,a)
=
\frac{x}{\varphi(q)}
+O_A\!\left(xe^{-c_A\sqrt{\log x}}\right)
\]

بانتظام عندما \(q\le(\log x)^A\) و\((a,q)=1\).

```text
VERDICT = PASS / INEFFECTIVE-CONSTANT
```

### النتائج `ANT-COR-12-01/02/03`

الانتقال إلى الادخار اللوغاريتمي وإلى \(\vartheta\) صحيح. وفي الانتقال إلى \(\pi\)، عولج فشل شرط الترديد عند القيم الصغيرة بوضع

\[
y=\exp\!\left(q^{1/(2A)}\right)
\le e^{\sqrt{\log x}},
\]

واستعمال

\[
\frac{x}{\log x}+\int_y^x\frac{dt}{\log^2t}
=
\operatorname{Li}(x)-\operatorname{Li}(y)+\frac{y}{\log y}.
\]

جميع الحدود المتبقية تمتص في

\[
O_{A,B}\!\left(\frac{x}{(\log x)^B}\right).
\]

```text
ANT-COR-12-01 = PASS / INEFFECTIVE-CONSTANT
ANT-COR-12-02 = PASS / INEFFECTIVE-CONSTANT
ANT-COR-12-03 = PASS / INEFFECTIVE-CONSTANT
```

## 3. التحقق المرجعي

### Thorner--Zaman (2024)

```text
TITLE    = Refinements to the Prime Number Theorem for Arithmetic Progressions
JOURNAL  = Mathematische Zeitschrift
VOLUME   = 306
NUMBER   = 3
ARTICLE  = 54
YEAR     = 2024
ARXIV    = 2108.10878
VERDICT  = VERIFIED
```

وصف الفصل لمنطقة Vinogradov--Korobov وتقديرات الكثافة الخالية من اللوغاريتم وظاهرة Deuring--Heilbronn مطابق لمحتوى المرجع.

### Drappeau--Fiorilli (2021)

```text
TITLE    = The First Moment of Primes in Arithmetic Progressions: Beyond the Siegel--Walfisz Range
JOURNAL  = Transactions of the London Mathematical Society
VOLUME   = 8
NUMBER   = 1
PAGES    = 174--185
YEAR     = 2021
DOI      = 10.1112/tlm3.12030
VERDICT  = VERIFIED
```

### Koukoulopoulos (2013)

```text
TITLE    = Pretentious Multiplicative Functions and the Prime Number Theorem for Arithmetic Progressions
JOURNAL  = Compositio Mathematica
VOLUME   = 149
NUMBER   = 7
PAGES    = 1129--1149
YEAR     = 2013
ARXIV    = 1203.0596
VERDICT  = VERIFIED
```

المنظور الادعائي منسوب بدقة.

### المراجع الكلاسيكية

- de la Vallée Poussin (1896).
- Davenport (2000).
- Montgomery--Vaughan (2007).

سبق التحقق منها، وهي مناسبة للمداخل الكمية المستعملة.

## 4. الاعتماديات والبناء

المعرفات المحال إليها موجودة:

```text
ANT-PROP-10-01 = PRESENT
ANT-THM-09-03  = PRESENT
ANT-COR-11-01  = PRESENT
ANT-LEM-09-02  = PRESENT
```

والبناء المحلي المتزامن سجل:

```text
LOCAL-HEAD       = 62fac059604136fd18ece01213a71fc90a5bded4
ORIGIN-HEAD      = 62fac059604136fd18ece01213a71fc90a5bded4
SYNC             = PASS / FF-ONLY
SOURCE-BUILD     = PASS
PDF-PAGES        = 184
PDF-SIZE-BYTES   = 741765
PDF-SHA256       = 3BF0BCE828DDF09C03D6527117992806FAD06010B161FC1B242472D0B5367749
XELATEX          = MiKTeX-XeTeX 4.18 (MiKTeX 26.5)
BIBER            = 2.21
```

لا توجد أخطاء محرفية حاجزة في متن الفصل أو صِيَغه. بقيت في سجل MiKTeX تحذيرات تنضيد عامة غير حاجزة، مثل `Overfull/Underfull hbox` وبعض تحذيرات الخطوط والروابط في مواضع متفرقة من الكتاب؛ تصنف كدين تنضيدي قبل `RELEASE-READY`، ولا تغير حكم صحة الفصل.

## 5. انضباط النطاق

الفصل يصرح بوضوح أنه لا يثبت:

- انتظامًا فرديًا لكل \(q\le x^\delta\).
- مبرهنة Bombieri--Vinogradov أو مستوى التوزيع \(1/2\).
- حدًا فعالًا عامًا بعد امتصاص الصفر الاستثنائي.
- مبرهنة Linnik.
- أي نتيجة مشروطة بـGRH.

```text
SCOPE-DISCIPLINE = PASS
```

## 6. ملاحظة بنيوية اختيارية

تعتمد الآلة الكمية على `ANT-THM-12-02` بوصفها مدخلًا مركبًا مقتبسًا. هذا مقبول ضمن النطاق المعلن، لكن يوصى بجعل صيغة Perron المقطوعة وتحويل المسار والصيغة الصريحة الكاملة هدفًا لفصل تقني كمي لاحق، حتى يمكن مستقبلاً ترقية هذا المدخل إلى `PROVED-HERE`.

```text
CLASSIFICATION = NONBLOCKING / FUTURE-TECHNICAL-CHAPTER
```

## الخلاصة والتوصية

الفصل صحيح رياضيًا، ومحاسبة الفعالية فيه دقيقة، وعدم الفعالية معزول في نقطة استعمال مبرهنة Siegel، والاستشهادات الحديثة منسوبة بدقة. لا توجد ملاحظات حاجزة.

```text
INDEPENDENT-REVIEW      = COMPLETED
REVIEW-VERDICT          = APPROVED
MATHEMATICAL-BLOCKERS   = 0
REFERENCE-BLOCKERS      = 0
TYPOGRAPHIC-BLOCKERS    = 0
RECOMMENDATION          = PROMOTE-TO-REVIEWED
MERGE-PR-20             = NOT AUTHORIZED
RELEASE-READY           = NO
```

هذا التقرير لا يمثل إذنًا بالدمج. تبقى ترقية الحالة والدمج عمليتين حوكميتين منفصلتين، والدمج مشروط بأمر صريح من مالك المشروع.
