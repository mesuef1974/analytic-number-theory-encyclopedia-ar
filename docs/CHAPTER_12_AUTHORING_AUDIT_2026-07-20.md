# تدقيق ما بعد تأليف الفصل الثاني عشر

## بيانات التدقيق

```text
CHAPTER       = 12 — مبرهنة Siegel--Walfisz
VERSION       = 0.16.0-dev
BRANCH        = agent/chapter-12-siegel-walfisz-v0.16.0
DATE          = 2026-07-20
AUDIT-STATE   = LOGIC-PASS / CI-PENDING
CHAPTER-STATE = DRAFT
```

## المواد المدققة

- `volumes/volume-01-foundations/chapters/chapter-12-siegel-walfisz.tex`
- `research/literature-reviews/chapter-12-siegel-walfisz-evidence.md`
- `research/literature-reviews/chapter-12-siegel-walfisz-proof-map.md`
- `docs/CHAPTER_12_PRE_AUTHORING_AUDIT_2026-07-20.md`
- `docs/CHAPTER_12_PERRON_CONTOUR_EXPLICIT_FORMULA_AUDIT_2026-07-20.md`
- `docs/CHAPTER_12_EXCEPTIONAL_ZERO_INEFFECTIVITY_AUDIT_2026-07-20.md`
- `docs/CHAPTER_12_LOGIC_AUDIT_2026-07-20.md`
- `docs/CHAPTER_12_REFERENCE_VERIFICATION_2026-07-20.md`
- `docs/RESULTS_REGISTRY.md`

## A. مطابقة النطاق

```text
FIXED-Q-RESULT          = SEPARATED
SIEGEL-WALFISZ-RANGE    = q <= (log x)^A
BOMBIERI-VINOGRADOV     = DEFERRED
LINNIK                  = NOT USED
GRH                     = NOT USED
VERDICT                 = PASS
```

لا يستعمل الفصل `ANT-THM-10-02` مع ترديد متغير. المعاد استعماله هو مرشح الشخصيات والهوية الجبرية فقط.

## B. منشأ المداخل الكمية

- `ANT-THM-12-01` موسومة `CITED` ولا تستخرج من PNT النوعية.
- `ANT-THM-12-02` موسومة `CITED`، مع بيان صريح لديون بيرون وتحويل المسار.
- النتائج الداخلية تبدأ بعد المدخلين المقتبسين.

```text
ORIGIN-LABELS = PASS
PERRON-DEBT   = VISIBLE
VERDICT       = PASS
```

## C. الرد إلى الجد البدائي

الفرق بين `psi(x,chi)` و`psi(x,chi*)` مدعوم على القوى الأولية للأعداد الأولية القاسمة للترديد المستحث، وحده

\[
O(\log(2q)\log(2x)).
\]

الاتجاه والدعم والانتظام صحيحة.

```text
ANT-LEM-12-01 = PASS
```

## D. اختيار ارتفاع القطع

الاختيار

\[
T=e^{\kappa\sqrt{\log x}}
\]

يحقق، في المجال `q <= (log x)^A`:

\[
\log(r(T+2))\ll_A\sqrt{\log x}.
\]

خطأ القطع والخسائر متعددة اللوغاريتمات تمتص بعد تصغير ثابت الأس. لم تثبت قيمة عددية غير موثقة لـ`kappa`.

```text
ANT-LEM-12-02 = PASS
```

## E. الصفر الاستثنائي

ظهر الحد

\[
-x^\beta/\beta
\]

صراحة قبل أخذه بالقيمة المطلقة. استعمل `ANT-COR-11-01` فقط عند عقدة الامتصاص. اختيار `A epsilon = 1/2` صحيح الاتجاه لأن `r <= q`.

```text
EXCEPTIONAL-ZERO = ISOLATED-BEFORE-ABSORPTION
SIEGEL-USE       = ONE-IDENTIFIED-NODE
ANT-LEM-12-03    = PASS / INEFFECTIVE
```

## F. تجميع الشخصيات

عامل `1/phi(q)` يلغي عدد الشخصيات عند توفر حد موحد لكل شخصية. لا تظهر خسارة إضافية من رتبة `q`.

```text
ANT-THM-12-03 = PASS / INEFFECTIVE-CONSTANT
```

## G. الانتقال إلى `theta`

مساهمة القوى الأولية العليا مضبوطة بواسطة `ANT-LEM-09-02` بحد أصغر من أي خطأ لوغاريتمي مستهدف.

```text
ANT-COR-12-02 = PASS
```

## H. الانتقال إلى `pi`

عولج خطر تغير الشرط `q <= (log t)^A` داخل التكامل بتطبيق نتيجة `theta` بالمعلم `2A`، ووضع

\[
y=\exp(q^{1/(2A)})\le e^{\sqrt{\log x}}.
\]

عولج الجزء الصغير بحد تشيبيشيف، والجزء الكبير بالصيغة الموحدة مع هامش قوة لوغاريتمية.

```text
ANT-COR-12-03 = PASS-WITH-LOG-POWER-MARGIN
```

## I. المعرفات والسجل

المعرفات التسعة موجودة في المتن ومسجلة في `docs/RESULTS_REGISTRY.md` بحالات منشأ مطابقة:

```text
ANT-LEM-12-01 = PROVED-HERE
ANT-THM-12-01 = CITED
ANT-THM-12-02 = CITED
ANT-LEM-12-02 = PROVED-HERE
ANT-LEM-12-03 = PROVED-HERE / INEFFECTIVE
ANT-THM-12-03 = PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-COR-12-01 = PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-COR-12-02 = PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-COR-12-03 = PROVED-HERE / INEFFECTIVE-CONSTANT
```

## J. المراجع

أضيفت بيانات Thorner--Zaman وKoukoulopoulos وDrappeau--Fiorilli إلى BibTeX بعد التحقق من صفحات الناشرين وarXiv. لا يعتمد البرهان الأدنى على الورقتين المقارنتين.

```text
REFERENCE-VERIFICATION = PASS-FOR-ADOPTED-ROUTE
```

## K. عدم الدور

لم يستعمل الفصل:

- Siegel--Walfisz لإثبات نفسها.
- Bombieri--Vinogradov.
- Linnik.
- GRH.
- نتيجة متوسطية على الترديدات.
- فعالية ثابت Siegel.

```text
CIRCULARITY = PASS
```

## ملاحظات قبل رفع الحالة

يلزم قبل رفع الفصل إلى `VERIFIED`:

1. نجاح `Quality checks` على الرأس المؤلف.
2. نجاح بناء PDF الكامل.
3. فحص سجل XeLaTeX وBiber وعدم وجود مراجع مفقودة.
4. تحديث هذا التقرير بأرقام التشغيل والرأس النهائي.

## الحكم المرحلي

```text
AUTHORING-CONTENT = PASS
LOGIC             = PASS
REFERENCES        = PASS-FOR-ADOPTED-ROUTE
QUALITY-CHECKS    = PENDING
PDF-BUILD         = PENDING
CHAPTER-STATE     = DRAFT
NEXT-ACTION       = RUN-CI-AND-PDF
```
