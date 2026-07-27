# إغلاق P0-03 — توحيد مرجع Titchmarsh

## المشكلة

أظهر التقييم الخارجي تكرار كتاب E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function* تحت عدة مفاتيح ببليوغرافية. أعيد إنتاج الادعاء على رأس فرع المعالجة، ووجدت ثلاث نسخ فعلية للكتاب نفسه:

```text
Titchmarsh1986
 titchmarshHeathBrown1986zeta
 titchmarsh1986zeta
```

## القرار القانوني

```text
CANONICAL KEY = Titchmarsh1986
LEGACY IDS    = titchmarshHeathBrown1986zeta, titchmarsh1986zeta
```

اختير `Titchmarsh1986` لأنه المدخل المركزي والأكمل، ويذكر بوضوح الطبعة الثانية ومراجعة D. R. Heath-Brown.

## الإصلاح

- الإبقاء على مدخل واحد فقط في `manuscript/bibliography.bib`.
- إضافة المفتاحين القديمين إلى حقل `ids` في BibLaTeX لضمان استمرار عمل الاستشهادات التاريخية دون طباعة مراجع مكررة.
- حذف المدخل المكرر من `manuscript/chapter-22-bibliography.bib`.
- حذف المدخل المكرر من `manuscript/chapter-23-bibliography.bib`.
- لم تُحذف أي إحالة علمية من المتن.

## التحقق

التنفيذ المختبر على الرأس:

```text
82ea2ea0da51e0d6c9f15c657c32795d8870d7b7
```

نتائج GitHub Actions:

```text
Quality checks #974          = PASS
Build encyclopedia PDF #781 = PASS
Draft build                  = PASS
Release build                = PASS
Biber                        = PASS
Publication metadata check  = PASS
```

جميع خطوات المهمة `Compile draft and release PDFs` نجحت، بما فيها بناء المسودة، وبناء النشر، واستخراج النص، وفحوص سلامة النص وفصل بيانات الحوكمة.

## الحكم

```text
P0-03 = REPRODUCED / FIXED / VERIFIED / CLOSED
```
