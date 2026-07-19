# خريطة برهان واعتمادات الفصل التاسع

## مبرهنة الأعداد الأولية

التاريخ: 2026-07-20  
الإصدار: `0.13.0-dev`  
الحالة: `PRE-AUTHORING-GATE-CLOSED / AUTHORING-AUTHORIZED`

## 1. النتيجة المركزية

يبنى الفصل حول

\[
\boxed{\psi(x)\sim x}.
\]

وسلسلة الاستنتاج المقفلة هي

\[
\psi(x)\sim x
\Longrightarrow
\vartheta(x)\sim x
\Longrightarrow
\pi(x)\sim\frac{x}{\log x}.
\]

الحلقة الأخيرة مغلقة سابقا في `ANT-THM-02-04`. والحلقة الأولى تغلق بحد
القوى الأولية العليا المثبت في تدقيق ما قبل التأليف.

## 2. المسارات الثلاثة

### المسار A — Wiener--Ikehara

هو المسار الأساسي النوعي. لا يستعمل بيرون أو تحويل المسار أو الصيغة الصريحة
أو منطقة كمية خالية من الأصفار.

### المسار B — Hadamard--de la Vallée Poussin

مسار كلاسيكي فعال يبدأ من عدم الانعدام ويضيف منطقة خالية كمية وتقديرات
للمشتقة اللوغاريتمية وبيرون وتحويل المسار. يبقى منفصلا لأن بعض أدواته
`CITED` أو `DEFERRED`.

### المسار C — Selberg--Erdős

مسار أولي مستقل مؤجل. لا تدمج هوياته في المسار A ولا يقدم بوصفه اختصارا
شكليا للمسار التحليلي.

## 3. مخطط المسار الأساسي

```text
ANT-THM-05-05
  -zeta'/zeta(s) = sum Lambda(n)n^{-s}, Re(s)>1
            |
            +------------------------------+
            |                              |
            v                              v
حد تشيبيشيف                    ANT-LEM-07-01
 theta(x) << x                 3+4cos u+cos 2u >= 0
            |                              |
            v                              v
 psi(x) << x                 ANT-LEM-09-01
            |                 المتراجحة الموزونة
            |                              |
            |                              v
            |                 ANT-THM-09-01
            |                 zeta(1+it) != 0
            |                              |
            +---------------+--------------+
                            v
       -zeta'/zeta(s)-1/(s-1) analytic on Re(s)>=1
                            |
                            v
          ANT-THM-09-02: Wiener--Ikehara [CITED]
                            |
                            v
                 ANT-THM-09-03: psi(x) ~ x
                            |
                            v
       ANT-LEM-09-02: psi(x)-theta(x)=O(sqrt(x)log x)
                            |
                            v
                 ANT-COR-09-01: theta(x) ~ x
                            |
                            v
                      ANT-THM-02-04
                            |
                            v
               ANT-COR-09-02: pi(x) ~ x/log x
```

## 4. وحدات المسار A

| الرمز | الوحدة | الاعتماد | الحالة بعد التدقيق |
|---|---|---|---|
| A0 | تعريف \(\psi,\vartheta,\pi\) | الفصول 2 و4 | `CLOSED` |
| A1 | \(-\zeta'/\zeta=\sum\Lambda(n)n^{-s}\) | `ANT-THM-05-05` | `PROVED-HERE` |
| A2 | تمثيل ستيلتج/ديريشليه بواسطة \(\psi\) | A0+A1 | `PROOF-READY` |
| A3 | الهوية المثلثية غير السالبة | `ANT-LEM-07-01` | `PROVED-HERE` |
| A4 | المتراجحة الموزونة للمشتقة اللوغاريتمية | A1+A3 | `PROVED-IN-AUDIT` |
| A5 | عدم انعدام \(\zeta(1+it)\) | A4 وقطب زيتا | `PROVED-IN-AUDIT` |
| A6 | إزالة القطب عند \(1\) | `ANT-THM-06-01` | `PASS` |
| A7 | هولومورفية الباقي على الخط | A5+A6 | `PASS` |
| A8 | صيغة Wiener--Ikehara | Korevaar 2006، Theorem 1.1 | `CITED / STATEMENT-LOCKED` |
| A9 | تطبيق Wiener--Ikehara على \(\Lambda\) | A1+A6+A7+A8 وحد \(\psi\ll x\) | `PROOF-READY` |
| A10 | حد تشيبيشيف والقوى الأولية العليا | المعامل الثنائي والتقسيم الثنائي | `PROVED-IN-AUDIT` |
| A11 | \(\vartheta\Rightarrow\pi\) | `ANT-THM-02-04` | `PROVED-HERE` |

## 5. برهان حد تشيبيشيف

لكل \(n\ge1\)، كل أولي \(p\) بين \(n\) و\(2n\) يقسم
\(\binom{2n}{n}\). لذلك

\[
\vartheta(2n)-\vartheta(n)
\le
\log\binom{2n}{n}
\le2n\log2.
\]

وبالجمع على الفترات الثنائية نحصل على

\[
\vartheta(x)\ll x.
\]

كما أن

\[
\psi(x)=\sum_{m\ge1}\vartheta\!\left(x^{1/m}\right),
\]

ومن ثم

\[
0\le\psi(x)-\vartheta(x)
\ll\sqrt{x}\log x=o(x),
\qquad
\psi(x)\ll x.
\]

هذا البرهان لا يستعمل PNT ولا تقديرا تقاربيا لـ\(\pi(x)\).

## 6. برهان عدم الانعدام المقفل

من `ANT-THM-05-05` و`ANT-LEM-07-01`، عندما \(\sigma>1\):

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{\zeta'}{\zeta}(\sigma+it)
-\Re\frac{\zeta'}{\zeta}(\sigma+2it)
\ge0.
\]

إذا كان \(1+it\) صفرا من الرتبة \(m\ge1\)، وكانت رتبة الصفر عند
\(1+2it\) هي \(m_2\ge0\)، فإن معامل \((\sigma-1)^{-1}\) في الطرف الأيسر
عندما \(\sigma\downarrow1\) هو

\[
3-4m-m_2\le-1,
\]

وهو تناقض. إذن

\[
\zeta(1+it)\ne0\qquad(t\ne0).
\]

وعند \(t=0\) توجد لزيتا قطب بسيط لا صفر.

## 7. صيغة Wiener--Ikehara المقفلة

النتيجة `ANT-THM-09-02` ستكون `CITED` من Korevaar 2006، Theorem 1.1،
الصفحتين 1107--1108، مع تطبيق PNT في الصفحتين 1108--1109.

إذا كانت

\[
f(s)=\sum_{n\ge1}\frac{a_n}{n^s},
\qquad a_n\ge0,
\]

وكانت المجاميع الجزئية \(S(n)=O(n)\)، وكان

\[
f(s)-\frac{A}{s-1}
\]

يمتد تحليليا أو باستمرار إلى \(\Re(s)\ge1\)، فإن

\[
S(n)\sim An.
\]

في التطبيق:

\[
a_n=\Lambda(n),
\qquad
f(s)=-\frac{\zeta'}{\zeta}(s),
\qquad
A=1.
\]

## 8. مطابقة الفروض

| فرض Korevaar | التحقق |
|---|---|
| \(a_n\ge0\) | \(\Lambda(n)\ge0\) |
| التقارب في \(\Re(s)>1\) | `ANT-THM-05-05` |
| \(S(n)=O(n)\) | حد تشيبيشيف يعطي \(\psi(n)\ll n\) |
| إزالة القطب عند \(1\) | \(\zeta(s)=h(s)/(s-1)\) و\(h(1)=1\) |
| عدم وجود أقطاب على بقية الخط | `ANT-THM-09-01` |
| معامل القطب | \(A=1\) |

إذن

\[
\psi(n)\sim n,
\]

ومن ثبات \(\psi\) بين الأعداد الصحيحة تنتج \(\psi(x)\sim x\).

## 9. المسار B وحالات ديونه

| الأداة | الحالة | الاستعمال في المسودة الأساسية |
|---|---|---|
| عدم الانعدام على الخط | `PROVED-IN-CHAPTER-09` | نعم |
| المنطقة الكلاسيكية الخالية | `CITED` في `ANT-THM-06-09` | لا |
| صيغة بيرون | `DEFERRED` | لا |
| تحويل المسار | `DEFERRED` | لا |
| الصيغة الصريحة | `CITED` في `ANT-THM-06-08` | لا |
| حد خطأ فعال | `DEFERRED` | لا |

يعرض المسار للمقارنة التاريخية والبنيوية فقط، ولا يستخدم لإثبات النتيجة
المركزية.

## 10. فحص عدم الدور

| السؤال | الحكم |
|---|---|
| هل يستعمل عدم الانعدام PNT؟ | `PASS` |
| هل يستعمل حد تشيبيشيف PNT؟ | `PASS` |
| هل يستعمل \(\psi\to\vartheta\) تقدير \(\pi\sim x/\log x\)؟ | `PASS` |
| هل تستعمل Wiener--Ikehara الصيغة الصريحة؟ | `PASS` |
| هل المنطقة الكمية لازمة للمسار A؟ | `PASS: NO` |
| هل يعود الاستنتاج النهائي إلى فرض سابق؟ | `PASS: NO` |
| هل اختلط المسار الأولي بالتحليلي؟ | `PASS: NO` |

## 11. النتائج وحالاتها عند بدء التأليف

| المعرّف | النتيجة | الحالة المستهدفة في المسودة |
|---|---|---|
| `ANT-LEM-09-01` | المتراجحة الموزونة للمشتقة اللوغاريتمية | `PROVED-HERE` |
| `ANT-THM-09-01` | عدم انعدام زيتا على \(\Re(s)=1\) | `PROVED-HERE` |
| `ANT-THM-09-02` | صيغة Wiener--Ikehara الخاصة | `CITED` |
| `ANT-LEM-09-02` | حد تشيبيشيف وضبط القوى الأولية العليا | `PROVED-HERE` |
| `ANT-PROP-09-01` | تمثيل ستيلتج/ديريشليه بواسطة \(\psi\) | `PROVED-HERE` |
| `ANT-THM-09-03` | \(\psi(x)\sim x\) | `PROVED-HERE` |
| `ANT-COR-09-01` | \(\vartheta(x)\sim x\) | `PROVED-HERE` |
| `ANT-COR-09-02` | \(\pi(x)\sim x/\log x\) | `PROVED-HERE` |

تبقى هذه الحالات غير معتمدة للاستشهاد حتى يكتب المتن وتنجح فحوصه وتحدث
`docs/RESULTS_REGISTRY.md`.

## 12. قرار البوابة

```text
DEPENDENCY-DAG = COMPLETE
CENTRAL-RESULT-ORDER = LOCKED
TAUBERIAN-ROUTE = PRIMARY-LOCKED
CLASSICAL-ROUTE = SECONDARY-BLOCKED-BY-DEBTS
ELEMENTARY-ROUTE = SEPARATE-DEFERRED
WIENER-IKEHARA-EXACT-STATEMENT = CLOSED
WIENER-IKEHARA-STATUS = CITED
ZETA-LINE-NONVANISHING = CLOSED-IN-AUDIT
CHEBYSHEV-BOUND = CLOSED-IN-AUDIT
PSI-TO-THETA-LEMMA = CLOSED-IN-AUDIT
PAGE-LEVEL-SOURCE-VERIFICATION = CLOSED-FOR-ADOPTED-ROUTE
NO-CIRCULARITY = PASS
PRE-AUTHORING-GATE = CLOSED
AUTHORING = AUTHORIZED
```

إغلاق البوابة يجيز إنشاء مسودة الفصل، ولا يرفعها تلقائيا إلى `VERIFIED` أو
`REVIEWED` أو `RELEASE-READY`.