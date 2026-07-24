# الإصدار الحالي

```text
0.18.0-dev
```

هذا الملف هو **المصدر الوحيد المعتمد لرقم الإصدار وحالة المرحلة الحالية**. تُحدَّث النسخ المكررة في بقية الملفات بواسطة:

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
BASE-MAIN                    = d2588c893d8d07be1e961813628e1bb210e0eece
BRANCH                       = agent/chapter-14-barban-davenport-halberstam-v0.18.0
CHAPTER-14                   = AUTHORED-DRAFT / FINAL-REVIEW-CHANGES-REQUIRED
ISSUE                        = #25 / OPEN
PR                           = #26 / DRAFT / OPEN / UNMERGED
PRE-AUTHORING-GATE           = CLOSED
PASS-FOR-AUTHORING           = YES / OWNER-AUTHORIZED
AUTHORING                    = COMPLETE-AS-DRAFT
RESULTS                      = 5 / RESERVED
LOGIC-AUDIT                  = PASS
REFERENCE-AUDIT              = PASS
INDEPENDENT-REVIEW           = APPROVED-WITH-NONBLOCKING-CORRECTIONS
NONBLOCKING-CORRECTIONS      = 5 / 5 CLOSED
POST-AUTHORING-BUILD-AUDIT   = PASS
PDF-BUILD                    = PASS / 208 PAGES
FINAL-MANUSCRIPT-REVIEW      = CHANGES-REQUIRED
MATHEMATICAL-BLOCKERS        = 0
TEXTUAL-BLOCKERS             = 2
TRACKING-DOCS-SYNC           = IN PROGRESS
QUALITY-CHECKS               = PASS EXCEPT FINAL TEXTUAL CORRECTIONS
REVIEWED                     = NO
MERGE                        = NOT AUTHORIZED
RELEASE-READY                = NO
```

## النتيجة المؤلَّفة

لكل ثابت `A>0`، وبانتظام في

```text
x >= 3,
x/(log x)^A <= Q <= x,
```

يثبت الفصل الحد

```text
V_psi(x,Q) = sum_{q<=Q} sum_{a mod q, (a,q)=1}
               |psi(x;q,a) - x/phi(q)|^2
             <<_A x Q log x.
```

الثابت غير فعال في المسار الحالي بسبب مدخل Siegel--Walfisz للموصلات الصغيرة. لا يدعي الفصل الصيغة التقاربية لمونتغمري--هولي، ولا مبرهنة باربان العامة في كل المجالات.

## ما يمنع تصنيف `REVIEWED`

1. تصحيح ملاحظة المقارنة مع الفصل الثالث عشر بحيث تميز بين مبرهنة Bombieri--Vinogradov وحزمة الغربال الكبير المستعملة فعلًا.
2. حذف الاختصار الدخيل غير المعرّف `PVG` من قسم الحدود المفتوحة.
3. مزامنة `PROGRESS.md` و`CHANGELOG.md` مع الحالة الحالية.
4. إعادة بناء نهائية بعد التصحيحين النصيين وتسجيل نتيجة المراجعة.

## المرحلة السابقة

```text
CHAPTER-13          = REVIEWED / MERGED
PR-22               = MERGED
MERGE-COMMIT        = 2e28e51bd8334cd748d59f1e8cc9998975058a8c
GOVERNANCE-COMMIT   = d2588c893d8d07be1e961813628e1bb210e0eece
RELEASE-READY       = NO
```
