# طلب مراجعة مستقلة ضيقة لتصحيح الفصل الرابع والعشرين

## سبب الجولة الضيقة

أصدرت المراجعة المستقلة السابقة الحكم:

```text
REVIEW-COMMIT        = 1fb25deeac05beada7abe0e8f68a77f8d5fd2f70
VERDICT              = CHANGES-REQUIRED
BLOCKERS             = 1
PASS-FOR-AUTHORING   = NO
```

وكان العائق الوحيد هو صيغة هالاش الكمية المخططة: استُعمل سابقًا المجال \(|t|\le T\) وحُذف الحد \(T^{-1/2}\).

## التصحيح المطبق

ثُبّت الآن:

\[
\mathcal M(f;x,T)=\min_{|t|\le2T}\mathbb D(f,n^{it};x)^2,
\]

ومع \(x\ge2\) و\(T\ge1\):

\[
\left|\frac1x\sum_{n\le x}f(n)\right|
\ll
(1+\mathcal M(f;x,T))e^{-\mathcal M(f;x,T)}+T^{-1/2}.
\]

كما عُدّل مسار `ANT-COR-24-01` ليشترط اختيار \(T=T(x)\to\infty\) وتباعد \(\mathcal M(f;x,T(x))\) معًا.

## الملفات المطلوب فحصها

- `docs/CHAPTER_24_NORMALIZATION_TABLE_2026-07-26.md`
- `docs/CHAPTER_24_EVIDENCE_LEDGER_2026-07-26.md`
- `docs/CHAPTER_24_PROOF_MAP_2026-07-26.md`
- `docs/RESULTS_REGISTRY_CHAPTER_24.md`
- `docs/CHAPTER_24_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-26.md`

## أسئلة المراجعة الضيقة

1. هل مجال التصغير \(|t|\le2T\) مطابق للصيغة المصدرية المختارة؟
2. هل الحد \(+T^{-1/2}\) حاضر في كل موضع حاكم؟
3. هل استنتاج الإلغاء في `ANT-COR-24-01` يضبط الحدين ولا يثبت \(T\)؟
4. هل بقي أي خلط بين الصيغة الكلاسيكية المحسنة وصياغة 2019؟
5. هل التصحيح يغلق العائق الوحيد دون فتح ادعاء جديد؟

## صيغة الحكم المطلوبة

عند إغلاق العائق:

```text
VERDICT            = PASS
BLOCKERS           = 0
PASS-FOR-AUTHORING = YES
RESULTS-CITABLE    = NO
MERGE              = NOT AUTHORIZED
```

وعند بقاء خلل:

```text
VERDICT            = CHANGES-REQUIRED
BLOCKERS           = <N>
PASS-FOR-AUTHORING = NO
RESULTS-CITABLE    = NO
MERGE              = NOT AUTHORIZED
```

هذه الجولة لا تكتب متن الفصل، ولا تفعّل النتائج، ولا تدمج الفرع.