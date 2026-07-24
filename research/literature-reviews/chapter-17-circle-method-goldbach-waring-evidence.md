# سجل أدلة الفصل السابع عشر — الطريقة الدائرية وغولدباخ ووارينغ

آخر تحديث: 2026-07-25

```text
CHAPTER             = 17
VERSION             = 0.21.0-dev
BASE-MAIN           = 0bd442bc48490115bed48b18ed32783ad5bd1c9c
BRANCH              = agent/chapter-17-circle-method-goldbach-waring-v0.21.0
ISSUE               = #32 / OPEN
METHOD              = EVIDENCE-FIRST
AUTHORING           = BLOCKED
PRE-AUTHORING-GATE  = OPEN
RELEASE-READY       = NO
```

## 1. الموضوع المثبت من خريطة الطريق

العنوان الحاكم هو:

> **الطريقة الدائرية ومدخل إلى غولدباخ ووارينغ**.

موضعه البنيوي بعد تطبيقات الغربال والفجوات وقبل فصل المجاميع الأسية وفان دير كوربوت. لذلك يجب ألا يستهلك الفصل السابع عشر المادة التقنية الكاملة المخطط لها للفصل الثامن عشر.

## 2. سؤال الفصل

كيف تتحول مسألة تمثيل عدد صحيح على صورة مجموع عناصر من مجموعة حسابية إلى تكامل فورييه، وكيف تفصل الطريقة الدائرية هذا التكامل إلى أقواس كبرى تحمل الحد الرئيس وأقواس صغرى يجب ضبطها تحليليًا؟

## 3. النطاق المجمد مبدئيًا

1. دالة التوليد الأسية
   \[
   F(\alpha)=\sum_{n\in\mathcal A}w(n)e(\alpha n),
   \qquad e(t)=e^{2\pi i t}.
   \]
2. هوية التعامد
   \[
   R_s(N)=\int_0^1F(\alpha)^s e(-N\alpha)\,d\alpha.
   \]
3. تعريف الأقواس الكبرى والصغرى واختيار معاملات الفصل.
4. التقريب المحلي قرب الكسور المختزلة \(a/q\).
5. ظهور السلسلة المفردة والتكامل المفرد ومعناهما المحلي/الأرخميدي.
6. تطبيق وارينغ تعليمي: اشتقاق صيغة العد وتفسير الحد الرئيس، مع اقتباس المبرهنة التقاربية العامة بدل الادعاء ببرهان كامل لتقديرات الأقواس الصغرى.
7. مبرهنة فينوغرادوف: كل عدد فردي كبير بما يكفي مجموع ثلاثة أوليات، بحالة `CITED`.
8. مبرهنة هلفغوت: كل عدد فردي أكبر من 5 مجموع ثلاثة أوليات، بحالة `CITED / MODERN COMPLETION`.
9. غولدباخ الثنائي: `HYPOTHESIS / OPEN` مع عرض تنبؤ هاردي–ليتلوود وحدود الطريقة.

## 4. المصادر الأولية والمتحقق منها

### 4.1 غولدباخ والطريقة الدائرية

- G. H. Hardy and J. E. Littlewood, *Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes*, Acta Mathematica 44 (1923), 1–70. DOI: `10.1007/BF02403921`.
- G. H. Hardy and J. E. Littlewood, *Some Problems of “Partitio Numerorum” (V): A Further Contribution to the Study of Goldbach's Problem*, Proceedings of the London Mathematical Society, s2-22 (1924), 46–56. DOI: `10.1112/plms/s2-22.1.46`.

### 4.2 فينوغرادوف

النتيجة العلمية المثبتة للاستخدام:

> كل عدد فردي كبير بما يكفي يمكن تمثيله مجموع ثلاثة أعداد أولية.

التصنيف: `CITED`.

يوجد اضطراب ببليوغرافي بين الفهارس في بيانات الورقة القصيرة لسنة 1937؛ ظهرت صيغ متعددة للمجلد والصفحات، منها:

- Doklady Akademii Nauk SSSR 15 (1937), 129–132؛
- C. R. (Dokl.) Acad. Sci. URSS, new series 15 (1937), 169–172؛
- إحالات ثانوية أخرى إلى صفحات مختلفة.

كما توجد مقالة أطول ذات صلة:

- I. M. Vinogradov, *Some theorems concerning the theory of primes*, Matematicheskii Sbornik 44(2), 179–195.

قرار التوثيق الحالي:

```text
VINOGRADOV-THEOREM-STATEMENT = VERIFIED
VINOGRADOV-PRIORITY-YEAR      = VERIFIED / 1937
VINOGRADOV-EXACT-BIBLIOGRAPHY = OPEN / CONFLICTING INDEX RECORDS
```

لا يُغلق عائق الإحالة الدقيقة قبل اعتماد سجل فهرسي أولي واحد أو تصوير صفحة العنوان الأصلية.

### 4.3 هلفغوت

- H. A. Helfgott, *The ternary Goldbach conjecture is true*, arXiv:1312.7748.
- H. A. Helfgott, *The ternary Goldbach problem*, arXiv:1501.05438، عرض كامل موسع للبرهان.
- H. A. Helfgott and D. J. Platt, *Numerical Verification of the Ternary Goldbach Conjecture up to 8.875×10^30*, Experimental Mathematics 22 (2013), 406–409. DOI: `10.1080/10586458.2013.831742`.

قرار النطاق:

```text
HELFGOTT-SCOPE = INCLUDE AS CITED MODERN COMPLETION
FULL-PROOF     = OUT OF SCOPE
COMPUTATION    = FINITE-VERIFIED SUPPORTING COMPONENT
```

### 4.4 وارينغ والسلسلة المفردة

- G. H. Hardy and J. E. Littlewood, *Some problems of “Partitio Numerorum”: IV. The singular series in Waring's Problem and the value of the number G(k)*, Mathematische Zeitschrift 12 (1922), 161–188.
- G. H. Hardy and J. E. Littlewood, *Some Problems of “Partitio Numerorum” (VIII): The Number Γ(k) in Waring's Problem*, Proceedings of the London Mathematical Society, s2-28 (1928), 518–542. DOI: `10.1112/plms/s2-28.1.518`.

الهدف المجمد للفصل:

> عرض الصيغة التقاربية الكلاسيكية لعدد تمثيلات عدد صحيح كبير كمجموع \(s\) من القوى \(k\)-ية عندما يكون \(s\) كبيرًا بما يكفي بالنسبة إلى \(k\)، مع اشتقاق بنية الحد الرئيس والسلسلة والتكامل المفردين، وتصنيف تقدير الأقواس الصغرى الحاسم `CITED`.

لا يدعي الفصل أفضل حد معاصر لـ\(s\)، ولا يعيد برهنة مبرهنة القيمة المتوسطة لفينوغرادوف.

```text
WARING-TARGET = FROZEN / CLASSICAL ASYMPTOTIC FORMULA
PROOF-LEVEL   = STRUCTURE PROVED-HERE + DEEP MINOR-ARC INPUT CITED
```

## 5. الكتب المرجعية المرشحة

- R. C. Vaughan, *The Hardy–Littlewood Method*, Cambridge Tracts in Mathematics.
- H. Davenport, *Analytic Methods for Diophantine Equations and Diophantine Inequalities*.
- H. Iwaniec and E. Kowalski, *Analytic Number Theory*، للأدوات الخلفية ذات الصلة بالمجاميع الأسية والتوزيع في المتتاليات.
- T. D. Wooley، المراجع البحثية المتعلقة بوارينغ والطريقة الدائرية الحديثة.

هذه الكتب مراجع تفسيرية وتقنية؛ الأولوية التاريخية والادعاءات البحثية تعود إلى الأوراق الأصلية أو نسخها المنشورة.

## 6. سياسة التصنيف

| العنصر | التصنيف |
|---|---|
| هوية التعامد وتحويل عدد التمثيلات إلى تكامل | `IDENTITY / PROVED-HERE` |
| تفكيك الدائرة إلى أقواس كبرى وصغرى | `DEFINITION / PROVED-HERE` |
| اشتقاق شكل الحد الرئيس في نموذج وارينغ | `PROVED-HERE` |
| التقدير العميق العام للأقواس الصغرى | `CITED` |
| الصيغة التقاربية الكلاسيكية في وارينغ | `CITED / EXPLAINED` |
| مبرهنة فينوغرادوف للثلاثة أوليات | `CITED` |
| مبرهنة هلفغوت لغولدباخ الثلاثي الكامل | `CITED` |
| التحقق العددي لهلفغوت–بلات | `FINITE-VERIFIED` |
| الصيغة الحدسية لغولدباخ الثنائي | `HYPOTHESIS / OPEN` |
| شرح المعنى المحلي للسلسلة المفردة | `INTERPRETATION` |

## 7. حدود الادعاء

- لا ادعاء بإثبات حدسية غولدباخ الثنائية.
- لا تحويل لتنبؤ هاردي–ليتلوود إلى مبرهنة بلا ضبط كامل للأقواس الصغرى.
- لا ادعاء بإثبات أفضل نسخة حديثة من مسألة وارينغ.
- لا استعمال لنتائج الفصل الثامن عشر قبل تأليفها بوصفها نتائج داخلية؛ أي تقدير أسي متقدم يصنف `CITED`.
- لا خلط بين برهان فينوغرادوف للأعداد الفردية الكبيرة وبرهان هلفغوت الكامل لكل فردي أكبر من 5.

## 8. العوائق المفتوحة بعد هذا التحديث

1. حسم السجل الببليوغرافي الدقيق للورقة القصيرة الأصلية لفينوغرادوف بسبب تعارض الفهارس.
2. تثبيت صياغة كمية محددة لتقدير الأقواس الصغرى ومصدرها في مسار وارينغ المختار.
3. تجميد التطبيع الموحد لـ`e(α)`، مقاييس الأقواس، والسلسلة والتكامل المفردين.
4. إجراء تدقيق مستقل لبوابة ما قبل التأليف.

```text
EVIDENCE-LEDGER       = UPDATED
WARING-TARGET         = FROZEN
HELFGOTT-SCOPE        = DECIDED
VINOGRADOV-STATEMENT  = VERIFIED
PRIMARY-SOURCES       = PARTIALLY VERIFIED
PROOF-SCOPE           = PARTIALLY FROZEN
RESULT-IDS            = RESERVED / NON-CITABLE
PASS-FOR-AUTHORING    = NO
```
