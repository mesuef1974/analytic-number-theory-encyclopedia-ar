# التحقق المرجعي الأولي للفصل الحادي عشر

## الحالة

```text
DATE                 = 2026-07-20
REFERENCE-AUDIT      = PARTIAL / ACTIVE
CONSENSUS-SCAN       = COMPLETED-FIRST
PUBLISHER-CHECK      = STARTED
ARXIV-CHECK          = STARTED
AUTHORING             = BLOCKED
```

## الغرض

تثبيت الصيغ التي يجوز أن يبنى عليها الفصل، ومنع دمج نتائج متقاربة في الاسم لكنها مختلفة في نطاق الترديد والموصل ومعنى «الاستثناء الوحيد».

## النتيجة المرجعية الأولى: ثلاث طبقات للفرادة

### الطبقة A — دالة فردية

الصيغة القياسية لدالة بدائية منفردة هي:

- الأصفار غير الحقيقية لا تقترب من \(1\) أكثر من رتبة
  \(1/\log(q(|t|+2))\).
- إذا بقي استثناء قريب من \(1\)، فلا يظهر إلا لشخصية حقيقية، ويكون الصفر حقيقيًا.
- بساطة الصفر تحتاج أن تدخل صراحة في المبرهنة أو في لمّة مستقلة.

هذه الصيغة لا تقول وحدها إن جميع الدوال ذات الموصلات المختلفة تتشارك استثناءً واحدًا فقط.

### الطبقة B — جميع الشخصيات بترديد ثابت

يعرّف Benli--Goel--Twiss--Zaman، نقلًا عن McCurley مع الإشارة إلى تحسينات Kadiri:

\[
\mathscr L_q(s)=\prod_{\chi\pmod q}L(s,\chi).
\]

ولـ\(q\ge3\)، تملك \(\mathscr L_q\) على الأكثر صفرًا واحدًا في المنطقة الصريحة

\[
\Re(s)>
1-
\frac{1}
{10\log\max\{q,q|\Im(s)|,10\}}.
\]

إذا وجد الصفر، فهو:

```text
real + simple + associated to a real quadratic character modulo q
```

هذه صيغة ثابتة الترديد تخص حاصل الضرب \(\mathscr L_q\)، ولا يجوز عرضها بوصفها مبرهنة Page.

### الطبقة C — جميع الموصلات حتى Q

مبرهنة Landau--Page تعطي فرادة عبر عائلة من الشخصيات الحقيقية البدائية ذات موصلات محدودة بـ\(Q\)، في منطقة من رتبة

\[
\beta>1-\frac{c}{\log Q}.
\]

نص المبرهنة وثابتها وتطبيعها لم تُثبت بعد من الكتاب القياسي، ولذلك تبقى:

```text
LANDUA-PAGE-STATEMENT = NOT YET TEXTUALLY VERIFIED
```

## McCurley 1984

**البيانات المثبتة:**

- Kevin S. McCurley.
- “Explicit zero-free regions for Dirichlet L-functions”.
- *Journal of Number Theory* 19 (1984), 7--32.
- DOI: `10.1016/0022-314X(84)90089-1`.

**المثبت من صفحة الناشر:**

- البحث يدرس حاصل ضرب دوال ديريشليه بترديد ثابت.
- يثبت وجود منطقة عددية صريحة.
- لا يقع فيها أكثر من صفر واحد.
- الصفر الممكن حقيقي وبسيط ومن شخصية حقيقية غير رئيسية.

**الحكم:**

```text
MCCURLEY-BIBLIOGRAPHY = VERIFIED
MCCURLEY-ABSTRACT-CLAIMS = VERIFIED
MCCURLEY-FULL-PROOF-MAP = NOT YET EXTRACTED
```

## Kadiri 2018

**البيانات المثبتة:**

- Habiba Kadiri.
- “An explicit zero-free region for the Dirichlet L-functions”.
- arXiv:`math/0510570`, النسخة الثانية 2019.
- النسخة المنشورة: *Mathematika* 64 (2018), no. 2, 445--474.

**النص المثبت:**

للشخصية البدائية غير الرئيسية \(\chi\pmod q\)، في النطاق
\(3\le q\le400000\)، تثبت Kadiri عدم الانعدام في

\[
\Re(s)\ge
1-
\frac1{5.60\log(q\max(1,|\Im(s)|))}.
\]

وهذا يحسن ثابت McCurley العددي في النطاق المذكور.

**قيد مهم:**

هذه نتيجة صريحة ذات نطاق عددي محدد، وليست الصيغة النوعية العامة التي ينبغي أن تكون نواة الفصل.

```text
KADIRI-STATEMENT = VERIFIED-FROM-ARXIV-ABSTRACT
KADIRI-PROOF-SIGNS = NOT YET AUDITED
```

## Benli--Goel--Twiss--Zaman

**البيانات المثبتة:**

- Kübra Benli, Shivani Goel, Henry Twiss, Asif Zaman.
- “Explicit Deuring--Heilbronn phenomenon for Dirichlet L-functions”.
- arXiv:`2410.06082`.

**المثبت من المقدمة:**

- تعيد الورقة صياغة نتيجة McCurley لحاصل الضرب \(\mathscr L_q\).
- إذا وجد صفر \(\beta_1\) استثنائي، فإن أي صفر آخر
  \(\rho=\beta+i\gamma\) يخضع لحد تنافر صريح.
- الصيغة تعتمد على \(1-\beta_1\)، و\(\log q\)، و\(\log T\).
- الورقة تميز بين نسخة صريحة فعالة ونسخة أفضل الثوابت لكنها غير فعالة.

**الحكم:**

```text
DEURING-HEILBRONN-MECHANISM = VERIFIED
EXACT-COROLLARY-CONSTANTS = AVAILABLE / NOT ADOPTED
CHAPTER-CORE-USE = CITED-QUALITATIVE
```

## Li 1999

**البيانات المثبتة:**

- Hongze Li.
- “Zero-free regions for Dirichlet L-functions”.
- *Quarterly Journal of Mathematics* 50 (1999), 13--23.
- DOI: `10.1093/qjmath/50.197.13`.

البيانات الببليوغرافية مثبتة من Oxford Academic، لكن نص المبرهنة الكامل غير متاح في العرض المفتوح.

```text
LI-BIBLIOGRAPHY = VERIFIED
LI-THEOREM-TEXT = ACCESS-LIMITED
```

## Heath-Brown 1992

**البيانات المثبتة:**

- D. R. Heath-Brown.
- “Zero-Free Regions for Dirichlet L-Functions, and the Least Prime in an Arithmetic Progression”.
- *Proceedings of the London Mathematical Society* 64 (1992), 265--338.
- DOI: `10.1112/plms/s3-64.2.265`.

يستعمل بوصفه مرجعًا متقدمًا للربط بين المناطق الخالية وLinnik، لا بوصفه المسار التعليمي الأول للنواة.

```text
HEATH-BROWN-BIBLIOGRAPHY = VERIFIED
HEATH-BROWN-CORE-DEPENDENCY = NO
```

## Khale 2024

**البيانات المثبتة:**

- Tanmay Khale.
- “An Explicit Vinogradov--Korobov Zero-Free Region for Dirichlet L-Functions”.
- *Quarterly Journal of Mathematics* 75 (2024), 299--332.
- DOI: `10.1093/qmath/haae010`.

تثبت الورقة أول صيغة صريحة من نمط Vinogradov--Korobov لدوال ديريشليه. تُحجز لملحق أو فصل لاحق.

```text
KHALE-BIBLIOGRAPHY = VERIFIED
VINOGRADOV-KOROBOV = DEFERRED-ADVANCED
```

## تصحيحات مطلوبة في صياغة النتائج المقترحة

1. يجب ألا تُصاغ `ANT-THM-11-01` بكلمة «واحد» من دون تحديد المجال.
2. يُفصل داخل الفصل بين:
   - المنطقة الفردية للشخصية البدائية.
   - فرادة الاستثناء في \(\mathscr L_q\) لترديد ثابت.
   - فرادة Page عبر الموصلات حتى \(Q\).
3. لا يعتمد ثابت Kadiri \(5.60\) في النتيجة المركزية لأنه مقيد بنطاق \(q\) صريح.
4. الصيغة الأساسية التعليمية تستعمل ثابتًا مطلقًا غير محسن، ثم تعرض النتائج الصريحة في ملاحظة تاريخية.
5. Deuring--Heilbronn تسجل أولًا صيغة نوعية مقتبسة؛ الثوابت الحديثة لا تدخل قبل تدقيق مستقل.

## العناصر غير المتحققة بعد

- [ ] نص Landau--Page من Davenport أو Montgomery--Vaughan أو Iwaniec--Kowalski.
- [ ] نص مبرهنة Siegel وموضع الصفحة.
- [ ] الصيغة الدقيقة للمشتقة اللوغاريتمية المجمعة على الأصفار.
- [ ] تقدير عامل غاما في النطاق الصغير والكبير.
- [ ] برهان بساطة الاستثناء في المسار المختار.
- [ ] العلاقة الدقيقة بين صفر الشخصية غير البدائية وصفر الجد البدائي في كل المنطقة المستعملة.
- [ ] تحديد نتيجة Deuring--Heilbronn النوعية النهائية التي ستقتبس.

## الحكم الحالي

```text
REFERENCE-AUDIT      = PARTIAL-PASS
BLOCKING-CORRECTION  = DISTINGUISH-THREE-UNIQUENESS-LEVELS
PRE-AUTHORING-GATE   = OPEN
AUTHORING             = BLOCKED
```
