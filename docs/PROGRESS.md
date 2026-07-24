# تقدم المشروع

## الحالة العامة

- **الإصدار التطويري الحالي:** `0.18.0-dev`
- **المرحلة:** الفصل الرابع عشر — مبرهنة Barban--Davenport--Halberstam ومتوسط مربعات أخطاء التوزيع.
- **حالة الفصل:** `READY-FOR-REVIEWED-DECISION`
- **الفرع المستقر:** `main`
- **رأس `main` عند بدء المرحلة:** `d2588c893d8d07be1e961813628e1bb210e0eece`
- **فرع العمل:** `agent/chapter-14-barban-davenport-halberstam-v0.18.0`
- **بوابة ما قبل التأليف:** `CLOSED`
- **إذن التأليف:** `PASS-FOR-AUTHORING = YES`
- **التأليف:** `COMPLETE-AS-DRAFT`
- **التدقيق المنطقي:** `PASS`
- **التحقق المرجعي:** `PASS`
- **المراجعة المستقلة:** `APPROVED-WITH-NONBLOCKING-CORRECTIONS`
- **التصحيحات غير الحاجزة:** `5 / 5 CLOSED`
- **بناء PDF:** `PASS / 208 PAGES`
- **المراجعة النهائية للمتن:** `PASS`
- **تصحيحات المراجعة النهائية:** `2 / 2 CLOSED`
- **العوائق الرياضية:** `0`
- **العوائق النصية:** `0`
- **مزامنة ملفات التتبع:** `COMPLETE`
- **Issue:** `#25 / OPEN`
- **PR:** `#26 / DRAFT / OPEN / UNMERGED`
- **آخر تحديث:** 2026-07-24

```text
CHAPTER-14                   = READY-FOR-REVIEWED-DECISION
VERSION                      = 0.18.0-dev
BASE-MAIN                    = d2588c893d8d07be1e961813628e1bb210e0eece
BRANCH                       = agent/chapter-14-barban-davenport-halberstam-v0.18.0
ISSUE                        = #25 / OPEN
PR                           = #26 / DRAFT / OPEN / UNMERGED
PRE-AUTHORING-GATE           = CLOSED
PASS-FOR-AUTHORING           = YES
AUTHORING                    = COMPLETE-AS-DRAFT
RESULTS                      = 5 / RESERVED
LOGIC-AUDIT                  = PASS
REFERENCE-AUDIT              = PASS
INDEPENDENT-REVIEW           = APPROVED-WITH-NONBLOCKING-CORRECTIONS
NONBLOCKING-CORRECTIONS      = 5 / 5 CLOSED
POST-AUTHORING-BUILD-AUDIT   = PASS
PDF-BUILD                    = PASS / 208 PAGES
FINAL-MANUSCRIPT-REVIEW      = PASS
FINAL-MANUSCRIPT-CORRECTIONS = 2 / 2 CLOSED
MATHEMATICAL-BLOCKERS        = 0
TEXTUAL-BLOCKERS             = 0
TRACKING-DOCS-SYNC           = COMPLETE
QUALITY-CHECKS               = PASS
REVIEWED                     = PENDING OWNER DECISION
MERGE                        = NOT AUTHORIZED
RELEASE-READY                = NO
```

## إغلاق المرحلة السابقة

```text
CHAPTER-13          = REVIEWED / MERGED
PR-22               = MERGED
MERGE-COMMIT        = 2e28e51bd8334cd748d59f1e8cc9998975058a8c
GOVERNANCE-COMMIT   = d2588c893d8d07be1e961813628e1bb210e0eece
RELEASE-READY       = NO
```

## لوحة التقدم

| المكوّن | الحالة | التقدم التقريبي |
|---|---:|---:|
| هيكل المستودع | مكتمل مبدئيًا | 100% |
| أهداف المشروع | مكتملة للإصدار الأول | 100% |
| نظام التوثيق والمتابعة | مكتمل مبدئيًا | 100% |
| بناء PDF المحلي والآلي | مسار محلي وآلي عامل | 100% |
| الفصل الأول: التاريخ والمنهج | مدقق داخليًا؛ الإحالات التفصيلية باقية | 85% |
| الفصل الثاني: اللغة التقاربية والجمع الجزئي | `VERIFIED` | 85% |
| الفصل الثالث: التحليل المركب الموجّه | `VERIFIED`؛ التوسعات مؤجلة | 80% |
| الفصل الرابع: الدوال الحسابية والالتفاف | `VERIFIED` | 92% |
| الفصل الخامس: سلاسل ديريشليه والمنتجات الأويلرية | `REVIEWED` | 78% |
| الفصل السادس: دالة زيتا لريمان | `REVIEWED` | 85% |
| الفصل السابع: دوال ديريشليه \(L\) | `REVIEWED` | 95% |
| الفصل الثامن: مبرهنة ديريشليه | `REVIEWED` | 90% |
| الفصل التاسع: مبرهنة الأعداد الأولية | `REVIEWED` | 92% |
| الفصل العاشر: PNT في المتتاليات الحسابية | `REVIEWED` | 94% |
| الفصل الحادي عشر: المناطق الخالية والأصفار الاستثنائية | `REVIEWED / MERGED` | 95% |
| الفصل الثاني عشر: Siegel--Walfisz | `REVIEWED / MERGED` | 95% |
| الفصل الثالث عشر: Bombieri--Vinogradov | `REVIEWED / MERGED` | 95% |
| الفصل الرابع عشر: Barban--Davenport--Halberstam | `READY-FOR-REVIEWED-DECISION` | 99% |
| فصل الجبهات الحديثة | نواة أولية | 10% |
| الملحق الحاسوبي | أول تجربة مسجلة وقابلة للتشغيل | 15% |

## لقطة بوابات الفصول

| الفصل | البوابة الحالية | ما يمنع البوابة التالية |
|---|---|---|
| 1 | `DRAFT` | الإحالات التاريخية والحلول والمراجعة المستقلة |
| 2 | `VERIFIED` | مراجعة ثانية مستقلة |
| 3 | `VERIFIED` | مراجعة ثانية مستقلة والتوسعات المعلنة |
| 4 | `VERIFIED` | مراجعة ثانية مستقلة |
| 5 | `REVIEWED` | الديون التحريرية قبل `RELEASE-READY` |
| 6 | `REVIEWED` | براهين بيرون وتحويل المسار قبل `RELEASE-READY` |
| 7 | `REVIEWED` | حلول وتوسعات قبل `RELEASE-READY` |
| 8 | `REVIEWED` | أمثلة وتمارين وتدقيق إصدار |
| 9 | `REVIEWED` | الديون الفعالة والتحريرية |
| 10 | `REVIEWED` | أربعة تحسينات اختيارية وتدقيق إصدار |
| 11 | `REVIEWED / MERGED` | ديون الإصدار قبل `RELEASE-READY` |
| 12 | `REVIEWED / MERGED` | ديون المجلد والتنضيد قبل `RELEASE-READY` |
| 13 | `REVIEWED / MERGED` | ديون الإصدار قبل `RELEASE-READY` |
| 14 | `READY-FOR-REVIEWED-DECISION` | قرار صريح من المالك بالترقية، ثم قرار مستقل بشأن تحويل PR من Draft والدمج |

التدقيق الداخلي والمراجعة المستقلة والبناء لا تجعل أي فصل `RELEASE-READY` تلقائيًا.

## الفصل الثالث عشر — المنجز

- دُمج PR #22 في `main`.
- اكتملت المراجعة المستقلة بحكم `APPROVED-WITH-NONBLOCKING-CORRECTIONS` بصفر عوائق.
- اعتمد مالك المشروع ترقية الفصل إلى `REVIEWED`.
- أُغلقت الحوكمة عند `d2588c893d8d07be1e961813628e1bb210e0eece`.

## الفصل الرابع عشر — المنجز

- أُنشئ الفرع من رأس `main` المغلق حوكميًا، ورفع الإصدار إلى `0.18.0-dev`.
- فُتحت Issue #25 وDraft PR #26.
- أُنشئت سجلات الأدلة وخريطة البرهان قبل التأليف.
- اكتمل البرهان الداخلي للحد الكلاسيكي في المجال
  \[
  \frac{x}{(\log x)^A}\le Q\le x.
  \]
- اجتاز البرهان التدقيق المنطقي والمرجعي.
- أصدرت المراجعة المستقلة الحكم `APPROVED-WITH-NONBLOCKING-CORRECTIONS`.
- أُغلقت التصحيحات الخمسة غير الحاجزة، ثم أصدر المالك `PASS-FOR-AUTHORING = YES`.
- أُنشئ متن الفصل وربط بالمخطوط، وحُجزت خمسة معرّفات نتائج.
- نجح Biber وبناء XeLaTeX في إنتاج `main.pdf` من 208 صفحات بصفر أخطاء قاتلة.
- أُغلقت ملاحظتا التنضيد المحليتان: أمر `\atop` وعنوان المبرهنة الطويل.
- تحققت المراجعة النهائية من تطابق المتن مع المسار الرياضي المعتمد وسلامة التصنيفات والمراجع الداخلية.
- أُغلق التصحيحان النصيان النهائيان: توضيح اعتماد الفصل على حزمة الغربال الكبير دون استعمال مبرهنة Bombieri--Vinogradov، وحذف الاختصار غير المعرّف `PVG`.
- اكتملت مزامنة ملفات التتبع، وأصبح الفصل جاهزًا لقرار المالك بشأن تصنيف `REVIEWED`.

## النتيجة المؤلَّفة

لكل ثابت \(A>0\):

\[
V_\psi(x,Q)=
\sum_{q\le Q}
\sum_{\substack{a\bmod q\\(a,q)=1}}
\left|\psi(x;q,a)-\frac{x}{\varphi(q)}\right|^2
\ll_A xQ\log x
\]

بانتظام في

\[
x\ge3,
\qquad
\frac{x}{(\log x)^A}\le Q\le x.
\]

الثابت غير فعال بسبب استعمال Siegel--Walfisz للموصلات الصغيرة.

## الخطوة التالية

يحتاج الفصل الآن إلى قرار صريح من مالك المشروع بشأن:

1. ترقية الحالة إلى `REVIEWED`.
2. إبقاء PR #26 مسودة أو تحويله إلى Ready for review.
3. الإذن بالدمج في `main` أو إبقائه غير مدمج.

لا يُستنتج أي من هذه القرارات تلقائيًا من نجاح المراجعة والبناء.
