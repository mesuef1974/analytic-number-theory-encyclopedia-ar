# الفصل الثامن عشر — تدقيق عدم الدور مع الفصل السابع عشر

التاريخ: 2026-07-25

## السؤال

هل يعتمد الفصل الثامن عشر في إثبات أدواته العامة على تقديرات الأقواس الصغرى أو النتائج التطبيقية المقتبسة في الفصل السابع عشر؟

## النتيجة

```text
NONCIRCULARITY-AUDIT = PASS
CIRCULAR-DEPENDENCIES = 0
```

## اتجاه الاعتماد الصحيح

```text
Chapter 18 general exponential-sum tools
        |
        v
illustrative minor-arc applications
        |
        v
conceptual support for Chapter 17
```

ولا يجوز قلب السهم إلى:

```text
Chapter 17 cited minor-arc bound
        |
        v
proof of Chapter 18 general tools
```

## تفصيل البنود

1. الحد التافه والجمع الجزئي مستقلان تمامًا عن الفصل 17.
2. متباينة فرق فان دير كوربوت تثبت من توسعة مربع مجموع ومتوسط الإزاحات، بلا أي مدخل من الطريقة الدائرية.
3. اختبار المشتقة الأولى يثبت من تحليل المجموع الهندسي والرتابة والبعد عن الأعداد الصحيحة.
4. اختبار المشتقة الثانية يعرض مقتبسًا من مصادر المجاميع الأسية، لا من الفصل 17.
5. عملية `A` تعتمد على فرق فان دير كوربوت داخل الفصل 18.
6. عملية `B` وإطار الأزواج الأسية يعتمدان على مصادر متخصصة مستقلة.
7. الفصل 17 أبقى تقدير الأقواس الصغرى في وارينغ بحالة `CITED / COMPOSITE INPUT`؛ الفصل 18 لا يغير هذا التصنيف تلقائيًا.
8. الأمثلة المرتبطة بمجاميع فايل في الفصل 18 توضيحية، ولا تدعي إعادة بناء الصيغة التقاربية الكاملة لوارينغ.

## حدود الادعاء

```text
CHAPTER-17-MINOR-ARC-RESULT = REMAINS CITED
WARING-ASYMPTOTIC-FORMULA   = NOT REPROVED
GOLDBACH-BINARY             = OPEN / UNCHANGED
DEPENDENCY-DIRECTION        = CH18 TO APPLICATIONS ONLY
```

## الحكم

```text
NONCIRCULARITY-BLOCKER = CLOSED
AUTHORING-GATE         = STILL OPEN FOR INDEPENDENT THEOREM REVIEW
```
