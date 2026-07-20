# التدقيق المنطقي للفصل الثاني عشر — مبرهنة Siegel--Walfisz

## بيانات التدقيق

```text
CHAPTER       = 12 — مبرهنة Siegel--Walfisz
VERSION       = 0.16.0-dev
BRANCH        = agent/chapter-12-siegel-walfisz-v0.16.0
BASE-COMMIT   = 9d02c583d416053550d22dfd7acc44d9c264a02c
AUDIT-DATE    = 2026-07-20
AUDIT-STATE   = CLOSED / PASS
AUTHORING     = BLOCKED-UNTIL-PRE-AUTHORING-CLOSURE
```

## المواد المدققة

- `research/literature-reviews/chapter-12-siegel-walfisz-evidence.md`
- `research/literature-reviews/chapter-12-siegel-walfisz-proof-map.md`
- `docs/CHAPTER_12_PERRON_CONTOUR_EXPLICIT_FORMULA_AUDIT_2026-07-20.md`
- `docs/CHAPTER_12_EXCEPTIONAL_ZERO_INEFFECTIVITY_AUDIT_2026-07-20.md`
- نتائج الفصول 7 و10 و11 المسجلة في `docs/RESULTS_REGISTRY.md`.

## الحكم العام

```text
SCOPE-SEPARATION       = PASS
DEPENDENCY-CHECK       = PASS
FIXED-Q-MISUSE         = NONE
EXPLICIT-FORMULA-STATE = CITED
EXCEPTIONAL-ZERO       = PASS
INEFFECTIVITY          = PASS
CIRCULARITY            = PASS
THETA-TRANSFER         = PASS
PI-TRANSFER            = PASS-WITH-LOG-POWER-MARGIN
BOMBIERI-VINOGRADOV    = DEFERRED
GRH                    = NOT USED
```

## A. الفصل عن نتيجة الترديد الثابت

لا تستعمل نتيجة الفصل العاشر مع \(q=q(x)\). يعاد استعمال مرشح الشخصيات والهوية الجبرية فقط، أما الحد الموحد فيستخرج من الصيغة الصريحة والمنطقة الخالية ومبرهنة Siegel.

**الحكم:** `PASS`.

## B. الرد إلى الجد البدائي

الفرق بين \(\psi(x,\chi)\) و\(\psi(x,\chi^*)\) مدعوم على قوى أوليات تقسم الترديد المستحث. الحد

\[
O(\log q\log x)
\]

موحد وكاف، ويمتص في الهدف الأسي أو في أي ادخار لوغاريتمي.

**الحكم:** `PASS`.

## C. الصيغة الصريحة

الصيغة الصريحة المقطوعة لا تسجل `PROVED-HERE`. هذا يمنع الاعتماد الدائري على دين بيرون القديم أو الادعاء الكاذب بإغلاق تحويل المسار.

**الحكم:** `PASS-AS-CITED`.

## D. اختيار ارتفاع القطع

الاختيار

\[
T=e^{\kappa\sqrt{L}},\qquad L=\log x,
\]

يوازن بين:

- خطأ القطع الذي ينخفض مثل قوة سالبة لـ\(T\)، بعد خسائر لوغاريتمية.
- المنطقة الخالية التي تعطي
  \[
  x^\beta\le x\exp\left(-\frac{cL}{\log(qT)}\right).
  \]

عندما \(q\le L^A\)، فإن \(\log(qT)\ll_{A,\kappa}\sqrt L\)، فينتج ادخار \(e^{-c_A\sqrt L}\).

يجب في المتن اختيار \(\kappa\) أصغر من الثوابت اللازمة، لا تثبيت قيمة عددية غير موثقة.

**الحكم:** `PASS`.

## E. عد الأصفار والخسائر اللوغاريتمية

تقدير عدد الأصفار حتى الارتفاع \(T\) أو مجموع \(1/|\rho|\) يعطي خسائر متعددة الحدود في \(\log(rT)\). هذه الخسائر تمتص في الادخار الأسي بعد تصغير الثابت، لأن

\[
(\log x)^C e^{-c\sqrt{\log x}}
\le
e^{-c'\sqrt{\log x}}
\]

لكبر \(x\).

يجب أن يظهر تقدير عد الأصفار صراحة في المتن أو يقتبس مع الصيغة الصريحة.

**الحكم:** `PASS-WITH-CITED-ZERO-COUNT`.

## F. الصفر الاستثنائي

الحد \(x^{\beta_1}/\beta_1\) يعزل قبل القيمة المطلقة. استعمال

\[
1-\beta_1\gg_\varepsilon r^{-\varepsilon}
\]

مع \(r\le q\le L^A\) واختيار \(A\varepsilon=1/2\) صحيح الاتجاه ويعطي الادخار المطلوب.

**الحكم:** `PASS / INEFFECTIVE`.

## G. الشخصية الرئيسية

لا تستنتج صيغة الخطأ الفعالة من PNT النوعية في الفصل التاسع. تعتمد نتيجة de la Vallée Poussin بحد خطأ أسي بوصفها `CITED`، ثم يضاف خطأ حذف الأوليات القاسمة لـ\(q\).

**الحكم:** `PASS-AS-CITED`.

## H. تجميع الشخصيات

مرشح الفئة يحتوي عامل \(1/\varphi(q)\) ومجموعًا على \(\varphi(q)\) شخصية. إذا كان الحد موحدًا لكل شخصية فلا تظهر خسارة إضافية في \(q\).

**الحكم:** `PASS`.

## I. الانتقال إلى \(\vartheta\)

مساهمة القوى الأولية العليا لا تتجاوز حدًا من رتبة \(\sqrt{x}\log^2x\)، وهو أصغر من \(x/(\log x)^B\) لأي \(B\) ثابت عند كبر \(x\). لا يحتاج هذا الانتقال إلى تقدير موحد جديد في \(q\).

**الحكم:** `PASS`.

## J. الانتقال إلى \(\pi\)

يوجد خطر دقيق: عند الجمع الجزئي على المتغير \(t\)، لا يظل الشرط

\[
q\le(\log t)^A
\]

صحيحًا لكل \(2\le t\le x\). المسار المعتمد هو تقسيم التكامل عند

\[
y=e^{q^{1/A}},
\]

أو عند حد مكافئ يضمن \(q\le(\log t)^A\) للجزء الكبير، ومعالجة الجزء الصغير بتقدير تافه. ويستعمل تقدير \(\vartheta\) بقوة لوغاريتمية أكبر من القوة النهائية المطلوبة.

بديل مكافئ: إثبات صيغة \(\pi\) مباشرة من \(\psi\) بواسطة جمع جزئي مقطوع مع هامش قوة لوغاريتمية.

**الحكم:** `PASS-WITH-LOG-POWER-MARGIN`.

## K. عدم الدور

لا تعتمد أي عقدة على:

- Siegel--Walfisz نفسها.
- Bombieri--Vinogradov.
- Linnik.
- GRH.
- نتيجة متوسطية للأخطاء في الترديدات.
- فعالية ثابت Siegel.

Deuring--Heilbronn مرجع مقارن وغير لازم للمسار الأدنى.

**الحكم:** `PASS`.

## النتائج المحجوزة

```text
ANT-LEM-12-01 = DRAFT / EXPECTED-PROVED-HERE
ANT-THM-12-01 = DRAFT / EXPECTED-CITED
ANT-THM-12-02 = DRAFT / EXPECTED-CITED
ANT-LEM-12-02 = DRAFT / EXPECTED-PROVED-HERE
ANT-LEM-12-03 = DRAFT / EXPECTED-PROVED-HERE / INEFFECTIVE
ANT-THM-12-03 = DRAFT / EXPECTED-PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-COR-12-01 = DRAFT / EXPECTED-PROVED-HERE / INEFFECTIVE-CONSTANT
ANT-COR-12-02 = DRAFT / EXPECTED-PROVED-HERE
ANT-COR-12-03 = DRAFT / EXPECTED-PROVED-HERE
```

## الديون غير الحاجزة قبل التأليف

- تثبيت موضع الصفحة الدقيق للصيغة الصريحة في النسخ المحلية من الكتب القياسية.
- اختيار صيغة منصفة أو ملساء واحدة وعدم مزجهما في المتن.
- تثبيت صيغة تقدير عد الأصفار المستعملة مع اعتمادها.
- اختيار ثابت رمزي \(\kappa\) من دون ادعاء أفضل قيمة.
- تنفيذ التقسيم الآمن في الجمع الجزئي لـ\(\pi\).

هذه نقاط تنفيذ داخل المتن، وقد حدد مسارها ولا تفتح اعتمادًا دائريًا.

## القرار

```text
LOGIC-AUDIT          = PASS
BLOCKING-CORRECTIONS = NONE
PRE-AUTHORING        = MAY-CLOSE
AUTHORING            = NOT-YET-STARTED
NEXT-DOCUMENT        = CHAPTER_12_PRE_AUTHORING_AUDIT_2026-07-20.md
```
