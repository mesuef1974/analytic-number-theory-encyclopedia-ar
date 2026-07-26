# طلب مراجعة ضيقة لتصحيحات بوابة الفصل الثاني والعشرين

```text
TARGET-BRANCH       = agent/chapter-22-moments-extreme-values-v0.26.0
TARGET-HEAD         = 9f56ae57afaa1e37eee55c54dc94a5e01563b004
PR                  = #44 / DRAFT / OPEN
AUTHORING           = BLOCKED
PASS-FOR-AUTHORING  = NO
```

## نطاق المراجعة الضيقة

راجع فقط إغلاق الملاحظات السبع الواردة في:

`docs/CHAPTER_22_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-25.md`

مع مقارنة الملفات المصححة:

- `docs/CHAPTER_22_EVIDENCE_LEDGER_2026-07-25.md`
- `docs/CHAPTER_22_PROOF_MAP_2026-07-25.md`
- `docs/RESULTS_REGISTRY_CHAPTER_22.md`
- `docs/CHAPTER_22_PRE_AUTHORING_AUDIT_2026-07-25.md`

## الأسئلة الحاسمة

1. هل صُحح إسناد حد خطأ العزم الثاني إلى Ingham بلا مبالغة تاريخية؟
2. هل فُصل Harper كـpreprint عن Soundararajan المنشور والمحكّم؟
3. هل أصبحت أداة ضبط غير القطري مسماة ومحددة بما يكفي لفتح التأليف؟
4. هل ثُبتت سنة Ingham الرسمية 1928 ومجال Soundararajan عند `k >= 0` الثابت؟
5. هل توزيع المعرفات العشرة بعد إضافة المعادلة الوظيفية التقريبية متسق؟
6. هل بيانات Florea مكتملة؟
7. هل بقي عدم الدور مغلقًا؟

## المخرج المطلوب

أنشئ ملفًا جديدًا فقط:

`docs/CHAPTER_22_INDEPENDENT_NARROW_REVIEW_2026-07-25.md`

ويجب أن يتضمن:

```text
REVIEWED-HEAD      = 9f56ae57afaa1e37eee55c54dc94a5e01563b004
VERDICT            = PASS | CHANGES-REQUIRED | FAIL
BLOCKERS           = <integer>
PASS-FOR-AUTHORING = YES | NO
```

لا تنشئ متن الفصل، ولا تعدّل الحزمة الأصلية، ولا تفعّل النتائج، ولا تدمج PR.