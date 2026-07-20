# المراجعة المستقلة للفصل الثاني عشر

## بيانات المراجعة

```text
DATE                     = 2026-07-21
CHAPTER                  = 12 — مبرهنة Siegel--Walfisz
BRANCH                   = agent/chapter-12-siegel-walfisz-v0.16.0
REVIEW-BASE              = 89c8128443008c3e2f38679b7983b626272c756d
CORRECTED-CONTENT-HEAD   = 05dca3f1175d0be5d61f7c5dcc7bbce5361a7b36
LOCAL-BUILD-SOURCE-HEAD  = 62fac059604136fd18ece01213a71fc90a5bded4
RECEIPT-HEAD             = c79c6f3cc314004911a3fc80633a1476e62f98b5
PR                       = #20
```

## الحكم

```text
R1-EXPLICIT-FORMULA      = CLOSED
R2-PI-TRANSFER           = CLOSED
LOCAL-SYNC               = PASS / FF-ONLY
SOURCE-BUILD             = PASS
LOCAL-PDF-PAGES          = 184
LOCAL-PDF-SHA256         = 3BF0BCE828DDF09C03D6527117992806FAD06010B161FC1B242472D0B5367749
QUALITY-CHECKS           = RUN-307 / SUCCESS
PDF-BUILD-CI             = RUN-302 / SUCCESS
VERDICT                  = APPROVED-WITH-NONBLOCKING-TYPOGRAPHY-DEBT
MERGE                    = NOT AUTHORIZED
RELEASE-READY            = NO
```

## نطاق المراجعة

شملت المراجعة:

1. فحص الصياغة الرياضية والاعتماد المنطقي للنتائج التسع.
2. التحقق من الفصل بين النتائج المبرهنة داخليًا والمداخل المقتبسة.
3. التحقق من موضع عدم الفعالية الناتج من مبرهنة Siegel.
4. فحص انتقالات \(\psi\to\vartheta\to\pi\).
5. التحقق من PDF الناتج عن CI بعد التصحيحات.
6. التحقق من البناء المحلي المتزامن على جهاز المالك وإيصال SHA256 وعدد الصفحات.

## إغلاق الملاحظة R1

كان `ANT-THM-12-02` يجمع عدة مكونات قياسية في عبارة واحدة، مع ظهور ارتفاع مختار لا يستعمل اتساقًا في حدود الصيغة.

أغلق التصحيح الملاحظة عبر:

- توصيف النتيجة بأنها `CITED / COMPOSITE-INPUT`، لا اقتباسًا حرفيًا من مبرهنة واحدة.
- اختيار ارتفاع واحد

  \[
  U\in[T,2T]
  \]

  واستعماله في مقام المنطقة الخالية، وخطأ القطع، والخسائر اللوغاريتمية، وفي البرهان اللاحق.
- تثبيت مواضع المسار في Davenport، الفصول 20--23، الصفحات 115--134، وMontgomery--Vaughan، الفصلين 11--12، الصفحات 358--418.
- إبقاء ديون Perron وتحويل المسار معلنة، وعدم ترقية المدخل إلى `PROVED-HERE`.

```text
R1 = CLOSED
```

## إغلاق الملاحظة R2

كان برهان `ANT-COR-12-03` يصف فرق الحد الرئيسي بعد القطع عند \(y\) بأنه ثابت محدود، مع أنه يعتمد على \(y\).

سجل التصحيح الهوية

\[
\frac{x}{\log x}+\int_y^x\frac{dt}{\log^2t}
=
\operatorname{Li}(x)-\operatorname{Li}(y)+\frac{y}{\log y},
\]

ومن ثم صار الفرق عن \(\operatorname{Li}(x)\) من رتبة \(O(y)\)، ويمتص لأن

\[
y\le e^{\sqrt{\log x}}
=o\!\left(\frac{x}{(\log x)^B}\right).
\]

```text
R2 = CLOSED
```

## التحقق المحلي المتزامن

سجل الإيصال المرفوع:

```text
LOCAL-HEAD       = 62fac059604136fd18ece01213a71fc90a5bded4
ORIGIN-HEAD      = 62fac059604136fd18ece01213a71fc90a5bded4
SYNC             = PASS / FF-ONLY
SOURCE-BUILD     = PASS
PDF-PAGES        = 184
PDF-SIZE-BYTES   = 741765
PDF-SHA256       = 3BF0BCE828DDF09C03D6527117992806FAD06010B161FC1B242472D0B5367749
XELATEX          = MiKTeX-XeTeX 4.18 (MiKTeX 26.5)
BIBER            = 2.21
```

الالتزامات الواقعة بعد رأس المحتوى المصحح وحتى رأس الإيصال غيرت ملف
`docs/LOCAL_BUILD_RECEIPT.md` فقط، ولم تغير المتن الرياضي.

## الديون غير الحاجزة

يحتوي سجل MiKTeX تحذيرات تنضيد سابقة ومتفرقة، منها:

- `Overfull/Underfull hbox`، وبخاصة في مسارات ملفات طويلة وبعض العناوين.
- محارف عربية وضعت في خط Latin Modern داخل بعض مواضع الببليوغرافيا.
- تحذيرات `hyperref` عند وجود رياضيات داخل عناوين PDF.

هذه التحذيرات لم تمنع البناء، ولا تغير صحة نتائج الفصل الثاني عشر. لكنها يجب أن تعالج في جولة تنضيد عامة قبل `RELEASE-READY`.

## النتيجة نتيجةً نتيجة

```text
ANT-LEM-12-01 = PASS
ANT-THM-12-01 = PASS-AS-CITED
ANT-THM-12-02 = PASS-AS-COMPOSITE-CITED-INPUT
ANT-LEM-12-02 = PASS
ANT-LEM-12-03 = PASS / INEFFECTIVE
ANT-THM-12-03 = PASS / INEFFECTIVE-CONSTANT
ANT-COR-12-01 = PASS / INEFFECTIVE-CONSTANT
ANT-COR-12-02 = PASS / INEFFECTIVE-CONSTANT
ANT-COR-12-03 = PASS / INEFFECTIVE-CONSTANT
```

## القرار الحاكم

```text
INDEPENDENT-REVIEW      = COMPLETED
REVIEW-VERDICT          = APPROVED-WITH-NONBLOCKING-TYPOGRAPHY-DEBT
MATHEMATICAL-BLOCKERS   = 0
REFERENCE-BLOCKERS      = 0
LOCAL-BUILD-GATE        = CLOSED / PASS
MERGE-PR-20             = NOT AUTHORIZED
RELEASE-READY           = NO
```

لا يمثل هذا التقرير إذنًا بالدمج. يبقى الدمج مشروطًا بأمر صريح من مالك المشروع.
