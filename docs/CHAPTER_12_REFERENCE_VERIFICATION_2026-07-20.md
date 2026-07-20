# التحقق المرجعي للفصل الثاني عشر

## بيانات التحقق

```text
CHAPTER       = 12 — مبرهنة Siegel--Walfisz
VERSION       = 0.16.0-dev
BRANCH        = agent/chapter-12-siegel-walfisz-v0.16.0
DATE          = 2026-07-21
STATE         = PASS-AFTER-LOCAL-REVIEW-CORRECTIONS
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
- Davenport، *Multiplicative Number Theory*، الطبعة الثانية، الفصل 19، الصفحات 111--114.
- Montgomery--Vaughan، *Multiplicative Number Theory I*، الفصل 6، الصفحات 168--198.

الحالة:

```text
ORIGIN      = CITED
EFFECTIVITY = EFFECTIVE
VERDICT     = PASS
```

### `ANT-THM-12-02` — مدخل كمي مركب للصيغة الصريحة

الصيغة المستعملة ليست نقلًا حرفيًا لمبرهنة واحدة، بل مدخل مركب يجمع:

1. الصيغة الصريحة المقطوعة لـ\(\psi_0(x,\chi)\).
2. اختيار ارتفاع جيد \(U\in[T,2T]\) لا يقع على ارتفاع صفر.
3. تقدير عد الأصفار والخسائر اللوغاريتمية.
4. المنطقة القياسية الخالية بعد فصل الصفر الاستثنائي الممكن.
5. امتصاص الأصفار البديهية وعامل غاما وخطأ القطع في حد موحد.

المواضع الدقيقة للمسار الكلاسيكي:

- Davenport، *Multiplicative Number Theory*، الطبعة الثانية:
  - الفصل 20: *The Explicit Formula for \(\psi(x,\chi)\)*، الصفحات 115--120.
  - الفصل 21: *The Prime Number Theorem for Arithmetic Progressions (I)*، الصفحات 121--125.
  - الفصل 22: *Siegel's Theorem*، الصفحات 126--131.
  - الفصل 23: *The Prime Number Theorem for Arithmetic Progressions (II)*، الصفحات 132--134.
- Montgomery--Vaughan، *Multiplicative Number Theory I*:
  - الفصل 11: *Primes in arithmetic progressions: II*، الصفحات 358--396.
  - الفصل 12: *Explicit formulæ*، الصفحات 397--418.

بعد المراجعة المحلية صُحح اتساق متغير الارتفاع: الارتفاع المختار هو
\(U\in[T,2T]\)، وتظهر \(U\) نفسها في جميع حدود الصيغة وفي البرهان اللاحق.

الحالة:

```text
ORIGIN             = CITED / COMPOSITE-INPUT
VERBATIM-CLAIM     = NO
PERRON-DEBT         = DECLARED
CONTOUR-SHIFT-DEBT  = DECLARED
HEIGHT-VARIABLE     = CONSISTENT / U
VERDICT             = PASS-AS-COMPOSITE-CITED-INPUT
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

## إغلاق ملاحظات المراجعة المحلية

### R1 — الصيغة الصريحة المقطوعة

```text
STATUS = CLOSED
FIX    = COMPOSITE-CITED-INPUT + EXACT CHAPTER/PAGE PROVENANCE
DETAIL = T_0 REMOVED; U USED CONSISTENTLY
```

### R2 — الانتقال إلى \(\pi(x;q,a)\)

سُجلت الهوية الدقيقة

\[
\frac{x}{\log x}+\int_y^x\frac{dt}{\log^2t}
=
\operatorname{Li}(x)-\operatorname{Li}(y)+\frac{y}{\log y},
\]

ومن ثم صار الفرق عن \(\operatorname{Li}(x)\) موسومًا \(O(y)\)، لا «ثابتًا محدودًا».

```text
STATUS = CLOSED
FIX    = MAIN-TERM-DIFFERENCE EXPLICITLY O(y)
```

## تدقيق عدم المبالغة

- لا تنسب الصيغة الصريحة المركبة إلى نص حرفي لمبرهنة واحدة.
- لا تنسب عدم الفعالية إلى المنطقة الخالية؛ مصدرها استعمال مبرهنة Siegel.
- لا تستعمل ورقة Thorner--Zaman لإثبات المسار الأدنى ثم تدعي استقلاله عنها.
- لا توصف Bombieri--Vinogradov بأنها نتيجة من Siegel--Walfisz.
- لا يدعى أفضل ثابت في الأس.
- لا يدعى إغلاق بيرون وتحويل المسار داخل الموسوعة.

## ديون غير حاجزة

- إعادة بناء محلية متزامنة على جهاز المالك وإيداع `docs/LOCAL_BUILD_RECEIPT.md`.
- مراجعة بكسلية للـPDF الناتج بعد التصحيح.
- تدقيق إصدار نهائي مستقل قبل `RELEASE-READY`.

## الحكم

```text
CONSENSUS-FIRST       = PASS
PUBLISHER-METADATA    = PASS
ARXIV-METADATA        = PASS
CITED-INPUTS          = IDENTIFIED
COMPOSITE-PROVENANCE  = PASS
HEIGHT-CONSISTENCY    = PASS
PI-TRANSFER           = PASS-AFTER-CORRECTION
REFERENCE-VERDICT     = PASS-AFTER-LOCAL-REVIEW-CORRECTIONS
LOCAL-SYNC-BUILD      = REQUIRED-BEFORE-FINAL-REVIEW-VERDICT
RELEASE-READY         = NO
```
