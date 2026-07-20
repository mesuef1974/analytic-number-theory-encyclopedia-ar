# التحقق المرجعي للفصل العاشر — 2026-07-20

## الهوية

```text
CHAPTER = 10 — مبرهنة الأعداد الأولية في المتتاليات الحسابية
ROUTE   = FIXED-MODULUS / QUALITATIVE / TAUBERIAN
VERDICT = PASS-FOR-AUTHORING
```

هذا التحقق يثبت ملاءمة المسار المرجعي ومواضع الأبواب المعتمدة قبل كتابة
المتن. النتائج المركزية ستبرهن داخل الموسوعة، ولن تنقل من المرجع بلا برهان.

## 1. Montgomery--Vaughan

المرجع: `MontgomeryVaughan2007`.

تحققت من فهرس الناشر Cambridge University Press المواضع الآتية:

- الفصل 4: **Primes in arithmetic progressions: I**، الصفحات 108--136.
- الفصل 10: **Analytic properties of the zeta function and L-functions**،
  الصفحات 326--357.
- الفصل 11: **Primes in arithmetic progressions: II**، الصفحات 358--396.

تغطي هذه الأبواب على مستوى المسار: شخصيات ديريشليه، الخواص التحليلية لدوال
`L`، وعدم الانعدام والمناطق الخالية، ثم النتائج الخاصة بالأوليات في
المتتاليات الحسابية. يستخدم الفصل العاشر الجزء النوعي فقط؛ ولا يستورد
النتائج الكمية أو الموحدة من الفصل 11.

```text
MONTGOMERY-VAUGHAN-CHAPTERS = VERIFIED
MONTGOMERY-VAUGHAN-PAGES    = VERIFIED
```

## 2. Tenenbaum

المرجع: `Tenenbaum2015`.

تحقق فهرس AMS من وجود:

```text
Part II — Complex analysis methods
Chapter II.7 — Tauberian theorems
Chapter II.8 — Primes in arithmetic progressions
```

وهذا يطابق بنية المسار المختار: نتيجة تاوبيرية يعقبها تطبيق على الأوليات
في الفئات الحسابية. لا نسجل أرقام صفحات لم نتحقق منها مباشرة.

```text
TENENBAUM-CHAPTER-II.8 = VERIFIED
TENENBAUM-PAGE-RANGE   = NOT CLAIMED
```

## 3. Davenport

المرجع: `Davenport2000`، الطبعة الثالثة.

تحققت هوية الطبعة الثالثة وكون الكتاب معالجة مركزية لتوزيع الأوليات في
المتتاليات الحسابية. كما يبين فهرس الطبعة الثانية لدى Springer الأبواب:

- **Primes in Arithmetic Progression**، الصفحات 1--11.
- **Primes in Arithmetic Progression: The General Modulus**، الصفحات 27--34.
- **Zero-Free Regions for L(s, chi)**، الصفحات 88--96.
- **The Prime Number Theorem**، الصفحات 111--114.
- **The Explicit Formula for psi(x, chi)**، الصفحات 115--120.

وتظهر فهارس الطبعات المتاحة أبوابًا مستقلة لمبرهنة الأعداد الأولية في
المتتاليات الحسابية. وبسبب اختلاف ترقيم الصفحات بين الطبعات، لا تنسب هذه
الأرقام إلى `Davenport2000` في متن الفصل. يستعمل المرجع على مستوى الكتاب
والباب، وتثبت النتائج النوعية داخليًا.

```text
DAVENPORT-BOOK-SCOPE = VERIFIED
DAVENPORT-EDITION-SENSITIVE-PAGES = NOT TRANSFERRED
```

## 4. DLMF

### §27.8 — Dirichlet Characters

تحقق تعريف شخصيات ديريشليه، انعدامها عندما لا يكون العدد أوليًا مع
الترديد، ووجود علاقات التعامد. هذا يدعم صياغة مرشح الفئة، مع بقاء البرهان
الداخلي معتمدًا على الفصل السابع.

### §25.15 — Dirichlet L-functions

تحقق ما يأتي:

- تعريف `L(s,chi)` بالمتسلسلة في `Re(s)>1`.
- المنتج الأويلري في `Re(s)>1`.
- عدم الانعدام في هذا النصف المستوي.
- قطب الشخصية الرئيسية البسيط عند `s=1` وباقيه `phi(q)/q`.
- تمامية الدالة للشخصية غير الرئيسية.

### §27.11 — Asymptotic Formulas: Partial Sums

تحقق أن القسم يعالج صيغ المجاميع الجزئية والأوليات في المتتاليات
الحسابية، ويميز نتيجة ديريشليه عن الصيغ التقاربية الأقوى.

```text
DLMF-27.8  = VERIFIED
DLMF-25.15 = VERIFIED
DLMF-27.11 = VERIFIED
```

## 5. Wiener--Ikehara

المصدر: `Korevaar2006`.

سبق التحقق المباشر في الفصل التاسع من:

- Theorem 1.1، الصفحات 1107--1108.
- تطبيق مبرهنة الأعداد الأولية، الصفحات 1108--1109.

يعيد الفصل العاشر استعمال النتيجة المسجلة `ANT-THM-09-02` بحالة `CITED`،
ولا يعيد صياغة مصدرها أو يغير فروضها.

```text
KOREVAAR-ROUTE = REUSED-FROM-VERIFIED-CHAPTER-09
```

## 6. المصدر التاريخي

المصدر `DeLaValleePoussin1896` مسجل في ملف المراجع بوصفه أصلًا تاريخيًا
للمسار التحليلي. لا يعتمد البرهان الداخلي على نقل صياغة حديثة حرفيًا من
المقالة التاريخية.

## 7. مطابقة الادعاءات بالمصادر

| الادعاء | البرهان في الفصل | دعم المرجع |
|---|---|---|
| مرشح الفئة بالشخصيات | داخلي من الفصل 7 | DLMF §27.8؛ Montgomery--Vaughan Ch. 4 |
| متسلسلة `-L'/L` | داخلي من الفصل 7 | DLMF §25.15؛ Montgomery--Vaughan Ch. 10 |
| عدم الانعدام على `Re(s)=1` | برهان داخلي جديد | Davenport؛ Montgomery--Vaughan Ch. 10 |
| تحليل قطب الرئيسية | داخلي | DLMF §25.15 |
| Wiener--Ikehara | `CITED` من الفصل 9 | Korevaar 2006 |
| `psi(x;q,a)` التقاربية | داخلي عبر التاوبيري | Tenenbaum II.8؛ Montgomery--Vaughan Chs. 4, 11 |
| الانتقال إلى `theta` و`pi` | داخلي | المعالجات القياسية نفسها |

## 8. حدود الاعتماد

لا يدعم هذا التحقق أي ادعاء داخل الفصل عن:

- انتظام النتيجة في `q`.
- حد خطأ فعال.
- Siegel--Walfisz.
- Bombieri--Vinogradov.
- الأصفار الاستثنائية.
- نتائج GRH.

تبقى هذه موضوعات `DEFERRED` صراحة.

## الحكم

```text
BIBLIOGRAPHIC-GATE = PASS
CLAIM-LEVEL-ROUTE  = VERIFIED
PAGE-LEVEL-CLAIMS  = USED ONLY WHERE VERIFIED
AUTHORING          = MAY BE AUTHORIZED
```
