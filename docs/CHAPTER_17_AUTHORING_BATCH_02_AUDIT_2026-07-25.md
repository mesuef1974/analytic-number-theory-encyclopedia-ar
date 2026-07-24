# تدقيق دفعة التأليف الثانية — الفصل السابع عشر

التاريخ: 2026-07-25

```text
CHAPTER                 = 17
AUTHORING-BATCH          = 02
SCOPE                    = WARING STRUCTURE / REFERENCES / LOCAL-ARCHIMEDEAN FACTORS
CHAPTER-TEX              = UPDATED
BIBLIOGRAPHY             = ADDED AND REGISTERED
MATHEMATICAL-AUDIT       = INITIAL PASS WITH OPEN ITEMS
REFERENCE-AUDIT          = INITIAL PASS
PDF-BUILD                = NOT YET RUN
REVIEWED                 = NO
MERGE                    = NOT AUTHORIZED
RELEASE-READY            = NO
```

## 1. ما أضيف

- تعريف مجموع القوى الكامل
  \[
  S_k(q,a)=\sum_{r=1}^{q}e(ar^k/q).
  \]
- تعريف التقريب الأرخميدي
  \[
  v_k(\beta;P)=\int_0^P e(\beta t^k)\,dt.
  \]
- صيغة صريحة مرشحة للسلسلة المفردة `𝔖_{s,k}(N)`.
- صيغة صريحة مرشحة للتكامل المفرد `𝔍_{s,k}(N)`.
- تفسير رتبة الحجم
  \[
  P^{s-k}=N^{s/k-1}.
  \]
- إدراج معرفات النتائج وشارات التصنيف داخل المتن.
- إدراج إحالات إلى Hardy--Littlewood وVaughan وVinogradov وHelfgott.
- إنشاء `manuscript/chapter-17-bibliography.bib` وربطه بـ`preamble.tex`.

## 2. التدقيق الرياضي الأولي

### PASS

- هوية التعامد صحيحة مع التطبيع `e(t)=exp(2πit)`.
- هوية عد التمثيلات صحيحة لأن الأوزان ذات دعم منتهٍ.
- تقسيم الدائرة هوية دقيقة.
- رتبة التكامل المفرد متسقة أبعاديًا مع `P=N^{1/k}`.
- تقدير الأقواس الصغرى مصنف `CITED / COMPOSITE INPUT` ولا ينسب إلى الفصل بوصفه نتيجة داخلية.
- مبرهنتا فينوغرادوف وهلفغوت مصنفتان `CITED`.
- غولدباخ الثنائية مصنفة `HYPOTHESIS / OPEN`.

### OPEN ITEMS

1. بناء PDF محلي للتحقق من سلامة مفاتيح BibTeX والبيئات الرياضية.
2. تدقيق اصطلاح `x_j∈ℕ`: هل يشمل الصفر في بقية الموسوعة؟ ينبغي توحيده أو استبداله بـ`x_j≥1`.
3. مراجعة الصيغة الدقيقة للتكامل المفرد إذا اختير لاحقًا فصل عامل القياس الصريح عن `𝔍_{s,k}(N)`.
4. تدقيق شروط تقارب السلسلة المفردة وإيجابيتها عند عرضها كقضية كاملة؛ النص الحالي يعرض البنية فقط.
5. لا تزال قضية الأقواس الكبرى `AUTHORED-DRAFT` وليست `PROVED-HERE` كاملة.

## 3. التدقيق المرجعي الأولي

المفاتيح المضافة:

```text
HardyLittlewood1922Waring
HardyLittlewood1923Goldbach
Vinogradov1937ThreePrimes
Vaughan1997HardyLittlewood
Helfgott2015TernaryGoldbach
```

الحكم:

```text
BIBLIOGRAPHIC-METADATA = INITIAL PASS
IN-TEXT-CITATIONS      = PRESENT
UNDEFINED-CITATIONS    = NOT TESTED UNTIL BUILD
```

## 4. الحكم

```text
AUTHORING-BATCH-02     = COMPLETE-AS-DRAFT
MATHEMATICAL-BLOCKERS  = 0 FATAL / 4 AUDIT ITEMS
REFERENCE-BLOCKERS     = 0 FATAL / BUILD VERIFICATION PENDING
NEXT                    = LOCAL BUILD + POST-AUTHORING CORRECTIONS
```

لا تمنح هذه الوثيقة حالة `VERIFIED` أو `REVIEWED`، ولا تجيز الدمج.
