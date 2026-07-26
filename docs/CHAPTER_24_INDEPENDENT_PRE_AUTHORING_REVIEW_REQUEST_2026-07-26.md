# طلب مراجعة مستقلة قبل تأليف الفصل الرابع والعشرين

## الرأس المطلوب مراجعته

```text
BRANCH                 = agent/chapter-24-pretentious-multiplicative-functions-v0.28.0
REVIEW-STAGE           = PRE-AUTHORING
AUTHORING              = BLOCKED
RESULTS                = 10 RESERVED / NON-CITABLE
MERGE                  = NOT AUTHORIZED
```

يراجع العميل المستقل الملفات الآتية كاملة:

- `docs/CHAPTER_24_SCOPE_2026-07-26.md`
- `docs/CHAPTER_24_EVIDENCE_LEDGER_2026-07-26.md`
- `docs/CHAPTER_24_NORMALIZATION_TABLE_2026-07-26.md`
- `docs/CHAPTER_24_PROOF_MAP_2026-07-26.md`
- `docs/RESULTS_REGISTRY_CHAPTER_24.md`
- `docs/CHAPTER_24_PRE_AUTHORING_AUDIT_2026-07-26.md`

## الاختبارات المطلوبة

1. مطابقة بيانات Halász الأصلية والصياغة الحديثة المنشورة.
2. التحقق من تعريف
   \[
   \mathbb D(f,g;x)^2=\sum_{p\le x}\frac{1-\Re(f(p)\overline{g(p)})}{p}.
   \]
3. فحص صلاحية مسار إثبات `ANT-PROP-24-01`، ولا سيما المتباينة المثلثية.
4. فحص التطبيع الكمي المخطط لمبرهنة هالاش ومنع تثبيت صيغة خاطئة أو ناقصة.
5. فحص الفصل المنطقي بين \(n^{it}\) و\(\chi(n)n^{it}\).
6. فحص أن `ANT-PRIN-24-01` تفسير منقول مضبوط، وأن `ANT-PRIN-24-02` مبدأ منهجي لا مبرهنة.
7. فحص أن Matomäki–Radziwiłł وتشاو والارتباطات تقع خارج النواة ولا تُستخدم في إثباتها.
8. عد المعرفات: عشرة بالضبط، بلا تكرار أو تصادم مع السجل العام.
9. تدقيق عدم الدور وعدم تكرار نتائج الفصول 4 و7 و8 و19.

## صيغة الحكم المطلوبة

عند النجاح فقط:

```text
VERDICT            = PASS
BLOCKERS           = 0
PASS-FOR-AUTHORING = YES
RESULTS-CITABLE    = NO
MERGE              = NOT AUTHORIZED
```

وعند وجود خلل:

```text
VERDICT            = CHANGES-REQUIRED
BLOCKERS           = <N>
PASS-FOR-AUTHORING = NO
RESULTS-CITABLE    = NO
MERGE              = NOT AUTHORIZED
```

يجب تسجيل كل ملاحظة بدرجة `BLOCKER` أو `MAJOR` أو `MINOR`، مع الملف والموضع والتصحيح المطلوب. لا يكتب المراجع متن الفصل ولا يفعّل النتائج ولا يدمج الفرع.
