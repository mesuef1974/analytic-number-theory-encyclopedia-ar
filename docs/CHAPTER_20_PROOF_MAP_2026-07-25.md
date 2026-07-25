# خريطة برهان الفصل العشرين — 2026-07-25

## الحالة الحاكمة

```text
PROOF-MAP            = REVISED / NOT FROZEN
PRIMARY-SCOPE        = LEVEL 1 / TRIVIAL CHARACTER
CIRCULARITY-AUDIT    = PRELIMINARY PASS / REVIEW PENDING
PRE-AUTHORING-GATE   = OPEN
PASS-FOR-AUTHORING   = NO
AUTHORING            = BLOCKED
```

## سلسلة الاعتماد

1. هندسة \(\mathbb H\)، فعل \(SL_2(\mathbb R)\)، وثبات \(d\mu=dx\,dy/y^2\).
2. تعريف الأشكال المعيارية الهولومورفية وشروط الرؤوس.
3. توسعات فورييه وفضاءات الحدبة.
4. حاصل بيترسون ومؤثرات Hecke.
5. أشكال مااس ولابلاس والتوسع Fourier--Whittaker.
6. مجاميع Kloosterman ونوى Bessel.
7. صيغة Petersson عند المستوى \(1\).
8. صيغة Kuznetsov للزمرة المعيارية مع الطيف المستمر.
9. نموذج Selberg المدمج بوصفه مدخلًا بنيويًا فقط.
10. جسور تطبيقية معلنة إلى الفصل 21 بلا استعمال عكسي.

## تصنيف النتائج المرشحة

| العقدة | التصنيف المقترح | المصدر/الموضع | الحالة |
|---|---|---|---|
| فعل الزمرة وثبات القياس | `PROVED-HERE` | حساب مباشر | `MAP-READY` |
| التعريفات الهولومورفية وشروط الرؤوس | `PROVED-HERE / DEFINITIONS` | Diamond--Shurman أو Miyake؛ الموضع معلق | `LOCATOR-PENDING` |
| توسع فورييه عند رأس | `PROVED-HERE` | برهان دوري محلي مع ضبط عرض الرأس | `MAP-READY / SOURCE-CHECK-PENDING` |
| مؤثرات Hecke الأساسية | `MIXED` | مرجع قياسي + علاقات بسيطة داخليًا | `SCOPE-FIXED / LOCATOR-PENDING` |
| أشكال مااس والطيف | `CITED-CORE` | Iwaniec؛ Kuznetsov §2 للسياق الأصلي | `LOCATOR-PENDING` |
| التوسع Fourier--Whittaker | `CITED` | Kuznetsov (2.10) مع تطبيع الفصل | `FORMULA-LOCATED / MATCH-PENDING` |
| حد Weil لـKloosterman | `CITED` | Iwaniec--Kowalski؛ الموضع معلق | `LOCATOR-PENDING` |
| صيغة Petersson مستوى 1 | `CITED-CORE` | Knightly--Li Cor. 3.12؛ الأصل Petersson 1932 | `LOCATED / CROSS-CHECK-PENDING` |
| صيغة Kuznetsov | `CITED-CORE` | Kuznetsov Thms. 1--2، (2.14)، (2.23) | `LOCATED / FULL-MATCH-PENDING` |
| صيغة Selberg | `DEFERRED-FULL-PROOF` | Hejhal I، الفصل الأول، ص 1--38 | `STRUCTURAL-INTRO-ONLY` |

## فصل Petersson عن Kuznetsov

- Petersson: فضاء هولومورفي محدود البعد؛ مجموع طيفي منفصل؛ نواة \(J_{k-1}\).
- Kuznetsov: طيف مااس منفصل **وطيف مستمر**؛ تحويلات Bessel تعتمد على دالة اختبار.
- التشابه بين الطرفين لا يجيز اشتقاق إحداهما من الأخرى داخل الفصل دون بناء تحليلي إضافي.

## تدقيق عدم الدور

| الاعتماد | المسموح | المحظور | الحكم |
|---|---|---|---|
| الفصل 6 | التحليل المركب وزيتا | استيراد التحليل الطيفي الآلي | `PASS` |
| الفصل 7 | الشخصيات والتعامد المنتهي | افتراض دوال \(L\) الآلية | `PASS` |
| الفصل 13 | سياق الغربال الكبير وType I/II | استعمال Kuznetsov قبل تثبيتها | `PASS WITH ORDERING GUARD` |
| الفصل 18 | المجاميع الأسية وفان دير كوربوت | استبدال حد طيفي بحد مجموع أسي غير مكافئ | `PASS` |
| الفصل 19 | نتائج الفترات القصيرة | استعمالها لإثبات صيغة أثر | `NO DEPENDENCY` |
| الفصل 21 | لا اعتماد سابق | دون التحدب أو لانجلاندز لإغلاق الفصل 20 | `HARD BLOCK` |

التدقيق البنيوي لا يظهر دورة، لكنه يبقى `REVIEW-PENDING` حتى يقرأ مراجع كل عقدة مراجع مستقل.

## قرار المرحلة

الخريطة منضبطة بنيويًا لكن غير مجمدة. لا يُكتب المتن قبل إغلاق مواضع المصادر، وتجميد جدول التطبيعات، ومراجعة الصيغ حدًا بحد، والمراجعة المستقلة.
