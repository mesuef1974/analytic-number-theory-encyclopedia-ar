# طلب مراجعة مستقلة بعد تأليف الفصل الخامس والعشرين

```text
CHAPTER                 = 25
VERSION                 = 0.29.0-dev
REVIEW-STAGE            = POST-AUTHORING
REVIEWED-HEAD           = d5210099d2c6c901a1756d5761d3a93a7af98fc3
CI-QUALITY              = PASS
CI-PDF                  = PASS
RESULTS                 = 10 RESERVED / NON-CITABLE
OWNER-ADOPTION          = NOT REQUESTED
MERGE                   = NOT AUTHORIZED
```

## الملفات المطلوب فحصها

1. `volumes/volume-15-modern-frontiers/chapters/chapter-25-decoupling-efficient-congruencing.tex`
2. `manuscript/chapter-25-bibliography.bib`
3. `manuscript/preamble.tex`
4. `manuscript/main.tex`
5. `docs/CHAPTER_25_SCOPE_2026-07-26.md`
6. `docs/CHAPTER_25_EVIDENCE_LEDGER_2026-07-26.md`
7. `docs/CHAPTER_25_NORMALIZATION_TABLE_2026-07-26.md`
8. `docs/CHAPTER_25_PROOF_MAP_2026-07-26.md`
9. `docs/RESULTS_REGISTRY_CHAPTER_25.md`
10. `docs/CHAPTER_25_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-26.md`

## المطلوب من المراجع المستقل

1. قراءة متن الفصل كاملًا، لا الاكتفاء بالفروق أو الملخصات.
2. مطابقة تعريف \(J_{s,k}(X)\)، وتطبيع \(e(t)=\exp(2\pi it)\)، وهوية التعامد مع المصادر الأصلية.
3. تدقيق برهان الحدين السفليين:
   \[
   J_{s,k}(X)\gg_{s,k}X^s+X^{2s-k(k+1)/2}.
   \]
4. التحقق من أن الحد العلوي الأمثل منقول بوضوح بوصفه `CITED-CORE` وليس `PROVED-HERE`:
   \[
   J_{s,k}(X)\ll_{s,k,\varepsilon}X^\varepsilon
   \left(X^s+X^{2s-k(k+1)/2}\right).
   \]
5. تدقيق النطاق التاريخي بدقة:
   - Wooley 2012: تأسيس التوافق الفعّال وحدود قوية، لا الحل الكامل العام.
   - Wooley 2016: الحالة التكعيبية \(k=3\).
   - Bourgain--Demeter--Guth 2016: الدرجات \(k\ge4\).
   - Wooley 2019: التوافق الفعّال المتداخل لجميع الدرجات.
6. تدقيق صياغة مبرهنة فك الاقتران للمنحنى اللحظي وعدم خلطها بمبرهنة الأسطح العامة.
7. التأكد من أن الانتقال من فك الاقتران المستمر إلى VMVT لا يُعرض كبرهان كامل داخل الفصل.
8. فحص عدم الدور مع الفصلين 17 و18، وأن تطبيقات وارينغ والمجاميع الأسية جسور تابعة فقط.
9. تدقيق جميع الاستشهادات الخمسة والبيانات الببليوغرافية وDOI والنطاقات المنسوبة إليها.
10. فحص المعرفات العشرة وتصنيفاتها وحراسها، وعدم وجود نتيجة زائدة أو مفقودة.
11. فحص لغة الفصل من جهة المبالغة، والغموض، والتمييز بين:
    `PROVED-HERE / CITED-CORE / CITED-INTERPRETATION / METHODOLOGICAL-PRINCIPLE / DERIVED-BRIDGE / OPEN`.
12. فحص موضع الفصل في المخطوط والتأكد من بقاء خريطة الجبهات الفصل الأخير.

## تصنيف الملاحظات

يجب تصنيف كل ملاحظة مع الملف والموضع والتصحيح المطلوب:

- `BLOCKER`
- `MAJOR`
- `MINOR`

## الحكم المقبول

عند النجاح:

```text
VERDICT             = PASS
BLOCKERS            = 0
POST-AUTHORING-PASS = YES
RESULTS-CITABLE     = NO
OWNER-ADOPTION      = REQUIRED
MERGE               = NOT AUTHORIZED
```

وعند وجود خلل:

```text
VERDICT             = CHANGES-REQUIRED
BLOCKERS            = <N>
POST-AUTHORING-PASS = NO
RESULTS-CITABLE     = NO
OWNER-ADOPTION      = NOT REQUESTED
MERGE               = NOT AUTHORIZED
```

## مخرج المراجعة

ينشئ المراجع الملف:

`docs/CHAPTER_25_INDEPENDENT_POST_AUTHORING_REVIEW_2026-07-26.md`

ثم يدفعه في التزام مستقل إلى الفرع نفسه. لا تُفعّل النتائج، ولا يُعتمد الفصل نيابة عن المالك، ولا يتحول PR إلى Ready، ولا يحدث دمج.
