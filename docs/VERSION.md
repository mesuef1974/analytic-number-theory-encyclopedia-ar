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
CHAPTER-14                   = REVIEWED / MERGED
PR                           = #26 / MERGED
MERGE-COMMIT                 = 8c208e1c43f42fda754e4ed3dadb51a0256b5e60
ISSUE                        = #25 / CLOSED
BRANCH                       = agent/chapter-14-barban-davenport-halberstam-v0.18.0
PRE-AUTHORING-GATE           = CLOSED
PASS-FOR-AUTHORING           = YES / OWNER-AUTHORIZED
AUTHORING                    = COMPLETE
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
OWNER-REVIEWED-DECISION      = YES
MERGE                        = COMPLETE
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

## إغلاق المرحلة

اعتمد مالك المشروع الفصل الرابع عشر بحالة `REVIEWED`. حُوّل PR #26 من Draft إلى Ready for review ثم دُمج في `main` عند الالتزام `8c208e1c43f42fda754e4ed3dadb51a0256b5e60`. لا يترتب على هذا الإغلاق تصنيف الفصل أو المجلد بأنه `RELEASE-READY`.

## المرحلة السابقة

```text
CHAPTER-13          = REVIEWED / MERGED
PR-22               = MERGED
MERGE-COMMIT        = 2e28e51bd8334cd748d59f1e8cc9998975058a8c
GOVERNANCE-COMMIT   = d2588c893d8d07be1e961813628e1bb210e0eece
RELEASE-READY       = NO
```
