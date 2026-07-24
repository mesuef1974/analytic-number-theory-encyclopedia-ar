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

## 3. النطاق المرشح

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
6. تطبيق تعليمي على وارينغ يوضح البنية العامة.
7. تطبيق على غولدباخ الثلاثي بوصفه نتيجة مقتبسة أو خريطة برهان، لا برهانًا داخليًا كاملًا ما لم تغلق كل مدخلاته.
8. مناقشة غولدباخ الثنائي بوصفه `OPEN` مع عرض التنبؤ الهاردي–ليتلوودي وحدود الطريقة.

## 4. المصادر الأولية المثبتة مبدئيًا

### 4.1 غولدباخ والطريقة الدائرية

- G. H. Hardy and J. E. Littlewood, *Some problems of ‘Partitio numerorum’; III: On the expression of a number as a sum of primes*, Acta Mathematica 44 (1923), 1–70. DOI: `10.1007/BF02403921`.
- G. H. Hardy and J. E. Littlewood, *Some Problems of “Partitio Numerorum” (V): A Further Contribution to the Study of Goldbach's Problem*, Proceedings of the London Mathematical Society, s2-22 (1924), 46–56. DOI: `10.1112/plms/s2-22.1.46`.
- I. M. Vinogradov, *Representation of an odd number as the sum of three primes*, Doklady Akademii Nauk SSSR 15 (1937), 129–132.

### 4.2 وارينغ والسلسلة المفردة

- G. H. Hardy and J. E. Littlewood, *Some problems of “Partitio Numerorum”: IV. The singular series in Waring's Problem and the value of the number G(k)*, Mathematische Zeitschrift 12 (1922), 161–188.
- G. H. Hardy and J. E. Littlewood, *Some Problems of “Partitio Numerorum” (VIII): The Number Γ(k) in Waring's Problem*, Proceedings of the London Mathematical Society, s2-28 (1928), 518–542. DOI: `10.1112/plms/s2-28.1.518`.

## 5. الكتب المرجعية المرشحة

- R. C. Vaughan, *The Hardy–Littlewood Method*, Cambridge Tracts in Mathematics.
- H. Davenport, *Analytic Methods for Diophantine Equations and Diophantine Inequalities*.
- H. Iwaniec and E. Kowalski, *Analytic Number Theory*، للأدوات الخلفية ذات الصلة بالمجاميع الأسية والتوزيع في المتتاليات.
- T. D. Wooley، المراجع المسحية والبحثية المتعلقة بوارينغ والطريقة الدائرية الحديثة.

هذه الكتب مراجع تفسيرية وتقنية؛ الأولوية التاريخية والادعاءات البحثية يجب أن تعود إلى الأوراق الأصلية أو نسخها المنشورة.

## 6. سياسة التصنيف

| العنصر | التصنيف المرشح |
|---|---|
| هوية التعامد وتحويل عدد التمثيلات إلى تكامل | `IDENTITY / PROVED-HERE` |
| تفكيك الدائرة إلى أقواس كبرى وصغرى | `DEFINITION / PROVED-HERE` |
| حساب التكامل المفرد في نموذج وارينغ المناسب | `PROVED-HERE` إذا اكتملت التفاصيل |
| تقارب/إيجابية السلسلة المفردة | `PROVED-HERE` أو `CITED` بحسب مستوى التفاصيل |
| مبرهنة فينوغرادوف للثلاثة أوليات | `CITED` |
| الصيغة الحدسية لغولدباخ الثنائي | `HYPOTHESIS / OPEN` |
| تجارب عددية لعدد التمثيلات | `FINITE-VERIFIED` فقط |
| شرح المعنى المحلي للسلسلة المفردة | `INTERPRETATION` |

## 7. حدود الادعاء

- لا ادعاء بإثبات حدسية غولدباخ الثنائية.
- لا تحويل لتنبؤ هاردي–ليتلوود إلى مبرهنة بلا ضبط كامل للأقواس الصغرى.
- لا ادعاء بإثبات نسخة حديثة مثلى من مسألة وارينغ.
- لا استعمال لنتائج الفصل الثامن عشر قبل تأليفها بوصفها نتائج داخلية؛ أي تقدير أسي متقدم يلزم أن يصنف `CITED`.
- لا خلط بين برهان فينوغرادوف التاريخي، وبرهان هلفغوت الكامل لغولدباخ الضعيف، والصيغ الحديثة المحسنة.

## 8. العوائق المفتوحة

1. اختيار مبرهنة وارينغ الدقيقة التي يمكن إثباتها داخليًا دون تضخم الفصل.
2. تحديد مستوى تقديرات الأقواس الصغرى المسموح باقتباسه قبل الفصل الثامن عشر.
3. تثبيت مصدر أولي دقيق لصياغة مبرهنة فينوغرادوف المستخدمة.
4. تحديد هل تُذكر مبرهنة هلفغوت الكاملة لغولدباخ الضعيف في هذا الفصل أم تؤجل إلى ملاحظة تاريخية موثقة.
5. تثبيت التطبيع الموحد لـ`e(α)`، مقاييس الأقواس، والسلسلة والتكامل المفردين.

```text
EVIDENCE-LEDGER      = INITIALIZED
PRIMARY-SOURCES      = PARTIALLY VERIFIED
PROOF-SCOPE          = NOT FROZEN
RESULT-IDS           = NOT YET ACTIVE
PASS-FOR-AUTHORING   = NO
```