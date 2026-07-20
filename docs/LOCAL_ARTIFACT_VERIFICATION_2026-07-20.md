# التحقق المحلي من Artifact الفصل الثاني عشر

## الحالة

```text
DATE                    = 2026-07-20
BRANCH                  = agent/chapter-12-siegel-walfisz-v0.16.0
VERIFIED-CI-HEAD        = e6c87affd453f6088b0d1f5400432f7e4228ed57
QUALITY-CHECKS          = RUN-287 / SUCCESS
PDF-BUILD               = RUN-282 / SUCCESS
ARTIFACT-ID             = 8474272515
ARTIFACT-DOWNLOADED     = YES
LOCAL-PDF-OPEN          = PASS
LOCAL-PDF-PREFLIGHT     = PASS
PDF-PAGES               = 184
PDF-SIZE-BYTES          = 740994
PDF-SHA256              = 8614C02802E080121875CB0AE7FFD06194D73236E226DB1A41112A8D9E30D763
SOURCE-SYNC-IN-AGENT    = BLOCKED / NO-DNS-TO-GITHUB
SOURCE-BUILD-IN-AGENT   = NOT CLAIMED
RELEASE-READY           = NO
```

## ما تم فعليًا

نُزّل ملف `analytic-number-theory-encyclopedia-preview.pdf` من Artifact الخاص بتشغيل GitHub Actions رقم 282 إلى بيئة محلية مستقلة، ثم:

1. فُك ضغط ملف Artifact محليًا.
2. طُبق فحص فتح وبنية PDF بواسطة `pdfinfo` وPyMuPDF.
3. تحقق أن الملف غير مشفر وقابل للفتح وغير ممسوح ضوئيًا.
4. عُدّت الصفحات: 184 صفحة.
5. حُسب SHA256 مباشرة من ملف PDF المحلي.
6. طابق SHA256 الملف النصي المرفق داخل Artifact.

## حد الادعاء

هذا **تحقق محلي لملف PDF الناتج من CI**، وليس بناء مصدر محليًا من شجرة Git. تعذر استنساخ المستودع داخل بيئة الوكيل بسبب عدم توفر DNS خارجي مباشر إلى GitHub؛ لذلك لا تسجل الوثيقة `SOURCE-BUILD = PASS`.

لإجراء بناء مصدر محلي متزامن على جهاز Windows المالك، استعمل:

```powershell
cd "D:\analytic-number-theory-encyclopedia-ar"
.\scripts\sync-build.ps1 -Open -CommitReceipt -Push
```

ينفذ السكربت مزامنة `ff-only`، ثم XeLaTeX وBiber، ويولد `docs/LOCAL_BUILD_RECEIPT.md` من النتائج الفعلية على الجهاز المحلي.
