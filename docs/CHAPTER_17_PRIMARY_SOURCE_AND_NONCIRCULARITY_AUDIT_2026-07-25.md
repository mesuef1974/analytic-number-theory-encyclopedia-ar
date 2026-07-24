# تدقيق المصادر الأولية وعدم الدور — الفصل السابع عشر

التاريخ: 2026-07-25

```text
CHAPTER                  = 17
AUDIT-SCOPE              = PRIMARY SOURCES / ATTRIBUTION / DEPENDENCIES
VERDICT                  = PASS-FOR-RESEARCH-INTAKE
PASS-FOR-AUTHORING       = NO
AUTHORING                = BLOCKED
REFERENCE-BLOCKERS       = 3
CIRCULARITY-BLOCKERS     = 0
```

## 1. المصادر الأولية التي ثبتت بياناتها

### هاردي–ليتلوود وغولدباخ

1. G. H. Hardy and J. E. Littlewood,
   *Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes*,
   *Acta Mathematica* 44 (1923), 1–70,
   DOI `10.1007/BF02403921`.

2. G. H. Hardy and J. E. Littlewood,
   *Some Problems of “Partitio Numerorum” (V): A Further Contribution to the Study of Goldbach's Problem*,
   *Proceedings of the London Mathematical Society* s2-22 (1924), 46–56,
   DOI `10.1112/plms/s2-22.1.46`.

### هاردي–ليتلوود ووارينغ

3. G. H. Hardy and J. E. Littlewood,
   *Some problems of “Partitio Numerorum”: IV. The singular series in Waring's Problem and the value of the number G(k)*,
   *Mathematische Zeitschrift* 12 (1922), 161–188.

4. G. H. Hardy and J. E. Littlewood,
   *Some Problems of “Partitio Numerorum” (VIII): The Number Γ(k) in Waring's Problem*,
   *Proceedings of the London Mathematical Society* s2-28 (1928), 518–542,
   DOI `10.1112/plms/s2-28.1.518`.

### فينوغرادوف

5. I. M. Vinogradov,
   *Representation of an odd number as the sum of three primes*,
   *Doklady Akademii Nauk SSSR* 15 (1937), 129–132.

بيانات المصدر الخامس مثبتة مبدئيًا، لكن يلزم فحص نسخة رقمية موثوقة أو ترجمة منشورة قبل نسبة صياغة كمية دقيقة إليه.

## 2. ما الذي تثبته المصادر وما الذي لا تثبته تلقائيًا

- ورقة Hardy–Littlewood III تؤسس المعالجة التحليلية لمسائل جمع الأوليات وتقدم صيغًا تنبؤية؛ لا يجوز تحويل نتائجها المشروطة أو الحدسية إلى مبرهنات حديثة غير مشروطة.
- ورقة Hardy–Littlewood IV مصدر أصلي للسلسلة المفردة في مسألة وارينغ، لكنها لا تعفي الفصل من تدقيق التطبيع الحديث والتقارب والإيجابية.
- ورقة Vinogradov هي مصدر تاريخي لمبرهنة الثلاثة أوليات للأعداد الفردية الكبيرة بما يكفي؛ لا يجوز الادعاء منها مباشرة بأن كل عدد فردي أكبر من 5 ممثل من دون إدخال نتيجة Helfgott الحديثة والتحقق منها مستقلًا.
- نتيجة غولدباخ الثنائية تبقى `OPEN`، وصيغة عدد التمثيلات تبقى `HYPOTHESIS` ما لم يذكر نطاق مبرهن مثبت بدقة.

## 3. تدقيق عدم الدور

### الفصول السابقة

- الفصل 10: يسمح بتوزيع الأوليات في المتتاليات لترديد ثابت.
- الفصل 11: يسمح بالمناطق الخالية والأصفار الاستثنائية وفق صيغته المعتمدة.
- الفصل 12: يسمح بـSiegel–Walfisz في المجال اللوغاريتمي.
- الفصل 13: يسمح بـBombieri–Vinogradov.
- الفصل 14: يسمح بـBarban–Davenport–Halberstam.
- الفصل 15: يقدم حدودًا غربالية، لكنها لا تنتج تقديرات الأقواس الصغرى.
- الفصل 16: يقدم تطبيقات غربالية وفجوات أولية، ولا يعتمد الفصل 17 عليها منطقيًا.

لا توجد دورة اعتماد حالية، بشرط ألا يستعمل الفصل 17 نتيجة من الفصل 18 المخطط بوصفها `PROVED-HERE`.

### الفصل الثامن عشر المخطط

الفصل 18 مخصص للمجاميع الأسية وفان دير كوربوت. لذلك يعتمد الفصل 17 السياسة التالية:

```text
GENERAL EXPONENTIAL-SUM THEORY  = DEFERRED TO CHAPTER 18
SPECIFIC MINOR-ARC ESTIMATES    = CITED IN CHAPTER 17
ORTHOGONALITY AND ARC SPLIT     = PROVED-HERE IN CHAPTER 17
```

## 4. العوائق المرجعية

1. **VINOGRADOV-PRIMARY-TEXT:** تثبيت نسخة أو ترجمة موثوقة للورقة الأصلية وتحديد الصياغة المنسوبة إليها.
2. **WARING-TARGET:** اختيار مبرهنة وارينغ الدقيقة ومصدرها الأولي أو المرجعي المباشر.
3. **HELFGOTT-SCOPE:** اتخاذ قرار حوكمي: هل تدخل مبرهنة غولدباخ الضعيف الكاملة بوصفها `CITED`، أم يقتصر الفصل على مبرهنة فينوغرادوف التاريخية؟

## 5. حكم التدقيق

```text
PRIMARY-SOURCE-IDENTIFICATION = PASS
ATTRIBUTION-SAFETY            = PASS WITH BLOCKERS
NONCIRCULARITY                 = PASS
CLAIM-SCOPE                    = NOT YET FROZEN
AUTHORING                      = BLOCKED
```

يجوز متابعة البحث وحجز النتائج مبدئيًا، ولا يجوز إنشاء متن الفصل قبل إغلاق العوائق الثلاثة وإصدار حكم جديد صريح.