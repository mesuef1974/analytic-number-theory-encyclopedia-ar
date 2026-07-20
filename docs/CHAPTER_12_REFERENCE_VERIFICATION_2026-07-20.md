# التحقق المرجعي للفصل الثاني عشر

## بيانات التحقق

```text
CHAPTER       = 12 — مبرهنة Siegel--Walfisz
VERSION       = 0.16.0-dev
BRANCH        = agent/chapter-12-siegel-walfisz-v0.16.0
DATE          = 2026-07-20
STATE         = PASS-FOR-ADOPTED-ROUTE
```

## منهج التحقق

بدأ المسح عبر Consensus قبل بقية المصادر، ثم تحققت بيانات الأوراق من arXiv وصفحات الناشرين. استعملت الكتب القياسية لتثبيت المسار الكلاسيكي للصيغة الصريحة والمناطق الخالية، لا بوصفها بديلًا عن بيان منشأ كل نتيجة.

## المداخل المقتبسة في المتن

### `ANT-THM-12-01` — حد دو لا فاليه بوسان

الصيغة المستعملة:

\[
\psi(x)=x+O\left(xe^{-c\sqrt{\log x}}\right).
\]

المراجع المعتمدة:

- de la Vallée Poussin (1896).
- Davenport، *Multiplicative Number Theory*، الطبعة الثالثة.
- Montgomery--Vaughan، *Multiplicative Number Theory I*.

الحالة:

```text
ORIGIN      = CITED
EFFECTIVITY = EFFECTIVE
VERDICT     = PASS
```

### `ANT-THM-12-02` — الصيغة الصريحة المقطوعة

يستعمل الفصل صيغة مقطوعة موحدة بعد عزل الصفر الاستثنائي، مع خطأ قطع وحد من المنطقة الخالية. لا يدعي الفصل إثبات بيرون وتحويل المسار كاملين.

المراجع المعتمدة:

- Davenport، الفصول الكمية الخاصة بـPNT في المتتاليات الحسابية.
- Montgomery--Vaughan، الصيغة الصريحة وعد الأصفار والمناطق الخالية.
- Iwaniec--Kowalski، البنية الموحدة للأصفار الاستثنائية والتقديرات الصريحة.

الحالة:

```text
ORIGIN             = CITED
PERRON-DEBT         = DECLARED
CONTOUR-SHIFT-DEBT  = DECLARED
VERDICT             = PASS-AS-CITED
```

## الأوراق الحديثة المتحققة

### Thorner--Zaman

```text
AUTHORS  = Jesse Thorner; Asif Zaman
TITLE    = Refinements to the Prime Number Theorem for Arithmetic Progressions
JOURNAL  = Mathematische Zeitschrift
VOLUME   = 306
NUMBER   = 3
ARTICLE  = 54
YEAR     = 2024
DOI      = 10.1007/s00209-023-03414-3
ARXIV    = 2108.10878
```

أكدت صفحة Springer أن الورقة نشرت في 20 فبراير 2024، وأن نتيجتها الموحدة تستنتج Siegel--Walfisz، مع استعمال منطقة Vinogradov--Korobov وتقدير كثافة خال من اللوغاريتم وتنافر الأصفار. أكد arXiv العنوان والمؤلفين والمرجع المنشور.

الاستعمال داخل الفصل: مقارنة مع مسار أقوى، لا اعتماد برهاني لازم للنواة الكلاسيكية.

### Koukoulopoulos

```text
AUTHOR   = Dimitris Koukoulopoulos
TITLE    = Pretentious Multiplicative Functions and the Prime Number Theorem for Arithmetic Progressions
JOURNAL  = Compositio Mathematica
VOLUME   = 149
NUMBER   = 7
PAGES    = 1129--1149
YEAR     = 2013
DOI      = 10.1112/S0010437X12000802
```

أكدت صفحة Cambridge بيانات النشر وأن الورقة تقدم برهانًا حديثًا من منظور الدوال الضربية الادعائية.

الاستعمال داخل الفصل: مسار مقارن فقط.

### Drappeau--Fiorilli

```text
AUTHORS  = Sary Drappeau; Daniel Fiorilli
TITLE    = The First Moment of Primes in Arithmetic Progressions: Beyond the Siegel--Walfisz Range
JOURNAL  = Transactions of the London Mathematical Society
VOLUME   = 8
NUMBER   = 1
PAGES    = 174--185
YEAR     = 2021
DOI      = 10.1112/tlm3.12030
ARXIV    = 2003.02201
```

أكدت صفحة الناشر وarXiv البيانات الأساسية، وأن الدراسة المتوسطية خارج مجال Siegel--Walfisz تتتبع أثر أصفار Landau--Siegel.

الاستعمال داخل الفصل: تفسير حدود النطاق والفرق بين النتيجة الفردية والنتائج المتوسطية.

## تدقيق عدم المبالغة

- لا تنسب الصيغة الصريحة إلى برهان داخلي.
- لا تنسب عدم الفعالية إلى المنطقة الخالية؛ مصدرها استعمال مبرهنة Siegel.
- لا تستعمل ورقة Thorner--Zaman لإثبات المسار الأدنى ثم تدعي استقلاله عنها.
- لا توصف Bombieri--Vinogradov بأنها نتيجة من Siegel--Walfisz.
- لا يدعى أفضل ثابت في الأس.

## ديون غير حاجزة

- أرقام الصفحات الدقيقة في النسخ المحلية للكتب القياسية.
- مطابقة حرفية إضافية لصيغة الخطأ المقطوعة مع طبعة كتاب واحدة قبل `RELEASE-READY`.
- مراجعة مستقلة ثانية للفصل بعد اكتمال البناء.

## الحكم

```text
CONSENSUS-FIRST       = PASS
PUBLISHER-METADATA    = PASS
ARXIV-METADATA        = PASS
CITED-INPUTS          = IDENTIFIED
ORIGIN-LABELS         = PASS
REFERENCE-VERDICT     = PASS-FOR-ADOPTED-ROUTE
RELEASE-READY         = NO
```
