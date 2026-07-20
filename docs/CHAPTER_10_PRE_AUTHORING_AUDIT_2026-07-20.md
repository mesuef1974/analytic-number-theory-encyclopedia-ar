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

## قرار البوابة النهائي

```text
PRE-AUTHORING-GATE = CLOSED
AUTHORING = AUTHORIZED
CHAPTER-FILE = MAY BE CREATED
MAIN-TEX-LINK = AUTHORIZED AFTER FILE CREATION
```

## المواد المعتمدة

- سجل الأدلة:
  `research/literature-reviews/chapter-10-prime-number-theorem-arithmetic-progressions-evidence.md`
- خريطة البرهان:
  `research/literature-reviews/chapter-10-prime-number-theorem-arithmetic-progressions-proof-map.md`
- التدقيق المنطقي:
  `docs/CHAPTER_10_LOGIC_AUDIT_2026-07-20.md`
- التحقق المرجعي:
  `docs/CHAPTER_10_BIBLIOGRAPHIC_VERIFICATION_2026-07-20.md`
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

## الادعاءات المحظورة

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
- [x] تحديد النتيجة الحدية المطلوبة: عدم انعدام \(L(s,\chi)\) على ‎\(\Re(s)=1\).
- [x] فصل حالة \(t=0\) عن \(t\ne0\).
- [x] تدقيق الشخصيات غير البدائية والعوامل المحلية.
- [x] تحديد القطب الرئيسي وباقيه \(1/\varphi(q)\).
- [x] مطابقة فروض Wiener--Ikehara بندًا بندًا.
- [x] فصل القوى الأولية العليا والجمع الجزئي.
- [x] إجراء تدقيق إشارات مستقل للمتراجحة الموزونة.
- [x] إجراء تدقيق عدم الدور مستقل.
- [x] التحقق المرجعي الدقيق من مواضع المراجع المعتمدة.
- [x] إصدار حكم `PASS` على خريطة البرهان.

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

تبقى المعرّفات `DRAFT` أثناء التأليف، ولا يجوز الاستشهاد بها حتى اكتمال
البراهين واجتياز التدقيق الداخلي اللاحق.

## إغلاق الشروط

1. المتراجحة الموزونة لكل ‎\(|z|\le1\): `PASS`.
2. عدم الانعدام على الخط لكل الشخصيات من دون استعمال PNT-AP: `PASS`.
3. الشخصيات غير البدائية والعوامل المحلية: `PASS`.
4. القطب الوحيد وباقيه \(1/\varphi(q)\): `PASS`.
5. فروض Wiener--Ikehara: `PASS`.
6. التدقيق المنطقي المكتوب: `PASS`.
7. التحقق المرجعي: `PASS-FOR-AUTHORING`.

## الحكم

```text
VERDICT = AUTHORING AUTHORIZED
LOGIC-GATE = PASS
BIBLIOGRAPHIC-GATE = PASS
NEXT ACTION = CREATE CHAPTER DRAFT AND LINK MANUSCRIPT
```
