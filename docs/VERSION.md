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
BASE-MAIN              = 9d02c583d416053550d22dfd7acc44d9c264a02c
BRANCH                 = agent/chapter-12-siegel-walfisz-v0.16.0
MODE                   = EVIDENCE-FIRST / AUTHORED
PRE-AUTHORING-GATE     = CLOSED / PASS
POST-AUTHORING-GATE    = CLOSED / PASS
CHAPTER-12             = VERIFIED
FINAL-HEAD             = b2fae17de3e598b2d3ec96e77ca3d24b191229fc
QUALITY-CHECKS         = RUN-283 / SUCCESS
PDF-BUILD              = RUN-278 / SUCCESS
PDF-ARTIFACT-SHA256    = a8ead92a87ab43d3e7779fd58c936e6f98f97f0d268ff913441421f48c30df75
EXPLICIT-FORMULA       = CITED-INPUT
SIEGEL-CONSTANT        = INEFFECTIVE
BOMBIERI-VINOGRADOV    = DEFERRED
INDEPENDENT-REVIEW     = NOT YET STARTED
RELEASE-READY          = NO
```

## النتيجة المركزية

لكل \(A>0\)، توجد ثوابت غير فعالة في المسار العام بحيث، بانتظام عندما
\(q\le(\log x)^A\) و\((a,q)=1\):

\[
\psi(x;q,a)
=
\frac{x}{\varphi(q)}
+O_A\!\left(xe^{-c_A\sqrt{\log x}}\right).
\]

وسجل الفصل أيضًا صيغة الادخار اللوغاريتمي الاعتباطي والصيغ الموافقة للدالتين
\(\vartheta(x;q,a)\) و\(\pi(x;q,a)\).

## الفصل بين النتائج

1. الفصل العاشر يثبت النتيجة النوعية لترديد ثابت.
2. الفصل الثاني عشر يثبت الانتظام للترديدات \(q\le(\log x)^A\).
3. Bombieri--Vinogradov نتيجة متوسطية مؤجلة إلى فصل لاحق.

## النزاهة البرهانية

- حد PNT الفعال والصيغة الصريحة المقطوعة مسجلان `CITED`.
- صيغة بيرون العامة وتحويل المسار الكاملان ما يزالان دينين معلنين.
- حد الصفر الاستثنائي عُزل قبل امتصاصه.
- تدخل مبرهنة Siegel عند عقدة واحدة محددة، ومنها تأتي عدم فعالية الثابت النهائي.
- لا يستعمل الفصل Bombieri--Vinogradov أو Linnik أو GRH.

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
