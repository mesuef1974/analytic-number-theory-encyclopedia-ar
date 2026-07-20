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

تحقق من قسمة `C(2n,n)`، ومن الحد
`theta(2n)-theta(n)<=2n log 2`، ومن الجمع الثنائي، ومن الهوية
`psi(x)=sum theta(x^(1/m))`، ومن الحد
`psi(x)-theta(x)<<sqrt(x)log x=o(x)`، من دون استعمال PNT.

### 4.2 تمثيل ستيلتج

تحقق من القفزات وإشارة التكامل بالتجزئة وزوال الحد الطرفي في:

\[
-\frac{\zeta'}{\zeta}(s)
=
\int_{1^-}^{\infty}x^{-s}\,d\psi(x)
=
s\int_1^\infty\psi(x)x^{-s-1}\,dx.
\]

### 4.3 المتراجحة وعدم الانعدام

تحقق من المتراجحة الموزونة ومن أن الصفر المفترض عند `1+it` من الرتبة
`m>=1`، والصفر المحتمل عند `1+2it` من الرتبة `m_2>=0`، يعطيان معاملًا

\[
3-4m-m_2\le-1
\]

لـ`1/(sigma-1)`. تحقق من فصل `t!=0` عن النقطة `s=1`، وهي قطب بسيط.

### 4.4 Wiener--Ikehara

قارن العبارة مع Korevaar (2006), Theorem 1.1, pp. 1107--1108، والتطبيق
في 1108--1109. افحص عدم سلبية المعاملات، وحد المجاميع الجزئية، ومعامل
القطب `A=1`، ونوع الامتداد، وعدم خلط صيغ تاوبيرية مختلفة.

### 4.5 النتيجة المركزية والاستنتاجات

تحقق من الانتقال

\[
\psi(n)\sim n
\Longrightarrow
\psi(x)=\psi(\lfloor x\rfloor)\sim x,
\]

ثم من `psi-theta=o(x)`، ومن سلامة استعمال `ANT-THM-02-04`.

## 5. عدم الدور وحدود الادعاء

يعد مانعًا استعمال PNT داخل مقدماتها، أو استعمال الصيغة الصريحة أو بيرون
كأنهما `PROVED-HERE`، أو ادعاء حد خطأ فعال، أو خلط Selberg--Erdős بالمسار
التاوبيري، أو ادعاء `RELEASE-READY`.

## 6. نموذج تقرير المراجع

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

## 7. قاعدة اعتماد الحكم

لا يرتفع الفصل من `VERIFIED` إلى `REVIEWED` إلا بحكم `APPROVED` أو
`APPROVED WITH MINOR CORRECTIONS`، مع تنفيذ التصحيحات في الحالة الثانية
وإعادة البناء. الحزمة لا تمنح `RELEASE-READY` ولا تجيز الدمج تلقائيًا.