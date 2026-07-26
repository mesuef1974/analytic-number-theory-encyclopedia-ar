# طلب مراجعة مستقلة قبل تأليف الفصل الخامس والعشرين

```text
CHAPTER                 = 25
REVIEW-STAGE            = PRE-AUTHORING
AUTHORING               = BLOCKED
RESULTS                 = 10 RESERVED / NON-CITABLE
MERGE                   = NOT AUTHORIZED
```

## الملفات المطلوب قراءتها كاملة

1. `docs/CHAPTER_25_SCOPE_2026-07-26.md`
2. `docs/CHAPTER_25_EVIDENCE_LEDGER_2026-07-26.md`
3. `docs/CHAPTER_25_NORMALIZATION_TABLE_2026-07-26.md`
4. `docs/CHAPTER_25_PROOF_MAP_2026-07-26.md`
5. `docs/RESULTS_REGISTRY_CHAPTER_25.md`
6. `docs/CHAPTER_25_PRE_AUTHORING_AUDIT_2026-07-26.md`

## المطلوب من المراجع

1. مطابقة تعريف \(J_{s,k}(X)\) وهوية التعامد مع مصدر أولي.
2. التحقق من الحد الرئيسي كاملًا:
   \[
   J_{s,k}(X)\ll_{s,k,\varepsilon}X^\varepsilon
   \left(X^s+X^{2s-k(k+1)/2}\right).
   \]
3. التحقق من عدم حذف \(X^s\) أو \(X^\varepsilon\)، ومن اعتماد الثابت الصحيح.
4. تدقيق النطاق التاريخي:
   - Wooley 2012 تقدم بالتوافق الفعّال وليس وحده إثبات الصيغة النهائية العامة.
   - BD 2015 مبرهنة فك اقتران عامة.
   - BDG 2016 يثبت VMVT للدرجات الأعلى من ثلاثة.
   - التوافق الفعّال المتداخل يغطي جميع الدرجات.
5. تدقيق الفصل بين المنحنى اللحظي والأسطح المحدبة العامة.
6. تدقيق وصف المسارين: لا دمج مفاهيمي ولا ادعاء أنهما البرهان نفسه.
7. تدقيق عدم الدور مع الفصلين 17 و18.
8. تدقيق المعرفات العشرة وتصنيفاتها، خصوصًا `ANT-PROP-25-02` و`ANT-COR-25-01`.
9. إصدار ملاحظات `BLOCKER / MAJOR / MINOR` مع مواقعها الدقيقة.

## الحكم المطلوب

لا يفتح التأليف إلا بالحكم:

```text
VERDICT            = PASS
BLOCKERS           = 0
PASS-FOR-AUTHORING = YES
RESULTS-CITABLE    = NO
MERGE              = NOT AUTHORIZED
```

وعند وجود أي خلل جوهري يكون الحكم `CHANGES-REQUIRED` مع إبقاء التأليف محظورًا.

## مخرج المراجعة

ينشئ المراجع ملفًا جديدًا:

`docs/CHAPTER_25_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-26.md`

ثم يلتزم به ويدفعه إلى الفرع نفسه، دون كتابة المتن أو تفعيل النتائج أو الدمج.
