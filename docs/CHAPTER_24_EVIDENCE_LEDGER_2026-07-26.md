# سجل أدلة الفصل الرابع والعشرين

## الحالة

```text
CHAPTER        = 24
VERSION        = 0.28.0-dev
TOPIC          = PRETENTIOUS MULTIPLICATIVE FUNCTIONS
AUTHORING      = BLOCKED
RESULTS        = RESERVED / NON-CITABLE
MERGE          = NOT AUTHORIZED
REVIEW-STATUS  = CHANGES-REQUIRED / 1 BLOCKER CORRECTED-PENDING-REVIEW
```

## النواة المصدرية

| الرمز | المصدر | الوظيفة | التصنيف |
|---|---|---|---|
| E24-01 | G. Halász, *Über die Mittelwerte multiplikativer zahlentheoretischer Funktionen*, Acta Math. Acad. Sci. Hungar. 19 (1968), 365–403 | المصدر التاريخي لمبرهنة المتوسط | PRIMARY / CITED-CORE |
| E24-02 | A. Granville and K. Soundararajan, *Pretentious multiplicative functions and an inequality for the zeta-function*, in *Anatomy of Integers*, CRM Proc. Lecture Notes 46 (2008), 191–197; arXiv:math/0608407 | تعريف قاموس الادعاء والمسافة | PRIMARY / CITED-CORE |
| E24-03 | A. Granville, A. J. Harper and K. Soundararajan, *A new proof of Halász's theorem, and its consequences*, Compos. Math. 155 (2019), 126–163 | صياغة حديثة مرنة لمبرهنة هالاش وعواقبها | PEER-REVIEWED / CITED-CORE |
| E24-04 | P. D. T. A. Elliott, *A mean-value theorem for multiplicative functions*, Proc. London Math. Soc. (3) 31 (1975), 418–438 | سياق تاريخي ومعايير المتوسط | PEER-REVIEWED / SUPPORTING |
| E24-05 | P. D. T. A. Elliott, *Probabilistic Number Theory I: Mean-Value Theorems*, Springer, 1979 | معالجة مرجعية لمبرهنات Delange–Wirsing–Halász | BOOK / SUPPORTING |
| E24-06 | K. Matomäki and M. Radziwiłł, *Multiplicative functions in short intervals*, Ann. of Math. 183 (2016), 1015–1056 | جبهة لاحقة: المتوسطات القصيرة | PEER-REVIEWED / DEFERRED-FRONTIER |

## الحقائق المجمدة

1. للدالتين الضربيتين ذواتي القيم في قرص الوحدة نعرّف
   \[
   \mathbb D(f,g;x)^2=\sum_{p\le x}\frac{1-\Re(f(p)\overline{g(p)})}{p}.
   \]
2. النماذج الأساسية التي قد تتظاهر بها دالة ضربـية هي \(n^{it}\)، ومع وجود بنية توافقية تُستعمل \(\chi(n)n^{it}\).
3. للصيغة الكمية الأساسية نثبت
   \[
   \mathcal M(f;x,T)=\min_{|t|\le2T}\mathbb D(f,n^{it};x)^2,
   \]
   ومع \(x\ge2\) و\(T\ge1\):
   \[
   \left|\frac1x\sum_{n\le x}f(n)\right|
   \ll(1+\mathcal M)e^{-\mathcal M}+T^{-1/2}.
   \]
4. لا يجوز حذف \(T^{-1/2}\) أو تقليص مجال التصغير إلى \(|t|\le T\).
5. عدم الادعاء تجاه جميع النماذج المناسبة يقود إلى الإلغاء المتوسط بعد اختيار \(T\) وضبط الحدين معًا، لكنه لا يعني تلقائيًا إلغاءً نقطيًا ولا نتائج فترات قصيرة.
6. انتقالات Matomäki–Radziwiłł إلى الفترات القصيرة مؤجلة ولا تُدمج في نواة هذا الفصل.

## سجل المراجعة والتصحيح

```text
INDEPENDENT-REVIEW-COMMIT = 1fb25deeac05beada7abe0e8f68a77f8d5fd2f70
VERDICT                  = CHANGES-REQUIRED
BLOCKERS                 = 1
BLOCKER                  = HALASZ-T-RANGE-AND-REMAINDER
CORRECTION               = |t| <= 2T AND + T^(-1/2)
RE-REVIEW                = REQUIRED
```

## حراس الاستدلال

- المسافة الادعائية شبه مسافة على فئات الدوال المقيدة، ولا تُقدّم هنا كمسافة مترية كاملة دون تدقيق الشروط.
- القرب على الأوليات لا يساوي تطابق الدالتين على جميع الأعداد.
- مبرهنة هالاش لا تثبت فرضية ريمان، ولا تعطي وحدها تقديرات مثلى لمجاميع موبيوس القصيرة.
- الشخصيات الرئيسية وغير الرئيسية يجب فصلها عند مناقشة \(\chi(n)n^{it}\).
- معيار الإلغاء يجب أن يضبط حد \(T^{-1/2}\) مع تباعد \(\mathcal M(f;x,T)\)، لا أن يعتمد على الحد الأسي وحده.

## تدقيق الحداثة والمصادر

- عمل Granville–Harper–Soundararajan منشور في *Compositio Mathematica*، المجلد 155 (2019)، الصفحات 126–163.
- عمل Matomäki–Radziwiłł منشور في *Annals of Mathematics*، المجلد 183 (2016)، الصفحات 1015–1056، ويظل خارج النواة المثبتة للفصل 24.