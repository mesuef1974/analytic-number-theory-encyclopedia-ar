# استقبال التقييم الخارجي — مرحلة P1 العلمية

```text
ISSUE                 = #64
BRANCH                = agent/release-p1-external-review-math-v0.31.0-dev
BASE                  = main
VERSION               = 0.31.0-dev
P0 BLOCKERS           = 0
P1 STATUS             = REMEDIATED / VERIFICATION PENDING
PUBLICATION-READY     = YES FOR P0 SCOPE ONLY
STABLE RELEASE        = BLOCKED
MERGE                 = NOT AUTHORIZED
```

## قاعدة العمل

لا يُعامل أي بند في التقرير الخارجي بوصفه خطأً مثبتًا قبل إعادة إنتاجه على رأس الفرع الحالي. يمر كل بند عبر الحالات:

`EXTERNAL-CLAIM → REPRODUCED / NOT-REPRODUCED → FIXED → VERIFIED → CLOSED`.

## حزم P1

### P1-01 — الجسر من المنطقة الخالية لدوال L إلى ζ

- الادعاء الخارجي: الكتاب يبرهن الحالة العامة لدوال L في الفصل 11، لكنه يستورد الحالة الخاصة لـ ζ في الفصل 6.
- المطلوب: فحص التطبيعات والفرضيات، ثم تقرير إمكان اشتقاق نتيجة ζ من الحالة العامة عند الشخصية التافهة أو صياغة جسر صريح مضبوط.
- الحالة: `EXTERNAL-CLAIM / OPEN`.

### P1-02 — مبرهنة الأعداد الأولية الكمية

- الادعاء الخارجي: السلسلة الكمية تعتمد على نتائج مستوردة رغم وجود معظم مكوناتها داخل الكتاب.
- المطلوب: تحديد أقل حزمة براهين تكفي لتحويل النتيجة إلى `PROVED-HERE` دون تضخيم غير منضبط للنطاق.
- الحالة: `EXTERNAL-CLAIM / OPEN`.

### P1-03 — صياغة Baker–Harman–Pintz

- الادعاء الخارجي: المصدر الأصلي يصوغ النتيجة على `[x-x^{0.525},x]` بينما الكتاب يعرضها على `(x,x+x^{0.525}]`.
- المطلوب: التحقق من المصدر الأصلي والثابت، ثم إضافة انتقال صريح إن كانت الصياغة الحالية مشتقة بصورة صحيحة.
- الحالة: `EXTERNAL-CLAIM / OPEN`.

### P1-04 — رامانوجان للهولومورفي ومااس

- الادعاء الخارجي: العبارة `|α_f(p)|=|β_f(p)|=1` صحيحة مبرهنة في الحالة الهولومورفية، لكنها مفتوحة عمومًا لأشكال مااس.
- المطلوب: فحص سياق الاقتراح 21.1 وتقييد العبارة أو فصل الحالتين صراحةً.
- الحالة: `EXTERNAL-CLAIM / OPEN`.

## بوابة الإغلاق

```text
P1-01                    = VERIFIED / CLOSED
P1-02                    = VERIFIED / CLOSED أو OWNER-DEFERRED مع تسبيب
P1-03                    = VERIFIED / CLOSED
P1-04                    = VERIFIED / CLOSED
QUALITY CHECK            = PASS
DRAFT BUILD              = PASS
RELEASE BUILD            = PASS
REFERENCE AUDIT          = PASS
INDEPENDENT REVIEW       = PASS
P1 OPEN BLOCKERS         = 0
```

لا يتحول طلب الدمج إلى Ready ولا يُدمج قبل اكتمال هذه البوابة وقرار المالك.
