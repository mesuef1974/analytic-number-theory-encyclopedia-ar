# تقدم المشروع

## الحالة العامة

- **الإصدار التطويري الحالي:** `0.30.0-dev`
- **الفصول:** 1--26 موجودة ومندمجة على `main`.
- **المرحلة الحالية:** ما بعد إغلاق P1؛ تنفيذ حواجز الإصدار المتبقية.
- **المراجعة الشاملة:** `PASS / OPEN-MAJORS 0 / TECHNICAL-BLOCKERS 0`
- **P1 العلمي:** `APPROVED / ISSUE #64 CLOSED / PR #65 MERGED`
- **الموسوعة:** `NOT-RELEASE-READY`
- **آخر تحديث:** 2026-07-28

```text
CHAPTERS-1--26          = IN MANUSCRIPT / MERGED
VERSION                 = 0.30.0-dev
RELEASE-WIDE-REVIEW     = PASS
ISSUE-53                = CLOSED
PR-54                   = MERGED
P1-ISSUE                = #64 / CLOSED
P1-PR                   = #65 / MERGED
P1-REVIEW               = APPROVED
P1-BLOCKERS             = 0
P1-MERGE-HEAD           = 1a96640ec8e5744b076afc91c58eabe893a43001
OWNER-ADOPTION          = CONFIRMED
OPEN-MAJORS             = 0
TECHNICAL-BLOCKERS      = 0
FINAL-PDF               = PASS / 321 PAGES
FINAL-PDF-SIZE-BYTES    = 1212922
FINAL-PDF-SHA256        = 1A694020B0F787285D1363F75B24E3A1B02D2693D281868B22C1696F116C0439
FATAL-BUILD-ERRORS      = 0
UNDEFINED-REFERENCES    = 0
UNDEFINED-CITATIONS     = 0
OVERFULL-HBOX >= 20pt   = 0
INDEX-ISSUE             = #55 / RELEASE-BLOCKER
EXERCISES-ISSUE         = #56 / NON-BLOCKING
FORWARD-REFS-ISSUE      = #57 / NON-BLOCKING
RELEASE-READY           = NO
```

## لوحة التقدم

| المكوّن | الحالة |
|---|---|
| الفصول 1--26 | `MERGED / GOVERNANCE-RECONCILED` |
| سجل النتائج | `252 / 252 / ZERO MISSING / ZERO DUPLICATES` |
| النتائج المفعلة بلا حوكمة | `0` |
| BibTeX | `90 CITATION KEYS / 106 ENTRIES / ZERO MISSING / ZERO DUPLICATES` |
| DOI | `55/56 RESOLVER PASS / 1 LEGACY EXCEPTION` |
| الفحص البصري | `PASS / VISIBLE-BLOCKERS 0` |
| البناء النهائي | `PASS / 321 PAGES / FATAL ERRORS 0` |
| المراجعة المستقلة النهائية | `PASS` |
| P1 العلمي | `APPROVED / BLOCKERS 0` |
| PR #65 | `MERGED` |
| Issue #64 | `CLOSED` |
| الموسوعة الكاملة | `NOT-RELEASE-READY` |

## قرار المالك بعد المراجعة

اعتمد المالك الإصدار `0.30.0-dev` كجاهز للدمج وصرّح صراحة بدمج PR #54. تم الدمج مع إبقاء `RELEASE-READY = NO`.

ثم اعتمد المالك إغلاق مرحلة P1 العلمية وصرّح بدمج PR #65. دُمج الطلب عند `1a96640ec8e5744b076afc91c58eabe893a43001` بعد مراجعة مستقلة بحكم `APPROVED` وصفر حواجز P1، مع إبقاء الإصدار المستقر محجوبًا.

صُنفت الأعمال المؤجلة كما يلي:

1. **الفهارس — Issue #55:** غير حاجزة للدمج، لكنها حاجز صريح أمام الجاهزية للإصدار.
2. **التمارين والحلول — Issue #56:** دين بيداغوجي غير حاجز.
3. **الإحالات الأمامية — Issue #57:** دين تحريري غير حاجز؛ لا توجد إحالات معطوبة حاليًا.

الديون المقبولة تشمل DOI مقال Chen لعام 1973 كاستثناء قديم `resolver-404` موثق، و341 حالة `Overfull \hbox` أصغر من 20 نقطة، أقصاها 19.38495 نقطة، بعد نجاح الفحص البصري.

## الخطوة التالية

استكمال حواجز الإصدار المتبقية وإصدار قرار مالك مستقل قبل أي تغيير إلى `RELEASE-READY = YES`. أما Issue #56 وIssue #57 فيبقيان مساري تحسين غير حاجزين.
