# التحقق المحلي من Artifact الفصل الثاني عشر

## الحالة

```text
DATE                    = 2026-07-20
BRANCH                  = agent/chapter-12-siegel-walfisz-v0.16.0
VERIFIED-HEAD           = 2794c41e4bb1ef8a0cf43620de1184d1246d79cf
QUALITY-CHECKS          = RUN-295 / SUCCESS
PDF-BUILD               = RUN-290 / SUCCESS
ARTIFACT-ID             = 8474844277
ARTIFACT-ARCHIVE-SHA256 = 39B4ADCF938EDB750327B55E155C36FAF86EAFDE0448FE7B17A69FFEC1C42393
ARTIFACT-DOWNLOADED     = YES
LOCAL-PDF-OPEN          = PASS
LOCAL-PDF-PREFLIGHT     = PASS
LOCAL-VISUAL-SAMPLE     = PASS / PAGES 1, 170, 184
PDF-PAGES               = 184
PDF-SIZE-BYTES          = 740994
PDF-SHA256              = 71D8B628896529F100659AAA1029E7E53F793C529E5D568BB8F8BF5FA8FB6549
PDF-PAGE-SIZE           = A4
PDF-ENCRYPTED           = NO
SOURCE-SYNC-IN-AGENT    = BLOCKED / NO-DNS-TO-GITHUB
SOURCE-BUILD-IN-AGENT   = NOT CLAIMED
RELEASE-READY           = NO
```

## ما تم فعليًا

نُزّل ملف `analytic-number-theory-encyclopedia-preview.pdf` من Artifact الخاص بتشغيل GitHub Actions رقم 290 إلى بيئة محلية مستقلة، ثم:

1. فُك ضغط ملف Artifact محليًا.
2. طُبق فحص فتح وبنية PDF بواسطة `pdfinfo` وPyMuPDF.
3. تحقق أن الملف غير مشفر، قابل للفتح، بحجم A4، وليس ملفًا ممسوحًا ضوئيًا.
4. عُدت الصفحات: 184 صفحة.
5. حُسب SHA256 مباشرة من ملف PDF المحلي.
6. رُندرت عينات من الصفحات 1 و170 و184 وفُحصت بصريًا من دون ظهور قص أو تراكب أو مربعات سوداء أو تلف في العربية والمعادلات.

## تفسير قيم SHA256

- `ARTIFACT-ARCHIVE-SHA256` هو digest لأرشيف ZIP الذي أنشأه GitHub Actions.
- `PDF-SHA256` هو SHA256 لملف PDF بعد فك الأرشيف محليًا.
- لا يفترض أن تتطابق القيمتان لأنهما تخصان ملفين مختلفين.

## حد الادعاء

هذا **تحقق محلي لملف PDF الناتج من CI**، وليس بناء مصدر محليًا من شجرة Git. تعذر استنساخ المستودع داخل بيئة الوكيل بسبب عدم توفر DNS خارجي مباشر إلى GitHub؛ لذلك لا تسجل الوثيقة `SOURCE-BUILD = PASS`.

لإجراء بناء مصدر محلي متزامن على جهاز Windows المالك، استعمل:

```powershell
cd "D:\analytic-number-theory-encyclopedia-ar"
.\scripts\sync-build.ps1 -Open -CommitReceipt -Push
```

ينفذ السكربت مزامنة `ff-only`، ثم XeLaTeX وBiber، ويولد `docs/LOCAL_BUILD_RECEIPT.md` من النتائج الفعلية على الجهاز المحلي.
