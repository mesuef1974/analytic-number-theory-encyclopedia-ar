# سجل أدلة الفصل الحادي والعشرين — 2026-07-25

## الحالة

```text
LEDGER                 = FROZEN
LITERATURE-CUTOFF      = 2026-07-25
PRIMARY-SOURCES        = VERIFIED FOR GOVERNING CLAIMS
CONSENSUS              = DISCOVERY-ONLY
EXACT-LOCATORS         = FROZEN
PASS-FOR-AUTHORING     = PENDING INDEPENDENT REVIEW
```

## طبقات الدليل الحاكمة

| المصدر | الوظيفة | الموضع | الحالة |
|---|---|---|---|
| Michel--Venkatesh, “The subconvexity problem for (GL_2)” | الموصل التحليلي، حد التحدب، والنتيجة المركزية لدون التحدب | §1.1، Thm. 1.1، ص 172--173؛ §3.1.8، ص 206--207 | `PRIMARY / VERIFIED` |
| Iwaniec--Sarnak, “Perspectives on the analytic theory of L-functions” | منظور الموصل والعائلات وحدود التحدب | §§1--2، GAFA 2000، ص 705--741 | `STANDARD SURVEY / VERIFIED` |
| Iwaniec--Kowalski, *Analytic Number Theory* | دوال (L) الكلاسيكية والآلية والتطبيعات | §§5.1، 5.11--5.12، 14.5--14.6 | `CORE BOOK / LOCATORS FROZEN` |
| Jacquet--Langlands, *Automorphic Forms on GL(2)* | الخلفية التمثيلية العالمية والمحلية | مرجع خلفية؛ لا تُسند إليه صيغة حاكمة في هذا الفصل | `PRIMARY BACKGROUND / NON-GOVERNING` |
| Langlands, *Euler Products* | العوامل المحلية والمنظور التمثيلي | سجل IAS للعمل ومحاضرات 1967 | `PRIMARY / VERIFIED METADATA` |
| Langlands, “Problems in the Theory of Automorphic Forms” | المدخل التاريخي للمراسلات وfunctoriality | LNM 170 (1970)، ص 18--61 | `PRIMARY / VERIFIED` |
| مصادر الفصل 20 المعتمدة | تطبيع معاملات هيكه الهولومورفية ومااس | ANT-THM-20-01 وANT-THM-20-02 وسجل تطبيعات الفصل 20 | `INTERNAL / ACTIVE` |

## الصيغ والادعاءات المسموح بها

### عوامل غاما والموصل

نعتمد
[
Gamma_{mathbb R}(s)=pi^{-s/2}Gamma(s/2),
qquad
Gamma_{mathbb C}(s)=2(2pi)^{-s}Gamma(s).
]

إذا كان العامل الأرخميدي
[
L_infty(s,pi)=prod_jGamma_{F_v}(s+mu_{pi,j}),
]
فإن Michel--Venkatesh، §3.1.8، يعرّف الموصل المحلي غير الأرخميدي بـ
(q_v^{f(pi_v)})، والأرخميدي بجداء عوامل من نمط
((2+|mu_{pi,j}|)^{deg F_v}).
وعند (F=mathbb Q):
[
C(pi)asymp N_piprod_j(2+|mu_{pi,j}|),
qquad
C(pi,t):=C(piotimes|det|^{it}).
]
علامة (asymp) مقصودة لأن تعريفات الموصل التحليلي القياسية متكافئة حتى ثوابت تعتمد على الدرجة والتطبيع.

### حد التحدب

الادعاء المسموح:
[
L(1/2,pi)ll_{arepsilon,F,n} C(pi)^{1/4+arepsilon},
]
وللقيم على الخط الحرج نستعمل
[
L(1/2+it,pi)=L(1/2,piotimes|det|^{it}).
]
هذه نتيجة `CITED-CORE`؛ لا يزعم الفصل اشتقاقها من الفصل 3، لأن الفصل 3 يذكر مبدأ فراجمن--ليندلوف ولا يثبته.

### Michel--Venkatesh

الصياغة الحاكمة من Theorem 1.1:

- (F) حقل أعداد ثابت و(mathbb A_F) حلقة أديلاته.
- (pi) تمثيل آلي لـ(GL_1(mathbb A_F)) أو (GL_2(mathbb A_F)) ذو محرف مركزي وحدوي.
- يوجد ثابت مطلق (delta>0) بحيث
[
L(1/2,pi)ll_F C(pi)^{1/4-delta}.
]
- (delta) مطلق، أما الثابت الضمني فيعتمد على (F).
- التوحيد هو في جوانب الموصل المختلفة مع تثبيت الحقل؛ لا يُدّعى توحيد بلا قيد عند تغيير الحقل.
- لا تُذكر قيمة عددية لـ(delta)، فالورقة تصرح أنها قابلة للحساب لكنها لا تحسنها.

المصدر الأصلي:
https://www.numdam.org/article/PMIHES_2010__111__171_0.pdf

DOI:
https://doi.org/10.1007/s10240-010-0025-8

## أمثلة التطبيع عند (GL(2)/mathbb Q)

- للشكل الهولومورفي الجديد ذي الوزن (k)، بعد
  (a_f(n)=lambda_f(n)n^{(k-1)/2}):
[
L_infty(s,f)=Gamma_{mathbb C}!left(s+rac{k-1}{2}ight).
]
- لشكل مااس من الوزن صفر، ذي المعلمة الطيفية (r) والتكافؤ
  (kappain{0,1}):
[
L_infty(s,u)=
Gamma_{mathbb R}(s+kappa+ir)
Gamma_{mathbb R}(s+kappa-ir).
]

هذه أمثلة ضمن النواة التعليمية، ولا تُعمم على أنواع أرخميدية أخرى دون إعادة كتابة المعلمات.

## مدخل لانجلاندز

يسمح بالفصل بين ثلاث طبقات فقط:

1. `HISTORICAL`: دوافع توحيد عوامل أويلر.
2. `PROVED SPECIAL CASES`: أمثلة محددة وموسومة بمراجعها.
3. `OPEN / CONJECTURAL FRAMEWORK`: functoriality العامة.

لا يُنسب إلى Langlands إثبات عام لـfunctoriality، ولا يفتح الفصل تعريف (L)-groups العام.

## سجل Consensus

```text
QUERY = automorphic L-functions GL(2) convexity subconvexity Langlands program survey foundational results
DATE  = 2026-07-25
ROLE  = DISCOVERY ONLY
```

استُعمل Consensus لاكتشاف سجل Michel--Venkatesh فقط، ثم طوبقت البيانات والادعاء مع الورقة الأصلية وDOI. لا يُستشهد بملخص Consensus مصدرًا رياضيًا.

## إغلاق الفجوات

- [x] تعريف الموصل التحليلي وموضعه.
- [x] صيغة حد التحدب ومجال الثوابت.
- [x] صياغة Michel--Venkatesh من Theorem 1.1.
- [x] عوامل غاما للحالتين الهولومورفية ومااس.
- [x] حد مدخل المراسلة المحلية وبرنامج لانجلاندز.
- [ ] المراجعة المستقلة للحزمة.

## حكم المرحلة

السجل مجمد وصالح للمراجعة المستقلة، ولا يمنح وحده إذن التأليف.
