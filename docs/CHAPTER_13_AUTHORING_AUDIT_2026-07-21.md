# تدقيق ما بعد تأليف الفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER                 = 13
MANUSCRIPT              = volumes/volume-01-foundations/chapters/chapter-13-bombieri-vinogradov.tex
MANUSCRIPT-STATE        = DRAFT
RESULTS                 = 11
QUALITY-CHECKS          = RUN-340 / SUCCESS
PDF-BUILD               = RUN-334 / SUCCESS
XELATEX-BIBER           = SUCCESS
MATHEMATICAL-BLOCKERS   = 0
LOGICAL-BLOCKERS        = 0
REFERENCE-BLOCKERS      = 0
AUTHORING-VERDICT       = PASS
PROMOTION-RECOMMENDATION= DRAFT -> VERIFIED
RELEASE-READY           = NO
```

## 1. نطاق التدقيق

راجع هذا التدقيق متن الفصل بعد ربطه بـ`manuscript/main.tex`، وقارنه بسجلات
ما قبل التأليف وبراهين Type I وType II ورد الموصلات. كما تحقق من ظهور كل
معرّف نتيجة في سجل مؤقت يلتقطه فحص الجودة.

لا يدعي هذا التقرير مراجعة بشرية مستقلة ثانية، ولا بناء مصدر محليًا على جهاز
المالك، ولا فحصًا بصريًا صفحةً صفحة للـPDF.

## 2. بنية الفصل

يحتوي المتن، بالترتيب، على:

1. نطاق الفصل والفرق بين الانتظام الفردي والمتوسطي.
2. تعريف \(E(y;q,a)\) و\(E^*(x,q)\).
3. حزمة الغربال الكبير المقتبسة.
4. برهان Pólya--Vinogradov.
5. برهان هوية Vaughan.
6. الرد إلى Type I وType II.
7. تقديري Type I وType II.
8. مبرهنة القيمة المتوسطة.
9. الشخصية الرئيسية والموصلات.
10. مبرهنة Bombieri--Vinogradov.
11. نتائج `theta` و`pi` و«تقريبًا كل الترديدات».
12. المقارنة والحدود والتمارين والخلاصة.

الحكم: `STRUCTURE = PASS`.

## 3. مطابقة النتائج الأحد عشر

| المعرّف | الظهور في المتن | الحالة | الحكم |
|---|---:|---|---|
| `ANT-THM-13-01` | 1 | `CITED / COMPOSITE-INPUT` | `PASS` |
| `ANT-LEM-13-01` | 1 | `PROVED-HERE` | `PASS` |
| `ANT-PROP-13-01` | 1 | `PROVED-HERE` | `PASS` |
| `ANT-LEM-13-02` | 1 | `PROVED-HERE` | `PASS` |
| `ANT-LEM-13-03` | 1 | `PROVED-HERE` | `PASS` |
| `ANT-LEM-13-04` | 1 | `PROVED-HERE` | `PASS` |
| `ANT-THM-13-02` | 1 | `PROVED-HERE FROM CITED PACKAGE` | `PASS` |
| `ANT-THM-13-03` | 1 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | `PASS` |
| `ANT-COR-13-01` | 1 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | `PASS` |
| `ANT-COR-13-02` | 1 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | `PASS` |
| `ANT-COR-13-03` | 1 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | `PASS` |

نجح فحص المستودع بعد تسجيل هذه المعرفات في
`docs/RESULTS_REGISTRY_CHAPTER_13.md` بحالة `DRAFT / NON-CITABLE`.

## 4. مطابقة البرهان مع سجلات التدقيق

### حزمة الغربال الكبير

احتفظ المتن بصيغتي الحزمة: التربيعية والثنائية العظمى، مع الوزن
\(q/\varphi(q)\) والنجمة على الشخصيات البدائية. لم ينسب برهانهما إلى
الموسوعة.

### هوية Vaughan

نقل المتن برهان الالتفاف، وأظهر إلغاء حدود القطع، وشرح دعم الحد الرابع.
الإشارات مطابقة للتدقيق.

### Type I وType II

- ظهر حد \(Q^{5/2}U\) و\(Q^{5/2}V\) في Type I.
- ظهرت حدود \(QxU^{-1/2}\)، و\(QxV^{-1/2}\)، و\(Q^2x^{1/2}\) في Type II.
- ظهر الحد \(Qx^{1/2}(UV)^{1/2}\) في الجزء الكبير من \(S_2\).
- عولج المجال \(Q>x^{1/2}\) بالتطبيق المباشر مع \(M=1\) و\(b_n=\Lambda(n)\)،
  لا بالتفاف غير لازم.

### الموصلات والشخصية الرئيسية

استعمل المتن الدالة

\[
\psi'(Y,\chi)=\psi(Y,\chi)-\mathbf1_{\chi=\chi_0}Y
\]

قبل أخذ القيم المطلقة، ثم سجل الخطأ المحلي ومجموع تعدد الاستحثاثات. لم
يخلط بين الترديد والموصل.

### المبرهنة المركزية

ظهر الاختيار

\[
D=(\log x)^{A+4},
\qquad
Q=x^{1/2}(\log x)^{-(A+3)},
\]

وتحققت مواضع امتصاص الحدود الثلاثة. سجل المتن عدم الفعالية عند استعمال
Siegel--Walfisz للموصلات الصغيرة.

الحكم: `PROOF-TRANSFER = PASS`.

## 5. النتائج التابعة

- انتقال `psi -> theta` يستعمل خطأ القوى الأولية العليا، ومجموع الخطأ على
  الترديدات أصغر بقوتين لوغاريتميتين من المطلوب.
- انتقال `theta -> pi` يستعمل ادخارًا إضافيًا واحدًا، ولذلك يصرح بالمجال
  \(Q\le x^{1/2}(\log x)^{-(A+4)}\).
- نتيجة تقريبًا كل الترديدات تستعمل متراجحة ماركوف بعد تطبيق المبرهنة بالأس
  \(B+C\).

الحكم: `COROLLARIES = PASS`.

## 6. النطاق والنزاهة

صرح المتن صراحةً بأنه لا يثبت:

- Elliott--Halberstam؛
- مستوى توزيع عامًا أكبر من \(1/2\)؛
- Barban--Davenport--Halberstam؛
- الفترات القصيرة؛
- تطبيقات الفجوات المحدودة أو غولدباخ.

كما فصل المدخل المقتبس عن النتائج الداخلية، وأبقى عدم الفعالية ظاهرة.

الحكم: `HONESTY-AND-SCOPE = PASS`.

## 7. الفحوص الآلية

على الرأس الذي ربط الفصل بالكتاب وسجل المعرفات:

```text
QUALITY-CHECKS #340 = SUCCESS
PDF-BUILD      #334 = SUCCESS
```

اجتازت خطوات XeLaTeX وBiber والتحقق من وجود PDF وإعداد المعاينة ورفع
الـArtifact.

لا يسجل هذا التقرير عدد صفحات جديدًا أو SHA256 محليًا؛ هذه بيانات لا تعتمد
إلا بعد إيصال بناء محلي أو تحقق Artifact منفصل.

## 8. الدين التحريري غير الحاجز

- مراجعة بصرية لاحقة للجداول الطويلة وكسور السطور.
- إمكان إضافة فقرة تاريخية أوسع عن استقلال مساري Bombieri وVinogradov
  وتبسيط Gallagher.
- إمكان تحسين قوة اللوغاريتم أو مناقشة مسارات فعالة؛ كلاهما خارج شرط
  `VERIFIED` الحالي.
- المراجعة المستقلة الثانية ما تزال مطلوبة قبل `REVIEWED`.

## 9. الحكم

```text
AUTHORING-AUDIT = PASS
BLOCKERS        = 0
PROMOTE-TO      = VERIFIED
MERGE           = NOT AUTHORIZED
RELEASE-READY   = NO
```
