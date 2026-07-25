# جدول تطبيعات الفصل العشرين — 2026-07-25

## الحالة

```text
CHAPTER              = 20
VERSION              = 0.24.0-dev
TABLE                = FROZEN / INDEPENDENTLY REVIEWED
PRIMARY-SCOPE        = LEVEL 1 / TRIVIAL CHARACTER
PETERSSON-LEVEL-1    = CROSS-CHECK PASS
KUZNETSOV-LEVEL-1    = CROSS-CHECK PASS
SELBERG-COMPACT      = CROSS-CHECK PASS
AUTHORING            = AUTHORED-DRAFT / NON-CITABLE
RESULTS              = RESERVED / NON-CITABLE
```

الغرض من هذا الجدول منع نقل صيغة أثر من مرجع إلى آخر مع تغيير خفي في إشارة لابلاس أو قياس بيترسون أو معاملات فورييه أو تحويلات Bessel.

## نطاق الصيغ الدقيقة

| المكوّن | النطاق المعتمد مبدئيًا | ما يؤجل |
|---|---|---|
| Petersson | \(SL_2(\mathbb Z)\)، وزن زوجي \(k>2\)، شخصية تافهة | الصيغة الموحدة للمستوى العام والشخصية |
| Kuznetsov | الزمرة المعيارية، وزن مااس \(0\)، معاملات فورييه مطبعة صراحة | المستويات والشخصيات والراميفيكيشن الموضعي |
| Selberg | النموذج المدمج البنيوي: طيف لابلاس مقابل أصناف الاقتران/الجيوديسيات | الصيغة غير المدمجة الكاملة وحدود القطع والمبعثرات |

## القاموس المبدئي

| العنصر | تطبيع الفصل المرشح | موضع المطابقة | حالة التجميد |
|---|---|---|---|
| الدالة الأسية | \(e(x)=e^{2\pi i x}\) | مستعملة في فورييه وKloosterman معًا | `FROZEN` |
| القياس الزائدي | \(d\mu(z)=dx\,dy/y^2\) | Kuznetsov §2، قبل (2.6) | `SOURCE-MATCHED` |
| لابلاس | \(\Delta=-y^2(\partial_x^2+\partial_y^2)\)، \(\lambda=1/4+t^2\) | ترجمت إشارة المصدر الأصلي صراحة | `SOURCE-MATCHED` |
| فورييه الهولومورفي | \(f(z)=\sum_{n\ge1}a_f(n)e(nz)\) | Petersson/Knightly--Li §3 | `FROZEN / LEVEL-1` |
| حاصل بيترسون | \(\langle f,g\rangle=\int_{\Gamma\backslash\mathbb H}f(z)\overline{g(z)}y^k\,d\mu(z)\) عند المستوى 1 | Knightly--Li (3) يقسم على \(\psi(N)\)؛ لا فرق عند \(N=1\) | `SOURCE-MATCHED / LEVEL-1` |
| توسع مااس | \(u_j(z)=\sqrt y\sum_{n\ne0}\rho_j(n)K_{it_j}(2\pi|n|y)e(nx)\) | طوبق مع Kuznetsov (2.10) والصيغة الحديثة | `CROSS-CHECK PASS / LEVEL-1` |
| مجموع Kloosterman | \(S(m,n;c)=\sum_{d\bmod c}^{*}e((md+n\bar d)/c)\) | Kuznetsov (2.13) | `SOURCE-MATCHED` |
| نواة Petersson | \(J_{k-1}(4\pi\sqrt{mn}/c)\) | Knightly--Li Cor. 3.12؛ Iwaniec--Kowalski Prop. 14.5 | `CROSS-CHECK PASS / LEVEL-1` |
| تحويلات Kuznetsov | \(H^+\) مجمد للنواة ذات الإشارة المتساوية؛ تحويل \(K\) يذكر منفصلًا في سياق الإشارة المتعاكسة فقط | Kuznetsov (2.14)--(2.23)؛ تقرير المطابقة المستقل | `CROSS-CHECK PASS / CORE` |
| زوج Selberg التحويلي | \(g(u)=\frac1{2\pi}\int h(r)e^{-iru}dr\)، و\(h(r)=\int g(u)e^{iru}du\) | Marklof (69)، Thm. 4 (182)؛ Hejhal I، الفصل الأول | `CROSS-CHECK PASS / COMPACT` |

## مطابقة Petersson عند المستوى 1

تطابق Knightly--Li Corollary 3.12 مع Iwaniec--Kowalski Proposition 14.5 بعد وضع \(N=1\):

- \(\psi(1)=1\).
- \(\Gamma(k-1)=(k-2)!\).
- \(i^{-k}=1/i^k\).
- الحجة البسليّة والعامل \(2\pi\) والحد القطري متطابقة.
- تبديل معاملي Kloosterman يعالج بتغيير المتغير \(d\leftrightarrow \bar d\) في الحالة الكلاسيكية.

الحكم: `PETERSSON-LEVEL-1 = CROSS-CHECK PASS`.

## حواجز النقل بين المراجع

1. لا تنقل عامل \(\psi(N)=[SL_2(\mathbb Z):\Gamma_0(N)]\) من Knightly--Li إلى صيغة المستوى \(1\).
2. لا تستبدل معاملات \(a_f(n)\) بالمعاملات المعيارية \(\lambda_f(n)\) دون إظهار عامل \(a_f(1)n^{(k-1)/2}\) وفق الاصطلاح المختار.
3. لا تخلط تطبيع \(L^2\) لأشكال مااس مع التطبيع الهيكي \(\rho_j(1)=1\).
4. لا تحذف الطيف المستمر من Kuznetsov للزمرة غير المدمجة.
5. لا تعرض نموذج Selberg المدمج بوصفه صيغة المجموعة المعيارية غير المدمجة.
6. لا توحد تحويلات Bessel اعتمادًا على التشابه الشكلي؛ يجب مطابقة الإشارة وعامل \(\pi\) ودالة الاختبار.

## شروط التجميد

- [x] مطابقة صيغة Petersson مستوى \(1\) حدًا بحد مع مرجع قياسي ثانٍ.
- [x] مطابقة نواة Kuznetsov المعتمدة: الطيف المنفصل والمستمر والقطري وطرف Kloosterman وتحويل \(J\)، مع فصل سياق تحويل \(K\).
- [x] تثبيت اتجاه تحويل Selberg وعوامل \(2\pi\) للنموذج المدمج.
- [x] مراجعة مستقلة للجدول.

أُغلقت المطابقات العلمية الثلاث واجتاز الجدول المراجعة المستقلة. استعمل المتن هذه التطبيعات ضمن النطاق المجمد، وتبقى نتائجه `NON-CITABLE` حتى المراجعة اللاحقة واعتماد المالك.
