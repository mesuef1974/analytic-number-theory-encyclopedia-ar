# طلب مراجعة مستقلة بعد تأليف الفصل الثالث والعشرين

## الحالة

```text
CHAPTER                 = 23
VERSION                 = 0.27.0-dev
AUTHORING               = COMPLETED
LOCAL-BUILD             = PASS
PDF-PAGES               = 302
POST-AUTHORING-REVIEW   = REQUESTED
RESULTS                 = 10 AUTHORED-DRAFT / NON-CITABLE
OWNER-ADOPTION          = NOT REQUESTED
MERGE                   = NOT AUTHORIZED
```

## الرأس المطلوب مراجعته

راجع الرأس الحالي للفرع:

```text
agent/chapter-23-zero-statistics-random-matrices-v0.27.0
```

وتحقق أولًا من أن الرأس المحلي يطابق الرأس البعيد بعد جلب آخر التحديثات.

## الملفات الأساسية

- `volumes/volume-15-modern-frontiers/chapters/chapter-23-zero-statistics-random-matrices.tex`
- `manuscript/chapter-23-bibliography.bib`
- `manuscript/main.tex`
- `manuscript/preamble.tex`
- `docs/RESULTS_REGISTRY_CHAPTER_23.md`
- `docs/CHAPTER_23_PROOF_MAP_2026-07-26.md`
- `docs/CHAPTER_23_EVIDENCE_LEDGER_2026-07-26.md`
- `docs/CHAPTER_23_NORMALIZATION_TABLE_2026-07-26.md`
- `docs/CHAPTER_23_LOCAL_BUILD_RECEIPT_2026-07-26.md`
- جميع تقارير المراجعة السابقة للفصل 23.

## نطاق المراجعة العلمية

1. التحقق من أن صيغة ريمان--فون مانغولت إحالة داخلية إلى `ANT-THM-06-06` وليست مبرهنة جديدة في الفصل 23.
2. تدقيق تعريف دالة Montgomery الموزونة، الوزن، ترتيب الأزواج، إدخال القطر، وموضع شرط RH.
3. تدقيق الصيغة المعروضة لمبرهنة Montgomery ومجال `0 <= alpha < 1` وقيد دعم تحويل فورييه داخل `(-1,1)`.
4. التحقق من اتفاقية فورييه وهوية تحويل مربع نواة الجيب وتوافق التطبيع المحلي.
5. فصل مبرهنة GUE المصفوفية عن حدسية GUE لأصفار زيتا.
6. تدقيق بيانات Odlyzko وتصنيفها `NUMERICAL-EVIDENCE / FINITE-VERIFIED` فقط.
7. تدقيق حارس Katz--Sarnak ومرجع Rudnick--Sarnak.
8. التحقق من أن `ANT-PRIN-23-02` مبدأ منهجي لا يحمل `PROVED-HERE`.
9. مطابقة المعرفات العشرة بين المتن وسجل النتائج دون فقد أو تكرار.
10. التحقق من أن الفصل 23 يسبق خريطة الجبهات وأن خريطة الجبهات هي الفصل 24 والأخير.

## مراجعة البناء

أعد دورة بناء كاملة من الصفر:

```text
xelatex -> biber -> xelatex -> xelatex
```

وسجل:

```text
BUILD-EXIT-CODES
PDF-PAGES
UNRESOLVED-CITATIONS
UNDEFINED-REFERENCES
CHAPTER-23-NUMBER
FRONTIERS-MAP-NUMBER
FRONTIERS-MAP-LAST
WORKTREE-CLEAN
```

التحذيرات القديمة غير الحاجبة في الفصول السابقة لا تُنسب تلقائيًا إلى الفصل 23، لكن أي تحذير جديد أو خطأ ناتج عن تغييرات هذا الفرع يجب تسجيله.

## المخرج الوحيد المطلوب

أنشئ ملفًا جديدًا فقط:

```text
docs/CHAPTER_23_INDEPENDENT_POST_AUTHORING_REVIEW_2026-07-26.md
```

ويبدأ بالحكم:

```text
REVIEWED-HEAD    = <full commit sha>
REVIEWER         = INDEPENDENT LOCAL CLIENT
REVIEW-STAGE     = POST-AUTHORING
VERDICT          = PASS | CHANGES-REQUIRED | FAIL
BLOCKERS         = <integer>
RESULTS-CITABLE  = YES | NO
MERGE            = NOT AUTHORIZED
```

لا تعدّل المتن أو السجلات الأصلية أثناء المراجعة، ولا تفعّل النتائج، ولا تعتمد المالك، ولا تدمج PR #46.
