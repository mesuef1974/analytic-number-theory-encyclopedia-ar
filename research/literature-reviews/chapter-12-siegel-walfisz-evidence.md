# سجل أدلة الفصل الثاني عشر — مبرهنة Siegel--Walfisz

## بيانات المرحلة

```text
CHAPTER           = 12 — مبرهنة Siegel--Walfisz والتوزيع المنتظم للأعداد الأولية في المتتاليات الحسابية
VERSION           = 0.16.0-dev
BRANCH            = agent/chapter-12-siegel-walfisz-v0.16.0
BASE-COMMIT       = 9d02c583d416053550d22dfd7acc44d9c264a02c
MODE              = EVIDENCE-FIRST / PRE-AUTHORING
AUTHORING         = BLOCKED
LITERATURE-CUTOFF = 2026-07-20
```

## سؤال الفصل

كيف نرقّي نتيجة الفصل العاشر

\[
\psi(x;q,a)\sim \frac{x}{\varphi(q)}
\]

عندما يكون \(q\) ثابتًا، إلى تقدير موحد عندما يسمح للترديد أن ينمو مع \(x\) في المجال

\[
q\le (\log x)^A,
\]

مع إبراز مساهمة الصفر الاستثنائي وعدم إخفاء موضع استعمال مبرهنة Siegel وعدم فعالية الثوابت؟

## الصيغة المركزية المستهدفة

لكل \(A>0\) يوجد ثابت \(c_A>0\) بحيث، بانتظام لكل
\(x\ge3\)، و\(q\le(\log x)^A\)، و\((a,q)=1\)،

\[
\psi(x;q,a)
=
\frac{x}{\varphi(q)}
+
O_A\!\left(xe^{-c_A\sqrt{\log x}}\right).
\]

الثابت \(c_A\)، والثابت الضمني في الصياغة غير المشروطة العامة، غير فعالين بسبب استعمال مبرهنة Siegel لإبعاد الصفر الاستثنائي.

والصيغة المكافئة الأضعف، لكل \(A,B>0\)، هي

\[
\psi(x;q,a)
=
\frac{x}{\varphi(q)}
+
O_{A,B}\!\left(\frac{x}{(\log x)^B}\right),
\qquad q\le(\log x)^A.
\]

## الفصل بين ثلاث نتائج مختلفة

### 1. الفصل العاشر — ترديد ثابت

يثبت `ANT-THM-10-02` أنه لكل \(q\) ثابت:

\[
\psi(x;q,a)\sim\frac{x}{\varphi(q)}.
\]

هذه نتيجة نوعية لا تعطي ثوابت موحدة عندما يتغير \(q\) مع \(x\)، ولا تكفي وحدها لإثبات Siegel--Walfisz.

### 2. الفصل الثاني عشر — Siegel--Walfisz

المجال المستهدف هو

\[
q\le(\log x)^A,
\]

مع حد خطأ موحد في \(q\) و\(a\)، لكنه غير فعال بسبب الصفر الاستثنائي ومبرهنة Siegel.

### 3. Bombieri--Vinogradov — مؤجل

Bombieri--Vinogradov نتيجة متوسطية على الترديدات تصل تقريبًا إلى مستوى \(x^{1/2}\) بعد خسائر لوغاريتمية. تحتاج الغربال الكبير أو تقديرات كثافة الأصفار وآليات متوسطية غير مطلوبة لإثبات Siegel--Walfisz. لا تدخل في برهان الفصل الثاني عشر ولا تستعمل بوصفها اختصارًا دائريًا.

## سجل الادعاءات المقترحة

| المعرّف | الادعاء | الحالة الأولية | التصنيف المتوقع |
|---|---|---|---|
| `ANT-LEM-12-01` | رد \(\psi(x,\chi)\) للشخصية المستحثة إلى الجد البدائي مع خطأ \(O(\log q\log x)\) | `DRAFT` | `PROVED-HERE` |
| `ANT-THM-12-01` | مبرهنة الأعداد الأولية بحد de la Vallée Poussin الفعال للشخصية الرئيسية | `DRAFT` | `CITED` |
| `ANT-THM-12-02` | صيغة صريحة مقطوعة موحدة لـ\(\psi(x,\chi)\) للشخصيات البدائية | `DRAFT` | `CITED` |
| `ANT-LEM-12-02` | ضبط مجموع الأصفار غير الاستثنائية باختيار \(T=e^{\kappa\sqrt{\log x}}\) | `DRAFT` | `PROVED-HERE` |
| `ANT-LEM-12-03` | امتصاص حد الصفر الاستثنائي باستعمال Siegel في مجال \(q\le(\log x)^A\) | `DRAFT` | `PROVED-HERE / INEFFECTIVE` |
| `ANT-THM-12-03` | مبرهنة Siegel--Walfisz بصيغة \(\psi\) | `DRAFT` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-12-01` | الصيغة ذات الادخار اللوغاريتمي الاعتباطي | `DRAFT` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-12-02` | الصيغة الموحدة لـ\(\vartheta(x;q,a)\) | `DRAFT` | `PROVED-HERE` |
| `ANT-COR-12-03` | الصيغة الموحدة لـ\(\pi(x;q,a)\) | `DRAFT` | `PROVED-HERE` |

لا تسمح حالة `DRAFT` بالاستشهاد الخارجي، ولا تعني أن متن الفصل كتب.

## التبعيات الداخلية المؤكدة

- `ANT-COR-07-01`: تعامد شخصيات ديريشليه.
- `ANT-THM-07-04`: الجد البدائي والموصل.
- `ANT-PROP-07-03`: العوامل المحلية للشخصية المستحثة.
- `ANT-PROP-07-06`: المشتقة اللوغاريتمية ومتسلسلة فون مانغولت الملتوية.
- `ANT-PROP-10-01`: تفكيك دالة فون مانغولت في فئة مختزلة بواسطة الشخصيات.
- `ANT-THM-10-02`: PNT في المتتاليات الحسابية لترديد ثابت؛ للاستدلال المقارن فقط، لا للاشتقاق الموحد.
- `ANT-THM-11-01`: المنطقة القياسية الخالية مع الاستثناء الحقيقي الممكن.
- `ANT-THM-11-02`: فرادة Landau--Page النوعية.
- `ANT-THM-11-03`: مبرهنة Siegel، `CITED / INEFFECTIVE`.
- `ANT-COR-11-01`: الإبعاد غير الفعال \(1-\beta\gg_\varepsilon q^{-\varepsilon}\).
- `ANT-THM-11-04`: Deuring--Heilbronn؛ ليس لازمًا للمسار الكلاسيكي الأدنى للفصل، ويُذكر للمقارنة فقط.

## مسح Consensus الأولي

بدأ البحث عبر Consensus قبل بقية المصادر. أبرز سجل ذي صلة مباشرة:

- Jesse Thorner وAsif Zaman، **Refinements to the prime number theorem for arithmetic progressions**.
- أعاد Consensus سنة النسخة الأولية 2021؛ ثم تحقق سجل النشر النهائي من صفحة الناشر: *Mathematische Zeitschrift* 306 (2024)، المقالة 54.
- DOI: `10.1007/s00209-023-03414-3`.
- arXiv: `2108.10878`.
- تؤكد الورقة أن نتيجتها الموحدة تستنتج Siegel--Walfisz، وأن الأداة الحاسمة لامتصاص الصفر الاستثنائي هي مبرهنة Siegel غير الفعالة.

Consensus طبقة اكتشاف، وليست بديلًا عن المصدر الكامل أو صفحة الناشر.

## المصادر المرجعية الأساسية

### الكتب القياسية

1. Davenport، *Multiplicative Number Theory*، الطبعة الثالثة، 2000.
   - المصدر الكلاسيكي المركزي لمبرهنة Siegel، والصيغة الصريحة، وPNT في المتتاليات الحسابية، وSiegel--Walfisz.
   - يستعمل بوصفه مرجعًا للمسار الكلاسيكي، مع عدم ادعاء أن الموسوعة أغلقت براهين بيرون العامة في الفصل السادس.

2. Montgomery--Vaughan، *Multiplicative Number Theory I: Classical Theory*، 2007.
   - مرجع للصيغ الصريحة المقطوعة، وعد الأصفار، والمناطق الخالية، والتقديرات الموحدة.

3. Iwaniec--Kowalski، *Analytic Number Theory*، 2004.
   - مرجع لبنية الأصفار الاستثنائية، والمناطق الخالية، والتوزيع الموحد للأوليات.

4. Apostol، *Introduction to Analytic Number Theory*، 1976.
   - مرجع لبنية الشخصيات والتعامد والانتقال إلى \(\psi,\vartheta,\pi\).
   - ليس المرجع الوحيد للصيغة الكمية لـSiegel--Walfisz.

### مصادر أصلية وحديثة متحققة

1. C. L. Siegel، الورقة الأصلية لعام 1935 عن حد \(L(1,\chi)\).
   - أساس عدم الفعالية.
   - مسجلة في الفصل الحادي عشر ومراجعة هناك.

2. Dimitris Koukoulopoulos، “Pretentious multiplicative functions and the prime number theorem for arithmetic progressions”، *Compositio Mathematica* 149 (2013)، 1129--1149.
   - DOI: `10.1112/S0010437X12000802`.
   - يقدم برهانًا حديثًا مختلفًا لنتيجة قوية في PNT للمتتاليات الحسابية.
   - مرجع مقارن، وليس المسار الأساسي المعتمد في الفصل.

3. Jesse Thorner وAsif Zaman، “Refinements to the prime number theorem for arithmetic progressions”، *Mathematische Zeitschrift* 306 (2024)، المقالة 54.
   - DOI: `10.1007/s00209-023-03414-3`.
   - arXiv: `2108.10878`.
   - يعزل مساهمة الصفر الاستثنائي حدًا ثانويًا، ويبين أن Siegel--Walfisz ينتج في مجال الترديدات اللوغاريتمية بعد استعمال مبرهنة Siegel.

4. Sary Drappeau وDaniel Fiorilli، “The first moment of primes in arithmetic progressions: beyond the Siegel--Walfisz range”، *Transactions of the London Mathematical Society* 8 (2021).
   - DOI: `10.1112/tlm3.12030`.
   - مرجع لتوضيح أن تجاوز مجال Siegel--Walfisz المتوسطـي مسألة مختلفة تتأثر أيضًا بإمكان صفر Landau--Siegel.

## موضع استعمال مبرهنة Siegel

إذا كانت \(\beta\) صفرًا استثنائيًا لشخصية حقيقية بدائية موصلها \(r\mid q\)، فإن الصيغة الصريحة تعطي حدًا من الشكل

\[
-\frac{x^\beta}{\beta}.
\]

بعد مرشح الفئة يظهر في \(\psi(x;q,a)\) حد ثانوي

\[
-\frac{\chi(a)}{\varphi(q)}\frac{x^\beta}{\beta}.
\]

لا يجوز حذفه أو تسميته خطأً صغيرًا قبل استعمال Siegel. من

\[
1-\beta\gg_\varepsilon r^{-\varepsilon}
\]

وبما أن \(r\le q\le(\log x)^A\)، نختار مثلًا
\(\varepsilon=1/(2A)\)، فنحصل على

\[
(1-\beta)\log x
\gg_A
\sqrt{\log x},
\]

ومن ثم

\[
x^\beta
=x\exp(-(1-\beta)\log x)
\ll_A
xe^{-c_A\sqrt{\log x}}.
\]

هنا بالضبط تدخل عدم الفعالية: \(c_A\) غير فعال لأنه يعتمد على ثابت Siegel.

## ديون بيرون وتحويل المسار والصيغة الصريحة

- `ANT-THM-03-09`، صيغة بيرون العامة، ما تزال `DEFERRED`.
- الفصل السادس يسجل صيغة صريحة لزيتا بحالة `CITED`، لكنه لا يغلق مسار بيرون المقطوع وتحويل المسار كاملًا.
- لذلك لا يدعي الفصل الثاني عشر أنه أثبت الصيغة الصريحة المقطوعة من الصفر.
- المسار المعتمد يقتبس صيغة صريحة موحدة محددة بوصفها `ANT-THM-12-02 = CITED`، ثم يثبت داخل الفصل اختيار الارتفاع، وضبط الأصفار، وامتصاص الاستثناء، وتجميع الشخصيات.
- هذا القرار يمنع نقل دين قديم إلى برهان داخلي مزعوم.

## حدود النطاق

لا يدعي الفصل في مرحلته الحالية:

- فعالية ثابت Siegel--Walfisz العام.
- أفضل ثابت في الأس الأسي.
- مجال ترديدات من رتبة قوة موجبة لـ\(x\).
- Bombieri--Vinogradov أو Elliott--Halberstam.
- Linnik أو الفترات القصيرة.
- GRH.
- برهانًا جديدًا لمبرهنة Siegel.

## الحكم الأولي لسجل الأدلة

```text
CONSENSUS-FIRST          = PASS
PRIMARY-SOURCE-CHECK     = PASS
SCOPE-SEPARATION         = PASS
SIEGEL-USE-LOCATION      = IDENTIFIED
INEFFECTIVITY            = EXPLICIT
EXCEPTIONAL-ZERO         = ISOLATED-BEFORE-ABSORPTION
PERRON-DEBT              = DECLARED
EXPLICIT-FORMULA-ROUTE   = CITED-INPUT
AUTHORING                 = BLOCKED-PENDING-AUDITS
```