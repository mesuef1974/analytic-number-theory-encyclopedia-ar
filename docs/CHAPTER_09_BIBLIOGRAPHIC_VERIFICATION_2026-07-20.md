# التحقق المرجعي للفصل التاسع

## مبرهنة الأعداد الأولية — المسار التاوبيري المعتمد

التاريخ: 2026-07-20  
الإصدار: `0.13.0-dev`  
الحالة: `PASS-FOR-ADOPTED-ROUTE`

## 1. نطاق الحكم

يشمل هذا الحكم فقط:

1. صيغة Wiener--Ikehara المستعملة في متن الفصل.
2. تطبيقها على متسلسلة \(-\zeta'/\zeta\) ودالة \(\psi\).
3. البيانات الببليوغرافية للمصادر التاريخية المذكورة في المتن.
4. مواضع الفصول العامة في الكتب القياسية المستخدمة لمسار القراءة.

لا يشمل الحكم إثباتات المسار الكلاسيكي الفعال عبر بيرون وتحويل المسار، ولا
يمنحها حالة `PROVED-HERE`. تبقى تلك الأدوات بحالاتها المسجلة في الفصل السادس.

## 2. المصدر الحاكم لصيغة Wiener--Ikehara

### Korevaar (2006)

البيانات:

- Jaap Korevaar.
- *The Wiener--Ikehara Theorem by Complex Analysis*.
- `Proceedings of the American Mathematical Society` 134 (2006),
  1107--1116.
- DOI: `10.1090/S0002-9939-05-08060-3`.

المواضع:

- Theorem 1.1، الصفحتان 1107--1108: صيغة المتسلسلات الديريشلية ذات
  المعاملات غير السالبة، وشرط المجاميع الجزئية \(O(n)\)، وامتداد الباقي
  بعد طرح القطب.
- القسم 2، الصفحتان 1108--1109: التطبيق على
  \(-\zeta'/\zeta\)، ودالة فون مانغولت، وعدم انعدام زيتا على الخط، ثم
  استنتاج مبرهنة الأعداد الأولية.

المطابقة مع المتن:

| عنصر الصيغة | موضعه في الفصل | الحكم |
|---|---|---|
| \(a_n\ge0\) | \(a_n=\Lambda(n)\) | `MATCH` |
| تقارب السلسلة في \(\Re(s)>1\) | `ANT-THM-05-05` | `MATCH` |
| المجاميع الجزئية \(O(n)\) | `ANT-LEM-09-02` | `MATCH` |
| القطب \(A/(s-1)\) | \(A=1\) | `MATCH` |
| امتداد الباقي إلى الخط | `ANT-THM-09-01` وإزالة القطب | `MATCH` |
| النتيجة | \(\psi(n)\sim n\) | `MATCH` |

قرار الحالة:

```text
ANT-THM-09-02 = CITED
```

## 3. المصدر الأصلي لـIkehara

- Shikao Ikehara.
- *An Extension of Landau's Theorem in the Analytical Theory of Numbers*.
- `Journal of Mathematics and Physics` 10 (1931), 1--12.
- DOI: `10.1002/sapm19311011`.

الحكم: `BIBLIOGRAPHY-VERIFIED`. يستعمل للإسناد التاريخي، بينما تضبط صيغة
Korevaar الحديثة العبارة الدقيقة المستعملة في البرهان.

## 4. المصدر الأصلي لـWiener

- Norbert Wiener.
- *Generalized Harmonic Analysis*.
- `Acta Mathematica` 55 (1930), 117--258.
- DOI: `10.1007/BF02546511`.

الحكم: `BIBLIOGRAPHY-VERIFIED`. دوره تاريخي وبنيوي، ولا تنقل منه صيغة
المتن حرفيًا.

## 5. المصدران التاريخيان لمبرهنة الأعداد الأولية

### Hadamard (1896)

- Jacques Hadamard.
- *Sur la distribution des zéros de la fonction \(\zeta(s)\) et ses
  conséquences arithmétiques*.
- `Bulletin de la Société Mathématique de France` 24 (1896), 199--220.
- DOI: `10.24033/bsmf.545`.

الحكم: `BIBLIOGRAPHY-VERIFIED`.

### de la Vallée Poussin (1896)

- *Recherches analytiques sur la théorie des nombres premiers*.
- `Annales de la Société Scientifique de Bruxelles` 20 (1896).
- الأجزاء المثبتة ببليوغرافيًا: 183--256، 281--362، 363--397.

الحكم: `BIBLIOGRAPHY-VERIFIED / CLAIM-LEVEL-DEFERRED`. لا تستعمل إحالة
داخلية إلى خطوة بعينها من الأصل في المسودة الحالية.

## 6. الكتب القياسية

| المرجع | الموضع المثبت | استعماله |
|---|---|---|
| Apostol (1976) | الفصل 13، 278--303 | البرهان التحليلي التعليمي ومبرهنة الأعداد الأولية |
| Davenport (2000) | فصل PNT، 111--114 | المسار الكلاسيكي المركز |
| Montgomery--Vaughan (2007) | الفصل 6، 168--198 | تنظيم المسار الكلاسيكي والتطبيقات |
| Iwaniec--Kowalski (2004) | الفصل 3 يبدأ ص31؛ الفصل 5 يبدأ ص93 | النظرية الأولية للأوليات والتحليل الكلاسيكي لدوال \(L\) |
| Tenenbaum (2015) | II.4 وII.7 | PNT والمبرهنات التاوبيرية |
| Titchmarsh (1986) | الفصول المبكرة في Hadamard--de la Vallée Poussin | زيتا وعدم الانعدام والمسار الفعال |

هذه الكتب مراجع مقارنة وتوسع. لا يحمل أي موضع عام منها عبء صياغة
Wiener--Ikehara؛ ذلك العبء محمول على Korevaar 2006.

## 7. قواعد الاستعمال في المتن

1. تذكر صفحات Korevaar مباشرة عند صياغة `ANT-THM-09-02`.
2. يوسم المصدر الأصلي تاريخيًا، ولا ينسب إليه نص الصيغة الحديثة من دون مطابقة.
3. لا تستعمل المنطقة الخالية أو الصيغة الصريحة كبرهان داخلي.
4. لا توصف إحالات الكتب العامة بأنها تحقق صفحة مستقلا لكل خطوة كمية.
5. أي توسع لاحق في حد الخطأ يحتاج تقرير تحقق جديدا مستقلا عن هذا الحكم.

## 8. الحكم النهائي

```text
KOREVAAR-METADATA = PASS
KOREVAAR-THEOREM-LOCATION = PASS
KOREVAAR-PNT-APPLICATION-LOCATION = PASS
IKEHARA-METADATA = PASS
WIENER-METADATA = PASS
HADAMARD-METADATA = PASS
DE-LA-VALLEE-POUSSIN-METADATA = PASS-WITH-CLAIM-LEVEL-DEFERRED
STANDARD-BOOK-LOCATIONS = PASS-FOR-READING-MAP
ADOPTED-ROUTE-REFERENCE-VERIFICATION = PASS
CLASSICAL-EFFECTIVE-ROUTE-VERIFICATION = NOT-COVERED
```

هذا الحكم مرجعي داخلي، وليس مراجعة ثانية مستقلة للفصل كله.