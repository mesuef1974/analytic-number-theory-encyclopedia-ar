# التحقق المرجعي النهائي قبل تأليف الفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                = 13
AUDIT                  = FINAL-REFERENCE-VERIFICATION
PRIMARY-SOURCES        = VERIFIED
TECHNICAL-THEOREMS     = VERIFIED BY NUMBER AND PRINTED PAGE
BIBTEX-KEYS            = VERIFIED / UNIQUE
CORRECTION-RECORD      = INCLUDED
VERDICT                = PASS-FOR-AUTHORING
REFERENCE-BLOCKERS     = 0
RELEASE-READY          = NO
```

## 1. Bombieri 1965

```text
KEY      = Bombieri1965LargeSieve
AUTHOR   = Enrico Bombieri
TITLE    = On the Large Sieve
JOURNAL  = Mathematika
VOLUME   = 12
ISSUE    = 2
YEAR     = 1965
PAGES    = 201--225
DOI      = 10.1112/S0025579300005313
STATUS   = VERIFIED / CAMBRIDGE CORE
```

صفحة الناشر تصف الورقة بأنها تقدم نسخة محسنة من غربال Linnik الكبير مع
تطبيقات. تستعمل بوصفها المصدر التاريخي الأصلي، لا بوصفها المرجع الوحيد
للصياغة التعليمية الحديثة.

## 2. A. I. Vinogradov 1965 والتصحيح 1966

### الورقة الأصلية

```text
KEY      = Vinogradov1965Density
AUTHOR   = A. I. Vinogradov
TITLE    = The Density Hypothesis for Dirichlet L-Series
JOURNAL  = Izv. Akad. Nauk SSSR Ser. Mat.
VOLUME   = 29
ISSUE    = 4
YEAR     = 1965
PAGES    = 903--934
MATHNET  = im3080
MR       = 0197414
STATUS   = VERIFIED / MATHNET
```

### التصحيح

```text
KEY      = Vinogradov1966Correction
AUTHOR   = A. I. Vinogradov
TITLE    = Correction to the Paper "The Density Hypothesis for Dirichlet L-Series"
JOURNAL  = Izv. Akad. Nauk SSSR Ser. Mat.
VOLUME   = 30
ISSUE    = 3
YEAR     = 1966
PAGES    = 719--720
MATHNET  = im2856
STATUS   = VERIFIED / MATHNET
```

إدراج التصحيح إلزامي في سجل الفصل حتى لا تظهر ورقة 1965 منفردة كما لو لم
يلحقها تصويب منشور.

## 3. Gallagher 1968

```text
KEY      = Gallagher1968Bombieri
AUTHOR   = Patrick X. Gallagher
TITLE    = Bombieri's Mean Value Theorem
JOURNAL  = Mathematika
VOLUME   = 15
ISSUE    = 1
YEAR     = 1968
PAGES    = 1--6
DOI      = 10.1112/S002557930000231X
STATUS   = VERIFIED / CAMBRIDGE CORE
```

يستعمل للسياق التاريخي للبرهان القصير، لا بوصفه المسار التعليمي المركزي
للفصل.

## 4. Vaughan 1975

```text
KEY      = Vaughan1975MeanValue
AUTHOR   = Robert C. Vaughan
TITLE    = Mean Value Theorems in Prime Number Theory
JOURNAL  = Journal of the London Mathematical Society
SERIES   = 2
VOLUME   = 10
ISSUE    = 2
YEAR     = 1975
PAGES    = 153--162
DOI      = 10.1112/jlms/s2-10.2.153
STATUS   = VERIFIED / OXFORD ACADEMIC
```

هذه الورقة هي المرجع التاريخي المباشر لمسار القيمة المتوسطة المبني على هوية
Vaughan.

## 5. Montgomery--Vaughan II

```text
KEY       = MontgomeryVaughan2026
AUTHORS   = Hugh L. Montgomery; Robert C. Vaughan
TITLE     = Multiplicative Number Theory II: Primes and Sieves
PUBLISHER = Cambridge University Press
YEAR      = 2026
SERIES    = Cambridge Studies in Advanced Mathematics
VOLUME    = 218
ISBN      = 9781009445054
EISBN     = 9781009445030
DOI       = 10.1017/9781009445030
STATUS    = VERIFIED / CAMBRIDGE CORE AND AUTHOR PDF
```

صفحة الناشر تثبت أن الفصل 19 هو **The Large Sieve** في الصفحات 149--188،
وأن الفصل 20 هو **Primes in Arithmetic Progressions: III**. استعملت نسخة
المؤلف لمطابقة أرقام المبرهنات والصفحات المطبوعة الآتية.

## 6. المطابقة التقنية بالمبرهنة والصفحة

| الاستعمال في الفصل 13 | الموضع المتحقق |
|---|---|
| هوية Vaughan ذات الحدود الأربعة | الصيغة (17.5)، الصفحتان 55--56 |
| الغربال الكبير للشخصيات البدائية مع الوزن \(q/\varphi(q)\) | المبرهنة 19.16، الصفحة 175 |
| المدخل الثنائي العظمى مع `sup_y` | المبرهنة 19.19، الصيغة (19.34)، الصفحة 181 |
| مبرهنة القيمة المتوسطة لـ\(\psi(y,\chi)\) | المبرهنة 20.1، الصفحة 189 |
| Bombieri--Vinogradov في صيغة \(E^*(x,q)\) | المبرهنة 20.2، الصفحة 195 |
| الرد من الترديد إلى الموصل واستعمال Siegel--Walfisz للصغار | برهان المبرهنة 20.2، الصفحتان 196--197 |

### الصيغ التي تمت مطابقتها

الغربال الكبير:

\[
\sum_{q\le Q}\frac q{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|\sum_{M<n\le M+N}c_n\chi(n)\right|^2
\le (N+Q^2)\sum|c_n|^2.
\]

القيمة المتوسطة:

\[
\sum_{q\le Q}\frac q{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|\psi(y,\chi)|
\ll
\left(x+x^{5/6}Q+x^{1/2}Q^2\right)(\log x)^3.
\]

ومتوسط أخطاء الفئات:

\[
\sum_{q\le Q}E^*(x,q)
\ll x^{1/2}Q(\log x)^3
\]

في المجال المرجعي القريب من مستوى \(x^{1/2}\).

## 7. حكم منشأ النتائج

| النتيجة | الحكم المرجعي |
|---|---|
| حزمة الغربال الكبير التربيعية والثنائية العظمى | `CITED / COMPOSITE-INPUT` |
| هوية Vaughan | الصيغة مطابقة للمصدر، والبرهان في المشروع `PROVED-HERE` |
| Pólya--Vinogradov | `PROVED-HERE` من نتائج الفصل السابع |
| Type I وType II | `PROVED-HERE` اعتمادًا على الحزمة المقتبسة |
| مبرهنة القيمة المتوسطة | `PROVED-HERE` اعتمادًا على الحزمة المقتبسة |
| Bombieri--Vinogradov والنتائج التابعة | `PROVED-HERE / INEFFECTIVE-CONSTANT` |

## 8. تحقق BibTeX

الملف:

`manuscript/chapter-13-bibliography.bib`

يحتوي ستة مفاتيح فريدة:

1. `Bombieri1965LargeSieve`
2. `Vinogradov1965Density`
3. `Vinogradov1966Correction`
4. `Gallagher1968Bombieri`
5. `Vaughan1975MeanValue`
6. `MontgomeryVaughan2026`

ورُبط الملف بـ`biblatex` من خلال:

```tex
\addbibresource{manuscript/chapter-13-bibliography.bib}
```

لا يوجد تعارض مع مفاتيح `manuscript/bibliography.bib` الحالية.

## 9. حدود التحقق

- بيانات الصفحات داخل كتاب 2026 طابقت نسخة المؤلف؛ بيانات النشر وDOI وISBN
  طابقت صفحة Cambridge الرسمية.
- لا تنسب الموسوعة البرهان الكامل للغربال الكبير إلى نفسها.
- لا تستعمل الأوراق الحديثة التي تتجاوز حاجز \(1/2\) مصدرًا للمبرهنة
  الكلاسيكية.
- التحقق المرجعي لا يجعل الفصل `VERIFIED` أو `REVIEWED` قبل كتابة المتن
  واجتياز تدقيق ما بعد التأليف.

## 10. الحكم

```text
REFERENCE-BLOCKERS = 0
BIBLIOGRAPHIC-DEBT = 0 FOR PRE-AUTHORING
VERDICT            = PASS-FOR-AUTHORING
```
