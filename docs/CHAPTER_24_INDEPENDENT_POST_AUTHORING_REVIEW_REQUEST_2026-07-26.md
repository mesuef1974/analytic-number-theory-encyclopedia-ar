# طلب مراجعة مستقلة بعد تأليف الفصل الرابع والعشرين

## الرأس المطلوب مراجعته

```text
BRANCH                  = agent/chapter-24-pretentious-multiplicative-functions-v0.28.0
REVIEW-STAGE            = POST-AUTHORING
AUTHORING                = COMPLETED
LOCAL-BUILD              = PASS
RESULTS                  = 10 AUTHORED-DRAFT / NON-CITABLE
OWNER-ADOPTION           = NOT REQUESTED
MERGE                    = NOT AUTHORIZED
```

يُراجع العميل المستقل المتن الفعلي والوثائق الحاكمة، ولا يكتفي بخطة الفصل.

## الملفات الأساسية

- `volumes/volume-15-modern-frontiers/chapters/chapter-24-pretentious-multiplicative-functions.tex`
- `manuscript/chapter-24-bibliography.bib`
- `manuscript/main.tex`
- `manuscript/preamble.tex`
- `docs/RESULTS_REGISTRY_CHAPTER_24.md`
- `docs/CHAPTER_24_LOCAL_BUILD_RECEIPT_2026-07-26.md`
- وثائق النطاق والأدلة والتطبيعات وخريطة البرهان والمراجعات السابقة.

## الاختبارات المطلوبة

1. قراءة المتن كاملًا والتحقق من وجود المعرفات العشرة مرة واحدة لكل معرّف وبلا تصادم.
2. فحص برهان `ANT-PROP-24-01`، ولا سيما الهوية الإقليدية ومسار متباينة مينكوفسكي.
3. التحقق من تعريف
   \[
   \mathbb D(f,g;x)^2=\sum_{p\le x}\frac{1-\Re(f(p)\overline{g(p)})}{p}.
   \]
4. التحقق من أن
   \[
   \mathcal M(f;x,T)=\min_{|t|\le2T}\mathbb D(f,n^{it};x)^2
   \]
   حاضر بلا نسخة قديمة مخالفة.
5. التحقق من صيغة هالاش الكمية ووجود الحد `+T^{-1/2}` في المتن، ومن تصنيفها `CITED-CORE` لا `PROVED-HERE`.
6. التحقق من سلامة اشتقاق `ANT-COR-24-01` باشتراط `T(x) -> infinity` وتباعد المقياس معًا.
7. فحص الفصل الصريح بين `n^{it}` و`chi(n)n^{it}` وعدم الخلط بين الصورة العامة والصورة التوافقية.
8. التحقق من أن `ANT-PRIN-24-01` تفسير منقول مضبوط، وأن `ANT-PRIN-24-02` مبدأ منهجي لا مبرهنة.
9. التحقق من أن Matomäki–Radziwiłł والفترات القصيرة والارتباطات وتشاو خارج نواة البرهان.
10. فحص الاستشهادات الببليوغرافية وعدم وجود مفاتيح مفقودة بعد Biber.
11. التحقق من أن الفصل 24 يسبق خريطة الجبهات، وأن الخريطة هي الفصل 25 والأخير.
12. فحص تحذيرات التنضيد الجديدة داخل الفصل 24 وتحديد ما إن كانت مانعة أو تحريرية فقط.

## صيغة الحكم المطلوبة

```text
VERDICT                 = PASS | CHANGES-REQUIRED
BLOCKERS                = integer
MAJORS                  = integer
MINORS                  = integer
RESULTS-CITABLE         = YES | NO
PASS-FOR-OWNER-ADOPTION = YES | NO
MERGE-AUTHORIZED        = NO
REVIEWED-HEAD           = full commit SHA
```

يجب تسجيل كل ملاحظة مع الدرجة والملف والموضع والتصحيح المطلوب. لا يحرر المراجع متن الفصل أثناء المراجعة، ولا يفعّل النتائج، ولا يعتمد الفصل نيابة عن المالك، ولا يدمج الفرع.
