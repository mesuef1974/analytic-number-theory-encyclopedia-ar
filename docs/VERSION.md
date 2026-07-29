# الإصدار الحالي

```text
0.30.0-dev
```

هذا الملف هو **المصدر الوحيد المعتمد لرقم الإصدار وحالة المرحلة الحالية**.

## الحالة المعتمدة

```text
VERSION                 = 0.30.0-dev
VOLUME-IDENTITY         = المجلد الأول من مشروع موسوعي متعدد المجلدات (منذ P2)
CHAPTERS                = 1--26 / MERGED (main) — فرع P2 يضيف طبقة بصرية
                          وتصحيحات إخراجية فوق المتن نفسه، لا فصولًا جديدة
RELEASE-WIDE-ISSUE      = #53 / CLOSED
RELEASE-WIDE-PR         = #54 / MERGED
RELEASE-WIDE-REVIEW     = PASS
P1-ISSUE                = #64 / CLOSED
P1-PR                   = #65 / MERGED
P1-REVIEW               = APPROVED
P1-BLOCKERS             = 0
P1-MERGE-HEAD           = 1a96640ec8e5744b076afc91c58eabe893a43001
P2-BRANCH               = agent/release-p2-external-review-production-v0.31.0-dev
P2-ISSUE                = لم يُفتح بعد؛ ينتظر إذن المالك
P2-PR                   = لم يُفتح بعد؛ ينتظر إذن المالك
P2-SCOPE                = طبقة بصرية (P2-01) + بطاقات جبهات مؤرَّخة (P2-06) +
                          تدقيق براهين مستقل (P2-04) + إصلاح تسرّب فهارس (P2-05)
                          + إصلاح تشوّه بطاقات الحالة (تحكيم صريح) + هوية
                          المجلد الأول (P2-C جزئي) + خطة المجلدات ٢-٥
P2-BLOCKED              = P2-02 (وسم PDF/UA) — عطل منبع في حزمة latex-lab
                          بتوزيعة MiKTeX المحلية، موثَّق ومنفصل عن مصدر الكتاب
OPEN-MAJORS             = 0
TECHNICAL-BLOCKERS      = 1 (P2-02، خارج نطاق المشروع)
OWNER-ADOPTION          = CONFIRMED (حتى P1)؛ P2 قيد المراجعة
MERGED-REVIEW-HEAD      = 6fbdb370d5df2d23af5fc6c47f05f2a8ded5f9a4
MAIN-MERGE-COMMIT       = b8396c932cbdd50d69d68f202663bc91aefc0c82
FINAL-PDF (P1, main)    = PASS / 321 PAGES
FINAL-PDF-SHA256 (P1)   = 1A694020B0F787285D1363F75B24E3A1B02D2693D281868B22C1696F116C0439
DRAFT-PDF (P2, branch)  = PASS / 314 PAGES
DRAFT-PDF-SHA256 (P2)   = c9b73b0f60081159d733e0854bf6cb1fc10d8d6562405f79a1220dcd5fb918d2
RELEASE-PDF (P2, branch)= PASS / 292 PAGES
RELEASE-PDF-SHA256 (P2) = 796b75ce62055a926651188a6a57b3cd97e52fc294a55c27eb1b00d0ecaabd67
UNDEFINED-REFERENCES    = 0
UNDEFINED-CITATIONS     = 0
FATAL-ERRORS            = 0
OVERFULL-HBOX >= 20pt   = 0
INDEX-TRACKING          = #55 / RELEASE-BLOCKER (P2-05 يُصلح الجزء الظاهر
                          للقارئ؛ إغلاق Issue #55 نفسه قرار مالك منفصل)
EXERCISES-TRACKING      = #56 / NON-BLOCKING
FORWARD-REFS-TRACKING   = #57 / NON-BLOCKING
RELEASE-READY           = NO
STABLE-RELEASE          = BLOCKED
```

اعتمد المالك المراجعة الشاملة النهائية وصرّح بدمج PR #54، فدُمج المسار وأُغلق Issue #53. ثم أُغلقت مرحلة P1 العلمية بعد مراجعة مستقلة بحكم `APPROVED` وصفر حواجز، وصرّح المالك بدمج PR #65، فدُمج عند `1a96640ec8e5744b076afc91c58eabe893a43001` وأُغلق Issue #64.

بعد ذلك فُتح فرع P2 (تقييم خارجي إخراجي/تحريري) من `main` دون Issue/PR بعد؛ يضيف طبقة بصرية، ويُصلح عيبين حرِجين حقيقيين اكتُشفا هذه الجلسة نفسها (تسرّب نصّي في الفهارس، وتشوّه بطاقات الحالة العلمية داخل بيئات مركزية)، ويُثبت هوية «المجلد الأول» للمشروع، ويضع خطة تفصيلية للمجلدات ٢–٥. **لا شيء من هذا مدموج بـ`main` بعد.** لا يعني إنجاز P2 محليًّا الجاهزية للإصدار المستقر؛ تبقى حواجز الإصدار وقرار مالك مستقل — بما فيه فتح Issue/PR لهذا الفرع أصلًا — مطلوبة قبل أي دمج أو تغيير `RELEASE-READY` إلى `YES`.
