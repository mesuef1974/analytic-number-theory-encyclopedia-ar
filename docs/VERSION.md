# الإصدار الحالي

```text
0.18.0-dev
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

تستهدف `0.18.0-dev` الفصل الرابع عشر:

**مبرهنة Barban--Davenport--Halberstam ومتوسط مربعات أخطاء توزيع الأعداد الأولية في المتتاليات الحسابية.**

```text
BASE-MAIN              = d2588c893d8d07be1e961813628e1bb210e0eece
BRANCH                 = agent/chapter-14-barban-davenport-halberstam-v0.18.0
CHAPTER-14             = RESEARCH-INTAKE
ISSUE                  = #25 / OPEN
PRE-AUTHORING-GATE     = OPEN
AUTHORING              = BLOCKED
RESULTS                = 0 / NOT RESERVED
REFERENCE-VERIFICATION = NOT STARTED
PROOF-MAP              = NOT STARTED
QUALITY-CHECKS         = PENDING
PDF-BUILD              = NOT APPLICABLE / NO MANUSCRIPT DELTA
RELEASE-READY          = NO
```

## الكمية المرشحة

تبدأ المرحلة بدراسة التباين

```text
V(x,Q) = sum_{q<=Q} sum_{a mod q, (a,q)=1}
         |psi(x;q,a) - x/phi(q)|^2.
```

هذه صيغة عمل أولية فقط. يجب تثبيت التطبيع ومجال `Q` والتمييز بين الحد العلوي والصيغة التقاربية ذات الحد الرئيسي قبل إنشاء متن الفصل أو حجز نتائج.

## بوابة ما قبل التأليف

لا يبدأ التأليف قبل:

1. التحقق من المصادر الأصلية لـBarban وDavenport وHalberstam.
2. تثبيت النطاق الدقيق للمتغيرين `x` و`Q`.
3. تحديد ما سيُقتبس وما سيُثبت داخليًا.
4. إعداد خريطة برهان وتدقيق الثوابت والفعالية.
5. إصدار حكم صريح `PASS-FOR-AUTHORING`.

## المرحلة السابقة

```text
CHAPTER-13          = REVIEWED / MERGED
PR-22               = MERGED
MERGE-COMMIT        = 2e28e51bd8334cd748d59f1e8cc9998975058a8c
GOVERNANCE-COMMIT   = d2588c893d8d07be1e961813628e1bb210e0eece
RELEASE-READY       = NO
```
