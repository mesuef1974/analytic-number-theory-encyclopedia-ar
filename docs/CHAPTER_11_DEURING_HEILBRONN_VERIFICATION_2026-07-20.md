# التحقق من ظاهرة Deuring--Heilbronn — الفصل الحادي عشر

## بيانات التحقق

```text
DATE                 = 2026-07-20
SCOPE                = ANT-THM-11-04
AUDIT-STATE          = PASS-FOR-CITED-QUALITATIVE-FORM
RESULT-REGISTRY      = REMAINS-DRAFT-UNTIL-AUTHORING
CHAPTER-AUTHORING     = BLOCKED
```

## 1. مجال الصياغة

لكل ترديد \(q\ge3\)، نعرف

\[
\mathscr L_q(s)
=
\prod_{\chi\pmod q}L(s,\chi),
\]

حيث يجري الضرب على جميع شخصيات ديريشليه بترديد \(q\).

نفترض أن \(\mathscr L_q\) تملك صفر Landau--Siegel الحقيقي البسيط

\[
\beta_1=1-\eta_1.
\]

بحسب المنطقة الصريحة القياسية لحاصل الضرب، يرتبط هذا الصفر بشخصية حقيقية تربيعية بترديد \(q\).

## 2. الصيغة النوعية المعتمدة

توجد ثوابت مطلقة فعالة موجبة

\[
c_0,c_1,c_2>0
\]

بحيث إذا كان \(T\ge2\)، و

\[
\lambda_1
=
(1-\beta_1)\log(q(T+2))
\le c_0,
\]

وكان

\[
\rho=\beta+i\gamma,
\qquad
|\gamma|\le T,
\qquad
\rho\ne\beta_1,
\]

صفرًا آخر لـ\(\mathscr L_q\)، فإن

\[
1-\beta
\ge
\frac{c_1}{\log(q(T+2))}
\log\!\left(\frac{c_2}{\lambda_1}\right).
\tag{2.1}
\]

بعد تصغير \(c_0\) عند الحاجة يكون اللوغاريتم موجبًا.

هذه ليست مطالبة بالثوابت المثلى ولا نقلًا حرفيًا لثوابت الورقة؛ إنها الصيغة النوعية الدقيقة المستخلصة من نسختها الصريحة.

```text
DEURING-HEILBRONN-SHAPE = VERIFIED
CONSTANTS                = ABSOLUTE / EFFECTIVE / NOT OPTIMIZED
```

## 3. معنى النتيجة

إذا اقترب \(\beta_1\) أكثر من \(1\)، صغرت \(\lambda_1\)، وكبر الحد

\[
\log(1/\lambda_1).
\]

ومن ثم تكبر المسافة الإلزامية بين بقية الأصفار والخط \(\Re(s)=1\).

هذا هو **تنافر الأصفار**، وهو أقوى من مجرد فرادة الصفر الاستثنائي.

## 4. الفرق عن Landau--Page

### Landau--Page

تمنع وجود شخصيتين بدائيتين مختلفتين لهما صفران حقيقيان شديدا القرب من \(1\) عبر الموصلات حتى \(Q\).

### Deuring--Heilbronn

تفترض وجود صفر استثنائي واحد، ثم تعطي حدًا كميًا محسنًا على **كل صفر آخر**، بما في ذلك الأصفار غير الحقيقية، ضمن نطاق الترديد والارتفاع المحددين.

إذن:

```text
LANDAU-PAGE        = UNIQUENESS
DEURING-HEILBRONN  = QUANTITATIVE-REPULSION
```

ولا يجوز عرض إحداهما بوصفها مرادفًا للأخرى.

## 5. المصدر الحديث المعتمد

- Kübra Benli, Shivani Goel, Henry Twiss, Asif Zaman.
- “Explicit Deuring--Heilbronn phenomenon for Dirichlet L-functions”.
- *Proceedings of the American Mathematical Society* 154 (2026), no. 2, 509--525.
- DOI: `10.1090/proc/17450`.
- arXiv:`2410.06082`, النسخة الثالثة بتاريخ 8 يناير 2026.

تثبت الورقة:

- نسخة صريحة فعالة موحدة في الشريط الحرج كله.
- تحسينًا للنسخة الصريحة السابقة لـThorner--Zaman.
- نسخة غير صريحة غير فعالة ذات ثوابت أفضل، باستعمال حد Siegel غير الفعال.

```text
BGTZ-BIBLIOGRAPHY = VERIFIED
EXPLICIT-VERSION  = EFFECTIVE
IMPROVED-VERSION  = INEFFECTIVE
```

## 6. النسخة الفعالة والنسخة غير الفعالة

يجب الفصل في المتن بين:

### النسخة الفعالة

- ثوابتها قابلة للحساب.
- أضعف عدديًا من بعض النسخ غير الفعالة.
- مناسبة للتطبيقات الصريحة.

### النسخة غير الفعالة

- تستعمل مبرهنة Siegel.
- تعطي ثوابت أو أسسًا أفضل.
- ترث عدم فعالية ثابت Siegel.

يحظر أخذ أفضل ثابت من النسخة الثانية ووصف النتيجة بأنها فعالة.

## 7. درجة الاعتماد في الموسوعة

البرهان الحديث يستعمل:

- تقديرات نمو أو دون تحدب لدوال \(L\).
- مجاميع مولّفة تكشف الأصفار.
- غربال Selberg وأوزانًا محسنة.
- مقارنة حدين متنافسين يتأثر أحدهما بالصفر الاستثنائي.

هذه البنية تتجاوز الأدوات المثبتة حتى الفصل العاشر. لذلك يكون القرار:

```text
ANT-THM-11-04 = CITED
PROOF-IN-CHAPTER = EXPLANATORY-SKETCH-ONLY
FULL-PROOF        = DEFERRED
```

لا يُسجل أي جزء من البرهان العميق على أنه `PROVED-HERE`.

## 8. عدم الدور

في ترتيب الفصل:

1. تثبت المنطقة القياسية أولًا.
2. تثبت Landau--Page ثانيًا.
3. تقتبس مبرهنة Siegel مع وسم عدم الفعالية.
4. تقتبس Deuring--Heilbronn أخيرًا.

لا تستعمل Deuring--Heilbronn لإثبات المنطقة القياسية أو Landau--Page داخل الموسوعة.

```text
DEPENDENCY-ORDER = PASS
CIRCULARITY      = PASS
```

## 9. حدود الادعاء

لا يدعي الفصل في نسخته الأساسية:

- ثوابت Corollary 1.1 العددية الكاملة.
- أفضل معلمات النسخة غير الفعالة.
- البرهان الكامل بغربال Selberg.
- التعميم إلى دوال Hecke أو Rankin--Selberg.
- تطبيق Linnik الكامل.
- Siegel--Walfisz أو Bombieri--Vinogradov.

## 10. الحكم النهائي

```text
ANT-THM-11-04 SOURCE       = VERIFIED
ANT-THM-11-04 STATUS       = CITED
QUALITATIVE-STATEMENT      = PASS
EFFECTIVITY-SEPARATION     = PASS
LANDAU-PAGE-SEPARATION     = PASS
FULL-PROOF                 = DEFERRED
RESULT-STATUS              = DRAFT-UNTIL-AUTHORING
PRE-AUTHORING-GATE         = OPEN
CHAPTER-AUTHORING           = BLOCKED
```

## 11. الإجراء التالي

إصدار تدقيق منطقي شامل يجمع:

- المنطقة القياسية الفردية.
- بساطة وواقعية الاستثناء.
- Landau--Page.
- مبرهنة Siegel وعدم الفعالية.
- Deuring--Heilbronn المقتبسة.
- فحص عدم الدور وترتيب الاعتمادات.

إذا صدر الحكم `PASS`، تُغلق بوابة ما قبل التأليف ويصبح إنشاء متن الفصل مصرحًا.