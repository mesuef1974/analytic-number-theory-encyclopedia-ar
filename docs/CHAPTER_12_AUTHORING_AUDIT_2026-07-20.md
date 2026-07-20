# تدقيق ما بعد تأليف الفصل الثاني عشر

## بيانات التدقيق

```text
CHAPTER              = 12 — مبرهنة Siegel--Walfisz
VERSION              = 0.16.0-dev
BRANCH               = agent/chapter-12-siegel-walfisz-v0.16.0
DATE                 = 2026-07-20
AUTHORING-HEAD       = 7ea41ec1f20d3821ea98aa832a710946f64277b8
SYNCHRONIZED-HEAD    = 6a5388fa6c58d3cec921d352c66814aa89761ae0
AUDIT-STATE          = CLOSED / PASS
CHAPTER-STATE        = VERIFIED
AUTHORING-QUALITY    = RUN-272 / SUCCESS
AUTHORING-PDF        = RUN-267 / SUCCESS
FINAL-QUALITY        = RUN-280 / SUCCESS
FINAL-PDF            = RUN-275 / SUCCESS
PDF-ARTIFACT         = analytic-number-theory-encyclopedia-preview
ARTIFACT-SHA256      = 5d9746daee8dec19c25ced8e47756abceee53ee1c481241560c7c022ab13d13a
ARTIFACT-SIZE        = 726239 bytes
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

الفرق بين `psi(x,chi)` و`psi(x,chi*)` مدعوم على القوى الأولية القاسمة للترديد المستحث، وحده

\[
O(\log(2q)\log(2x)).
\]

```text
ANT-LEM-12-01 = PASS
```

## D. اختيار ارتفاع القطع

الاختيار

\[
T=e^{\kappa\sqrt{\log x}}
\]

يحقق في المجال `q <= (log x)^A`:

\[
\log(r(T+2))\ll_A\sqrt{\log x}.
\]

خطأ القطع والخسائر متعددة اللوغاريتمات تمتص بعد تصغير ثابت الأس، من دون تثبيت قيمة عددية غير موثقة لـ`kappa`.

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

أضيفت بيانات Thorner--Zaman وKoukoulopoulos وDrappeau--Fiorilli إلى BibTeX بعد التحقق من صفحات الناشرين وarXiv. لا يعتمد البرهان الأدنى على المراجع المقارنة الحديثة.

```text
REFERENCE-VERIFICATION = PASS-FOR-ADOPTED-ROUTE
```

## K. عدم الدور

لم يستعمل الفصل Siegel--Walfisz لإثبات نفسها، ولا Bombieri--Vinogradov، ولا Linnik، ولا GRH، ولا فعالية ثابت Siegel.

```text
CIRCULARITY = PASS
```

## L. فحوص البناء

اجتاز رأس التأليف فحوص #272/#267، ثم جرى توحيد حالة الفصل ووثائق الحوكمة وسجل التغييرات. اجتاز الرأس المتزامن `6a5388fa6c58d3cec921d352c66814aa89761ae0` فحص الجودة #280 وبناء PDF #275، ورفع Artifact جديدًا بملخص SHA256 المسجل أعلاه.

```text
VERSION-CONSISTENCY = PASS
UNICODE-CHECK       = PASS
RESULT-ID-CHECK     = PASS
XELATEX              = PASS
BIBER                = PASS
PDF-EXISTS           = PASS
ARTIFACT-UPLOAD      = PASS
```

## الحكم النهائي

```text
AUTHORING-CONTENT    = PASS
LOGIC                = PASS
REFERENCES           = PASS-FOR-ADOPTED-ROUTE
QUALITY-CHECKS       = RUN-280 / SUCCESS
PDF-BUILD            = RUN-275 / SUCCESS
POST-AUTHORING-GATE  = CLOSED / PASS
CHAPTER-STATE        = VERIFIED
REVIEW-STATE         = NOT YET INDEPENDENTLY REVIEWED
RELEASE-READY        = NO
NEXT-ACTION          = PREPARE-INDEPENDENT-REVIEW-PACKET
```
