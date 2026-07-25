# المراجعة المستقلة لما قبل تأليف الفصل الحادي والعشرين — 2026-07-25

## نطاق المراجعة

راجعت هذه الدفعة بصورة مستقلة وظيفيًا عن إعداد الحزمة، قبل إنشاء متن الفصل، الرأس:

~~~text
REVIEWED-HEAD = fbc53af1e93ca221eb69b56ee68234d8482763be
PR            = #41 / DRAFT
CHAPTER       = 21
VERSION       = 0.25.0-dev
~~~

المراجعة مستقلة عن مسار التأليف بمعنى أنها أعادت فحص الادعاءات من المصادر الأصلية ولم تعتمد على ملخصات الحزمة وحدها. وهي مراجعة داخل سير العمل، لا ادعاء بأنها تحكيم بشري خارجي.

## المواد المقروءة

- `CHAPTER_21_SCOPE_2026-07-25.md`
- `CHAPTER_21_EVIDENCE_LEDGER_2026-07-25.md`
- `CHAPTER_21_NORMALIZATION_TABLE_2026-07-25.md`
- `CHAPTER_21_PROOF_MAP_2026-07-25.md`
- `CHAPTER_21_PRE_AUTHORING_AUDIT_2026-07-25.md`
- `RESULTS_REGISTRY_CHAPTER_21.md`
- الفصل 3 من الموسوعة للتحقق من وضع فراجمن--ليندلوف.
- الفصل 20 من الموسوعة للتحقق من معاملات هيكه وتطبيعي الهولومورفي ومااس.

## تحقق المصادر الأصلية

### Jacquet--Langlands

طوبق `Automorphic Forms on GL(2)`، Chapter III, §11، Theorem 11.1، مع سجل الأدلة. تؤكد المبرهنة:

- التقارب المطلق في نصف مستوى أيمن.
- الاستمرار الميرومورفي، والتمام في الحالة الحدبية.
- الانضباط في الشرائط الرأسية.
- المعادلة الوظيفية مع التمثيل المقابل.

كما يؤكد نص §11 استعمال مبدأ فراجمن--ليندلوف. لذلك كان تصنيف المبدأ مدخلًا مقتبسًا صحيحًا، إذ إن الفصل 3 من الموسوعة يذكره ولا يثبته.

المصدر:
https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf

### Michel--Venkatesh

طوبقت الورقة الأصلية، ولا سيما §1.1 وTheorem 1.1 و§3.1.8:

- حد التحدب المركزي هو
  \[
  L(1/2,\pi)\ll_{n,F,\varepsilon}C(\pi)^{1/4+\varepsilon}.
  \]
- Theorem 1.1 تعطي ثابتًا مطلقًا \(\delta>0\) و
  \[
  L(1/2,\pi)\ll_F C(\pi)^{1/4-\delta}
  \]
  لتمثيلات \(GL_1\) أو \(GL_2\) ذات طابع مركزي وحدوي فوق حقل أعداد ثابت.
- يدخل جانب \(t\) بالالتواء \(\pi\otimes|\det|^{it}\).
- لا توجد في الحزمة قيمة عددية مصطنعة لـ\(\delta\)، ولا ادعاء بتوحيد الثابت الضمني عند تغيير الحقل.

المصدر:
https://www.numdam.org/article/PMIHES_2010__111__171_0.pdf

## مراجعة التطبيعات

| البند | الحكم |
|---|---|
| \(a_f(n)=\lambda_f(n)n^{(k-1)/2}\) | PASS |
| \(\Gamma_{\mathbb R}\) و\(\Gamma_{\mathbb C}\) | PASS |
| العامل الهولومورفي | PASS |
| عامل مااس ذو الزوجية \(\kappa\) | PASS |
| \(\Lambda(s,\pi)=N_\pi^{s/2}L_\infty(s,\pi)L(s,\pi)\) | PASS WITH NORMALIZATION GUARD |
| \(C(\pi,t)=C(\pi\otimes|\det|^{it})\) | PASS |
| مقارنة الموصل الهولومورفي | PASS / COMPARABILITY ONLY |
| مقارنة موصل مااس | PASS / COMPARABILITY ONLY |
| حد التحدب | PASS / CITED-CORE |
| Michel--Venkatesh | PASS / CITED-CORE |

حارس الدالة المكتملة يعني أن الثوابت المستقلة عن \(s\) قد تختلف باختلاف اصطلاح \(\Gamma_{\mathbb C}\)، ولا يجوز تحويل المقارنة إلى مساواة بين اصطلاحات مختلفة دون قاموس.

## تدقيق عدم الدور

- الفصل 3 لا يثبت فراجمن--ليندلوف: أُغلق الخطر بتصنيفه مدخلًا مقتبسًا.
- الفصل 20 مغلق ومعتمد قبل الفصل 21: لا اعتماد خلفي.
- الفصل 18 لا يستعمل لإثبات Michel--Venkatesh.
- لا يوجد اعتماد على الفصل 22 أو ما بعده.
- لا تُعرض functoriality العامة مبرهنة مثبتة.

الحكم: `CIRCULARITY-AUDIT = PASS`.

## ملاحظات غير مانعة للتأليف

1. يجب أن يكرر المتن قيد «حقل أعداد ثابت» داخل صياغة ANT-THM-21-03 نفسها، لا في الهامش فقط.
2. يجب أن يبقى ANT-THM-21-02 ذا شارة `CITED-CORE`، ولو أضيف شرح فراجمن--ليندلوف.
3. لا يوضع ANT-OPEN-21-01 داخل بيئة `theorem`.
4. أي توسع إلى Rankin--Selberg أو \(GL(n)\) يحتاج بوابة نطاق جديدة.

هذه حراس تأليف، لا عوائق تمنع فتحه.

## الحكم النهائي

~~~text
INDEPENDENT-PRE-AUTHORING-REVIEW = PASS
SCOPE                             = APPROVED
EVIDENCE-LEDGER                   = APPROVED / FROZEN
NORMALIZATION-TABLE               = APPROVED / FROZEN
PROOF-MAP                         = APPROVED / FROZEN
CIRCULARITY-AUDIT                 = PASS
PASS-FOR-AUTHORING                = YES
AUTHORING                         = AUTHORIZED ON PR #41 BRANCH ONLY
RESULTS                           = 10 RESERVED / NON-CITABLE
OWNER-ADOPTION                    = NOT REQUESTED
MERGE                             = NOT AUTHORIZED
RELEASE-READY                     = NO
~~~

يسمح هذا الحكم بإنشاء متن الفصل وملف مراجع مرحلي على فرع PR #41 فقط. لا يفعّل النتائج ولا يجيز الدمج.