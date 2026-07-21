# التحقق المرجعي بعد تأليف الفصل الثالث عشر

التاريخ: 2026-07-21

```text
CHAPTER              = 13
AUDIT                = POST-AUTHORING-REFERENCE
CITATION-KEYS        = PASS
BIBER                = SUCCESS
PROVENANCE-LABELS    = PASS
REFERENCE-BLOCKERS   = 0
VERDICT              = PASS
RELEASE-READY        = NO
```

## 1. الملفات المفحوصة

- `volumes/volume-01-foundations/chapters/chapter-13-bombieri-vinogradov.tex`
- `manuscript/chapter-13-bibliography.bib`
- `manuscript/preamble.tex`
- `docs/CHAPTER_13_REFERENCE_VERIFICATION_2026-07-21.md`

## 2. مفاتيح الاستشهاد في المتن

تستعمل حزمة الغربال الكبير في المتن المفتاحين:

```text
Bombieri1965LargeSieve
MontgomeryVaughan2026
```

وكلاهما موجود في ملف BibTeX الخاص بالفصل. وبسبب وجود `\nocite{*}` في الملف
الجامع، تدخل كذلك المصادر التاريخية المحققة الآتية في قائمة المراجع:

```text
Vinogradov1965Density
Vinogradov1966Correction
Gallagher1968Bombieri
Vaughan1975MeanValue
```

اجتاز Biber بناء PDF #334، فلا يوجد مفتاح مفقود أو تعارض يمنع البناء.

## 3. حالات المنشأ في المتن

- `ANT-THM-13-01` موسوم `CITED`، وهو يضم الحزمة المقتبسة فقط.
- هوية Vaughan وPólya--Vinogradov وType I وType II موسومة `PROVED-HERE`.
- مبرهنة القيمة المتوسطة موسومة `PROVED-HERE` مع تصريح واضح بأنها تعتمد على
  الحزمة المقتبسة.
- Bombieri--Vinogradov والنتائج التابعة موسومة `PROVED-HERE`، مع تسجيل عدم
  فعالية الثابت في نص النتائج وحدود الادعاء.

لا توجد نتيجة مقتبسة موسومة على أنها برهان داخلي كامل.

## 4. المطابقة مع المصادر

| الموضع في المتن | المرجع الحاكم | الحكم |
|---|---|---|
| الغربال الكبير التربيعي | Montgomery--Vaughan II، المبرهنة 19.16، ص. 175 | `PASS` |
| المدخل الثنائي العظمى | المبرهنة 19.19، الصيغة (19.34)، ص. 181 | `PASS` |
| صيغة هوية Vaughan | الصيغة (17.5)، ص. 55--56 | `PASS` |
| الشكل النهائي لمبرهنة القيمة المتوسطة | المبرهنة 20.1، ص. 189 | `PASS` |
| شكل \(E^*(x,q)\) ومستوى \(1/2\) | المبرهنة 20.2، ص. 195 | `PASS` |
| رد الموصلات واستعمال Siegel--Walfisz | برهان المبرهنة 20.2، ص. 196--197 | `PASS` |

المتن لا ينسخ برهان المصدر حرفيًا؛ بل يعيد بناء المسار من المدخل المقتبس
والهويات واللمم المثبتة داخل الموسوعة.

## 5. التصحيح التاريخي

يبقى تصحيح A. I. Vinogradov المنشور سنة 1966 مسجلًا في BibTeX وفي التحقق
المرجعي، فلا تعرض ورقة 1965 منفردة من دون سجل التصويب.

## 6. نتيجة البناء

```text
QUALITY-CHECKS #340 = SUCCESS
PDF-BUILD      #334 = SUCCESS
BIBER                = SUCCESS
```

هذا يثبت سلامة مفاتيح المراجع وبنية BibLaTeX في بيئة CI. لا يثبت فحصًا بصريًا
نهائيًا لقائمة المراجع أو جاهزية إصدار.

## 7. الحكم

```text
REFERENCE-VERIFICATION = PASS
REFERENCE-BLOCKERS     = 0
PROMOTION              = VERIFIED ALLOWED
INDEPENDENT-REVIEW     = NOT YET STARTED
RELEASE-READY          = NO
```
