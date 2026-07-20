# تدقيق ما قبل تأليف الفصل العاشر — 2026-07-20

## الهوية

```text
CHAPTER       = 10 — مبرهنة الأعداد الأولية في المتتاليات الحسابية
VERSION       = 0.14.0-dev
BRANCH        = agent/chapter-10-prime-number-theorem-arithmetic-progressions-v0.14.0
BASE-COMMIT   = 601d8eef29e973e882f6d2213a382d15e3870d42
MODE          = EVIDENCE-FIRST / PRE-AUTHORING
```

تحقق أن فرع العمل كان مطابقًا تمامًا لالتزام دمج الفصل التاسع عند بداية المرحلة.

## قرار البوابة الحالي

```text
PRE-AUTHORING-GATE = OPEN
AUTHORING = BLOCKED
CHAPTER-FILE = NOT CREATED
MAIN-TEX-LINK = NOT AUTHORIZED
```

## المواد المتاحة

- سجل الأدلة:
  `research/literature-reviews/chapter-10-prime-number-theorem-arithmetic-progressions-evidence.md`
- خريطة البرهان:
  `research/literature-reviews/chapter-10-prime-number-theorem-arithmetic-progressions-proof-map.md`
- الفصول المعتمدة السابقة: الثاني، السابع، الثامن، التاسع.
- صيغة Wiener--Ikehara المعتمدة بحالة `CITED` في `ANT-THM-09-02`.

## نطاق الادعاء المسموح

لـ\(q\) ثابت و\((a,q)=1\):

\[
\psi(x;q,a)\sim\frac{x}{\varphi(q)},
\qquad
\vartheta(x;q,a)\sim\frac{x}{\varphi(q)},
\qquad
\pi(x;q,a)\sim\frac{x}{\varphi(q)\log x}.
\]

## الادعاءات المحظورة في هذه المرحلة

- أي حد خطأ فعال.
- أي انتظام عندما ينمو \(q\) مع \(x\).
- Siegel--Walfisz.
- Bombieri--Vinogradov.
- منطقة خالية كمية موحدة.
- معالجة الأصفار الاستثنائية كأنها مغلقة داخليًا.
- أي نتيجة مشروطة بـGRH من دون وسم صريح.

## قائمة فحص الأدلة

- [x] تثبيت الهدف النوعي لترديد ثابت.
- [x] تحديد سلسلة ديريشليه ذات معاملات غير سالبة لكل فئة.
- [x] تحديد دور مرشح الشخصيات.
- [x] تحديد النتيجة الحدية المطلوبة: عدم انعدام \(L(s,\chi)\) على \(\Re(s)=1\).
- [x] فصل حالة \(t=0\) عن \(t\ne0\).
- [x] تسجيل معالجة الشخصيات غير البدائية.
- [x] تحديد القطب الرئيسي وباقيه \(1/\varphi(q)\).
- [x] تحديد تطبيق Wiener--Ikehara.
- [x] فصل القوى الأولية العليا والجمع الجزئي.
- [ ] إجراء تدقيق إشارات مستقل للمتراجحة الموزونة.
- [ ] إجراء تدقيق عدم الدور مستقل.
- [ ] التحقق المرجعي الدقيق من مواضع Davenport وMontgomery--Vaughan وTenenbaum.
- [ ] إصدار حكم `PASS` أو `FAIL` على خريطة البرهان.

## المعرّفات المحجوزة

```text
ANT-PROP-10-01 = DRAFT
ANT-LEM-10-01  = DRAFT
ANT-THM-10-01  = DRAFT
ANT-PROP-10-02 = DRAFT
ANT-THM-10-02  = DRAFT
ANT-COR-10-01  = DRAFT
ANT-COR-10-02  = DRAFT
```

لا يجوز الاستشهاد بهذه المعرّفات ما دامت `DRAFT`.

## شروط إغلاق البوابة

لا تتحول `AUTHORING` إلى `AUTHORIZED` إلا بعد:

1. إثبات المتراجحة الموزونة لكل ‎\(|z|\le1\) مع تدقيق الإشارة.
2. إثبات عدم الانعدام على الخط لكل الشخصيات من دون استعمال PNT-AP.
3. التحقق من الشخصيات غير البدائية والعوامل المحلية.
4. إثبات أن القطب الوحيد في سلسلة الفئة هو قطب الرئيسية بباقٍ \(1/\varphi(q)\).
5. مطابقة فروض Wiener--Ikehara بندًا بندًا.
6. إصدار تدقيق منطقي مكتوب بحكم `PASS`.

## الحكم الحالي

```text
VERDICT = PRE-AUTHORING REMAINS OPEN
NEXT ACTION = LOGIC AND BIBLIOGRAPHIC AUDIT
```
