# المراجعة المستقلة للفصل الحادي عشر

## بيانات المراجعة

```text
DATE                 = 2026-07-20
CHAPTER              = 11 — المناطق الخالية من الأصفار والأصفار الاستثنائية
REVIEW-BRANCH        = review/chapter-11-zero-free-regions-exceptional-zeros-rc1
FROZEN-REVIEW-HEAD   = 617549dfd76cd2582c85217d39fab94ffaad1a9f
REVIEW-SCOPE         = FULL-CHAPTER / PROOFS / DEPENDENCIES / REFERENCES / EFFECTIVITY
VERDICT              = APPROVED-WITH-BLOCKING-BIBLIOGRAPHIC-CORRECTION
MATHEMATICAL-ERRORS  = NONE FOUND
BLOCKING-CORRECTION  = BASAK-PRATT-METADATA
```

## الحكم العام

البراهين الرياضية المنجزة داخل الفصل سليمة. لم تكشف المراجعة خطأ في
المنطقة القياسية، أو مبرهنة Landau--Page، أو حد المشتقة قرب الواحد، أو
الإبعاد غير الفعال للصفر الاستثنائي. كما وجدت المراجعة أن الفصل بين
النتائج الفعالة وغير الفعالة واضح وأمين.

كشفت المراجعة خطأ ببليوغرافيا صريحا في مدخل `BasakPratt2026`: اسم المؤلف
الأول كان مسجلا `Soham Basak`، والصحيح `Debmalya Basak`. كما كان المدخل
يسجل الورقة بوصفها preprint فقط، مع أنها منشورة في *Research in Number
Theory*، المجلد 12، العدد 1، المقالة 17 (2026).

أثر الخطأ منخفض رياضيا لأن المرجع مستعمل في ملاحظة سياقية، لا بوصفه حاملا
لبرهان. لكنه تصحيح حاجز أمام رفع الفصل إلى `REVIEWED` لأنه خطأ في اسم علم
وبيانات النشر.

## منهج المراجعة

شملت المراجعة:

1. قراءة متن الفصل كاملا.
2. إعادة اشتقاق المتراجحات في النتائج المثبتة داخليا.
3. تدقيق الاعتمادات على الفصلين السابع والعاشر.
4. فحص الماكروهات ومعرفات النتائج والعلامات المرجعية.
5. تدقيق الاستشهادات الحديثة على arXiv وصفحات الناشرين.
6. فحص الفصل بين الفعالية وعدم الفعالية وعدم ادعاء نتائج تتجاوز النطاق.

## النتائج الرياضية المدققة

### `ANT-PROP-11-01`

صيغة الرد إلى الجد البدائي صحيحة. العوامل المحلية لا تنعدم في
\(\Re(s)>0\)، والفرق بين المشتقتين اللوغاريتميتين مضبوط بـ

\[
\sum_{p\mid q}\log p
=
\log\operatorname{rad}(q)
\le
\log q.
\]

```text
ANT-PROP-11-01 = PASS
```

### `ANT-LEM-11-01`

اشتقاق صيغة المشتقة اللوغاريتمية من جداء هادامار صحيح، وإشارة مساهمة كل
صفر في \(-\Re L'/L\) صحيحة. العبارة التي تجعل
\(\Re b_\chi=0\) تعتمد على المعادلة الوظيفية وتناظر الأصفار، وهي صحيحة؛
وإضافة إسناد صريح لها تحسين غير حاجز.

```text
ANT-LEM-11-01 = PASS
```

### `ANT-THM-11-01`

راجعت المراجعة الحالات الثلاث:

- الشخصية غير الحقيقية.
- الشخصية الحقيقية مع صفر غير حقيقي.
- الصفر الحقيقي وبساطته وفرادته داخل الدالة.

تحققت المراجعة من

\[
G(r,v)
=
3+
\frac1{1+v^2}
-
\frac4r
-
\frac{4r}{r^2+v^2},
\]

ومن

\[
G(1,v)\le-1,
\qquad
\left|\frac{\partial G}{\partial r}\right|
\le8.
\]

كما تحققت من أن حالة الرتبة الكلية \(\ge2\) تعطي الحد
\(-4/(3\delta)\) بعد طرح مساهمة الأصفار من القطبين.

```text
ANT-THM-11-01 = PASS
```

### `ANT-THM-11-02`

برهان Landau--Page صحيح: معاملات حاصل الضرب غير سالبة بسبب

\[
(1+\chi_1(n))(1+\chi_2(n))\ge0,
\]

ورد شخصية حاصل الضرب إلى جدها البدائي يضيف كلفة لا تتجاوز
\(O(\log Q)\)، لأن الموصل لا يتجاوز \(Q^2\). والمتراجحة النهائية

\[
\frac1A-
\frac2{A+c}+C<0
\]

تغلق الحجة باختيار الثوابت بالترتيب الصحيح.

```text
ANT-THM-11-02 = PASS
```

### حد المشتقة و`ANT-COR-11-01`

حد

\[
|L'(\sigma,\chi)|
\ll
\log^2(2q)
\]

قرب الواحد صحيح من الدورية والجمع الجزئي. ومنه، مع مبرهنة Siegel بالأس
\(\varepsilon/2\):

\[
1-\beta
\gg_\varepsilon
q^{-\varepsilon}.
\]

وقد وسم الفصل الثابت المشتق بأنه غير فعال، وهو الوسم الصحيح.

```text
DERIVATIVE-BOUND = PASS
ANT-COR-11-01    = PASS / INEFFECTIVE-CONSTANT
```

### النتائج المقتبسة

- صيغة مبرهنة Siegel صحيحة وموسومة `CITED / INEFFECTIVE`.
- صيغة Deuring--Heilbronn شرطية بوجود صفر Landau--Siegel، وموسومة
  `CITED`، مع فصل صحيح بين النسخة الفعالة والنسخة غير الفعالة.
- `ANT-PROP-11-02` مؤجلة بحق إلى فصل الصيغة الصريحة الكمية.

```text
ANT-THM-11-03  = PASS-FOR-CITATION
ANT-THM-11-04  = PASS-FOR-CITATION
ANT-PROP-11-02 = PASS-AS-DEFERRED
```

## التحقق المرجعي

### مراجع صحيحة

- Siegel (1935), *Acta Arithmetica* 1, 83--86.
- Liu, arXiv:2202.00635، بوصفه preprint حديثا.
- McCurley (1984).
- Kadiri (2018).
- Benli--Goel--Twiss--Zaman، *Proceedings of the American Mathematical
  Society* 154 (2026), no. 2, 509--525، DOI `10.1090/proc/17450`،
  arXiv:2410.06082.

### التصحيح الحاجز

المدخل الصحيح لورقة Basak--Pratt هو:

```text
AUTHORS  = Debmalya Basak; Kyle Pratt
TITLE    = A Conditional Refinement of Page's Theorem on Zeros of Dirichlet L-Functions
JOURNAL  = Research in Number Theory
VOLUME   = 12
NUMBER   = 1
ARTICLE  = 17
YEAR     = 2026
DOI      = 10.1007/s40993-025-00695-x
ARXIV    = 2607.06433
```

## الاعتمادات والنظافة

- `ANT-PROP-07-03` و`ANT-LEM-10-01` موجودان.
- الماكروهات `resultid` و`provedhere` و`citedresult` و`deferredresult`
  معرفة.
- لا محارف تحكم أو محارف فارسية حاجزة في النص المراجع.
- النطاق منضبط: لا أفضل ثابت، ولا برهان كامل لـDeuring--Heilbronn، ولا
  Siegel--Walfisz أو Bombieri--Vinogradov أو Linnik أو GRH.

## تحسينات غير حاجزة

1. إضافة إسناد أو سطر توضيحي لهوية \(\Re b_\chi=0\).
2. إبقاء معرف arXiv:2410.06082 في مدخل الورقة المنشورة.
3. وصف Liu (2022) صراحة بوصفه preprint.
4. تذكير القارئ بأن المنطقة تمتد إلى الشخصيات غير البدائية بواسطة
   `ANT-PROP-11-01`.

## قرار البوابة

```text
MATHEMATICAL-REVIEW = APPROVED
REFERENCE-REVIEW    = APPROVED-AFTER-BASAK-PRATT-CORRECTION
CHAPTER-11          = MAY-ADVANCE-TO-REVIEWED-AFTER-CORRECTION-AND-CI
MERGE               = NOT AUTHORIZED
RELEASE-READY       = NO
```

لا يحتاج المتن الرياضي إلى تعديل حاجز. بعد تطبيق التصحيح الببليوغرافي
ونجاح فحوص الجودة وبناء PDF، يجوز رفع الفصل إلى `REVIEWED` وإغلاق Issue
#18، مع إبقاء PR #17 غير مدمج حتى أمر صريح من مالك المشروع.
