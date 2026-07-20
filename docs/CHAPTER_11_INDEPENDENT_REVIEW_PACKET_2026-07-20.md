# حزمة المراجعة المستقلة للفصل الحادي عشر

## بيانات النسخة المرشحة

```text
DATE                     = 2026-07-20
CHAPTER                  = 11 — المناطق الخالية من الأصفار والأصفار الاستثنائية
VERSION                  = 0.15.0-dev
MATHEMATICAL-CONTENT-HEAD = c7f6e8dca491cdb408ae8bcffea14baf7eac979c
QUALITY-CHECKS           = RUN-246 / SUCCESS
PDF-BUILD                = RUN-242 / SUCCESS
CHAPTER-STATUS           = VERIFIED
REVIEW-STATUS            = REQUESTED / NOT YET RECEIVED
PR-17                    = DRAFT / UNMERGED
MERGE                    = NOT AUTHORIZED
```

## المطلوب من المراجع

يرجى إجراء مراجعة مستقلة كاملة للنص، لا مراجعة شكلية، مع التركيز على صحة
العبارات والبراهين، وسلامة الاعتمادات، وعدم الدور، ودقة الفصل بين النتائج
الفعالة وغير الفعالة.

## الملفات الأساسية

1. متن الفصل:
   `volumes/volume-01-foundations/chapters/chapter-11-zero-free-regions-exceptional-zeros.tex`
2. سجل الأدلة:
   `research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-evidence.md`
3. خريطة البرهان:
   `research/literature-reviews/chapter-11-zero-free-regions-exceptional-zeros-proof-map.md`
4. تدقيق ما قبل التأليف:
   `docs/CHAPTER_11_PRE_AUTHORING_AUDIT_2026-07-20.md`
5. التدقيق المنطقي الشامل:
   `docs/CHAPTER_11_LOGIC_AUDIT_2026-07-20.md`
6. تدقيق ما بعد التأليف:
   `docs/CHAPTER_11_AUTHORING_AUDIT_2026-07-20.md`
7. سجل النتائج:
   `docs/RESULTS_REGISTRY.md`

## النتائج المطلوب فحصها

```text
ANT-PROP-11-01 = PROVED-HERE
ANT-LEM-11-01  = PROVED-HERE
ANT-THM-11-01  = PROVED-HERE
ANT-THM-11-02  = PROVED-HERE
ANT-THM-11-03  = CITED / INEFFECTIVE
ANT-COR-11-01  = PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-THM-11-04  = CITED
ANT-PROP-11-02 = DEFERRED / DIAGNOSTIC
```

## قائمة الفحص الرياضية

### أ. الرد إلى الجد البدائي

- [ ] صحة صيغة العوامل المحلية للشخصية المستحثة.
- [ ] صحة عدم انعدام العوامل المحلية في \(\Re(s)>0\).
- [ ] صحة حد \(O(\log q)\) للمشتقة اللوغاريتمية.

### ب. صيغة المشتقة اللوغاريتمية

- [ ] صحة استعمال جداء هادامار للدالة المكتملة.
- [ ] صحة التخلص من الجزء الحقيقي للثابت المنتظم.
- [ ] صحة إشارة مساهمة الصفر في \(-\Re L'/L\).
- [ ] صحة نطاق الجمع المتماثل على الأصفار.

### ج. المنطقة القياسية

- [ ] صحة تقدير عامل غاما والموصل والعوامل المحلية.
- [ ] صحة المتراجحة الموزونة ذات المعاملات \(3,4,1\).
- [ ] صحة استبعاد الشخصية غير الحقيقية.
- [ ] صحة معالجة حالة الشخصية الحقيقية والصفر غير الحقيقي.
- [ ] التأكد من إبقاء الصفر المرافق وقطب \(\chi^2\) الرئيسي معًا.
- [ ] صحة المتراجحة في المتغيرين \(r,v\).
- [ ] صحة إثبات بساطة الصفر الحقيقي وفرادته داخل الدالة.
- [ ] صحة توصيف الشخصية الاستثنائية بأنها حقيقية تربيعية.

### د. Landau--Page

- [ ] صحة أن حاصل ضرب الشخصيتين غير رئيسي عند تميزهما البدائي.
- [ ] صحة إبقاء شخصية حاصل الضرب غير البدائية في خطوة الموجبية.
- [ ] صحة الهوية
  \((1+\chi_1(n))(1+\chi_2(n))\ge0\).
- [ ] صحة ضبط موصل الجد البدائي بحد \(Q^2\).
- [ ] صحة المتراجحة النهائية واختيار الثوابت.

### هـ. Siegel وعدم الفعالية

- [ ] صحة نص مبرهنة Siegel وافتراضاتها.
- [ ] صحة وسمها `CITED` وعدم ادعاء برهان داخلي.
- [ ] صحة شرح معنى عدم الفعالية.
- [ ] صحة حد \(|L'(\sigma,\chi)|\ll\log^2 q\) قرب الواحد.
- [ ] صحة الاشتقاق إلى
  \(1-\beta\gg_\varepsilon q^{-\varepsilon}\).
- [ ] التأكد من أن الثابت المشتق موسوم غير فعال.

### و. Deuring--Heilbronn

- [ ] صحة الصيغة النوعية المقتبسة.
- [ ] صحة تطبيع \((1-\beta_1)\log(q(T+2))\).
- [ ] صحة الفصل بين النسخة الفعالة وغير الفعالة.
- [ ] عدم الخلط بين تنافر الأصفار وفرادة Landau--Page.
- [ ] عدم ادعاء البرهان الكامل.

### ز. عدم الدور والحدود

- [ ] عدم استعمال Siegel--Walfisz أو Bombieri--Vinogradov أو Linnik.
- [ ] عدم استعمال Deuring--Heilbronn لإثبات المنطقة القياسية.
- [ ] عدم استعمال Siegel لإثبات Landau--Page.
- [ ] عدم استعمال GRH.
- [ ] صحة إبقاء الصيغة الصريحة الكاملة لـ\(\psi(x,\chi)\) مؤجلة.

## المراجع المركزية

- Davenport, *Multiplicative Number Theory*.
- Montgomery--Vaughan, *Multiplicative Number Theory I*.
- Iwaniec--Kowalski, *Analytic Number Theory*.
- McCurley (1984), explicit zero-free regions.
- Kadiri (2018), explicit improvements.
- Siegel (1935), class-number theorem and ineffective lower bound.
- Liu (2022), modern proof of Siegel's theorem.
- Benli--Goel--Twiss--Zaman (2026), explicit Deuring--Heilbronn phenomenon.
- Basak--Pratt (2026), modern discussion of Page's theorem.

## نموذج الحكم

يرجى إرجاع أحد الأحكام الآتية:

```text
APPROVED
APPROVED-WITH-NONBLOCKING-CORRECTIONS
CHANGES-REQUIRED
REJECTED
```

مع تضمين:

1. الأخطاء الرياضية الحاجزة، إن وجدت.
2. التصحيحات غير الحاجزة.
3. النتائج التي فحصت مباشرة.
4. حدود المراجعة، ولا سيما ما إذا كانت تبعيات الفصلين السابع والعاشر قد
   أعيدت مراجعتها أو اعتبرت مدخلات معتمدة.
5. تصريح واضح بشأن صحة الفصل بين الفعالية وعدم الفعالية.

## قرار الحوكمة

لا يرتفع الفصل إلى `REVIEWED`، ولا يدمج PR #17، قبل استلام حكم مستقل
مكتوب وتسجيله في المستودع. نجاح الفحوص الداخلية لا يحسب مراجعة مستقلة.