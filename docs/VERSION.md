# الإصدار الحالي

```text
0.17.0-dev
```

هذا الملف هو **المصدر الوحيد المعتمد لرقم الإصدار**. تُحدَّث النسخ المكررة في بقية الملفات بواسطة:

```powershell
.\scripts\sync-version.ps1
```

## معنى رقم الإصدار

- الرقم الأول: إصدار موسوعي رئيسي.
- الرقم الثاني: مرحلة علمية كبيرة أو فصل رئيسي.
- الرقم الثالث: تحديث تحريري أو تقني.
- اللاحقة `dev`: النسخة لا تزال قيد التطوير ولم تُعتمد للنشر.

## المرحلة الحالية

تستهدف `0.17.0-dev` الفصل الثالث عشر:

**مبرهنة Bombieri--Vinogradov والتوزيع المتوسطي للأعداد الأولية في المتتاليات الحسابية.**

```text
BASE-MAIN              = 607c6f8ad76f8085828f49ce6b566c846950ab2a
BRANCH                 = agent/chapter-13-bombieri-vinogradov-v0.17.0
CHAPTER-13             = REVIEWED / MERGED
PRE-AUTHORING-GATE     = CLOSED / PASS
POST-AUTHORING-AUDIT   = PASS
LOGIC-AUDIT            = PASS
REFERENCE-VERIFICATION = PASS
RESULTS                = 11
QUALITY-CHECKS         = RUN-372 / SUCCESS
PDF-BUILD              = RUN-366 / SUCCESS
INDEPENDENT-REVIEW     = COMPLETED / APPROVED-WITH-NONBLOCKING-CORRECTIONS
PROMOTION              = OWNER-AUTHORIZED / EXECUTED
PR-22                  = MERGED
MERGE-COMMIT            = 2e28e51bd8334cd748d59f1e8cc9998975058a8c
RELEASE-READY          = NO
```

## النتيجة المركزية

لكل `A>0`، إذا

```text
Q <= x^(1/2) / (log x)^(A+3),
```

فإن متوسط أكبر خطأ في `psi(y;q,a)` على `q<=Q` والفئات المختزلة و`y<=x` هو من رتبة `x/(log x)^A`.

الثابت العام غير فعال بسبب استعمال Siegel--Walfisz للموصلات الصغيرة. لا يدعي الفصل Elliott--Halberstam أو مستوى توزيع عامًا أكبر من `1/2`.

## المرحلة السابقة

```text
CHAPTER-12          = REVIEWED / MERGED
PR-20               = MERGED
GOVERNANCE-PR-21    = MERGED
GOVERNANCE-MERGE    = 607c6f8ad76f8085828f49ce6b566c846950ab2a
LOCAL-SOURCE-BUILD  = PASS / 184 PAGES
RELEASE-READY       = NO
```
