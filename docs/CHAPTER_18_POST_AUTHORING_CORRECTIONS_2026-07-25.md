# تصحيحات تدقيق ما بعد التأليف للفصل الثامن عشر

التاريخ: 2026-07-25

## النطاق

أُغلقت ثلاث ملاحظات حاجزة كُشفت بعد بناء دفعة التأليف الثالثة:

1. فرضية لمّة كوسمين--لانداو المنفصلة.
2. تطبيع تعريف الزوج الأسي.
3. الإحالات الفعلية لتعريف الزوج الأسي وعملية `B`.

## التصحيح الرياضي الأول

كانت الصياغة السابقة تفترض فقط

```text
||theta_n|| >= lambda
```

عند نقاط المتتالية المنفصلة، ثم يستعمل البرهان تغير الدالة
`q(t)=1/(1-e(t))` على المجال المتصل بين الطرفين. لا تمنع الفرضية
القديمة قفزة المتتالية فوق عدد صحيح؛ مثلًا قد ينتقل حد من `0.9` إلى
`1.1`.

شُددت الفرضية إلى

```text
||t|| >= lambda
for every real t between theta_1 and theta_(N-1).
```

وبذلك يقع المجال المتصل كله في مركبة واحدة من مجموعة البعد عن
الأعداد الصحيحة. كما أضيف في برهان اختبار المشتقة الأولى تفسير صريح
لأن هذا الشرط ينتقل من مدى الدالة المتصلة الرتيبة `f'`.

## التصحيح الرياضي الثاني

صُححت صيغة إطار الزوج الأسي من

```text
F^kappa N^lambda F^(-1) + F^(-1)
```

إلى

```text
F^kappa N^lambda + F^(-1).
```

تتسق الصيغة المصححة مع العبارة اللاحقة مباشرة: الزوج التافه `(0,1)`
يعطي حدًا من رتبة `N`.

## التصحيح المرجعي

- أُنشئ `manuscript/chapter-18-bibliography.bib`.
- أضيف مرجع:
  S. W. Graham and Grigori Kolesnik,
  *Van der Corput's Method of Exponential Sums*,
  Cambridge University Press, 1991,
  LMS Lecture Note Series 126,
  DOI `10.1017/CBO9780511661976`.
- رُبط المرجع بتعريف الزوج الأسي، والتحويل العام بعملية `A`، وقضية
  عملية `B`، مع إحالة إلى الفصل 3، الصفحات 21--37.

## الحالة

```text
CORRECTIONS-REQUIRED       = 3
CORRECTIONS-APPLIED        = 3
MATHEMATICAL-BLOCKERS      = 0 BEFORE REBUILD
REFERENCE-BLOCKERS         = 0 BEFORE REBUILD
QUALITY-CHECKS             = RUN-593 / SUCCESS
PDF-REBUILD                = RUN-520 / SUCCESS / 249 PAGES
PDF-SHA256                 = 13FF6784F1D40E8ABCE1DD12AE66D4E9659DE2A3002FBADFE6EB6AF3BE62B3C2
UNDEFINED-CITATIONS-FINAL  = 0
UNDEFINED-REFERENCES-FINAL = 0
VISUAL-AUDIT               = PASS
INDEPENDENT-REVIEW         = PENDING
CHAPTER-18                 = AUTHORED-DRAFT / NON-CITABLE
PR-35                      = DRAFT / OPEN / UNMERGED
MERGE                      = NOT AUTHORIZED
RELEASE-READY              = NO
```

## تحقق البناء والفحص البصري

- نجح فحص الجودة في GitHub Actions: `run #593`.
- نجح بناء XeLaTeX وBiber في GitHub Actions: `run #520`.
- الناتج: PDF 1.7 من 249 صفحة وحجم 967956 بايت.
- طابقت بصمة الملف ملف البصمة داخل Artifact.
- لم يظهر في مرور XeLaTeX النهائي أي مرجع أو إحالة غير معرّفة.
- فُحصت بصريًا صفحات لمّة كوسمين--لانداو، وتعريف الزوج الأسي،
  وعملية `B`، ومدخل Graham--Kolesnik في قائمة المراجع، بلا قص أو
  تراكب.
