# الإصدار الحالي

```text
0.18.0-dev
```

هذا الملف هو **المصدر الوحيد المعتمد لرقم الإصدار وحالة المرحلة الحالية**.

## معنى رقم الإصدار

- الرقم الأول: إصدار موسوعي رئيسي.
- الرقم الثاني: مرحلة علمية كبيرة أو فصل رئيسي.
- الرقم الثالث: تحديث تحريري أو تقني.
- اللاحقة `dev`: النسخة لا تزال قيد التطوير ولم تُعتمد للنشر.

## المرحلة المغلقة

```text
CHAPTER-14                   = REVIEWED / MERGED
PR                           = #26 / MERGED
MERGE-COMMIT                 = 8c208e1c43f42fda754e4ed3dadb51a0256b5e60
ISSUE                        = #25 / CLOSED
PASS-FOR-AUTHORING           = YES / OWNER-AUTHORIZED
AUTHORING                    = COMPLETE
RESULTS                      = 5 / ACTIVE
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

يثبت الفصل:

```text
V_psi(x,Q) <<_A x Q log x.
```

الثابت غير فعال بسبب مدخل Siegel--Walfisz للموصلات الصغيرة.

## المرحلة التالية

أُغلقت مزامنة ملفات حوكمة الفصل الرابع عشر. يجوز الآن فتح المرحلة:

```text
VERSION-NEXT  = 0.19.0-dev
CHAPTER-NEXT  = 15
TOPIC-NEXT    = BASIC SIEVE METHODS / SELBERG SIEVE / PARITY BARRIER
STATE-NEXT    = AUTHORIZED-FOR-INITIALIZATION / NOT YET AUTHORED
```

لا يبدأ التأليف قبل إنشاء سجل الأدلة وخريطة البرهان وإغلاق بوابة ما قبل التأليف. لا يترتب على الانتقال إلى المرحلة التالية تصنيف `RELEASE-READY`.
