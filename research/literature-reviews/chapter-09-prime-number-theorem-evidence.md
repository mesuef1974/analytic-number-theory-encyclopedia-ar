# سجل أدلة الفصل التاسع

## مبرهنة الأعداد الأولية

التاريخ: 2026-07-20  
الإصدار: `0.13.0-dev`  
الفرع: `agent/chapter-09-prime-number-theorem-v0.13.0`  
الحالة: `EVIDENCE-FIRST / PRE-AUTHORING-GATE-CLOSED`

## 1. النطاق والنتيجة المركزية

النتيجة المركزية للفصل هي

\[
\psi(x)=\sum_{n\le x}\Lambda(n)\sim x.
\]

ثم يستنتج الفصل

\[
\vartheta(x)=\sum_{p\le x}\log p\sim x
\]

ومن النتيجة السابقة `ANT-THM-02-04` يستنتج

\[
\pi(x)\sim\frac{x}{\log x}.
\]

النسخة الأساسية نوعية ولا تتضمن حد خطأ فعالا. وأي تقدير فعال يعامل بوصفه
مسارا أقوى مستقلا يحتاج المنطقة الكمية الخالية من الأصفار وصيغة بيرون
وتحويل المسار وتقديرات النمو المناسبة.

## 2. قرار المسارات

### 2.1 المسار الأساسي المعتمد

اعتمد المسار التاوبيري عبر صيغة خاصة من Wiener--Ikehara:

```text
المشتقة اللوغاريتمية لزيتا
        |
        v
عدم انعدام زيتا على Re(s)=1
        |
        v
إزالة القطب عند s=1
        |
        v
Wiener--Ikehara
        |
        v
psi(x) ~ x
        |
        v
theta(x) ~ x
        |
        v
pi(x) ~ x/log x
```

هذا المسار لا يستعمل بيرون أو تحويل المسار أو الصيغة الصريحة أو المنطقة
الكمية الخالية من الأصفار.

### 2.2 المسار الكلاسيكي الفعال

مسار Hadamard--de la Vallée Poussin مسجل بوصفه مسارا ثانيا تاريخيا وكميا.
عدم الانعدام على الخط يدخل فيه، لكن استخراج حد خطأ فعال يحتاج أدوات ما تزال
`DEFERRED` أو `CITED` في الفصل السادس. لذلك لا يستعمل لإثبات النتيجة
المركزية في المسودة الأولى.

### 2.3 المسار الأولي

برهان Selberg--Erdős الأولي مسار مستقل لاحق. لا تخلط لممه بالمسار
التاوبيري، ولا يوصف بأنه مجرد حذف للتحليل العقدي من البرهان نفسه.

## 3. هرم الاعتماد المرجعي

1. المصدر الأصلي للادعاء التاريخي أو المبرهنة المنسوبة.
2. مرجع قياسي لتثبيت الصياغة الحديثة والفروض والاصطلاحات.
3. قواعد الاكتشاف الأكاديمي لتحديد السجلات فقط.
4. النسخ الأولية الحديثة للمقارنة، لا لاعتماد ادعاء قبل الرجوع إلى الأصل.

## 4. سجل الاكتشاف الأكاديمي

| القناة | عبارات البحث | الاستعمال | الحكم |
|---|---|---|---|
| zbMATH Open | `prime number theorem`, `Hadamard`, `de la Vallée Poussin`, `Wiener-Ikehara` | اكتشاف السجلات والمراجعات | اكتشاف فقط |
| Semantic Scholar | `Wiener-Ikehara theorem prime number theorem` | اكتشاف صيغ حديثة | لا اعتماد من الملخص |
| arXiv | `Tauberian proof prime number theorem` | مقارنة تعليمية | مصدر استكشافي |
| OpenAlex | البحث بالعنوان وDOI | مطابقة بيانات السجل | لا يغني عن الأصل |
| Consensus | المسارات الثلاثة | تعذر بسبب نفاد الحصة الشهرية | قيد اكتشاف، لا فجوة علمية |

تاريخ القطع الأدبي: `2026-07-20`.

## 5. المصادر الأصلية

### 5.1 Hadamard (1896)

- Jacques Hadamard, *Sur la distribution des zéros de la fonction
  \(\zeta(s)\) et ses conséquences arithmétiques*.
- `Bulletin de la Société Mathématique de France` 24 (1896), 199--220.
- DOI: `10.24033/bsmf.545`.
- الدور: أحد البرهانين التحليليين المستقلين لمبرهنة الأعداد الأولية.
- الحالة: `BIBLIOGRAPHY-VERIFIED`.

### 5.2 de la Vallée Poussin (1896)

- Charles-Jean de la Vallée Poussin, *Recherches analytiques sur la théorie
  des nombres premiers*، الأجزاء الثلاثة في المجلد 20.
- الصفحات: 183--256، 281--362، 363--397.
- الدور: البرهان المستقل وعدم الانعدام على الخط والتطوير الكمي اللاحق.
- الحالة: `BIBLIOGRAPHY-VERIFIED / CLAIM-LEVEL-CITATION-DEFERRED`.

### 5.3 Wiener (1930)

- Norbert Wiener, *Generalized Harmonic Analysis*.
- `Acta Mathematica` 55 (1930), 117--258.
- DOI: `10.1007/BF02546511`.
- الدور: الأصل التحليلي لمبرهنة Wiener التاوبيرية.
- الحالة: `BIBLIOGRAPHY-VERIFIED`.

### 5.4 Ikehara (1931)

- Shikao Ikehara, *An Extension of Landau's Theorem in the Analytical
  Theory of Numbers*.
- `Journal of Mathematics and Physics` 10 (1931), 1--12.
- DOI: `10.1002/sapm19311011`.
- الدور: الصيغة التاوبيرية الأصلية وتطبيقها على مبرهنة الأعداد الأولية.
- الحالة: `BIBLIOGRAPHY-VERIFIED`.

## 6. صيغة Wiener--Ikehara المعتمدة

اعتمدت الصيغة الخاصة للمتسلسلات الديريشلية في:

- Jaap Korevaar, *The Wiener--Ikehara theorem by complex analysis*.
- `Proceedings of the American Mathematical Society` 134 (2006), 1107--1116.
- DOI: `10.1090/S0002-9939-05-08060-3`.
- نص المبرهنة: Theorem 1.1، الصفحتان 1107--1108.
- تطبيقها على \(-\zeta'/\zeta\) ومبرهنة الأعداد الأولية: القسم 2،
  الصفحتان 1108--1109.

الصيغة المستعملة:

لتكن

\[
f(s)=\sum_{n\ge1}\frac{a_n}{n^s},
\qquad a_n\ge0,
\]

متقاربة عندما \(\Re(s)>1\)، ولتكن

\[
S(x)=\sum_{n\le x}a_n.
\]

إذا كان \(S(n)=O(n)\)، وكان

\[
f(s)-\frac{A}{s-1}
\]

يمتد تحليليا أو باستمرار إلى نصف المستوى المغلق \(\Re(s)\ge1\)، فإن

\[
S(n)\sim An.
\]

قرار الحالة:

```text
ANT-THM-09-02 = CITED
```

لم تخلط هذه الصيغة بنسخ أضعف ذات شروط حدية توزيعية.

## 7. الكتب القياسية ومسؤولية كل مرجع

| المرجع | الموضع | الدور | الحالة |
|---|---|---|---|
| Apostol (1976) | الفصل 13، الصفحات 278--303 | برهان تحليلي تعليمي ومبرهنة الأعداد الأولية | `PAGE-RANGE-VERIFIED` |
| Davenport (2000) | فصل مبرهنة الأعداد الأولية، الصفحات 111--114 | المسار الكلاسيكي المركز | `PAGE-RANGE-VERIFIED` |
| Montgomery--Vaughan (2007) | الفصل 6، الصفحات 168--198 | تنظيم المسار الكلاسيكي وتطبيقاته | `PAGE-RANGE-VERIFIED` |
| Iwaniec--Kowalski (2004) | الفصل 3 يبدأ ص31، والفصل 5 يبدأ ص93 | لغة حديثة وحدود كمية | `SECTION-START-VERIFIED` |
| Tenenbaum (2015) | II.4 وII.7 | مقارنة PNT بالمبرهنات التاوبيرية | `SECTION-VERIFIED` |
| Titchmarsh (1986) | الفصول المبكرة في Hadamard--de la Vallée Poussin | زيتا وعدم الانعدام والمسار الكمي | `CHAPTER-LEVEL-VERIFIED` |
| Korevaar (2006) | 1107--1109 | الصيغة المعتمدة وتطبيق PNT | `CLAIM-PAGES-VERIFIED` |

المرجع الحاكم للصيغة التاوبيرية في متن الفصل هو Korevaar 2006.

## 8. الأدلة المغلقة داخل الموسوعة

| المعرّف | النتيجة | الحالة | الدور |
|---|---|---|---|
| `ANT-THM-02-02` | الجمع الجزئي لأبيل | `PROVED-HERE` | الانتقال بين دوال العد |
| `ANT-THM-02-04` | \(\vartheta\sim x\Rightarrow\pi\sim x/\log x\) | `PROVED-HERE` | الاستنتاج النهائي |
| `ANT-THM-05-05` | \(-\zeta'/\zeta=\sum\Lambda(n)n^{-s}\) | `PROVED-HERE` | السلسلة المركزية |
| `ANT-THM-06-01` | قطب زيتا البسيط عند \(1\) | `PROVED-HERE` | معامل الحد الرئيسي |
| `ANT-THM-06-03` | الاستمرار الميرومورفي | `PROVED-HERE` | دراسة الخط \(\Re(s)=1\) |
| `ANT-LEM-07-01` | \(3+4\cos u+\cos2u\ge0\) | `PROVED-HERE` | برهان عدم الانعدام |
| `ANT-THM-06-08` | الصيغة الصريحة | `CITED` | لا تدخل المسار الأساسي |
| `ANT-THM-06-09` | المنطقة الكلاسيكية الخالية | `CITED` | للمسار الكمي فقط |
| `ANT-THM-03-09` | نواة بيرون | `DEFERRED` | لا تدخل المسار الأساسي |

## 9. الأدلة المغلقة في تدقيق ما قبل التأليف

سجلت التفاصيل في:

```text
docs/CHAPTER_09_PRE_AUTHORING_AUDIT_2026-07-20.md
```

وأغلق التدقيق:

1. حد تشيبيشيف \(\vartheta(x)\ll x\).
2. الحد \(\psi(x)\ll x\).
3. الحد \(\psi(x)-\vartheta(x)\ll\sqrt{x}\log x=o(x)\).
4. المتراجحة الموزونة للمشتقة اللوغاريتمية.
5. عدم انعدام \(\zeta(s)\) على الخط \(\Re(s)=1\) من دون دور.
6. إزالة قطب \(-\zeta'/\zeta\) عند \(s=1\).
7. مطابقة فروض Korevaar مع \(a_n=\Lambda(n)\) و\(A=1\).

## 10. مراجعة ديون الفصل السادس

- مبدأ الحجة المجرد: `PROVED-HERE`، ولا يحتاجه المسار الأساسي.
- صيغة بيرون: `DEFERRED`، ولا تستعمل.
- تحويل المسار: `DEFERRED`، ولا يستعمل.
- المنطقة الخالية الكمية: `CITED`، للمسار الفعال فقط.
- الصيغة الصريحة: `CITED`، ولا تستعمل لإثبات \(\psi(x)\sim x\).

## 11. فحص عدم الدور

| السؤال | الحكم |
|---|---|
| هل يستعمل عدم الانعدام PNT؟ | `PASS`؛ يستعمل المنتج الأويلري والقطب والمتراجحة فقط |
| هل يستعمل حد تشيبيشيف PNT؟ | `PASS`؛ يستعمل المعامل الثنائي والتقسيم الثنائي |
| هل يستعمل الانتقال \(\psi\to\vartheta\) تقدير \(\pi\)؟ | `PASS` |
| هل تستعمل Wiener--Ikehara الصيغة الصريحة؟ | `PASS`؛ لا |
| هل النتيجة النوعية مختلطة بحد فعال؟ | `PASS`؛ المساران مفصولان |
| هل يعود الاستنتاج \(\pi\sim x/\log x\) إلى فرض سابق؟ | `PASS`؛ لا |

## 12. قرار البوابة

```text
MAIN-HEAD = VERIFIED-AT-2071a05a5cc3eb623a9217827ae71a2833dfe18c
WIENER-IKEHARA-EXACT-STATEMENT = CLOSED
WIENER-IKEHARA-STATUS = CITED
CHEBYSHEV-LINEAR-BOUND = PROVED-IN-AUDIT
ZETA-LINE-NONVANISHING = PROVED-IN-AUDIT
REMOVABLE-POLE-CHECK = PASS
PSI-TO-THETA-LEMMA = PROVED-IN-AUDIT
PAGE-LEVEL-SOURCE-VERIFICATION = CLOSED-FOR-ADOPTED-ROUTE
NO-CIRCULARITY = PASS
PRE-AUTHORING-GATE = CLOSED
AUTHORING = AUTHORIZED
CHAPTER-TEXT = NOT-YET-VERIFIED
```

إغلاق البوابة يسمح ببدء المسودة فقط، ولا يجعل الفصل `VERIFIED` أو
`REVIEWED` أو `RELEASE-READY`.