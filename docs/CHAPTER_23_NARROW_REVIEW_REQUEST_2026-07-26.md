# طلب مراجعة ضيقة لتصحيحات بوابة الفصل الثالث والعشرين

```text
CHAPTER            = 23
VERSION            = 0.27.0-dev
REVIEW-STAGE       = PRE-AUTHORING NARROW RE-REVIEW
PRIMARY-REVIEW     = CHANGES-REQUIRED / 0 BLOCKERS
CORRECTIONS        = APPLIED
PASS-FOR-AUTHORING = NO
RESULTS            = 10 RESERVED / NON-CITABLE
MERGE              = NOT AUTHORIZED
```

## نطاق المراجعة الضيقة

راجع فقط إغلاق الملاحظات الثلاث الواردة في:

`docs/CHAPTER_23_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-26.md`

### 1. منع ازدواج صيغة ريمان--فون مانغولت

تحقق من أن:

- خريطة البرهان لم تعد تسجل صيغة ريمان--فون مانغولت كمبرهنة جديدة `PROVED-HERE` في الفصل 23.
- `ANT-DEF-23-01` يحيل صراحة إلى `ANT-THM-06-06` في الفصل 6.
- سجل النتائج لا يحجز معرّفًا ثانيًا للصيغة نفسها.
- بقي عدد معرفات الفصل 23 عشرة دون تصادم.

### 2. تحديث حالة Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh

تحقق من تسجيل الورقة بوصفها منشورة ومحكمة:

- *Acta Arithmetica* 214 (2024), 357--376.
- مع إبقاء arXiv:2306.04799 معرّفًا سابقًا، لا وصفًا لحالة النشر الحالية.

### 3. استكمال Rudnick--Sarnak

تحقق من البيانات:

Z. Rudnick and P. Sarnak, *Zeros of principal L-functions and random matrix theory*, Duke Math. J. 81 (1996), 269--322.

## ملفات المراجعة

1. `docs/CHAPTER_23_EVIDENCE_LEDGER_2026-07-26.md`
2. `docs/CHAPTER_23_PROOF_MAP_2026-07-26.md`
3. `docs/RESULTS_REGISTRY_CHAPTER_23.md`
4. `docs/CHAPTER_23_PRE_AUTHORING_AUDIT_2026-07-26.md`
5. `docs/CHAPTER_23_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-26.md`
6. مصدر الفصل 6 للتحقق من `ANT-THM-06-06`.

## المخرج المطلوب

أنشئ ملفًا جديدًا فقط:

`docs/CHAPTER_23_INDEPENDENT_NARROW_REVIEW_2026-07-26.md`

ويجب أن يتضمن:

```text
REVIEWED-HEAD      = <full SHA>
REVIEWER           = INDEPENDENT LOCAL CLIENT
REVIEW-STAGE       = PRE-AUTHORING NARROW RE-REVIEW
VERDICT            = PASS | CHANGES-REQUIRED | FAIL
BLOCKERS           = <integer>
PASS-FOR-AUTHORING = YES | NO
RESULTS-CITABLE    = NO
MERGE              = NOT AUTHORIZED
```

لا تعدّل ملفات الحزمة ولا تكتب متن الفصل. لا تمنح `PASS-FOR-AUTHORING = YES` إلا مع `VERDICT = PASS` و`BLOCKERS = 0`.
