# P0-04 — نقل تعليق تدقيق مرجع Chen 1973 خارج الببليوغرافيا المطبوعة

## إعادة الإنتاج

أعيد إنتاج ملاحظة التقييم الخارجي على فرع المعالجة. كان مدخل:

```text
Chen1973PrimePlusP2
```

في `manuscript/chapter-16-bibliography.bib` يحتوي حقل `note` داخليًا يذكر نتيجة محاولة حل DOI وتاريخ تدقيق الإصدار. لأن `note` حقل مطبوع في BibLaTeX، ظهر التعليق الإداري داخل قائمة المراجع العامة.

## الإصلاح

- حُذف حقل `note` من المدخل المطبوع.
- أُبقيت بيانات المقالة الورقية كما هي: المؤلف، العنوان، المجلة، المجلد، العدد، السنة، الصفحات، والـDOI.
- نُقلت ملاحظة التحقق إلى هذا السجل غير المطبوع.

## سجل التدقيق غير المطبوع

```text
REFERENCE KEY = Chen1973PrimePlusP2
DOI           = 10.1360/YA1973-16-2-157
AUDIT NOTE    = The legacy DOI was retained because it matches the article metadata.
                During the 2026-07-27 release audit, doi.org and Crossref resolution
                attempts returned HTTP 404. Manual publisher verification remains advisable.
PRINT STATUS  = NOT PRINTED
```

## التحقق

```text
QUALITY #979 = PASS
BUILD   #786 = PASS
DRAFT PDF    = PASS
RELEASE PDF  = PASS
```

## الحالة

```text
P0-04 = REPRODUCED / FIXED / VERIFIED / CLOSED
```