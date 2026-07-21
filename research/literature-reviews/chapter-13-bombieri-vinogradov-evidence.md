# سجل أدلة الفصل الثالث عشر — مبرهنة بومبييري--فينوغرادوف

تاريخ القطع الأدبي: 2026-07-21

```text
CHAPTER                 = 13
TOPIC                   = BOMBIERI--VINOGRADOV
MODE                    = EVIDENCE-FIRST / PRE-AUTHORING
BASE-MAIN               = 607c6f8ad76f8085828f49ce6b566c846950ab2a
BRANCH                  = agent/chapter-13-bombieri-vinogradov-v0.17.0
LARGE-SIEVE             = CLOSED / CITED
LOG-LOSS                = CLOSED / B(A)=A+3
EFFECTIVITY             = INEFFECTIVE-IN-ADOPTED-ROUTE
AUTHORING               = BLOCKED
RELEASE-READY           = NO
```

## 1. الغرض العلمي

ينتقل الفصل من الانتظام الفردي في مبرهنة Siegel--Walfisz، حيث
\(q\le (\log x)^A\)، إلى انتظام **متوسطي** على الترديدات حتى مستوى
\(x^{1/2}\) مع خسارة لوغاريتمية. لا يدعي الفصل تقديرًا فرديًا بهذا المجال،
ولا يثبت فرضية Elliott--Halberstam، ولا يتجاوز حاجز \(1/2\) في الصيغة العامة
غير الموزونة.

## 2. الصيغة المركزية المرشحة

لكل \(A>0\)، الهدف هو إثبات أنه إذا

\[
Q\le \frac{x^{1/2}}{(\log x)^{A+3}},
\]

فإن

\[
\sum_{q\le Q}
\max_{(a,q)=1}
\max_{2\le y\le x}
\left|
\psi(y;q,a)-\frac{y}{\varphi(q)}
\right|
\ll_A \frac{x}{(\log x)^A}.
\]

هذه الصيغة ما تزال `TARGET / NOT YET ADOPTED`. القوة \(A+3\) ثبتت في
`docs/CHAPTER_13_LARGE_SIEVE_MEAN_VALUE_AUDIT_2026-07-21.md` من العامل
\((\log x)^3\) في مسار Montgomery--Vaughan.

قبل اعتمادها يجب إغلاق:

1. برهان هوية Vaughan.
2. تقدير Type I.
3. تقدير Type II.
4. التدخيل الداخلي لـ`max_{y\le x}`.
5. التدقيق الداخلي للموصل والترديد والشخصية الرئيسية.
6. فحص عدم الدور.

## 3. المصادر الأصلية الحاكمة

### 3.1 بومبييري

- Enrico Bombieri, **On the large sieve**, *Mathematika* 12 (1965),
  201--225.
- DOI: `10.1112/S0025579300005313`.
- المرجع الأصلي لمسار بومبييري والغِربال الكبير.

### 3.2 أ. إ. فينوغرادوف

- A. I. Vinogradov, **The density hypothesis for Dirichlet L-series**,
  *Izv. Akad. Nauk SSSR Ser. Mat.* 29:4 (1965), 903--934.
- MathNet: `im3080`; MR 0197414.
- التصحيح الملحق واجب التسجيل:
  **Correction to the paper ...**، المجلد 30:3 (1966)، 719--720،
  MathNet `im2856`.

### 3.3 غالاغر

- P. X. Gallagher, **Bombieri's mean value theorem**, *Mathematika* 15
  (1968), 1--6.
- DOI: `10.1112/S002557930000231X`.
- يقدم برهانًا قصيرًا لمبرهنة القيمة المتوسطة لبومبييري.

### 3.4 فوغان

- R. C. Vaughan, **Mean Value Theorems in Prime Number Theory**,
  *Journal of the London Mathematical Society* s2-10 (1975), 153--162.
- DOI: `10.1112/jlms/s2-10.2.153`.
- المرجع التاريخي لمسار القيمة المتوسطة المعتمد على هوية Vaughan.

## 4. المرجع التقني الحاكم للمسار

H. L. Montgomery and R. C. Vaughan,
*Multiplicative Number Theory II: Primes and Sieves*، 2026.

تم التحقق من نسخة المؤلف المستضافة لدى R. C. Vaughan:

- المبرهنة 19.16، الصفحة المطبوعة 175: الغربال الكبير للشخصيات البدائية.
- المبرهنة 20.1، الصفحة المطبوعة 189: متوسط
  \(\sup_{y\le x}|\psi(y,\chi)|\).
- المبرهنة 20.2، الصفحة المطبوعة 195: Bombieri--Vinogradov في صيغة
  \(E^*(x,q)\).
- الصفحتان 196--197: الرد من الترديد إلى الموصل واستعمال Siegel--Walfisz
  للترديدات الصغيرة.

## 5. نتائج التدقيق المرجعي

### 5.1 الغربال الكبير

الصيغة المحققة هي

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\left|\sum_{M<n\le M+N}c_n\chi(n)\right|^2
\le (N+Q^2)\sum_{M<n\le M+N}|c_n|^2.
\]

تشمل فترة منقولة عامة والوزن الدقيق والنجمة على الشخصيات البدائية.

```text
ANT-THM-13-01 = CITED
```

### 5.2 مبرهنة القيمة المتوسطة

المصدر يثبت

\[
\sum_{q\le Q}\frac{q}{\varphi(q)}
\sum_{\chi\bmod q}^{*}
\sup_{y\le x}|\psi(y,\chi)|
\ll
\left(x+x^{5/6}Q+x^{1/2}Q^2\right)(\log x)^3.
\]

وجود `max` أو `sup` في \(y\) أصلي في النتيجة، وليس إضافة لاحقة.

### 5.3 الخسارة اللوغاريتمية

المصدر يعطي

\[
\sum_{q\le Q}E^*(x,q)
\ll x^{1/2}Q(\log x)^3.
\]

باختيار \(Q_0=x^{1/2}(\log x)^{-(A+3)}\)، يكون الطرف الأيمن
\(x/(\log x)^A\)، وتغطي الرتابة كل \(Q\le Q_0\).

```text
LOG-LOSS-AUDIT = PASS
B(A)           = A+3
```

### 5.4 الموصل والترديد

تحقق المصدر من:

- خطأ العوامل المحلية \(O((\log qy)^2)\).
- جمع تعدد الاستحثاثات بواسطة

\[
\sum_{\substack{q\le Q\\d\mid q}}\frac1{\varphi(q)}
\ll \frac1{\varphi(d)}\log\frac{2Q}{d}.
\]

الحالة: `SOURCE-VERIFIED / INTERNALIZATION-OPEN`.

### 5.5 الفعالية

المسار يستعمل Siegel--Walfisz للترديدات الصغيرة، ولذلك يرث عدم الفعالية من
الفصل الثاني عشر.

```text
EFFECTIVITY = INEFFECTIVE-IN-ADOPTED-ROUTE
```

لا يمنع هذا اعتماد الفصل مستقبلًا، لكنه يجب أن يذكر في النتيجة وحدود الادعاء.

## 6. مسح Consensus والسياق الحديث

بدأ المسح عبر Consensus قبل التوسع في المصادر الأخرى. أكدت أوراق حديثة الصيغة
القياسية ذات مستوى \(1/2\) و`max` على الفئات وعلى \(y\le x\). هذه الأوراق
سياقية وليست مصدر البرهان الكلاسيكي المعتمد.

ظهرت أيضًا أعمال تتجاوز \(1/2\) تحت بنى إضافية:

- أوزان well-factorable وترديدات خاصة.
- موديلات ذات قواسم مناسبة.
- غربال Harman ومجاميع ثنائية أو ثلاثية.

تسجل هذه النتائج في الجبهة الحديثة فقط، ولا تدخل في البرهان المركزي.

## 7. الفصل المفاهيمي الحاكم

| النتيجة | نوع الانتظام | مجال الترديد | الحالة في الموسوعة |
|---|---|---:|---|
| PNT في AP، الفصل 10 | فردي، \(q\) ثابت | ثابت | `REVIEWED` |
| Siegel--Walfisz، الفصل 12 | فردي موحد | \(q\le(\log x)^A\) | `REVIEWED` |
| Bombieri--Vinogradov، الفصل 13 | متوسط على \(q\) | \(q\le x^{1/2}(\log x)^{-(A+3)}\) | `TARGET` |
| Elliott--Halberstam | متوسط تخميني | \(q\le x^{1-\varepsilon}\) | `CONJECTURE / OUT-OF-SCOPE` |
| نتائج موزونة بعد \(1/2\) | متوسط ببنية إضافية | يتجاوز \(1/2\) | `FRONTIER / OUT-OF-SCOPE` |

## 8. مسار البرهان المعتمد

1. مرشح الشخصيات وفصل الشخصية الرئيسية.
2. الرد من الشخصيات المستحثة إلى البدائية.
3. الغربال الكبير للشخصيات البدائية بوصفه مدخلًا `CITED`.
4. إثبات هوية Vaughan داخل المشروع.
5. تقديرات Type I وType II.
6. إثبات مبرهنة القيمة المتوسطة مع `max_{y\le x}`.
7. جمع الموصلات والترديدات واستعادة الفئات الحسابية.
8. تطبيق Siegel--Walfisz للترديدات الصغيرة مع التصريح بعدم الفعالية.
9. اختيار \(Q=x^{1/2}(\log x)^{-(A+3)}\).
10. الانتقال إلى `theta` و`pi` و«تقريبًا كل الترديدات».

## 9. قرارات منشأ النتائج المرشحة

| المعرّف المؤقت | النتيجة | الحالة المرشحة |
|---|---|---|
| `ANT-THM-13-01` | الغربال الكبير للشخصيات البدائية | `CITED` |
| `ANT-LEM-13-01` | هوية Vaughan | `PROVED-HERE` |
| `ANT-PROP-13-01` | تفكيك Type I/II | `PROVED-HERE` |
| `ANT-LEM-13-02` | تقدير Type I | `PROVED-HERE` |
| `ANT-LEM-13-03` | تقدير Type II | `PROVED-HERE` |
| `ANT-THM-13-02` | مبرهنة القيمة المتوسطة | `PROVED-HERE` اعتمادًا على الغربال الكبير المقتبس |
| `ANT-THM-13-03` | Bombieri--Vinogradov في صيغة `psi` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-13-01` | صيغة `theta` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-13-02` | صيغة `pi` | `PROVED-HERE / INEFFECTIVE-CONSTANT` |
| `ANT-COR-13-03` | تقريبًا كل الترديدات | `PROVED-HERE / INEFFECTIVE-CONSTANT` |

لا تصبح هذه المعرفات قابلة للاستشهاد قبل سجل حجز رسمي وإغلاق التدقيق.

## 10. المخاطر والديون المفتوحة

- خطر الدور إذا استُعمل Bombieri--Vinogradov داخل Type I أو Type II.
- كتابة الانتقال الداخلي بين الترديد والموصل.
- ضبط الشخصية الرئيسية عند جميع \(y\le x\).
- إثبات هوية Vaughan وحدود القطع.
- إغلاق Type I وType II وقوى اللوغاريتم داخل كل منهما.
- تجاوز حاجز \(1/2\)، والفترات القصيرة، وBarban--Davenport--Halberstam،
  وElliott--Halberstam، وتطبيقات الفجوات وغولدباخ مؤجلة.

## 11. حكم مرحلة الأدلة

```text
PRIMARY-SOURCES-IDENTIFIED    = PASS
ORIGINAL-CORRECTION-RECORDED  = PASS
CENTRAL-TARGET-FORMULATED     = PASS / NOT YET ADOPTED
PROOF-ROUTE-SELECTED          = VAUGHAN-LARGE-SIEVE
LARGE-SIEVE-AUDIT             = PASS / CITED
MAX-Y-SOURCE-AUDIT            = PASS
LOG-LOSS-AUDIT                = PASS / B(A)=A+3
EFFECTIVITY-AUDIT             = PASS / INEFFECTIVE-ROUTE
DEPENDENCY-AUDIT              = OPEN
VAUGHAN-IDENTITY              = OPEN
TYPE-I                        = OPEN
TYPE-II                       = OPEN
PRE-AUTHORING-GATE            = OPEN
AUTHORING                      = BLOCKED
```
