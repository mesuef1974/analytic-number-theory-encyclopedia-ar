# طلب مراجعة مستقلة ضيقة لتصحيحات ما بعد تأليف الفصل الثاني والعشرين

## الرأس المستهدف

```text
TARGET-HEAD          = aa8bb3066600b8af2ff59827db7c3a4dcdeeb191
ORIGINAL-REVIEW-HEAD = 812ac2355d4ede8dba88354c02bc85c7bc3c9a4a
ORIGINAL-VERDICT     = CHANGES-REQUIRED
ORIGINAL-BLOCKERS    = 0
RESULTS-CITABLE      = NO
MERGE                = NOT AUTHORIZED
```

## نطاق المراجعة الضيقة

راجع فقط إغلاق الملاحظات الثلاث المسجلة في:

`docs/CHAPTER_22_INDEPENDENT_POST_AUTHORING_REVIEW_2026-07-26.md`

وقارن المتن الحالي بالرأس المراجَع سابقًا، مع التحقق الفعلي من:

1. أن صيغة حد الخطأ في `ANT-PROP-22-01` أصبحت
   \[
   O(x^{-1/2}+y^{-1/2})
   \]
   تحت الشرط \(xy=t/(2\pi)\)، وأن التخصيص المتناظر يعطي \(O(t^{-1/4})\).
2. أن قسم العزم الثاني ينسب الصيغة الثنائية الحد وحد الخطأ الكلاسيكي صراحة إلى Ingham، مع فصل الخلفية التاريخية لـHardy--Littlewood.
3. أن ملف الفصل لا يبدأ بعلامة BOM.
4. أن التصحيحات لم تُدخل خطأ LaTeX أو استشهادًا غير محلول أو تغييرًا غير مقصود في المعرفات العشرة.
5. أن ترتيب المخطوط يجعل فصل العزوم هو الفصل 22، وخريطة الجبهات البحثية هي الفصل الأخير.

## المطلوب من المراجع

أنشئ ملفًا جديدًا فقط:

`docs/CHAPTER_22_INDEPENDENT_POST_AUTHORING_NARROW_REVIEW_2026-07-26.md`

ويجب أن يتضمن:

```text
REVIEWED-HEAD    = aa8bb3066600b8af2ff59827db7c3a4dcdeeb191
REVIEWER         = INDEPENDENT LOCAL CLIENT
VERDICT          = PASS | CHANGES-REQUIRED | FAIL
BLOCKERS         = <integer>
RESULTS-CITABLE  = YES | NO
```

صنّف أي ملاحظة جديدة إلى `BLOCKER`, `MAJOR`, `MINOR`, أو `EDITORIAL`.

لا تعدّل متن الفصل أو وثائق الحوكمة الأصلية.
لا تفعّل النتائج.
لا تدمج PR #44.
لا تصدر `RESULTS-CITABLE = YES` إلا عند نجاح البناء، وصفر عوائق، وإغلاق الملاحظات الثلاث فعليًا.
