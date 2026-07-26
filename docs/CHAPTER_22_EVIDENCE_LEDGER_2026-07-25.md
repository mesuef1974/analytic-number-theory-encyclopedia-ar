# سجل أدلة الفصل الثاني والعشرين

## حالة السجل

```text
EVIDENCE-LEDGER     = CORE SOURCES VERIFIED / REVIEW CORRECTIONS APPLIED
AUTHORING           = BLOCKED PENDING NARROW RE-REVIEW
PRIMARY-SOURCES     = VERIFIED FOR CORE STATEMENTS
FRONTIER-MATERIAL   = QUARANTINED UNTIL REVIEW
```

## المصادر الأساسية المثبتة

| المحور | المصدر | الصيغة المثبتة للاستعمال | الحالة |
|---|---|---|---|
| العزم الثاني | A. E. Ingham, *Mean-Value Theorems in the Theory of the Riemann Zeta-Function*, Proc. LMS (2) 27 (1928), 273--300؛ مع Hardy--Littlewood خلفية تاريخية، وTitchmarsh--Heath-Brown مرجعًا معياريًا لاحقًا | \(\int_0^T|\zeta(1/2+it)|^2dt=T\log(T/2\pi)+(2\gamma-1)T+E_1(T)\)، ويكفي للنواة الحد الكلاسيكي \(E_1(T)=O(T^{1/2}\log T)\) | CORE-VERIFIED / ATTRIBUTION-CORRECTED |
| العزم الرابع | A. E. Ingham, *Mean-Value Theorems in the Theory of the Riemann Zeta-Function*, Proc. LMS (2) 27 (1928), 273--300، DOI: 10.1112/plms/s2-27.1.273 | \(\int_0^T|\zeta(1/2+it)|^4dt=\frac{1}{2\pi^2}T\log^4T+O(T\log^3T)\)؛ النسخة الحديثة الأدق تكتب \(TP_4(\log T)+E_2(T)\) ومعامل الحد الأعلى \(1/(2\pi^2)\) | CORE-VERIFIED |
| الحدود العليا | K. Soundararajan, *Moments of the Riemann zeta function*, Annals of Mathematics 170 (2009), 981--993 | تحت RH: لكل \(k\ge0\) ثابت و\(\varepsilon>0\)، \(J_k(T)\ll_{k,\varepsilon}T(\log T)^{k^2+\varepsilon}\)؛ حالة \(k=0\) تافهة وتُذكر فقط لتوحيد المجال | PRIMARY-VERIFIED / PEER-REVIEWED |
| تحسين الحدود العليا | A. J. Harper, *Sharp conditional bounds for moments of the Riemann zeta function*, arXiv:1305.4618 (2013) | تحت RH: لكل \(k\ge0\) ثابت، \(J_k(T)\ll_k T(\log T)^{k^2}\) | PRIMARY-VERIFIED / PREPRINT / NOT PEER-REVIEWED |
| الحدود الدنيا | Radziwiłł--Soundararajan, *Continuous lower bounds for moments of zeta and L-functions*, Mathematika 59 (2013), 119--128 | لكل \(k\ge1\) ثابت، حد أدنى غير مشروط من الرتبة \(T(\log T)^{k^2}\)؛ لا يُصاغ كتكافؤ تقاربي | PRIMARY-VERIFIED |
| حدود دنيا حديثة | Heap--Soundararajan, *Lower bounds for moments of zeta and L-functions revisited*, Mathematika 68 (2022) | تبسيط وتوسيع منهج الحدود الدنيا؛ يبقى CITED-SUPPORT لا بديلًا عن المصدر الأصلي | PRIMARY-VERIFIED / SUPPORT |
| نموذج المصفوفات العشوائية | Keating--Snaith, *Random matrix theory and \(\zeta(1/2+it)\)*, CMP 214 (2000), 57--89 | حدسية العزوم العامة بعامل حسابي وعامل Barnes \(G\) | PRIMARY-VERIFIED / CONJECTURAL |
| العزوم المزاحة | Ng--Shen--Wong, *Shifted moments of the Riemann zeta function*, CJM 76 (2024), 1556--1586 | سياق حديث خارج النواة الأساسية | VERIFIED-METADATA / DEFERRED |
| مسح 2026 | Alexandra Florea, *A survey of moment bounds for \(\zeta(s)\): From Heath-Brown's work to the present*, Journal of the London Mathematical Society 113 (2026), no. 1, e70376, DOI: 10.1112/jlms.70376 | اكتشاف ومقارنة فقط، لا مصدر تأسيسي للنواة | VERIFIED-SURVEY / NON-FOUNDATIONAL |

## الصيغ المجمدة

### العزم الثاني

\[
I_1(T)=\int_0^T\left|\zeta\!\left(\frac12+it\right)\right|^2dt
=T\log\frac{T}{2\pi}+(2\gamma-1)T+E_1(T).
\]

لأغراض الفصل يكفي تسجيل الحد الكلاسيكي
\[
E_1(T)=O(T^{1/2}\log T),
\]
مع إسناده إلى Ingham، ومن دون الادعاء أنه أفضل حد معروف.

### العزم الرابع

\[
I_2(T)=\int_0^T\left|\zeta\!\left(\frac12+it\right)\right|^4dt
=\frac{1}{2\pi^2}T\log^4T+O(T\log^3T).
\]

والصياغة الحديثة الأدق هي
\[
I_2(T)=TP_4(\log T)+E_2(T),
\]
حيث \(P_4\) كثيرة حدود من الدرجة الرابعة ومعامل \(x^4\) فيها \(1/(2\pi^2)\).

### حدسية Keating--Snaith

لكل \(k\) ثابت مع \(\Re k>-1/2\):
\[
I_k(T)\sim a(k)\,\frac{G(k+1)^2}{G(2k+1)}\,T\left(\log\frac{T}{2\pi}\right)^{k^2}.
\]

ويُجمّد العامل الحسابي على الصورة
\[
a(k)=\prod_p\left(1-\frac1p\right)^{k^2}
\sum_{m=0}^{\infty}
\left(\frac{\Gamma(m+k)}{m!\,\Gamma(k)}\right)^2p^{-m}.
\]

وعند \(k\in\mathbb N\):
\[
\frac{G(k+1)^2}{G(2k+1)}
=\prod_{j=0}^{k-1}\frac{j!}{(j+k)!}.
\]

هذه صيغة `CONJECTURAL` لدالة زيتا، مع أن متوسط كثير الحدود المميز على \(U(N)\) نتيجة مثبتة في نموذج المصفوفات العشوائية.

## حقائق الحوكمة المجمدة

1. الصيغة العامة المتوقعة للعزوم ليست مبرهنة لكل \(k\).
2. العزمان الثاني والرابع هما الحالتان الكلاسيكيتان ذواتا صيغ تقاربية مثبتة.
3. حد Soundararajan محكّم ومنشور؛ حد Harper preprint موثوق لكنه غير محكّم بحسب السجل المتاح.
4. كلا الحدين العلويين مشروط بفرضية ريمان.
5. الحدود الدنيا المستمرة غير مشروطة ضمن مجالها المعلن.
6. نموذج Keating--Snaith حدسي لدالة زيتا، لا نتيجة مثبتة فيها.
7. الانتقال من رتبة العزوم إلى قانون القيم القصوى يحتاج مدخلًا إضافيًا.
8. لا تُستعمل أفضل حدود الخطأ الحديثة إذا لم تكن لازمة لبنية الفصل.

## حالة ملاحظات المراجعة المستقلة

- MAJOR-1: CLOSED — صُحح إسناد حد خطأ العزم الثاني إلى Ingham.
- MAJOR-2: CLOSED — وُسم Harper صراحة `PREPRINT / NOT PEER-REVIEWED` وفُصل عن Soundararajan المنشور.
- MINOR-1: CLOSED — ثُبتت سنة النشر 1928، مع كون 1926 سنة الاستلام.
- MINOR-2: CLOSED — ثُبت مجال Soundararajan عند \(k\ge0\) الثابت، مع التنبيه إلى تفاهة \(k=0\).
- EDITORIAL-2: CLOSED — استُكملت بيانات Florea الببليوغرافية.

المتبقي قبل فتح التأليف: مراجعة ضيقة مستقلة للتصحيحات، مع بقاء `PASS-FOR-AUTHORING = NO` حتى صدور حكم جديد.