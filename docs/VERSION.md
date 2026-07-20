# الإصدار الحالي

```text
0.16.0-dev
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

تستهدف `0.16.0-dev` الفصل الثاني عشر:

**مبرهنة Siegel--Walfisz والتوزيع المنتظم للأعداد الأولية في المتتاليات الحسابية.**

```text
BASE-MAIN             = 9d02c583d416053550d22dfd7acc44d9c264a02c
BRANCH                = agent/chapter-12-siegel-walfisz-v0.16.0
MODE                  = EVIDENCE-FIRST / PRE-AUTHORING
EVIDENCE-LEDGER       = CREATED
PROOF-MAP             = CREATED
PERRON-DEBT-AUDIT     = PASS-FOR-CITED-INPUT-ROUTE
LOGIC-AUDIT           = PASS
PRE-AUTHORING-GATE    = CLOSED / PASS
AUTHORING             = AUTHORIZED / NOT YET STARTED
BOMBIERI-VINOGRADOV   = DEFERRED
RELEASE-READY         = NO
```

## النطاق المعتمد

يفصل الفصل بين:

1. نتيجة الترديد الثابت في الفصل العاشر.
2. مبرهنة Siegel--Walfisz للترديدات
   \(q\le(\log x)^A\).
3. مبرهنة Bombieri--Vinogradov المتوسطية المؤجلة إلى فصل لاحق.

الصيغة المركزية المخططة هي

\[
\psi(x;q,a)
=
\frac{x}{\varphi(q)}
+
O_A\!\left(xe^{-c_A\sqrt{\log x}}\right),
\qquad q\le(\log x)^A,
\]

مع وسم صريح بأن الثابت العام غير فعال بسبب استعمال مبرهنة Siegel في امتصاص مساهمة الصفر الاستثنائي.

## المرحلة السابقة

أغلقت `0.15.0-dev` إداريًا بعد دمج الفصل الحادي عشر ومراجعة حوكمته:

```text
CHAPTER-11          = REVIEWED / MERGED
PR-17               = MERGED
ISSUE-18            = CLOSED
CHAPTER-11-MERGE    = fb1571eaa6328eac597ddbebda79b09d0ebd1696
GOVERNANCE-PR-19    = MERGED
GOVERNANCE-MERGE    = 9d02c583d416053550d22dfd7acc44d9c264a02c
```
