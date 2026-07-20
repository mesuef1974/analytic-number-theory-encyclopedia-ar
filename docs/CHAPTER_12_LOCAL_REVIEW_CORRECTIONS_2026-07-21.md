# إغلاق تصحيحات المراجعة المحلية للفصل الثاني عشر

## بيانات النسخة

```text
DATE                     = 2026-07-21
CHAPTER                  = 12 — مبرهنة Siegel--Walfisz
BRANCH                   = agent/chapter-12-siegel-walfisz-v0.16.0
REVIEW-BASE-HEAD         = 89c8128443008c3e2f38679b7983b626272c756d
CORRECTION-1-HEAD        = a6c7c12ad410805c94d87426cf68ad4c80ae2ded
REFERENCE-CLOSURE-HEAD   = c54e0d85c2ef8713fea72e1c43bcc3de7f1c2a62
CHAPTER-STATUS           = VERIFIED
REVIEW-VERDICT           = PENDING-LOCAL-SYNC-REBUILD
PR-20                    = DRAFT / UNMERGED
RELEASE-READY            = NO
```

## الملاحظة R1 — الصيغة الصريحة المقطوعة

### المشكلة

ظهر ارتفاع مختار `T_0` في الفرض ثم استعملت الصيغة `T` في حدود الخطأ، كما بدت الصيغة المركبة كأنها اقتباس حرفي من مبرهنة واحدة.

### التصحيح

- استبدل الارتفاع الفعلي بمتغير واحد:

  \[
  U\in[T,2T].
  \]

- استعملت `U` نفسها في مقام المنطقة الخالية، وخطأ القطع، والخسائر اللوغاريتمية.
- عدلت `ANT-THM-12-02` إلى `CITED / COMPOSITE-INPUT` بدل الإيحاء باقتباس حرفي.
- سجلت مواضع المسار:
  - Davenport، الطبعة الثانية، الفصول 20--23، الصفحات 115--134.
  - Montgomery--Vaughan، الفصلان 11--12، الصفحات 358--418.
- بقيت ديون بيرون وتحويل المسار معلنة، ولم ترفع النتيجة إلى `PROVED-HERE`.

```text
R1 = CLOSED
```

## الملاحظة R2 — الانتقال من \(\vartheta\) إلى \(\pi\)

### المشكلة

وصف الفرق الناشئ من تقسيم التكامل عند

\[
y=\exp(q^{1/(2A)})
\]

بأنه «ثابت محدود»، مع أنه يعتمد على `y`.

### التصحيح

سجلت الهوية

\[
\frac{x}{\log x}+\int_y^x\frac{dt}{\log^2t}
=
\operatorname{Li}(x)-\operatorname{Li}(y)+\frac{y}{\log y},
\]

ومن ثم صار الفرق عن الحد الرئيسي الكامل مقدرًا بـ

\[
O(y),
\]

وهو يمتص لأن

\[
y\le e^{\sqrt{\log x}}
=o\!\left(\frac{x}{(\log x)^B}\right).
\]

كما فصل تقدير تكامل الخطأ عند \(\sqrt x\).

```text
R2 = CLOSED
```

## فحوص النص قبل الدفع

```text
LATEX-ENVIRONMENT-BALANCE = PASS
BRACE-BALANCE             = PASS
STALE-T_0                  = ABSENT
STALE-BOUNDED-CONSTANT     = ABSENT
RESULT-IDS                 = UNCHANGED
MATHEMATICAL-SCOPE         = UNCHANGED
```

## البوابة التالية: المزامنة والبناء المحليان

لا يحول هذا الإيصال الفصل إلى `REVIEWED`. يلزم تشغيل الأمر التالي من جهاز المالك:

```powershell
cd "D:\analytic-number-theory-encyclopedia-ar"
.\scripts\sync-build.ps1 -Open -CommitReceipt -Push
```

شروط قبول البوابة:

```text
LOCAL-HEAD       = ORIGIN-HEAD
SYNC             = PASS / FF-ONLY
SOURCE-BUILD     = PASS
PDF-PAGES        = RECORDED
PDF-SHA256       = RECORDED
LOCAL-RECEIPT    = COMMITTED / PUSHED
```

بعد ذلك تعاد مراجعة الصفحات المتأثرة ويصدر أحد الأحكام:

```text
APPROVED
APPROVED-WITH-NONBLOCKING-CORRECTIONS
CHANGES-REQUIRED
REJECTED
```

## قرار الحوكمة

```text
CORRECTIONS       = IMPLEMENTED
LOCAL-SYNC-BUILD  = REQUIRED
PROMOTE-REVIEWED  = BLOCKED-PENDING-LOCAL-RECEIPT
MERGE-PR-20       = NOT AUTHORIZED
RELEASE-READY     = NO
```
