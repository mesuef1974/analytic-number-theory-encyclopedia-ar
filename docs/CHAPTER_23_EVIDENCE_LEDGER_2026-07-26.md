# سجل أدلة الفصل الثالث والعشرين

```text
EVIDENCE-LEDGER   = REVIEW-CORRECTED / NARROW-REVIEW-PENDING
PRIMARY-SOURCES   = VERIFIED FOR PRE-AUTHORING REVIEW
AUTHORING         = BLOCKED
FRONTIER-MATERIAL = QUARANTINED
```

## المصادر الأساسية المثبتة

| المحور | المصدر | الصيغة المجمدة للاستعمال | الحالة |
|---|---|---|---|
| عد الأصفار | `ANT-THM-06-06` في الفصل 6؛ Riemann--von Mangoldt؛ Titchmarsh--Heath-Brown | \(N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\)، مع العد بالتعدد | INTERNAL-CROSS-REFERENCE / STANDARD-CORE |
| الارتباط الثنائي | H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24 (1973), 181--193، DOI: 10.1090/pspum/024/9944 | تحت RH، للدالة الموزونة \(F(\alpha,T)\): \(F(\alpha,T)=T^{-2\alpha}(\log T+O(1))+\alpha+o(1)\) بصورة منتظمة على المجالات المغلقة داخل \(0\le\alpha<1\) | PRIMARY-VERIFIED / CONDITIONAL-ON-RH |
| إعادة صياغة حديثة | Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta function*, Acta Arithmetica 214 (2024), 357--376؛ arXiv:2306.04799 | مرجع تدقيقي حديث؛ لا يحل محل الإسناد التاريخي إلى Montgomery | SUPPORT / PEER-REVIEWED |
| الحساب العددي | A. M. Odlyzko, *On the distribution of spacings between zeros of the zeta function*, Math. Comp. 48 (1987), 273--308، DOI: 10.1090/S0025-5718-1987-0866115-0 | أول \(10^5\) أصفار، وكتلة من \(10^5\) أصفار تبدأ عند الفهرس \(10^{12}+1\)، بدقة معلنة تقارب \(10^{-8}\) | PRIMARY-VERIFIED / NUMERICAL-EVIDENCE ONLY |
| المصفوفات العشوائية | Dyson--Mehta؛ حد GUE المحلي | بعد جعل متوسط التباعد واحدًا: \(K(u)=\sin(\pi u)/(\pi u)\)، و\(R_2(u)=1-K(u)^2\) للأزواج غير القطرية | STANDARD-CORE / RANDOM-MATRIX-THEOREM |
| عائلات دوال L | N. Katz and P. Sarnak, *Random Matrices, Frobenius Eigenvalues, and Monodromy*, AMS Colloquium Publications 45 (1999) | أنواع التناظر الوحدوي والتعامدي والسمبلكتي في عائلات مضبوطة؛ لا نقل آلي إلى زيتا الكلاسيكية | PRIMARY-VERIFIED / TRANSFER-GUARDED |
| دعم متعدد المستويات | Z. Rudnick and P. Sarnak, *Zeros of principal L-functions and random matrix theory*, Duke Math. J. 81 (1996), 269--322 | امتداد خارج النواة؛ لا يستعمل لإثبات مبرهنة Montgomery الثنائية | DEFERRED / CITED-CONTEXT |

## التعريف المجمد لدالة Montgomery

نفترض RH، ونكتب الأصفار \(\rho=1/2+i\gamma\)، مع العد بالتعدد، ونضع
\[
w(u)=\frac{4}{4+u^2},
\]
ثم
\[
F(\alpha,T)=
\left(\frac{T}{2\pi}\log T\right)^{-1}
\sum_{0<\gamma,\gamma'\le T}
T^{i\alpha(\gamma-\gamma')}w(\gamma-\gamma').
\]
الأزواج مرتبة، والقطر داخل المجموع. الدالة حقيقية وزوجية وغير سالبة.

## حدسية الارتباط الثنائي بصيغة دوال الاختبار

نعتمد
\[
\widehat f(\alpha)=\int_{\mathbb R}f(u)e^{-2\pi i\alpha u}\,du.
\]
بعد حذف القطر وتطبيع الفروق محليًا، تتنبأ الحدسية بأنه لكل دالة اختبار مناسبة:
\[
\frac{1}{N(T)}
\sum_{\substack{0<\gamma,\gamma'\le T\\ \gamma\ne\gamma'}}
f\!\left((\gamma-\gamma')\frac{\log T}{2\pi}\right)
\longrightarrow
\int_{\mathbb R}f(u)
\left[1-\left(\frac{\sin\pi u}{\pi u}\right)^2\right]du.
\]
الجزء الذي تثبته طريقة Montgomery يطابق هذه الصيغة فقط عندما يكون دعم \(\widehat f\) داخل \((-1,1)\)، وتحت RH في الصياغة التاريخية المعتمدة.

## الحدود الفاصلة بين الإحصاءات

- `PAIR CORRELATION`: متوسط على جميع الأزواج بدالة اختبار.
- `NEAREST-NEIGHBOR SPACING`: توزيع الفاصل المتتالي بعد التطبيع.
- `NUMBER VARIANCE`: تباين عدد النقاط في نافذة بطول \(L\).
- `n-LEVEL CORRELATION`: بنية أعلى لا تستعاد تلقائيًا من الإحصاء الثنائي.

## حراس الأدلة

1. لا تساوى مبرهنة Montgomery بحدسية الارتباط الثنائي الكاملة.
2. اتفاقية فورييه ذات \(2\pi\) هي الوحيدة المعتمدة.
3. بيانات Odlyzko دليل عددي منتهٍ وليست برهانًا على RH أو GUE.
4. توافق GUE لا يثبت أن كل الأصفار على الخط الحرج.
5. نتائج Katz--Sarnak فوق الحقول المنتهية لا تنقل آليًا إلى العائلات الكلاسيكية.
6. صيغة ريمان--فون مانغولت مصدر حقيقتها الداخلي هو `ANT-THM-06-06`، ولا تسجل كمبرهنة جديدة مستقلة في الفصل 23.

## حالة ملاحظات المراجعة

```text
MAJOR-1 DUPLICATE-RVM-RESULT      = CLOSED
MAJOR-2 BGSTB-PUBLICATION-STATUS  = CLOSED
MINOR-1 RUDNICK-SARNAK-METADATA   = CLOSED
NARROW-RE-REVIEW                  = PENDING
PASS-FOR-AUTHORING                = NO
```
