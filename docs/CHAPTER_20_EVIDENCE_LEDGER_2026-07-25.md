# سجل أدلة الفصل العشرين — 2026-07-25

## الحالة

```text
CHAPTER              = 20
VERSION              = 0.24.0-dev
MODE                 = EVIDENCE-FIRST / PRE-AUTHORING
LEDGER               = OPEN / PARTIALLY VERIFIED
NORMALIZATION-TABLE  = DRAFT / NOT FROZEN
AUTHORING            = BLOCKED
RESULTS              = RESERVED / NON-CITABLE
LITERATURE-CUTOFF    = 2026-07-25
```

لا يمنح هذا السجل أي نتيجة حالة `CITED` بعد. التحقق الببليوغرافي لا يساوي مطابقة الصيغة؛ ومطابقة صيغة واحدة لا تجمد جدول التطبيعات كله.

## نطاق الفصل

1. الفضاء العلوي وفعل \(SL_2(\mathbb Z)\) والزمر التوافقية الأساسية.
2. الأشكال المعيارية الهولومورفية وأشكال الحدبة وتوسعات فورييه.
3. حاصل بيترسون ومؤثرات Hecke ضمن مستوى وتطبيع مصرح بهما.
4. أشكال مااس ومؤثر لابلاس والتوسع Fourier--Whittaker.
5. مجاميع Kloosterman وتحويلات Bessel.
6. صيغة Petersson وصيغة Kuznetsov، ومدخل بنيوي محدود إلى صيغة Selberg.
7. لا تُستبق دوال \(L\) الآلية أو دون التحدب أو لانجلاندز المخصصة للفصل 21.

## قرار النطاق للصيغ الدقيقة

```text
PETERSSON-CORE = LEVEL 1 / TRIVIAL CHARACTER / EVEN k>2
KUZNETSOV-CORE = MODULAR GROUP / WEIGHT 0 / CONTINUOUS SPECTRUM INCLUDED
SELBERG-CORE   = COMPACT PROTOTYPE / STRUCTURAL INTRODUCTION
GENERAL LEVEL  = CONTEXT ONLY UNTIL NORMALIZATIONS ARE MATCHED
```

## المصادر المتحققة ومواضعها

| الرمز | المصدر | الموضع المثبت | ما يثبته | الحالة |
|---|---|---|---|---|
| E20-06 | Hans Petersson, *Über die Entwicklungskoeffizienten der automorphen Formen*, *Acta Mathematica* 58 (1932), 169--215، DOI: [10.1007/BF02547776](https://doi.org/10.1007/BF02547776) | المقالة الأصلية كاملة | الأصل الببليوغرافي لصيغة Petersson | `PRIMARY / BIBLIOGRAPHY-VERIFIED` |
| E20-09 | Knightly--Li, *A relative trace formula proof of the Petersson trace formula*, *Acta Arithmetica* 122 (2006), 297--313 | §3؛ حاصل بيترسون (3)، Theorem 3.9، Corollary 3.12 | نسخة مضبوطة للمستوى والشخصية، والنسخة الكلاسيكية | `FULL-TEXT / FORMULA-LOCATED` |
| E20-07 | N. V. Kuznetsov, *Petersson's conjecture for cusp forms of weight zero and Linnik's conjecture. Sums of Kloosterman sums*, *Math. USSR-Sb.* 39:3 (1981), 299--342، DOI: [10.1070/SM1981v039n03ABEH001518](https://doi.org/10.1070/SM1981v039n03ABEH001518) | §2؛ (2.10)، (2.13)، Theorems 1--2، ولا سيما (2.14) و(2.23) | توسع مااس، تعريف Kloosterman، والهوية الطيفية--الحسابية الأصلية | `PRIMARY / FULL-TEXT / CORE-CROSSCHECK-PASS` |
| E20-05 | D. A. Hejhal, *The Selberg Trace Formula for PSL(2,R)*, Vol. I, LNM 548, Springer (1976) | الفصل الأول: *The trace formula for compact Riemann surfaces*، ص 1--38 | موضع المدخل البنيوي المدمج | `PUBLISHER-VERIFIED / CHAPTER-LOCATED` |
| E20-10 | Jianya Liu--Yangbo Ye, *Petersson and Kuznetsov Trace Formulas* (2006) | المقالة الاستعراضية، أقسام Petersson/Kuznetsov | مرجع ثانٍ للمطابقة، لا مصدر أصلي | `CONSENSUS-FETCHED / FULL-TEXT-LOCATED` |
| E20-11 | Rizwanur Khan--Matthew P. Young, *Moments and hybrid subconvexity for symmetric-square L-functions* | §2.2، Lemma 2.1 | صيغة حديثة صريحة للطيف المنفصل والمستمر والقطري وتحويل \(J\) | `FULL-TEXT / FORMULA-CROSS-CHECKED` |
| E20-12 | Blomer--Assing, *Relative Trace Formulae in Analytic Number Theory*, Set 2 | ص 1--3 | تطبيع \(L^2\)، علاقة Hecke، Eisenstein، والاتجاهان الأمامي والخلفي | `FULL-TEXT / NORMALIZATION-CROSS-CHECKED` |

## مصادر الأساس التي ما تزال تحتاج مواضع دقيقة

| الرمز | المصدر | الدور | الحالة |
|---|---|---|---|
| E20-01 | Diamond--Shurman, *A First Course in Modular Forms* | Ch. 5؛ §5.4، ص 181--183 لبيترسون؛ §5.5 للمرافق؛ §5.8 للأشكال الذاتية | `SECONDARY / LOCATED` |
| E20-02 | Miyake, *Modular Forms* | Ch. 4، ص 96--194؛ §4.5 Hecke algebras، ص 131؛ §4.6 primitive forms، ص 153 | `SECONDARY / LOCATED` |
| E20-03 | Iwaniec, *Spectral Methods of Automorphic Forms*, 2nd ed. | Chs. 1--3؛ Chs. 4 و7؛ Ch. 9، ص 121--134؛ Ch. 10، ص 135--156 | `SECONDARY / LOCATED` |
| E20-04 | Iwaniec--Kowalski, *Analytic Number Theory* | Ch. 14، ص 353--382؛ Ch. 15، ص 383--402؛ §16.4، ص 406--412؛ §11.7، ص 287 | `SECONDARY / LOCATED` |
| E20-08 | A. Selberg, *Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with applications to Dirichlet series*, *J. Indian Math. Soc. (N.S.)* 20 (1956), 47--87 | المقالة الأصلية؛ مع مواد محاضرات غوتنغن 1954 المثبتة في Selberg Archive | الأصل التاريخي للصيغة؛ لا يجمّد اتجاه التحويل أو عوامل \(2\pi\) | `PRIMARY / BIBLIOGRAPHY-VERIFIED / TRANSFORM-PENDING` |

## اكتشافات Consensus

استُخدم Consensus للاكتشاف والفرز، ثم استُدعيت السجلات الكاملة قبل تسجيلها. لا تعتمد أرقام الاستشهادات ولا المقتطفات لتثبيت الثوابت.

| الرمز | السجل المسترجع | الحالة |
|---|---|---|
| C20-01 | Li--Knightly، *Kuznetsov's Trace Formula and the Hecke Eigenvalues of Maass Forms* (2012) | `CONSENSUS-FETCHED / SECONDARY` |
| C20-02 | Knightly--Li، *A relative trace formula proof of the Petersson trace formula* (2006) | `CONSENSUS-FETCHED / FULL-TEXT-VERIFIED-SEPARATELY` |
| C20-03 | Hejhal، Volume I (1976) | `CONSENSUS-FETCHED / PUBLISHER-VERIFIED-SEPARATELY` |
| C20-04 | R. Bruggeman، *Kuznetsov's proof of the Ramanujan--Petersson conjecture for modular forms of weight zero* (1979) | `CONSENSUS-FETCHED / HISTORICAL-TRIAGE` |
| C20-05 | Liu--Ye، *Petersson and Kuznetsov Trace Formulas* (2006) | `CONSENSUS-FETCHED / CROSS-CHECK-CANDIDATE` |
| C20-06 | Hejhal، Volume II (1983) | `CONSENSUS-FETCHED / NONCOMPACT-DETAILS-DEFERRED` |

## اختبارات قبول المصدر

- تطابق الوزن والمستوى والشخصية.
- تثبيت قياس القطع الزائد وإشارة لابلاس.
- تثبيت حاصل بيترسون وتطبيع معاملات فورييه وHecke.
- تثبيت تعريف \(S(m,n;c)\) وعوامل \(J\)- و\(K\)-Bessel.
- إبقاء الطيف المستمر في الحالة غير المدمجة.
- فصل الصيغة الدقيقة عن العرض التخطيطي.
- منع الاعتماد العكسي على الفصل 21.

## مطابقة Kuznetsov المغلقة

أغلقت المطابقة للنواة المعتمدة عند المستوى 1 في `CHAPTER_20_KUZNETSOV_CROSSCHECK_2026-07-25.md`: الطيف المنفصل، طيف Eisenstein، الحد القطري، حد Kloosterman، وتحويل \(J\). وفُصل تحويل \(K\) إلى سياق الإشارة المتعاكسة، فلا يخلط بالنواة الأساسية ولا يمنح صيغة عامة غير مطابقة.

## العوائق المفتوحة

1. تثبيت زوج تحويل Selberg وعوامل \(2\pi\) من النص الكامل ومطابقته مع Hejhal.
2. مراجعة مستقلة للحزمة قبل التجميد.

حتى إغلاق هذه البنود يبقى `PASS-FOR-AUTHORING = NO`.
