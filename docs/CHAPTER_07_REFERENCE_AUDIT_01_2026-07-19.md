# الفصل السابع — المراجعة المرجعية الأولى

التاريخ: 2026-07-19

الحالة: `REFERENCE-AUDIT-01-PASS / SECOND-INDEPENDENT-REVIEW-PENDING`

## النطاق

تراجع هذه الدفعة الاتفاقات الحساسة في الفصل السابع مقابل المراجع القياسية،
ولا سيما:

- NIST Digital Library of Mathematical Functions، §25.15.
- Apostol, *Introduction to Analytic Number Theory* (1976)، الأقسام التي
  يحيل إليها DLMF في §25.15.
- Davenport, *Multiplicative Number Theory*, 3rd ed. (2000).
- Montgomery--Vaughan, *Multiplicative Number Theory I* (2007).

هذه مراجعة داخل المشروع وليست مراجعة بشرية ثانية مستقلة.

## مصفوفة المطابقة

| البند | صيغة المشروع | مرجع المطابقة | الحكم |
|---|---|---|---|
| تعريف دالة `L` | `L(s,chi)=sum chi(n)n^{-s}` في `Re(s)>1` | DLMF 25.15.1؛ Apostol p. 249 وفق سجل DLMF | `PASS` |
| المنتج الأويلري | `prod_p(1-chi(p)p^{-s})^{-1}` | DLMF 25.15.2؛ Apostol p. 231 | `PASS` |
| الشخصية المستحثة | حذف العوامل عند `p|q` و`p∤f` | DLMF 25.15.4؛ Apostol p. 262 | `PASS` |
| عامل الزوجية | `a=0` إذا `chi(-1)=1` و`a=1` إذا `chi(-1)=-1` | اتفاق Apostol/DLMF للمعادلة الوظيفية | `PASS` |
| الدالة المكتملة | `(q/pi)^((s+a)/2) Gamma((s+a)/2)L(s,chi)` | الصيغة المكافئة لـ DLMF 25.15.5 | `PASS` |
| جذر العدد | `epsilon_chi=tau(chi)/(i^a sqrt(q))` | اتفاق مجموع غاوس الموافق لـ Apostol وMontgomery--Vaughan | `PASS` |
| المعادلة الوظيفية | `Lambda(s,chi)=epsilon_chi Lambda(1-s,bar chi)` | DLMF 25.15.5 | `PASS` |
| معيار جذر العدد | `|epsilon_chi|=1` من `|tau(chi)|=sqrt(q)` | نظرية مجموع غاوس القياسية | `PASS` |
| الأصفار البديهية | `s=-a-2n` | DLMF 25.15.7 و25.15.8 | `PASS` |
| عدم الانعدام عند الواحد | `L(1,chi) != 0` لغير الرئيسية | DLMF 25.15.9؛ Apostol p. 149 وفق سجل DLMF | `PASS` |

## فحص تحويل ثيتا

يعتمد الفصل الاتفاق

```text
hat f(y) = integral f(x) exp(-2 pi i x y) dx.
```

مع

```text
theta_chi(t) = sum_{n in Z} n^a chi(n) exp(-pi n^2 t/q).
```

وبهذا الاتفاق يكون التحويل الغاوسي عند `y=m/q`:

```text
hat f_{a,t}(m/q)
= (-i)^a q^(1/2) t^(-a-1/2) m^a exp(-pi m^2/(q t)).
```

وبعد عامل `1/q` في صيغة بواسون وهوية مجموع غاوس ينتج بالضبط

```text
theta_chi(t)
= tau(chi)/(i^a sqrt(q)) t^(-a-1/2) theta_bar_chi(1/t).
```

لا توجد إشارة سالبة مفقودة في الحالة الفردية؛ إذ إن
`(-i)^a=i^{-a}` عندما `a` يساوي `0` أو `1`.

## فحص تمثيل ميلين

جمع الحدين `n` و`-n` يعطي العامل `2` في تعريف `theta_chi`، ثم يؤدي
التكامل

```text
integral_0^infinity exp(-pi n^2 t/q) t^((s+a)/2) dt/t
```

إلى

```text
Gamma((s+a)/2) (q/(pi n^2))^((s+a)/2).
```

ومع العامل `n^a` يبقى `n^{-s}`، ولذلك عامل القياس في الدالة المكتملة
صحيح ولا توجد قوة زائدة لـ `n` أو `q`.

## فحص الأصفار عند الصفر

للشخصية البدائية الزوجية غير الرئيسية، يملك
`Gamma(s/2)` قطبًا بسيطًا عند `s=0`. وبعد إثبات
`L(1,bar chi) != 0` تكون `Lambda(0,chi)` غير صفرية بالمعادلة
الوظيفية، ومن ثم يلزم أن يكون صفر `L(s,chi)` عند الصفر بسيطًا بالضبط.
النص بعد التمرير التحريري يعكس هذه النتيجة، ولا يبقيها مؤجلة.

## الحدود

- لم تُراجع في هذه الدفعة أرقام صفحات جميع طبعات Davenport وMontgomery--Vaughan سطرًا بسطر.
- لا تعد هذه الوثيقة شهادة مراجعة بشرية مستقلة.
- لا تشمل أي ادعاء عن GRH أو منطقة كمية خالية من الأصفار.

## القرار

```text
FORMULA-CONVENTIONS = PASS
GAMMA-FACTOR = PASS
ROOT-NUMBER = PASS
THETA-SCALING = PASS
TRIVIAL-ZEROS = PASS
SECOND-INDEPENDENT-REVIEW = PENDING
CHAPTER-STATUS = DRAFT
```
