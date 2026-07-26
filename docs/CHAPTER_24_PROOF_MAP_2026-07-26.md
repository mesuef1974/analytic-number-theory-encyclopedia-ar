# خريطة برهان الفصل الرابع والعشرين

## الحالة

```text
CHAPTER              = 24
AUTHORING            = BLOCKED
PASS-FOR-AUTHORING   = NO
RESULTS              = 10 RESERVED / NON-CITABLE
REVIEW               = CHANGES-REQUIRED / BLOCKER-CORRECTED-PENDING-NARROW-REVIEW
```

## المعرفات المخطط لها

| المعرّف | المحتوى | التصنيف | مسار الإثبات أو الإسناد |
|---|---|---|---|
| ANT-DEF-24-01 | الدوال الضربية وشرط 1-bounded والمتوسط المطبع | DEFINITION | داخلي؛ إحالة إلى الفصل 4 عند الحاجة |
| ANT-DEF-24-02 | المسافة الادعائية \(\mathbb D(f,g;x)\) | DEFINITION / CITED-ORIGIN | Granville–Soundararajan |
| ANT-PROP-24-01 | عدم السلبية والتماثل والمتباينة المثلثية الملائمة | PROVED-HERE | تحويل كل حد أولي إلى مسافة إقليدية ثم Minkowski |
| ANT-DEF-24-03 | \(\mathcal M(f;x,T)=\min_{|t|\le2T}\mathbb D(f,n^{it};x)^2\) | DEFINITION | وفق التطبيع المصحح بعد المراجعة المستقلة |
| ANT-THM-24-01 | مبرهنة هالاش الكمية: \(|M_f(x)|\ll(1+\mathcal M)e^{-\mathcal M}+T^{-1/2}\) | CITED-CORE | Halász؛ والصياغة الحديثة Granville–Harper–Soundararajan |
| ANT-COR-24-01 | معيار الإلغاء بعد ضبط \(\mathcal M\) و\(T^{-1/2}\) معًا | DERIVED-FROM-CITED | اختيار \(T=T(x)\to\infty\) مع تباعد المقياس المصحح |
| ANT-EX-24-01 | مقارنة \(1\)، \(n^{it}\)، الشخصيات، موبيوس، ليوفيل | EXAMPLES / INTERPRETATION-GUARDED | حسابات أولية وإحالات داخلية |
| ANT-PRIN-24-01 | مبدأ العائق الوحيد للمتوسط الكبير: التشبه بنموذج طوري مناسب | CITED-INTERPRETATION | صياغة منضبطة لعاقبة هالاش، لا مبرهنة مستقلة أوسع |
| ANT-PRIN-24-02 | فصل الادعاء الطويل عن السلوك في الفترات القصيرة | METHODOLOGICAL-PRINCIPLE / INFERENCE-GUARDED | لا يحمل مسار برهان مستقلًا |
| ANT-OPEN-24-01 | الانتقال إلى الفترات القصيرة والارتباطات وتشاو | OPEN / DEFERRED-FRONTIER | Matomäki–Radziwiłł وما بعدها؛ خارج النواة |

## مسار الفصل

1. استيراد تعريف الدوال الضربية من الفصل 4 دون إعادة تسجيل نتائج قديمة.
2. تعريف المسافة الادعائية وإثبات خصائصها الأساسية فقط.
3. عرض النماذج \(n^{it}\) و\(\chi n^{it}\) مع الفصل بين النسختين.
4. تعريف المقياس على المجال الصحيح \(|t|\le2T\).
5. عرض حد هالاش مع الحدين معًا:
   \[
   (1+\mathcal M)e^{-\mathcal M}+T^{-1/2}.
   \]
6. اشتقاق معيار الإلغاء باختيار \(T(x)\to\infty\) وضمان تباعد \(\mathcal M(f;x,T(x))\)، فلا يهمل أي من الحدين.
7. تطبيقات تفسيرية على \(\mu\)، \(\lambda\)، والشخصيات دون ادعاءات تتجاوز المصادر.
8. إغلاق الفصل بحارس يمنع القفز إلى الفترات القصيرة أو ارتباطات تشاو.

## تدقيق عدم الدور

- لا يُستعمل معيار الإلغاء لإثبات مبرهنة هالاش التي اشتُق منها.
- خصائص \(\mathbb D\) تُثبت قبل استخدامها في المقياس \(\mathcal M\).
- لا يُستنتج الإلغاء من \(\mathcal M\to\infty\) وحده مع \(T\) ثابت؛ يجب أيضًا جعل \(T^{-1/2}\to0\).
- أمثلة موبيوس وليوفيل لا تُستعمل مصدرًا لمبرهنة عامة.
- النتائج المؤجلة لا تدخل في برهان أي نتيجة داخل النواة.

## سجل التصحيح

```text
REVIEW-COMMIT           = 1fb25deeac05beada7abe0e8f68a77f8d5fd2f70
BLOCKER                 = QUANTITATIVE-HALASZ-NORMALIZATION
OLD-T-RANGE             = |t| <= T
CORRECT-T-RANGE         = |t| <= 2T
MISSING-TERM            = T^(-1/2)
CORRECTION-STATUS       = APPLIED
NARROW-REVIEW           = REQUIRED
```

## بوابة التأليف

```text
EVIDENCE-LEDGER          = CORRECTED
NORMALIZATION-TABLE      = CORRECTED
PROOF-MAP                = CORRECTED
NO-CIRCULARITY-AUDIT     = INTERNAL-DRAFT
INDEPENDENT-REVIEW       = CHANGES-REQUIRED
NARROW-RE-REVIEW         = REQUESTED-NEXT
PASS-FOR-AUTHORING       = NO
```