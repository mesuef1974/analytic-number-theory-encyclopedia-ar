# تدقيق ما قبل تأليف الفصل التاسع عشر

التاريخ: 2026-07-25  
الفرع: agent/chapter-19-primes-short-intervals-v0.23.0  
رأس البداية: 2ec3f8fcb5eb365ca582af32771a7790bcded4b5

## الحكم الحالي

~~~text
PASS-FOR-RESEARCH-INTAKE = YES
PRIMARY-SOURCE-AUDIT     = PASS WITH ONE HISTORICAL CONSTANT WITHHELD
MODERN-FRONTIER-AUDIT    = PASS
DEPENDENCY-AUDIT         = PASS
CIRCULARITY-AUDIT        = PASS
SCOPE-FREEZE              = PASS
INDEPENDENT-REVIEW       = PASS
PRE-AUTHORING-GATE       = CLOSED
PASS-FOR-AUTHORING       = YES
AUTHORING                = OPEN
RESULTS                  = 8 RESERVED / NON-CITABLE
~~~

## ما أغلق

- ثبت Ingham من المصدر الأصلي، Theorem 1، مع المرحلة \(5/8\).
- ثبت Huxley بوصفه السجل التاريخي عند \(7/12\)، لا السجل الحالي.
- أضيفت نتيجة Guth--Maynard المنشورة في Annals of Mathematics سنة 2026 عند \(17/30+\varepsilon\)، Corollary 1.3.
- ثبت نص Baker--Harman--Pintz الأصلي في خاتمة ص. 561:
  \[
  \pi(x+x^{0.525})-\pi(x)
  >
  \frac{9}{100}\frac{x^{0.525}}{\log x}.
  \]
- ثبت أن arXiv:2308.04458 ما يزال preprint حتى v8، ولذلك يبقى محجورًا.
- ثبت أن الفصل 9 لا يعطي حد خطأ فعالًا، فلا ينسب إليه مسار الفترات القصيرة.
- أغلقت مساهمة القوى الأولية العليا والتحويلات \(\psi\to\theta\to\pi\).
- اجتاز مخطط الاعتماد تدقيق عدم الدور.
- جمدت ثمانية معرفات نتائج بالنطاق المصحح.

## التحفظ التاريخي

تعذر الوصول الرقمي إلى نص Hoheisel الأصلي. لذلك يسمح الفصل فقط بالصيغة النوعية: وجود \(\delta>0\). لا تسجل قيمة \(1/3300\) أو \(1/33000\)، لأن المصادر الثانوية التي ظهرت في الفحص غير متفقة ولا يجوز حسمها بالذاكرة.

هذا التحفظ غير حاجز إذا التزم المتن بعدم ذكر ثابت عددي.

## المراجعة المستقلة

أُنجزت المراجعة المستقلة وسُجلت في `CHAPTER_19_INDEPENDENT_PRE_AUTHORING_REVIEW_2026-07-25.md`. أعادت اشتقاق المسار الداخلي، وفحصت المصدرين الأعلى مخاطرة، وتحققت من `ANT-LEM-09-02`. الحكم `PASS` وصفر عوائق.

## قرار التأليف

أُغلقت بوابة ما قبل التأليف، وصدر `PASS-FOR-AUTHORING = YES`. يجوز الآن إنشاء متن LaTeX للفصل التاسع عشر ضمن النطاق المجمد. لا يرقّي هذا القرار النتائج إلى `ACTIVE` أو `CITABLE` ولا يجيز الدمج.

## شروط الإغلاق

- [x] تثبيت المصادر الأصلية للنتائج التي تحمل صياغة عددية.
- [x] تصنيف الصيغة الصريحة وكثافة الأصفار CITED-CORE.
- [x] إغلاق تحويلات \(\psi\to\theta\to\pi\).
- [x] اجتياز تدقيق عدم الدور.
- [x] تجميد سجل النتائج والنطاق.
- [x] مراجعة مستقلة للبوابة.
- [x] إصدار PASS-FOR-AUTHORING = YES صريح.
