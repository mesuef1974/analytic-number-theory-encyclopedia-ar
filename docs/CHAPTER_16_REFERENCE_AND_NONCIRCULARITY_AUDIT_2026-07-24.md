# تدقيق المراجع وعدم الدور للفصل السادس عشر

آخر تحديث: 2026-07-24

```text
CHAPTER                    = 16
VERSION                    = 0.20.0-dev
BRANCH                     = agent/chapter-16-sieve-applications-prime-gaps-v0.20.0
REFERENCE-AUDIT            = PARTIAL-PASS
NONCIRCULARITY-AUDIT       = PASS
MATHEMATICAL-BLOCKERS      = 0
REFERENCE-BLOCKERS         = 1
PRE-AUTHORING-GATE         = OPEN
AUTHORING                  = BLOCKED
PASS-FOR-AUTHORING         = NO
```

## 1. نتيجة تدقيق عدم الدور

يجتاز المسار المقترح تدقيق عدم الدور بشرط تثبيت التقسيم الآتي:

1. الفصل 13 يقدّم Bombieri--Vinogradov وأدوات التوزيع في المتتاليات الحسابية.
2. الفصل 15 يقدّم الحد العلوي المنتهي لغربال سيلبرغ، البعد الغربالي، واللمّة الأساسية بوصفها مدخلًا مقتبسًا، ثم يشرح عائق التكافؤ.
3. الفصل 16 لا يعيد إثبات Bombieri--Vinogradov ولا يعيد بناء غربال سيلبرغ الأحادي؛ بل يستعملهما مدخلين سابقين مصرحًا بهما.
4. نتيجة GPY تُعرض بوصفها نتيجة مقتبسة عن الفجوات الصغيرة نسبةً إلى المتوسط، لا كنتيجة تابعة تلقائيًا للفصل 15.
5. مسار Zhang يستعمل مدخل توزيع أقوى للمقامات الملساء، ولذلك لا يجوز رده إلى Bombieri--Vinogradov الكلاسيكي وحده.
6. مسار Maynard--Tao يغير بنية الوزن إلى وزن متعدد الأبعاد، ولذلك لا يجوز عرضه كإعادة تسمية لأوزان الفصل 15.
7. تحسين Polymath8b للثابت العددي والحدود على H_m نتيجة مقتبسة مستقلة، لا جزء من برهان الفصل 15.

الحكم:

```text
DEPENDENCY-DAG = ACYCLIC
NONCIRCULARITY = PASS
```

## 2. المراجع الأصلية المغلقة

### 2.1 GPY

المصدر الأصلي المختار:

- D. A. Goldston, J. Pintz, C. Y. Yıldırım,
  *Primes in tuples I*, Annals of Mathematics 170 (2009), 819--862.

النتيجة التي ستدخل الفصل:

\[
\liminf_{n\to\infty}
\frac{p_{n+1}-p_n}{\log p_n}=0.
\]

التصنيف: `CITED / PRIMARY-SOURCE-VERIFIED`.

### 2.2 Zhang

المصدر الأصلي المختار:

- Yitang Zhang,
  *Bounded gaps between primes*, Annals of Mathematics 179 (2014), 1121--1174.

النتيجة التاريخية في الورقة الأصلية:

\[
\liminf_{n\to\infty}(p_{n+1}-p_n)<7\times 10^7.
\]

التصنيف: `CITED / PRIMARY-SOURCE-VERIFIED`.

### 2.3 Maynard

المصدر الأصلي المختار:

- James Maynard,
  *Small gaps between primes*, Annals of Mathematics 181 (2015), 383--413.

النتائج المختارة:

- محدودية \(H_m\) لكل \(m\ge1\).
- الحد التاريخي \(H_1\le600\) في النسخة الأصلية.
- الوزن متعدد الأبعاد بوصفه الآلية المركزية.

التصنيف: `CITED / EXPLAINED / PRIMARY-SOURCE-VERIFIED`.

### 2.4 Polymath8b

المصدر المنشور المختار:

- D. H. J. Polymath,
  *Variants of the Selberg sieve, and bounded intervals containing many primes*,
  Research in the Mathematical Sciences 1 (2014), Article 12, 1--83.

النتائج المختارة:

\[
H_1\le246
\]

دون شرط، و

\[
H_1\le6
\]

تحت فرضية Elliott--Halberstam المعممة، مع التصريح بأن هذه نتيجة مشروطة.

التصنيف: `CITED / PRIMARY-SOURCE-VERIFIED`.

### 2.5 Chen

المصدر الأصلي المثبت:

- Jing-Run Chen,
  *On the representation of a larger even integer as the sum of a prime and the product of at most two primes*,
  1973, vol. 16, pp. 157--176.

الصياغة المعتمدة:

> كل عدد زوجي كبير بما يكفي هو مجموع عدد أولي وعدد له على الأكثر عاملان أوليان، مع العد وفق اصطلاح \(P_2\) الذي يجب تعريفه صراحة في الفصل.

كما ستذكر النتيجة المرافقة عن وجود عدد لا نهائي من الأوليات \(p\) التي يكون فيها \(p+2=P_2\) فقط إذا ثُبت موضعها النصي في المصدر المستخدم.

التصنيف: `CITED / PRIMARY-SOURCE-VERIFIED` للنتيجة الجمعية الأساسية.

## 3. قرار مرجع Tao

لم يُعثر في البحث الببليوغرافي على ورقة مستقلة محكمة لتاو تمثل مرجعًا أوليًا موازيًا لورقة Maynard في النتيجة المركزية نفسها. لذلك يعتمد الفصل السياسة التالية:

```text
TAO-INDEPENDENT-PAPER = NOT REQUIRED
MAYNARD               = PRIMARY TECHNICAL SOURCE
POLYMATH8B             = PRIMARY JOINT EXTENSION SOURCE
TAO CREDIT             = HISTORICAL / INDEPENDENT-DEVELOPMENT CREDIT
```

يُذكر التطوير المستقل لتاو تاريخيًا مع إسناد مناسب، لكن البرهان والصيغ المنشورة تُوثق من Maynard وPolymath8b.

## 4. برون

النتيجة التعليمية المرشحة هي تقارب مجموع مقلوبات الأوليات التوأم، ويمكن إثباتها داخل الفصل انطلاقًا من حد علوي من رتبة

\[
\pi_2(x)\ll \frac{x}{(\log x)^2}
\]

ثم الجمع الجزئي. بذلك تكون النتيجة الرياضية `PROVED-HERE` اعتمادًا على حد علوي غربالي سابق، بينما تبقى نسبة الأولوية التاريخية إلى Brun `CITED-HISTORICAL`.

لم يُغلق بعد موضع ببليوغرافي أولي موثوق للورقة الأصلية التي ستُستخدم لنسبة الأولوية التاريخية. لا يمنع هذا بناء خريطة البرهان، لكنه يمنع إغلاق بوابة ما قبل التأليف.

```text
BRUN-MATHEMATICAL-ROUTE = PROVED-HERE
BRUN-HISTORICAL-CITATION = PENDING-PRIMARY-BIBLIOGRAPHY
```

## 5. مصفوفة النتائج المقترحة

| النتيجة | التصنيف | الاعتماد |
|---|---|---|
| حد عدّ الأزواج الأولية من الأعلى | `PROVED-HERE` أو `REUSED-FROM-CH15` | الفصل 15 |
| تقارب مجموع برون | `PROVED-HERE` | الحد السابق + الجمع الجزئي |
| مبرهنة تشن الجمعية | `CITED` | Chen 1973 |
| نتيجة GPY النسبية | `CITED` | GPY 2009 |
| مبرهنة Zhang التاريخية | `CITED` | Zhang 2014 |
| مبرهنة Maynard العامة | `CITED / EXPLAINED` | Maynard 2015 |
| الحد H_1<=246 | `CITED` | Polymath8b 2014 |
| أي ادعاء بأن H_1=2 | `OPEN / PROHIBITED` | حدسية الأوليات التوأم |

## 6. الحكم الحالي

```text
PRIMARY-SOURCE-AUDIT      = PASS EXCEPT BRUN HISTORICAL LOCATION
NONCIRCULARITY-AUDIT      = PASS
REFERENCE-BLOCKERS        = 1
AUTHORING                  = BLOCKED
PASS-FOR-AUTHORING         = NO
NEXT-ACTION                = CLOSE BRUN PRIMARY BIBLIOGRAPHY
```
