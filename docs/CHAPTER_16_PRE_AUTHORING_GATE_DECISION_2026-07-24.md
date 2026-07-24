# قرار بوابة ما قبل التأليف — الفصل السادس عشر

آخر تحديث: 2026-07-24

```text
CHAPTER                = 16
VERSION                = 0.20.0-dev
BRANCH                 = agent/chapter-16-sieve-applications-prime-gaps-v0.20.0
ISSUE                  = #29 / OPEN
PR                     = #30 / DRAFT / OPEN / UNMERGED
RESEARCH-INTAKE        = CLOSED
PRIMARY-SOURCE-AUDIT   = PASS
NONCIRCULARITY-AUDIT   = PASS
MATHEMATICAL-BLOCKERS  = 0
REFERENCE-BLOCKERS     = 0
GOVERNANCE-BLOCKERS    = 0
PASS-FOR-AUTHORING     = YES
AUTHORING              = AUTHORIZED
RESULTS                = 0 / NOT YET RESERVED
RELEASE-READY          = NO
```

## النطاق المعتمد

يبنى الفصل السادس عشر حول الانتقال من الغربال الكلاسيكي إلى التطبيقات الحديثة على الفجوات بين الأوليات، وفق الترتيب الآتي:

1. تطبيق حد علوي ثنائي واستخراج تقارب مجموع برون ببرهان داخلي قصير.
2. الأعداد شبه الأولية وصياغة مبرهنة تشن بوصفها نتيجة مقتبسة، من دون محاولة إعادة بناء برهانها الكامل.
3. طريقة GPY ونتيجة الفجوات الصغيرة نسبة إلى المتوسط.
4. إنجاز Zhang بوصفه تحسينًا في مدخل توزيع الأوليات للمقامات الملساء.
5. طريقة Maynard متعددة الأبعاد بوصفها النواة التقنية المركزية.
6. نتائج Polymath8b والتحسينات العددية، مع الفصل بين غير المشروط والمشروط.
7. عائق التكافؤ وحدود ما يمكن أن تنتجه المعلومات الغربالية وحدها.

## تصنيف النتائج

| النتيجة | التصنيف |
|---|---|
| الحد العلوي لعد الأزواج الأولية حتى \(x\) | `PROVED-HERE` بالاعتماد على الفصل 15 |
| تقارب مجموع برون | `PROVED-HERE` مع إحالة تاريخية إلى Brun 1919 |
| مبرهنة تشن | `CITED` |
| نتيجة GPY | `CITED / EXPLAINED` |
| مبرهنة Zhang | `CITED / EXPLAINED` |
| مبرهنة Maynard | `CITED / EXPLAINED WITH DERIVATION OF THE VARIATIONAL CORE` |
| حد Polymath8b العددي | `CITED / TIME-STAMPED` |
| أفضل حد معاصر خارج المرجع المنشور المختار | `DEFERRED / TIME-SENSITIVE` |

## حدود الادعاء

- لا إثبات لحدسية الأوليات التوأم.
- لا إثبات لمبرهنة تشن داخل المتن.
- لا نسبة للفجوات المحدودة إلى غربال سيلبرغ التقليدي وحده.
- لا استعمال لنتيجة الفصل 16 في إثبات مدخل سابق من الفصلين 13 أو 15.
- لا وصف للحد \(246\) بأنه «نهائي»؛ يذكر بوصفه الحد المنشور في مرجع Polymath8b المختار.
- لا ترقية إلى `VERIFIED` أو `REVIEWED` قبل التدقيق والبناء والمراجعة المستقلة.

## قرار البوابة

جميع شروط قاعدة الانتقال في `ROADMAP.md` مستوفاة: سجل الأدلة موجود، خريطة البرهان موجودة، المصادر الأصلية مثبتة، التصنيف محدد، وتدقيق عدم الدور ناجح.

```text
PRE-AUTHORING-GATE = CLOSED
PASS-FOR-AUTHORING = YES
NEXT ACTION        = RESERVE RESULT IDS AND AUTHOR CHAPTER MANUSCRIPT
```
