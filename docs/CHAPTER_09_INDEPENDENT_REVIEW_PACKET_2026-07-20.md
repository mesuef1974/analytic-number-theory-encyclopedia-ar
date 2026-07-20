# حزمة المراجعة المستقلة — الفصل التاسع

التاريخ: 2026-07-20  
الفرع العامل: `agent/chapter-09-prime-number-theorem-v0.13.0`  
فرع المراجعة الثابت: `review/chapter-09-prime-number-theorem-rc1`  
الرأس الرياضي المرجعي: `ce50d0aa1fd43b344913e1811d2eb5152039a612`  
الحالة قبل المراجعة: `VERIFIED`  
طلب السحب: `PR #13`

يبنى حكم المراجع على الرأس الرياضي المحدد أعلاه، لا على تحديثات لاحقة في
فرع العمل.

## 1. غرض المراجعة

المطلوب قراءة الفصل من الصفر وإصدار حكم مستقل على:

1. حد تشيبيشيف وضبط القوى الأولية العليا.
2. تمثيل ستيلتج للمشتقة اللوغاريتمية.
3. المتراجحة الموزونة وإشاراتها.
4. عدم وجود أصفار لزيتا على `Re(s)=1`.
5. صياغة Wiener--Ikehara ومطابقة فروض Korevaar.
6. إزالة القطب والامتداد عبر الخط.
7. السلسلة `psi -> theta -> pi`.
8. عدم الدور وحدود الادعاء والمراجع.

## 2. الملفات الأساسية

```text
volumes/volume-01-foundations/chapters/chapter-09-prime-number-theorem.tex
research/literature-reviews/chapter-09-prime-number-theorem-evidence.md
research/literature-reviews/chapter-09-prime-number-theorem-proof-map.md
docs/RESULTS_REGISTRY.md
docs/RESULT_STATUS_POLICY.md
```

لا يطّلع المراجع على وثائق التدقيق الداخلي إلا بعد تكوين حكمه الأولي:

```text
docs/CHAPTER_09_PRE_AUTHORING_AUDIT_2026-07-20.md
docs/CHAPTER_09_LOGIC_AUDIT_2026-07-20.md
docs/CHAPTER_09_BIBLIOGRAPHIC_VERIFICATION_2026-07-20.md
```

## 3. النتائج المطلوب فحصها

| المعرّف | النتيجة | الحالة |
|---|---|---|
| `ANT-LEM-09-01` | المتراجحة الموزونة للمشتقة اللوغاريتمية | `PROVED-HERE` |
| `ANT-LEM-09-02` | حد تشيبيشيف والقوى الأولية العليا | `PROVED-HERE` |
| `ANT-THM-09-01` | عدم وجود أصفار على `Re(s)=1`، مع قطب بسيط عند الواحد | `PROVED-HERE` |
| `ANT-THM-09-02` | Wiener--Ikehara، الصيغة الخاصة | `CITED` |
| `ANT-PROP-09-01` | تمثيل ستيلتج بواسطة `psi` | `PROVED-HERE` |
| `ANT-THM-09-03` | `psi(x) ~ x` | `PROVED-HERE` |
| `ANT-COR-09-01` | `theta(x) ~ x` | `PROVED-HERE` |
| `ANT-COR-09-02` | `pi(x) ~ x/log x` | `PROVED-HERE` |

## 4. قائمة الفحص الرياضي

### 4.1 حد تشيبيشيف والقوى العليا

تحقق من:

- أن كل أولي `n<p<=2n` يقسم `C(2n,n)`.
- أن `theta(2n)-theta(n) <= 2n log 2`.
- صحة الجمع على الفترات الثنائية.
- الهوية `psi(x)=sum_{m>=1} theta(x^(1/m))`.
- الحد `psi(x)-theta(x) << sqrt(x) log x = o(x)`.
- عدم استعمال PNT في أي خطوة.

### 4.2 تمثيل ستيلتج

تحقق من القفزات، وإشارة التكامل بالتجزئة، وزوال الحد الطرفي في:

\[
-\frac{\zeta'}{\zeta}(s)
=
\int_{1^-}^{\infty}x^{-s}\,d\psi(x)
=
s\int_1^\infty\psi(x)x^{-s-1}\,dx.
\]

### 4.3 المتراجحة وعدم الانعدام

تحقق من أن المتسلسلة المطلقة تعطي:

\[
-3\frac{\zeta'}{\zeta}(\sigma)
-4\Re\frac{\zeta'}{\zeta}(\sigma+it)
-\Re\frac{\zeta'}{\zeta}(\sigma+2it)\ge0.
\]

إذا كانت رتبة الصفر عند `1+it` هي `m>=1`، وعند `1+2it` هي
`m_2>=0`، فتحقق من أن معامل `1/(sigma-1)` هو

\[
3-4m-m_2\le-1.
\]

وتحقق من فصل `t!=0` عن النقطة `s=1` التي هي قطب بسيط.

### 4.4 Wiener--Ikehara

قارن العبارة مباشرة مع:

```text
Jaap Korevaar,
The Wiener--Ikehara Theorem by Complex Analysis,
Proc. AMS 134 (2006), Theorem 1.1, pp. 1107--1108.
```

وافحص التطبيق في الصفحتين 1108--1109، وبخاصة:

- `a_n=Lambda(n)>=0`.
- تقارب السلسلة في `Re(s)>1`.
- `S(n)=psi(n)=O(n)`.
- معامل القطب `A=1`.
- امتداد الباقي بعد طرح `1/(s-1)`.
- عدم خلط صيغة Korevaar بصيغة تاوبيرية أخرى.

### 4.5 النتيجة المركزية والاستنتاجات

تحقق من:

\[
\psi(n)\sim n
\Longrightarrow
\psi(x)=\psi(\lfloor x\rfloor)\sim x,
\]

ثم من:

\[
\psi(x)-\vartheta(x)=o(x)
\Longrightarrow
\vartheta(x)\sim x,
\]

ومن سلامة استعمال `ANT-THM-02-04` لاستخراج
`pi(x)~x/log x`.

## 5. فحص عدم الدور وحدود الادعاء

المسار المقبول هو:

```text
Chebyshev bound -> psi(x) << x
log derivative + pole -> no zeros on Re(s)=1
Korevaar Wiener--Ikehara -> psi(x) ~ x -> theta(x) ~ x -> pi(x) ~ x/log x
```

يعد مانعًا:

- استعمال PNT داخل حد تشيبيشيف أو ضبط القوى العليا أو عدم الانعدام.
- استعمال الصيغة الصريحة أو بيرون كأنهما `PROVED-HERE`.
- ادعاء حد خطأ فعال.
- خلط مسار Selberg--Erdős بالمسار التاوبيري.
- ادعاء `RELEASE-READY`.

## 6. المراجع

- Korevaar (2006): Theorem 1.1، 1107--1108؛ التطبيق 1108--1109.
- Ikehara (1931): 1--12.
- Wiener (1930): 117--258.
- Hadamard (1896): 199--220.
- Apostol: الفصل 13، 278--303.
- Davenport: فصل PNT، 111--114.
- Montgomery--Vaughan: الفصل 6، 168--198.

كل نتيجة غير مبرهنة داخل النص يجب أن تكون موسومة `CITED` بمصدر مطابق.

## 7. نموذج تقرير المراجع

```text
REVIEWER NAME / IDENTIFIER =
REVIEW DATE =
SOURCE BRANCH = review/chapter-09-prime-number-theorem-rc1
SOURCE COMMIT = ce50d0aa1fd43b344913e1811d2eb5152039a612
REVIEW PR = #13

MATHEMATICAL CORRECTNESS = PASS / PASS-WITH-CORRECTIONS / FAIL
CHEBYSHEV-BOUND = PASS / FAIL
STIELTJES-REPRESENTATION = PASS / FAIL
ZETA-LINE-NONVANISHING = PASS / FAIL
WIENER-IKEHARA-STATEMENT = PASS / FAIL
WIENER-IKEHARA-APPLICATION = PASS / FAIL
PSI-THETA-PI-CHAIN = PASS / FAIL
NO-CIRCULARITY = PASS / FAIL
REFERENCE CHECK = PASS / PASS-WITH-CORRECTIONS / FAIL
EDITORIAL CHECK = PASS / PASS-WITH-CORRECTIONS / FAIL
CLAIM BOUNDARY = PASS / FAIL

MAJOR ISSUES =
MINOR ISSUES =
OPTIONAL IMPROVEMENTS =

FINAL VERDICT =
APPROVED
APPROVED WITH MINOR CORRECTIONS
MAJOR REVISION REQUIRED
REJECTED
```

## 8. قاعدة اعتماد الحكم

لا يرتفع الفصل من `VERIFIED` إلى `REVIEWED` إلا بحكم `APPROVED` أو
`APPROVED WITH MINOR CORRECTIONS`، مع تنفيذ التصحيحات في الحالة الثانية
وإعادة البناء. الحزمة لا تمنح `RELEASE-READY` ولا تجيز الدمج تلقائيًا.