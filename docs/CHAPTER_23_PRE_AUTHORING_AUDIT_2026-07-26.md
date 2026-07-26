# تدقيق ما قبل تأليف الفصل الثالث والعشرين

```text
CHAPTER                       = 23
VERSION                       = 0.27.0-dev
SCIENTIFIC-BLOCKERS           = 0
PRIMARY-INDEPENDENT-REVIEW    = CHANGES-REQUIRED / 0 BLOCKERS
FIRST-NARROW-RE-REVIEW        = CHANGES-REQUIRED / 0 BLOCKERS
REVIEW-CORRECTIONS            = APPLIED
READY-FOR-SECOND-NARROW-REVIEW= YES
PASS-FOR-AUTHORING            = NO
AUTHORING                     = BLOCKED
RESULTS                       = 10 RESERVED / NON-CITABLE
MERGE                         = NOT AUTHORIZED
RELEASE-READY                 = NO
```

## فحوص النطاق

- [x] الموضوع مستقل عن الفصل 22 ومتصل به منطقيًا.
- [x] خريطة الجبهات ستبقى آخر فصل.
- [x] RH وGUE خارجان عن ادعاءات الإثبات.
- [x] الحساب العددي مصنف دليلًا محدودًا لا برهانًا.
- [x] تثبيت تعريف Montgomery والوزن وشرط RH ومجال الدعم.
- [x] تثبيت اتفاقية فورييه وتطبيع نواة الجيب.
- [x] تثبيت ورقة Odlyzko لعام 1987 وأرقامها.
- [x] تثبيت حارس Katz--Sarnak.

## فحوص تصحيحات المراجعات

- [x] لا تسجل صيغة ريمان--فون مانغولت كمبرهنة جديدة؛ الإحالة إلى `ANT-THM-06-06` صريحة.
- [x] ورقة Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh مصنفة منشورة ومحكمة في Acta Arithmetica 214 (2024), 357--376.
- [x] بيانات Rudnick--Sarnak مكتملة.
- [x] أعيد تصنيف `ANT-PRIN-23-02` إلى `METHODOLOGICAL-PRINCIPLE / INFERENCE-GUARDED`.
- [x] لا يحمل `ANT-PRIN-23-02` وسم `PROVED-HERE` ولا يقدم كمبرهنة.
- [x] لا يوجد أي عنصر `PROVED-HERE` في سجل الفصل 23؛ النتائج الرياضية الجوهرية إما إحالة داخلية أو مقتبسة أو حدسية أو عددية.

## فحوص البرهان وعدم الدور

- [x] لا تستخدم حدسية GUE لإثبات الجزء المثبت.
- [x] لا تستخدم البيانات العددية كمدخل برهاني.
- [x] الفصل 22 مدخل مفاهيمي فقط.
- [x] الفصل 6 مصدر مباشر معلن لصيغة عد الأصفار.
- [x] لا توجد مبرهنة مكررة بين الفصلين 6 و23.
- [x] `CIRCULARITY = CLOSED` و`DUPLICATION = CLOSED`.

## فحوص التطبيع

- [x] \(N(T)\) يعد الأصفار بالتعدد.
- [x] مقياس الفروق هو \((\gamma-\gamma')\log T/(2\pi)\).
- [x] اتفاقية فورييه: \(e^{-2\pi i\alpha u}\).
- [x] \(K(u)=\sin(\pi u)/(\pi u)\) و\(R_2(u)=1-K(u)^2\).
- [x] الأزواج في \(F(\alpha,T)\) مرتبة والقطر داخل المجموع.
- [x] صيغة دوال الاختبار تستبعد القطر.
- [x] مجال الجزء المثبت: \(\operatorname{supp}\widehat f\subset(-1,1)\).

## فحوص النتائج

- [x] عشرة معرفات محجوزة فقط.
- [x] جميعها `NON-CITABLE`.
- [x] لا يوجد معرّف جديد لصيغة ريمان--فون مانغولت.
- [x] فُصل المقتبس والمشروط والحدسي والمصفوفي والعددي والمنهجي.
- [ ] مراجعة ضيقة مستقلة ثانية لتصنيف `ANT-PRIN-23-02` واتساق السجل والخريطة.

## الحكم الحالي

```text
VERDICT            = REVIEW-CORRECTED / SECOND-NARROW-RE-REVIEW-PENDING
BLOCKERS           = 0
PASS-FOR-AUTHORING = NO
```

لا يفتح التأليف إلا بعد حكم مستقل جديد:

```text
VERDICT            = PASS
BLOCKERS           = 0
PASS-FOR-AUTHORING = YES
```