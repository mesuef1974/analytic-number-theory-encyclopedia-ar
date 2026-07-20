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

أُغلقت مرحلة `0.16.0-dev` الخاصة بالفصل الثاني عشر علميًا وحوكميًا بعد المراجعة المستقلة والدمج، مع بقاء النسخة تطويرية وغير جاهزة للإصدار.

**مبرهنة Siegel--Walfisz والتوزيع المنتظم للأعداد الأولية في المتتاليات الحسابية.**

```text
MAIN-HEAD              = b1f09a3388aa34194eb8836b6977fe05f86aee7a
CHAPTER-12             = REVIEWED / MERGED
PR-20                  = MERGED
INDEPENDENT-REVIEW     = APPROVED
MATHEMATICAL-BLOCKERS  = 0
REFERENCE-BLOCKERS     = 0
TYPOGRAPHIC-BLOCKERS   = 0
QUALITY-CHECKS         = RUN-311 / SUCCESS
PDF-BUILD              = RUN-306 / SUCCESS
LOCAL-SYNC             = PASS / FF-ONLY
SOURCE-BUILD           = PASS
LOCAL-PDF-PAGES        = 184
LOCAL-PDF-SHA256       = 3BF0BCE828DDF09C03D6527117992806FAD06010B161FC1B242472D0B5367749
EXPLICIT-FORMULA       = CITED / COMPOSITE-INPUT
SIEGEL-CONSTANT        = INEFFECTIVE
BOMBIERI-VINOGRADOV    = DEFERRED
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

- حد PNT الفعال والصيغة الصريحة المقطوعة مسجلان `CITED`، والثانية موصوفة بدقة بأنها `COMPOSITE-INPUT`.
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
