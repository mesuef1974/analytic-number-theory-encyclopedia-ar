# سجل نتائج الفصل السابع عشر

آخر تحديث: 2026-07-25

```text
CHAPTER               = 17
VERSION               = 0.21.0-dev
STATUS                = AUTHORED-DRAFT / MATHEMATICAL-AUDIT-03
PRE-AUTHORING-GATE    = CLOSED
PASS-FOR-AUTHORING    = YES
RESULTS               = 9 / AUTHORED-DRAFT
REFERENCE-AUDIT       = INITIAL PASS / BUILD VERIFIED
MATHEMATICAL-AUDIT    = FOCUSED PASS / POST-CORRECTION BUILD PENDING
PDF-BUILD             = PASS / 235 PAGES BEFORE AUDIT-03
RELEASE-READY         = NO
```

| المعرّف | النوع | الوصف | التصنيف | الحالة |
|---|---|---|---|---|
| `ANT-ID-17-01` | هوية | تعامد الدوال الأسية على الدائرة | `IDENTITY / PROVED-HERE` | `AUTHORED-DRAFT` |
| `ANT-ID-17-02` | هوية | تمثيل عدد الحلول الموزون بتكامل فورييه | `IDENTITY / PROVED-HERE` | `AUTHORED-DRAFT` |
| `ANT-DEF-17-01` | تعريف | الأقواس الكبرى والأقواس الصغرى | `DEFINITION / PROVED-HERE` | `AUTHORED-DRAFT` |
| `ANT-PROP-17-01` | قضية مقتبسة | بنية مساهمة الأقواس الكبرى عبر السلسلة والتكامل المفردين في نموذج وارينغ | `CITED / EXPLAINED` | `AUTHORED-DRAFT` |
| `ANT-PROP-17-02` | قضية | هوية قياس التكامل المفرد: `J(N)=N^(s/k-1) J*` | `PROVED-HERE` | `AUTHORED-DRAFT` |
| `ANT-THM-17-01` | مبرهنة | الصيغة التقاربية الكلاسيكية لمسألة وارينغ في نطاق متغيرات كافٍ | `CITED / EXPLAINED` | `AUTHORED-DRAFT` |
| `ANT-THM-17-02` | مبرهنة | مبرهنة فينوغرادوف للثلاثة أوليات | `CITED` | `AUTHORED-DRAFT` |
| `ANT-THM-17-03` | مبرهنة | مبرهنة هلفغوت الكاملة لغولدباخ الثلاثي | `CITED` مع مكوّن `FINITE-VERIFIED` | `AUTHORED-DRAFT` |
| `ANT-CONJ-17-01` | حدسية | غولدباخ الثنائية وصيغة هاردي--ليتلوود المتوقعة | `HYPOTHESIS / OPEN` | `AUTHORED-DRAFT` |

## نتائج التدقيق الرياضي الثالث

- فُصل عامل النمو `N^(s/k-1)` عن الثابت الأرخميدي المطبع.
- أُثبتت هوية القياس داخليًا بتغيير متغيرين.
- سُجل شرط `s>k` للتقارب المطلق للتكامل المطبع.
- صُحح شرط إيجابية السلسلة المفردة إلى وجود حلول `p`-أدية غير منفردة مع تقارب حاصل الضرب المحلي.
- خُفض تصنيف `ANT-PROP-17-01` نهائيًا إلى `CITED / EXPLAINED`؛ لا ادعاء ببرهان كامل للأقواس الكبرى داخل الفصل.
- تقارب وإيجابية السلسلة المفردة في نطاق وارينغ الكلاسيكي يبقيان `CITED / LOCAL-DENSITY INPUT`.

## قيود الحوكمة

- `AUTHORED-DRAFT` لا تعني `VERIFIED` أو `REVIEWED`.
- تقدير الأقواس الصغرى المستخدم في وارينغ `CITED / COMPOSITE INPUT`.
- مبرهنة هلفغوت التحليلية `CITED`، أما التحقق الحاسوبي المنفصل فـ`FINITE-VERIFIED`.
- لا توجد دعوى بإثبات غولدباخ الثنائية.
- يلزم إعادة بناء PDF بعد إدراج تدقيق 03.
- لا دمج ولا تعديل لـ`main` دون إذن المالك.

```text
RESULT-ID-COLLISION   = NONE DETECTED
AUTHORING             = AUDIT-03 LINKED
POST-CORRECTION-BUILD = PENDING
REVIEWED              = NO
MERGE                 = NOT AUTHORIZED
```
