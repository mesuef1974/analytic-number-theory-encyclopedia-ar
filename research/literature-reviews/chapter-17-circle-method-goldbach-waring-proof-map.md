# خريطة البرهان والاعتمادات — الفصل السابع عشر

آخر تحديث: 2026-07-25

```text
CHAPTER             = 17
STATUS              = PRE-AUTHORING / FROZEN
AUTHORING           = BLOCKED PENDING FINAL GATE RECEIPT
DEPENDENCY-AUDIT    = PASS
SCOPE-FREEZE        = PASS
MINOR-ARC-INPUTS    = SOURCE-VERIFIED / CITED
NORMALIZATION       = FROZEN
```

## A. العمود البنيوي

### A1 — التعامد الفورييري

لكل عدد صحيح `m`:

\[
\int_0^1 e(\alpha m)\,d\alpha=
\begin{cases}
1,&m=0,\\
0,&m\ne0.
\end{cases}
\]

إذا

\[
F(\alpha)=\sum_n w(n)e(\alpha n),
\]

فإن معامل فورييه الموافق لـ`N` في `F(α)^s` هو

\[
R_s(N)=\int_0^1F(\alpha)^s e(-N\alpha)\,d\alpha.
\]

**التصنيف:** `IDENTITY / PROVED-HERE`.

### A2 — تشريح الدائرة

يعتمد الفصل

\[
e(t)=e^{2\pi i t}.
\]

في نموذج وارينغ نضع

\[
P=N^{1/k},
\qquad
Q=P^\eta,
\]

حيث `η` ثابت موجب صغير يثبت في بداية التطبيق، ويُختار بحيث تكون الأقواس الكبرى متباعدة وتتحقق صيغة التقدير المقتبسة للأقواس الصغرى. ويمكن، لأغراض العرض، تثبيت

\[
0<\eta<\frac{1}{4k}.
\]

وللكسور المختزلة `a/q` نعرّف

\[
\mathfrak M(q,a)
=
\left\{\alpha\in[0,1):
\left|\alpha-\frac aq\right|
\le \frac{Q}{qN}
\right\},
\]

ثم

\[
\mathfrak M
=
\bigcup_{1\le q\le Q}
\bigcup_{\substack{1\le a\le q\\(a,q)=1}}
\mathfrak M(q,a),
\qquad
\mathfrak m=[0,1)\setminus\mathfrak M.
\]

ومن ثم

\[
R_s(N)=
\int_{\mathfrak M}F(\alpha)^s e(-N\alpha)\,d\alpha
+
\int_{\mathfrak m}F(\alpha)^s e(-N\alpha)\,d\alpha.
\]

**التصنيف:** `DEFINITION + IDENTITY / PROVED-HERE`.

### A3 — الأقواس الكبرى

قرب `α=a/q+β` يبنى تقريب من النمط

\[
F(\alpha)\approx q^{-1}S(q,a)V(\beta),
\]

أو النظير الخاص بالأوليات. بعد جمع المساهمات يظهر الحد الرئيس

\[
\mathfrak S(N)\mathfrak J(N).
\]

في نموذج وارينغ تستخدم الرموز

\[
\mathfrak S_{s,k}(N),
\qquad
\mathfrak J_{s,k}(N).
\]

**التصنيف:** البنية والتفكيك `PROVED-HERE`، أما التقديرات الكمية اللازمة للاستبدال وتمديد المجاميع والتكاملات فتصنف كل واحدة صراحة `PROVED-HERE` أو `CITED` في المتن.

### A4 — الأقواس الصغرى

المدخل المعتمد في وارينغ هو:

\[
\int_{\mathfrak m}|f_k(\alpha;P)|^s\,d\alpha
\ll P^{s-k-\delta}
\]

لبعض `δ=δ(k,s)>0` عندما يكون `s` كبيرًا بما يكفي بدلالة `k`، وفق مسار Vaughan والمراجع الكلاسيكية.

**التصنيف:** `CITED / COMPOSITE INPUT`.

لا يثبت الفصل السابع عشر النظرية العامة للمجاميع الأسية، ولا أفضل عتبة حديثة لعدد المتغيرات.

## B. مسار وارينغ المجمد

نضع

\[
f_k(\alpha;P)=\sum_{1\le x\le P}e(\alpha x^k),
\qquad P=N^{1/k}.
\]

و

\[
r_{s,k}(N)=\int_0^1f_k(\alpha;P)^s e(-N\alpha)\,d\alpha.
\]

### سلسلة الاعتماد

1. التعامد — `PROVED-HERE`.
2. تعريف الأقواس مع `Q=P^η` — `PROVED-HERE`.
3. التقريب على الأقواس الكبرى — `PROVED-HERE / CITED BY SUBCLAIM`.
4. استخراج السلسلة والتكامل المفردين — `PROVED-HERE / EXPLAINED`.
5. التقارب والإيجابية المحلية — `CITED` حيث يلزم، مع بيان شرط عدم وجود عائق محلي.
6. توفير القوة على الأقواس الصغرى — `CITED / COMPOSITE INPUT`.
7. الصيغة التقاربية الكلاسيكية عندما يكون `s` كبيرًا بما يكفي بدلالة `k` — `CITED / EXPLAINED`.
8. أفضل الحدود الحديثة لـ`G(k)` و`\widetilde G(k)` — `DEFERRED`.

## C. مسار غولدباخ المجمد

نضع

\[
S(\alpha)=\sum_{n\le N}\Lambda(n)e(\alpha n),
\]

وعندئذ

\[
R_3(N)=\int_0^1S(\alpha)^3e(-N\alpha)\,d\alpha.
\]

### سلسلة الاعتماد

1. التعامد — `PROVED-HERE`.
2. تفسير الأقواس الكبرى عبر توزيع الأوليات في المتتاليات الحسابية — `EXPLAINED / CITED INPUTS` من الفصول السابقة والمراجع.
3. السلسلة المفردة — `EXPLAINED` مع عناصر محلية مثبتة حيث يناسب.
4. الأقواس الصغرى على الأوليات — `CITED`.
5. مبرهنة فينوغرادوف: كل فردي كبير بما يكفي مجموع ثلاثة أوليات — `CITED`.
6. مبرهنة هلفغوت: كل فردي أكبر من 5 مجموع ثلاثة أوليات — `CITED / MODERN COMPLETION`.
7. الجزء الحاسوبي في الإكمال الحديث — `FINITE-VERIFIED`.
8. غولدباخ الثنائية — `HYPOTHESIS / OPEN`.

## D. عدم الدور

### مع الفصول 10--14

تستعمل فقط النتائج المدمجة عن توزيع الأوليات في المتتاليات الحسابية وSiegel--Walfisz وBombieri--Vinogradov وBDH بوصفها مدخلات سابقة، ولا يعاد اشتقاقها من الفصل السابع عشر.

### مع الفصلين 15 و16

الحدود الغربالية العليا ونتائج تشن والفجوات المحدودة ليست بديلًا عن تحليل الأقواس الصغرى، ولا تدخل منطقيًا في إثبات الصيغ التقاربية هنا.

### مع الفصل 18

- الفصل 17 يستعمل تقديرات أسية محددة مصنفة `CITED`.
- الفصل 18 يطور أدوات فان دير كوربوت والمجاميع الأسية داخليًا.
- لا يعتمد الفصل 17 على فصل 18 غير المؤلف بوصفه مصدر برهان.

```text
CIRCULARITY = NONE
```

## E. خريطة النتائج

| المعرّف | المضمون | التصنيف المجمد |
|---|---|---|
| `ANT-ID-17-01` | هوية التعامد | `IDENTITY / PROVED-HERE` |
| `ANT-ID-17-02` | صيغة تكامل عدد التمثيلات | `IDENTITY / PROVED-HERE` |
| `ANT-DEF-17-01` | الأقواس الكبرى والصغرى | `DEFINITION / PROVED-HERE` |
| `ANT-PROP-17-01` | بنية الحد الرئيس `𝔖𝔍` | `PROVED-HERE / CITED INPUTS` |
| `ANT-THM-17-01` | الصيغة التقاربية الكلاسيكية في وارينغ | `CITED / EXPLAINED` |
| `ANT-THM-17-02` | مبرهنة فينوغرادوف للثلاثة أوليات | `CITED` |
| `ANT-THM-17-03` | مبرهنة هلفغوت لغولدباخ الثلاثي | `CITED` |
| `ANT-CONJ-17-01` | صيغة هاردي–ليتلوود لغولدباخ الثنائي | `HYPOTHESIS / OPEN` |

## F. حكم خريطة البرهان

```text
PROOF-MAP                  = FROZEN
DEPENDENCY-AUDIT           = PASS
CIRCULARITY                = NONE
MINOR-ARC-INPUTS           = SOURCE-VERIFIED / CITED
WARING-TARGET              = FROZEN
HELFGOTT-SCOPE             = DECIDED
NORMALIZATION              = FROZEN
OPEN TECHNICAL BLOCKERS    = 0
PASS-FOR-AUTHORING         = PENDING FINAL INDEPENDENT GATE RECEIPT
```
