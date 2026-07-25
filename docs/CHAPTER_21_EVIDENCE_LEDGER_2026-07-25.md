# سجل أدلة الفصل الحادي والعشرين — 2026-07-25

## الحالة

\`\`\`text
LEDGER                 = SCIENTIFIC CORE FROZEN
LITERATURE-CUTOFF      = 2026-07-25
PRIMARY-SOURCES        = VERIFIED WITH EXACT LOCATORS
CONSENSUS              = DISCOVERY-ONLY
INDEPENDENT-REVIEW     = PENDING
PASS-FOR-AUTHORING     = NO
\`\`\`

## طبقات الدليل

| المصدر | الوظيفة | الموضع المثبت | الحالة |
|---|---|---|---|
| Jacquet--Langlands, *Automorphic Forms on GL(2)* | حاصل أويلر، الاستمرار، والمعادلة الوظيفية | Chapter III, §11, Theorem 11.1، الصفحات المطبوعة 171--173 | \`PRIMARY / VERIFIED\` |
| Jacquet--Langlands, *Automorphic Forms on GL(2)* | العوامل المحلية الأرخميدية | Chapter I, §5, ولا سيما Theorem 5.15 | \`PRIMARY / VERIFIED\` |
| Langlands, *Euler Products* | المنظور التمثيلي للعوامل المحلية | محاضرات 1967، سجل IAS | \`PRIMARY / VERIFIED METADATA\` |
| Langlands, “Problems in the Theory of Automorphic Forms” | المدخل التاريخي والمراسلات | LNM 170 (1970), 18--61 | \`PRIMARY / VERIFIED\` |
| Iwaniec--Sarnak, “Perspectives on the analytic theory of L-functions” | الموصل التحليلي ومنظور العائلات | GAFA Special Volume (2000), 705--741 | \`STANDARD SURVEY / CROSS-CHECKED\` |
| Michel--Venkatesh, “The subconvexity problem for GL2” | تعريف الموصل والحدان المحدب ودون المحدب | §1، ص. 172؛ §3.1.8، ص. 206--207؛ Theorem 1.1، ص. 172 | \`PRIMARY / VERIFIED\` |
| Iwaniec--Kowalski, *Analytic Number Theory* | خلفية حد التحدب وفراجمن--ليندلوف | مرجع أساسي مساعد | \`CORE BOOK / SECONDARY CHECK\` |

## المواضع الأصلية الحاكمة

### Jacquet--Langlands

- النسخة: https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf
- Theorem 11.1 يثبت التقارب في نصف مستوى أيمن، والاستمرار التحليلي، والانعدام الكامل في الحالة الحدبية، والانضباط في الشرائط الرأسية، والمعادلة
  \[
  L(s,\pi)=\varepsilon(s,\pi)L(1-s,\widetilde\pi).
  \]
- المرجع نفسه يستعمل فراجمن--ليندلوف في §11 لضبط النمو داخل الشرائط. هذا استيراد مرجعي، وليس مبرهنة مثبتة في الفصل الثالث من الموسوعة.

### Michel--Venkatesh

- Philippe Michel and Akshay Venkatesh, *The subconvexity problem for \(GL_2\)*, Publ. Math. IHÉS 111 (2010), 171--271.
- DOI: https://doi.org/10.1007/s10240-010-0025-8
- النص الأصلي: https://www.numdam.org/article/PMIHES_2010__111__171_0.pdf
- §3.1.8، ص. 206--207: في الموضع غير الأرخميدي \(C(\pi_v)=q_v^{f(\pi_v)}\)، وفي الموضع الأرخميدي يبنى الموصل من إزاحات عوامل غاما.
- ص. 172: حد التحدب
  \[
  L(1/2,\pi)\ll_{n,F,\varepsilon} C(\pi)^{1/4+\varepsilon}.
  \]
- Theorem 1.1، ص. 172: يوجد ثابت مطلق \(\delta>0\) بحيث، لتمثيل آلي \(\pi\) على \(GL_1(\mathbb A_F)\) أو \(GL_2(\mathbb A_F)\) ذي طابع مركزي وحدوي،
  \[
  L(1/2,\pi)\ll_F C(\pi)^{1/4-\delta}.
  \]
- \(F\) ثابت في هذه الصياغة. ويدخل \(t\)-aspect عبر
  \[
  L(1/2+it,\pi)=L(1/2,\pi\otimes|\det|^{it}).
  \]
- لا تُخلط Theorem 1.1 مع Theorem 1.2 الخاصة بـRankin--Selberg، ولا يُنسب إلى Theorem 1.1 ثابت ضمني موحد في الحقل.

## عوامل غاما المجمدة لنواة \(GL(2)/\mathbb Q\)

نستعمل
\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),
\qquad
\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s)
=\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1).
\]

- لشكل جديد هولومورفي أولي ذي وزن \(k\)، بعد التطبيع التحليلي:
  \[
  L_\infty(s,\pi)=\Gamma_{\mathbb C}\!\left(s+\frac{k-1}{2}\right).
  \]
- لشكل مااس جديد أولي ذي طيف \(1/4+r^2\) وزوجية \(\kappa\in\{0,1\}\):
  \[
  L_\infty(s,\pi)=
  \Gamma_{\mathbb R}(s+\kappa+ir)
  \Gamma_{\mathbb R}(s+\kappa-ir).
  \]

هذه الصيغ لنواة \(\mathbb Q\) وبالتطبيع ذي خط التناظر \(\Re s=1/2\). أي انتقال إلى حقل أعداد أو طابع أرخميدي آخر يعاد تطبيعه.

## سجل Consensus

\`\`\`text
QUERY = automorphic L-functions GL(2) convexity subconvexity Langlands program survey foundational results
DATE  = 2026-07-25
ROLE  = DISCOVERY ONLY
\`\`\`

اكتشف Consensus سجل Michel--Venkatesh، ثم جرى التحقق من كل ادعاء حاكم من الورقة الأصلية. لا يُستشهد بملخص Consensus مصدرًا رياضيًا.

## إغلاق الفجوات

- [x] الموصل التحليلي وموضعه.
- [x] حد التحدب ومجال ثوابته.
- [x] صياغة Michel--Venkatesh الدقيقة.
- [x] عوامل غاما للهولومورفي ومااس.
- [x] نطاق لانجلاندز: تاريخي/مفاهيمي، بلا ادعاء functoriality عامة.
- [ ] مراجعة مستقلة للحزمة كاملة.

السجل العلمي مجمد وجاهز للمراجعة المستقلة، لكنه لا يجيز التأليف منفردًا.
